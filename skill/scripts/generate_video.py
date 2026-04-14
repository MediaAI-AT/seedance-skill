#!/usr/bin/env python3
"""
WaveSpeed Seedance 2.0 — Video Generator
Submits a prompt to WaveSpeed, polls until done, saves MP4 locally.

Usage:
    python generate_video.py --prompt "your prompt" --duration 5
    python generate_video.py --prompt "your prompt" --duration 10 --output my_video.mp4
    python generate_video.py --prompt "your prompt" --duration 15 --aspect-ratio 9:16
    python generate_video.py --prompt "your prompt" --duration 5 --refs image1.png image2.jpg
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

# ─────────────────────────────────────────────
# Cost table (720p only)
# ─────────────────────────────────────────────
COSTS = {5: 1.20, 10: 2.40, 15: 3.60}

API_BASE = "https://api.wavespeed.ai/api/v3"
SUBMIT_URL = f"{API_BASE}/bytedance/seedance-2.0/text-to-video"
POLL_INTERVAL = 4  # seconds between status checks


def get_api_key() -> str:
    key = os.environ.get("WAVESPEED_API_KEY", "")
    if not key:
        print("ERROR: WAVESPEED_API_KEY environment variable not set.")
        print("Set it with:  set WAVESPEED_API_KEY=your_key_here  (Windows)")
        print("              export WAVESPEED_API_KEY=your_key_here  (Mac/Linux)")
        sys.exit(1)
    return key


def upload_reference(file_path: str, api_key: str) -> str:
    """Upload a local file to WaveSpeed and return its public URL."""
    path = Path(file_path)
    if not path.exists():
        print(f"  WARNING: Reference file not found: {file_path} — skipping")
        return None

    # WaveSpeed file upload endpoint
    upload_url = f"{API_BASE}/files/upload"
    with open(path, "rb") as f:
        file_data = f.read()

    # Determine content type
    suffix = path.suffix.lower()
    content_types = {
        ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png",
        ".webp": "image/webp", ".gif": "image/gif",
        ".mp4": "video/mp4", ".mov": "video/quicktime",
        ".mp3": "audio/mpeg", ".wav": "audio/wav",
    }
    content_type = content_types.get(suffix, "application/octet-stream")

    # Build multipart form-data manually
    boundary = "----WaveSpeedBoundary"
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{path.name}"\r\n'
        f"Content-Type: {content_type}\r\n\r\n"
    ).encode() + file_data + f"\r\n--{boundary}--\r\n".encode()

    req = urllib.request.Request(
        upload_url,
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read().decode())
            url = result.get("url") or result.get("file_url") or result.get("data", {}).get("url")
            if url:
                print(f"  Uploaded {path.name} → {url}")
                return url
            else:
                print(f"  WARNING: Upload response had no URL: {result}")
                return None
    except urllib.error.HTTPError as e:
        print(f"  WARNING: Upload failed for {path.name}: {e.code} {e.reason}")
        return None


def submit_job(prompt: str, duration: int, aspect_ratio: str,
               ref_image_urls: list, ref_video_urls: list, ref_audio_urls: list,
               api_key: str) -> str:
    """Submit generation job, return prediction ID."""
    payload = {
        "prompt": prompt,
        "duration": duration,
        "resolution": "720p",
        "aspect_ratio": aspect_ratio,
    }
    if ref_image_urls:
        payload["reference_images"] = ref_image_urls
    if ref_video_urls:
        payload["reference_videos"] = ref_video_urls
    if ref_audio_urls:
        payload["reference_audios"] = ref_audio_urls

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        SUBMIT_URL,
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read().decode())

    pred_id = result.get("id") or result.get("data", {}).get("id")
    if not pred_id:
        print(f"ERROR: No prediction ID in response: {result}")
        sys.exit(1)
    return pred_id


def poll_until_done(pred_id: str, api_key: str) -> str:
    """Poll status endpoint until completed. Returns video URL."""
    poll_url = f"{API_BASE}/predictions/{pred_id}"
    req_headers = {"Authorization": f"Bearer {api_key}"}

    spinner = ["|", "/", "—", "\\"]
    tick = 0
    start_time = time.time()

    while True:
        req = urllib.request.Request(poll_url, headers=req_headers, method="GET")
        try:
            with urllib.request.urlopen(req) as resp:
                result = json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            print(f"\n  Poll error {e.code} — retrying...")
            time.sleep(POLL_INTERVAL)
            continue

        # Handle both flat and nested response shapes
        data = result.get("data", result)
        status = data.get("status", "unknown")
        elapsed = int(time.time() - start_time)

        print(f"\r  {spinner[tick % 4]}  Status: {status:<12} ({elapsed}s elapsed)", end="", flush=True)
        tick += 1

        if status == "completed":
            print()
            outputs = data.get("outputs", [])
            if not outputs:
                print("ERROR: Status completed but no outputs in response.")
                print(json.dumps(data, indent=2))
                sys.exit(1)
            return outputs[0]  # first video URL

        elif status == "failed":
            print()
            error_msg = data.get("error") or data.get("message") or "Unknown error"
            print(f"ERROR: Generation failed — {error_msg}")
            sys.exit(1)

        time.sleep(POLL_INTERVAL)


def download_video(url: str, output_path: Path) -> None:
    """Download video from URL to local path."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp:
        total = int(resp.headers.get("Content-Length", 0))
        downloaded = 0
        chunk_size = 8192
        with open(output_path, "wb") as f:
            while True:
                chunk = resp.read(chunk_size)
                if not chunk:
                    break
                f.write(chunk)
                downloaded += len(chunk)
                if total:
                    pct = downloaded / total * 100
                    print(f"\r  Downloading... {pct:.0f}% ({downloaded // 1024} KB)", end="", flush=True)
    print()


