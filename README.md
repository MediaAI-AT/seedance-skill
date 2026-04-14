# 🎬 Seedance 2.0 Prompt Builder — Skill for RUBRIC & Claude Code

> **This is a merged skill** — combining the cinematic shot-by-shot prompt structure from [MediaAI-AT's original skill](https://github.com/MediaAI-AT/seedance-skill) with the Seedance 2.0 platform knowledge (@ reference system, input constraints, use-case patterns) from [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill). The result covers both pure text-to-video workflows and full asset-based generation in a single skill.

A skill that turns any creative brief **or uploaded assets** into a complete, generation-ready video prompt for [Seedance 2.0](https://wavespeed.ai) — ByteDance's AI video generation model.

Works in two modes:
- **Text-to-video** — describe a concept, get a structured prompt with shot-by-shot effects timeline, density map, and energy arc
- **Asset-based** — share images, videos, or audio and the skill builds an `@reference` prompt with full cinematic breakdown

Every output includes the four sections Seedance needs to produce great results: a shot-by-shot effects timeline, a master effects inventory, an effects density map, and an energy arc.

---

## What it does

### Mode A — You have a written brief

Give it something like:

> "A trail runner at golden hour, mountain setting, epic but not over-the-top, 15 seconds"

Get back a fully structured prompt:

```
SHOT 1 (0:00–0:02) — Wide Establish / Runner Enters Frame
• EFFECT: Slow push-in (scale 1.0→1.08 over 2s) + atmospheric haze overlay
• Runner appears as small figure against ridge, walking toward camera
• Wide lens, low angle, camera static then begins gentle push
• Approximately 60% speed — unhurried, contemplative opening
• EXIT: dissolve into Shot 2 via soft bloom

[...more shots...]

MASTER EFFECTS INVENTORY
1. Speed ramp (deceleration) — used 3x — Shots 4, 7, 10
...

EFFECTS DENSITY MAP
0:00–0:06 = LOW DENSITY (push-in, haze — 2 effects in 6s)
0:06–0:12 = HIGH DENSITY (speed ramp + zoom + motion blur + whip pan — 4 effects in 2s)
...

ENERGY ARC
Act 1 (0:00–0:05): Atmospheric entry...
```

### Mode B — You have assets to upload

Share your files and describe what you want:

> "I have a product photo (@Image1) and a reference ad video (@Video1) — make a 10s product showcase"

The skill assigns `@reference` roles, maps platform constraints, and produces:

```
@Image1 as the first frame, product details reference @Image1,
reference @Video1's camera transitions and pacing.

SHOT 1 (0:00–0:03) — Product Entry
• EFFECT: Digital zoom (scale-in) + anamorphic lens flare (gold)
...
```

Supports all Seedance input types: images, videos, audio — up to 12 files combined.

---

## Capabilities

| Use case | Supported |
|---|---|
| Text-to-video brief → structured prompt | ✅ |
| Character consistency across shots | ✅ |
| Camera movement replication from reference video | ✅ |
| Effects / transition style replication | ✅ |
| Video extension (forward or backward) | ✅ |
| Video editing / plot subversion | ✅ |
| Music beat-matching | ✅ |
| Dialogue and voice acting | ✅ |
| One-take / long take sequences | ✅ |
| E-commerce product showcases | ✅ |
| Educational / scientific visualizations | ✅ |
| **Generate actual video via WaveSpeed API** | ✅ |
| **Save MP4 locally with cost confirmation** | ✅ |

---

## Generate the actual video

Once you have a prompt, Claude can run it directly via the WaveSpeed API:

```
"Generate this video on WaveSpeed"
```

Claude will show the cost, ask for confirmation, generate the video, and save it as an MP4 locally.

### Pricing (720p)

| Duration | Cost |
|---|---|
| 5s | $1.20 |
| 10s | $2.40 |
| 15s | $3.60 |

### Requirements

- Python 3.9+ (stdlib only — no pip installs)
- A [WaveSpeed](https://wavespeed.ai) API key set as `WAVESPEED_API_KEY`

### What happens

1. Claude shows a cost summary and asks: *"Generate this video for $1.20? [y/N]"*
2. Uploads any reference files to WaveSpeed CDN
3. Submits the job and polls until complete (~1–2 min)
4. Downloads the MP4 and saves it locally
5. Reports file path, size, and cost

---

## Install in Claude Code

### Option A — Project skill (recommended)

```bash
mkdir -p .claude/skills/video-prompt-builder
curl -o .claude/skills/video-prompt-builder/SKILL.md \
  https://raw.githubusercontent.com/MediaAI-AT/seedance-skill/main/skill/SKILL.md

mkdir -p .claude/skills/video-prompt-builder/references
curl -o .claude/skills/video-prompt-builder/references/effects-breakdown-reference.txt \
  https://raw.githubusercontent.com/MediaAI-AT/seedance-skill/main/skill/references/effects-breakdown-reference.txt
curl -o .claude/skills/video-prompt-builder/references/platform-reference.md \
  https://raw.githubusercontent.com/MediaAI-AT/seedance-skill/main/skill/references/platform-reference.md
```

Claude Code will auto-detect the skill. Trigger it by describing a video concept or sharing assets in chat.

### Option B — Global skill (available in all projects)

```bash
# Windows
mkdir -p ~/AppData/Roaming/Claude/skills/video-prompt-builder
# Mac / Linux
mkdir -p ~/.claude/skills/video-prompt-builder
```

Then download all three files (SKILL.md + both references) into that folder using the URLs above.

---

## Install in RUBRIC Skill Hub

The Skill Hub version appears as a card in the **Video** category with a "Run with Claude" button.

### Step 1 — Copy the skill file

```bash
mkdir -p <your-rubric-dir>/skill-hub/skills/video

curl -o <your-rubric-dir>/skill-hub/skills/video/video-seedance-prompt-builder.md \
  https://raw.githubusercontent.com/MediaAI-AT/seedance-skill/main/skill/skill-hub.md
```

Replace `<your-rubric-dir>` with your RUBRIC installation path (e.g. `C:/Users/you/Documents/Rubric`).

### Step 2 — Restart RUBRIC

```bash
cd <your-rubric-dir>/scaffold
node server.js
```

### Step 3 — Use it

1. Open RUBRIC → **Skill Hub** tab
2. Click **Video** in the sidebar
3. Click **Seedance 2.0 Prompt Builder**
4. Enter your brief or describe your assets
5. Click **Run with Claude** → your structured prompt appears instantly

---

## Works best with

- **[CineFlow Studio Standalone](https://github.com/MediaAI-AT/cineflow-studio-standalone)** — AI music video pipeline with built-in Seedance 2.0 support and an "✨ Enhance for Seedance" button that uses this skill's format
- **[RUBRIC Console](https://github.com/robonuggets/rubric)** — the agent command centre this skill is built for
- **[WaveSpeed](https://wavespeed.ai/?ref=krzysztof)** — the API that runs Seedance 2.0

---

## Repo structure

```
seedance-skill/
├── skill/
│   ├── SKILL.md                              ← Claude Code version (auto-triggers on video briefs)
│   ├── skill-hub.md                          ← RUBRIC Skill Hub card version
│   ├── scripts/
│   │   └── generate_video.py                 ← WaveSpeed API: generate, poll, download MP4
│   └── references/
│       ├── effects-breakdown-reference.txt   ← Cinematic effects calibration guide
│       └── platform-reference.md             ← Camera tables, modifiers, 11 use-case patterns
└── README.md
```

---

## Credits

This skill merges the best of two approaches:

- **Platform knowledge, @ reference syntax, and use-case patterns** — from **[dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill)** — a comprehensive Seedance 2.0 prompt writing skill covering input constraints, camera language, and ready-to-use templates for ads, dramas, MVs, and more.

- **Cinematic shot grammar, effects breakdown structure, and energy arc format** — originally developed for this repo, inspired by the work of **[Rourke Heath](https://www.youtube.com/@RourkeHeath)** on YouTube — check out his channel for in-depth Seedance 2.0 tutorials and prompt techniques.

---

Built by [Media AI](https://github.com/MediaAI-AT) · Works with RUBRIC · Powered by Seedance 2.0

---

## Changelog

### v1.1.0 — WaveSpeed API Integration + Bug Fixes

**Critical bug fixes in `generate_video.py`:**

- **Fixed file upload endpoint** — was calling `/api/v3/files/upload` (returns 404); correct endpoint is `/api/v3/media/upload/binary`. This was the root cause of character inconsistency — all reference images silently failed to upload, so Seedance generated videos from text only with random characters instead of your references.
- **Fixed poll URL** — now uses the `urls.get` field from the job submission response instead of a hardcoded path that doesn't exist on the WaveSpeed API
- **Fixed UTF-8 encoding crash on Windows** — Unicode box-drawing characters in the cost summary caused a `cp1252` codec error on Windows terminals; fixed with a UTF-8 stdout/stderr wrapper at script startup
- **Fixed output parsing** — `outputs[0]` from the completed job can be a plain string URL or an object with a `url` field; both cases are now handled

**Skill improvements:**

- Added **Mode A (Asset-Based)** with full `@reference` system — assign explicit roles to images, videos, and audio files
- Added **platform constraints table** — max 9 images, 3 videos, 3 audio, 12 total files; no real human faces
- Added **11 use-case patterns** in `references/platform-reference.md` (character consistency, camera replication, e-commerce, beat-sync, etc.)
- Added **Step 5** — after writing the prompt, the skill offers to run `generate_video.py` directly

### v1.0.0 — Merged Skill Release

- Combined cinematic shot grammar + effects breakdown structure from MediaAI-AT with @ reference system + platform knowledge from [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill)
- Full 4-section prompt output: shot-by-shot timeline, effects inventory, density map, energy arc
- WaveSpeed API script for direct video generation and download
