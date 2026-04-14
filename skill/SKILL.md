---
name: video-prompt-builder
description: Generate complete, production-ready AI video prompts for Seedance 2.0 from any creative brief or uploaded assets — and optionally generate the actual video via WaveSpeed API. Use this skill whenever the user wants to create a video prompt, write a shot list, plan a video sequence, describe a video concept for AI generation, or mentions Seedance, Jimeng, or ByteDance video generation. Also trigger when the user shares images, videos, or audio files they want turned into a video, or says "generate the video", "make the video", "run it", "create it on WaveSpeed". Trigger on phrases like "write me a video prompt", "Seedance prompt", "shot list", "plan a video", "video concept", "brand film prompt", "ad prompt", "I have photos I want to use", "extend this video", "make a video from these images", "beat-sync", "music video", or any time the user describes a visual sequence they want generated. Make sure to use this skill for ALL Seedance-related tasks — text-only briefs, asset-based prompts, video extension, character consistency, e-commerce ads, short dramas, and direct video generation alike.
---

# Video Prompt Builder — Seedance 2.0

Craft complete, generation-ready video prompts for Seedance 2.0. The skill adapts to two modes depending on what the user has:

- **Mode A — Asset-Based**: User has images, videos, or audio to upload → build an `@reference` preamble + 4-section cinematic prompt
- **Mode B — Text-to-Video**: User has only a written brief → build the 4-section cinematic prompt directly

## Step 1 — Assess what the user has

Before writing anything, ask one question if it's not already clear:

> "Do you have any images, videos, or audio you want to use — or should I build this from your description alone?"

If the brief already makes it clear (e.g. "here are 3 photos", "extend @Video1", "I just have a concept"), skip the question and proceed.

---

## Step 2 — Platform constraints (read before writing)

Seedance 2.0 input limits:

| Type | Max count | Formats | Max size |
|---|---|---|---|
| Images | 9 | jpeg, png, webp, bmp, tiff, gif | 30 MB each |
| Videos | 3 | mp4, mov | 50 MB each, 2–15s total |
| Audio | 3 | mp3, wav | 15 MB each, ≤15s |
| **Total files** | **12 combined** | — | — |

Output: 4–15 seconds, 480p–720p, auto sound effects/music included.

**Critical restriction**: No realistic human faces in uploaded images or videos — the platform blocks them. If the user tries, flag it before they waste credits.

---

## Step 3 — MODE A: Asset-Based Prompt

Use this mode when the user has files to upload.

### 3a. Assign @ roles to every asset

Every uploaded file needs an explicit role. Never write a bare `@Image1` — always say what it's for.

| Purpose | Syntax |
|---|---|
| First frame anchor | `@Image1 as the first frame` |
| Last frame anchor | `@Image2 as the last frame` |
| Character appearance | `@Image1's character as the subject` |
| Outfit / clothing | `wearing the outfit from @Image2` |
| Scene / background | `scene references @Image3` |
| Product reference | `product details reference @Image2` |
| Camera movement | `reference @Video1's camera movement` |
| Action choreography | `reference @Video1's action choreography` |
| Full effects replication | `completely reference @Video1's effects and transitions` |
| Edit rhythm / pacing | `video rhythm references @Video1` |
| Voice / narration tone | `narration voice references @Video1` |
| Background music | `BGM references @Audio1` |
| Sound effects | `sound effects reference @Video1's audio` |
| Beat-sync cuts | `match @Video1's rhythm for beat-synced cuts` |

### 3b. Build the @ preamble

Open the prompt with all asset assignments in one clear block before the shot descriptions:

```
@Image1's character as the subject, scene references @Image2,
reference @Video1's camera movement and pacing,
BGM references @Audio1.
```

Then follow immediately with the 4-section cinematic prompt (Section 4 below).

### 3c. Use-case patterns

For common scenarios, adapt from `references/platform-reference.md` which contains ready-made patterns for: character consistency, camera replication, effects replication, video extension (forward + backward), video editing/plot subversion, music beat-matching, dialogue and voice acting, one-take sequences, e-commerce product showcases, and educational/scientific visualizations.

---

## Step 4 — 4-Section Cinematic Prompt (both modes)

Always read `references/effects-breakdown-reference.txt` first to calibrate detail level. Then output ALL FOUR sections in this exact order. Never skip one.

---

### Section 1: SHOT-BY-SHOT EFFECTS TIMELINE

Each shot follows this format:

```
SHOT [N] ([timestamp]) — [Shot Name]
• EFFECT: [Primary effect] + [secondary effects if stacked]
• [What is happening visually — subject, environment, action]
• [Camera behaviour — angle, movement, lens]
• [Speed or timing — use percentages for slow-motion]
• [How this shot exits and connects to the next]
```

Guidelines:
- Each shot is 1–4 seconds unless the brief requires longer holds
- Name effects precisely: "speed ramp (deceleration)" not "slow it down"; "digital zoom (scale-in)" not "zoom"
- Stack effects explicitly — if 3 things happen simultaneously, list all 3
- Describe transitions as creative moments, not connectors — a whip pan or bloom flash is a shot
- Describe the visual result, not an editing instruction: "the frame scales inward rapidly" not "keyframe the scale property"
- Mark the most distinctive, memorable shot: "This is the SIGNATURE VISUAL EFFECT"
- Use specific percentages for slow-motion (e.g. "approximately 20–25% speed")
- Describe motion blur, light behaviour, and atmospheric texture where relevant

---

### Section 2: MASTER EFFECTS INVENTORY