def build_output_path(custom_name: str | None, duration: int) -> Path:
    """Build output file path. Default: seedance_5s_20260414_153012.mp4"""
    if custom_name:
        p = Path(custom_name)
        if p.suffix.lower() != ".mp4":
            p = p.with_suffix(".mp4")
        return p
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return Path(f"seedance_{duration}s_{timestamp}.mp4")


def main():
    parser = argparse.ArgumentParser(
        description="Generate a Seedance 2.0 video via WaveSpeed and save it locally."
    )
    parser.add_argument("--prompt", "-p", required=True, help="Video generation prompt")
    parser.add_argument("--duration", "-d", type=int, choices=[5, 10, 15], default=5,
                        help="Duration in seconds (5, 10, or 15)")
    parser.add_argument("--aspect-ratio", "-ar", default="16:9",
                        choices=["16:9", "9:16", "4:3", "3:4", "1:1", "21:9"],
                        help="Aspect ratio (default: 16:9)")
    parser.add_argument("--output", "-o", default=None,
                        help="Output filename (default: seedance_Xs_TIMESTAMP.mp4)")
    parser.add_argument("--refs", "-r", nargs="*", default=[],
                        help="Reference files to upload (images, videos, or audio)")
    parser.add_argument("--yes", "-y", action="store_true",
                        help="Skip cost confirmation prompt")
    args = parser.parse_args()

    api_key = get_api_key()
    cost = COSTS[args.duration]
    output_path = build_output_path(args.output, args.duration)

    # ── Cost confirmation ────────────────────────────────────────────
    print()
    print("╔══════════════════════════════════════════════════╗")
    print("║         Seedance 2.0 — WaveSpeed Generator       ║")
    print("╠══════════════════════════════════════════════════╣")
    print(f"║  Duration    : {args.duration}s                               ║")
    print(f"║  Resolution  : 720p                              ║")
    print(f"║  Aspect ratio: {args.aspect_ratio:<8}                        ║")
    print(f"║  Output file : {str(output_path):<34} ║")
    print(f"║  Refs        : {len(args.refs)} file(s)                       ║")
    print("╠══════════════════════════════════════════════════╣")
    print(f"║  COST        : ${cost:.2f}                            ║")
    print("╚══════════════════════════════════════════════════╝")
    print()
    print(f"  Prompt: {args.prompt[:80]}{'...' if len(args.prompt) > 80 else ''}")
    print()

    if not args.yes:
        try:
            answer = input(f"  Generate this video for ${cost:.2f}? [y/N] ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n  Aborted.")
            sys.exit(0)
        if answer not in ("y", "yes"):
            print("  Cancelled.")
            sys.exit(0)

    print()

    # ── Upload references ────────────────────────────────────────────
    ref_image_urls, ref_video_urls, ref_audio_urls = [], [], []

    if args.refs:
        print(f"  Uploading {len(args.refs)} reference file(s)...")
        image_exts = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp"}
        video_exts = {".mp4", ".mov"}
        audio_exts = {".mp3", ".wav"}

        for ref in args.refs:
            suffix = Path(ref).suffix.lower()
            url = upload_reference(ref, api_key)
            if url:
                if suffix in image_exts:
                    ref_image_urls.append(url)
                elif suffix in video_exts:
                    ref_video_urls.append(url)
                elif suffix in audio_exts:
                    ref_audio_urls.append(url)
        print()

    # ── Submit job ───────────────────────────────────────────────────
    print("  Submitting to WaveSpeed...")
    pred_id = submit_job(
        prompt=args.prompt,
        duration=args.duration,
        aspect_ratio=args.aspect_ratio,
        ref_image_urls=ref_image_urls,
        ref_video_urls=ref_video_urls,
        ref_audio_urls=ref_audio_urls,
        api_key=api_key,
    )
    print(f"  Job ID: {pred_id}")
    print()

    # ── Poll ─────────────────────────────────────────────────────────
    print("  Waiting for generation to complete...")
    video_url = poll_until_done(pred_id, api_key)
    print(f"  Video URL: {video_url}")
    print()

    # ── Download ─────────────────────────────────────────────────────
    print(f"  Saving to: {output_path.resolve()}")
    download_video(video_url, output_path)

    file_size_mb = output_path.stat().st_size / 1024 / 1024
    print()
    print("╔══════════════════════════════════════════════════╗")
    print("║                    ✓ DONE                        ║")
    print("╠══════════════════════════════════════════════════╣")
    print(f"║  File : {str(output_path):<41} ║")
    print(f"║  Size : {file_size_mb:.1f} MB                               ║")
    print(f"║  Cost : ${cost:.2f}                                   ║")
    print("╚══════════════════════════════════════════════════╝")
    print()


if __name__ == "__main__":
    main()