A numbered list of every distinct effect used. For each:
- Effect name
- How many times used (e.g. "used 3x")
- Which shots
- One-line description of its role in the edit

Group by category: Speed Manipulation / Camera & Lens / Particle & Light / Transitions / Digital & Compositing / Audio & Text.

---

### Section 3: EFFECTS DENSITY MAP

Break the timeline into 2–5 second segments, rated as:
- **HIGH DENSITY** — 4+ effects stacked or rapid-fire cuts
- **MEDIUM DENSITY** — 2–3 effects
- **LOW DENSITY** — 1 effect or clean footage

```
[timestamp range] = [DENSITY LEVEL] ([brief list of effects] — [count] effects in [duration])
```

Add one line describing the emotional or editorial purpose of each segment.

---

### Section 4: ENERGY ARC

Describe the video's energy structure as a narrative arc in acts. Write each act as a short paragraph (3–5 sentences), not bullet points. Explain the editorial logic — why the energy moves the way it does.

Standard structure (adapt to video length):
- **Act 1** — How it opens and grabs attention
- **Act 2** — How it develops; where signature moments land; what the video is "about"
- **Act 3** — How energy resolves and lands

A 5-second clip may only need two beats. A 30-second brand film may need four.

---

## Creative principles

1. **Contrast drives impact.** Alternate high-density and low-density moments. A clean shot after an explosion hits harder than two explosions back-to-back.
2. **Every video needs a signature effect.** One visually distinctive moment that defines the piece. Call it out explicitly in Section 1.
3. **Transitions are shots.** A whip pan, bloom flash, or motion blur smear is a creative decision, not just a cut.
4. **Specificity over vagueness.** "The frame rotates clockwise by approximately 15–20°" beats "the camera tilts." "Approximately 20–25% speed" beats "slow motion."
5. **Energy must resolve.** The final moments should feel intentional. The edit should land, not just stop.

---

## Tone

- Direct and technical — director's shot notes, not a marketing brief
- Bullet points within each shot block
- No hype language: no "stunning", "breathtaking", "amazing"
- Every detail earns its place

---

## Duration calibration

| Duration | Shots | Signature effects |
|---|---|---|
| 5–10s | 4–7, lean and punchy | 1 |
| 10–20s | 8–14, room for contrast | 1–2 |
| 20–30s | 12–20, full three-act arc | 2–3 |
| 30s+ | Scale up, maintain density contrast | 3+ |

Default to 15–20 seconds if not specified.

---

## Step 5 — Video Generation via WaveSpeed (optional)

After writing the prompt, offer to generate the actual video. Ask:

> "Want me to generate this video on WaveSpeed? It takes 1–2 minutes."

If yes, confirm the duration and run `scripts/generate_video.py`.

### Cost (720p, WaveSpeed)

| Duration | Cost |
|---|---|
| 5s | $1.20 |
| 10s | $2.40 |
| 15s | $3.60 |

**Always state the cost and wait for explicit approval before running.**

### Usage

```bash
# Set your API key first (one time)
export WAVESPEED_API_KEY=your_key_here   # Mac/Linux
set WAVESPEED_API_KEY=your_key_here      # Windows

# Text-to-video
python scripts/generate_video.py --prompt "your prompt here" --duration 5

# With custom output filename
python scripts/generate_video.py --prompt "your prompt" --duration 10 --output brand_film.mp4

# With reference files (images/video/audio)
python scripts/generate_video.py --prompt "your prompt" --duration 5 --refs logo.png hero.jpg

# Skip confirmation prompt
python scripts/generate_video.py --prompt "your prompt" --duration 5 --yes

# Different aspect ratio (default: 16:9)
python scripts/generate_video.py --prompt "your prompt" --duration 5 --aspect-ratio 9:16
```

### What the script does

1. **Shows cost summary** — duration, resolution, aspect ratio, output path, cost
2. **Asks for confirmation** — "Generate this video for $1.20? [y/N]"
3. **Uploads reference files** (if any) to WaveSpeed CDN
4. **Submits the job** — returns a prediction ID
5. **Polls until complete** — shows live status + elapsed time
6. **Downloads the MP4** — saves to the output path with progress indicator
7. **Confirms success** — shows file path, size, and cost charged

### Output filename

If no `--output` is given, the file is saved as:
```
seedance_10s_20260414_153012.mp4
```

Saved in the current working directory unless a full path is specified.

### Requirements

- Python 3.9+ (no external packages needed — stdlib only)
- `WAVESPEED_API_KEY` environment variable set

### Aspect ratios

| Ratio | Best for |
|---|---|
| `16:9` | Landscape, YouTube, desktop (default) |
| `9:16` | Portrait, TikTok, Instagram Reels |
| `1:1` | Square, Instagram feed |
| `21:9` | Cinematic ultra-wide |
| `4:3` / `3:4` | Classic or portrait formats |

---

## Common mistakes to avoid

1. **Bare @ references** — always assign a role: not just `@Video1` but `reference @Video1's camera movement`
2. **Conflicting instructions** — don't ask for "static camera" and "orbit shot" in the same segment
3. **Overloading short clips** — don't pack 6 scene changes into 4 seconds
4. **Missing audio direction** — sound design improves output; always include it when assets allow
5. **Uploading real faces** — the platform blocks them; flag this to the user before they try
6. **Vague speed descriptions** — "slow" is not enough; give a percentage
7. **Effects without contrast** — an unbroken wall of HIGH DENSITY has no impact; the map must breathe
