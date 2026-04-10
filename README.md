# 🎬 Seedance 2.0 Prompt Builder — Skill for RUBRIC & Claude Code

A skill that turns any creative brief into a **structured, shot-by-shot video prompt** optimised for [Seedance 2.0](https://wavespeed.ai) — ByteDance's AI video generation model.

Every output includes four sections Seedance needs to produce great results: a shot-by-shot effects timeline, a master effects inventory, an effects density map, and an energy arc.

---

## What it does

Give it a brief like:

> "A trail runner at golden hour, mountain setting, epic but not over-the-top, 15 seconds"

Get back a fully structured prompt like:

```
SHOT 1 (0:00–0:02) — Wide Establish / Runner Enters Frame
• EFFECT: Slow push-in (scale 1.0→1.08 over 2s) + atmospheric haze overlay
• Runner appears as small figure against ridge, walking toward camera
• Wide lens, low angle, camera static then begins gentle push
• Approximately 60% speed — unhurried, contemplative opening
• EXIT: dissolve into Shot 2 via soft bloom

[...10 more shots...]

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

---

## Install in Claude Code

### Option A — Project skill (recommended)

Copy `skill/SKILL.md` into your project's `.claude/skills/` folder:

```bash
# From your project root
mkdir -p .claude/skills/seedance-prompt-builder
curl -o .claude/skills/seedance-prompt-builder/SKILL.md \
  https://raw.githubusercontent.com/MediaAI-AT/seedance-skill/main/skill/SKILL.md
```

Claude Code will auto-detect the skill. Trigger it by describing a video concept in chat.

### Option B — Global skill (available in all projects)

```bash
mkdir -p ~/AppData/Roaming/Claude/skills/seedance-prompt-builder   # Windows
# or
mkdir -p ~/.claude/skills/seedance-prompt-builder                   # Mac/Linux

curl -o <path-above>/SKILL.md \
  https://raw.githubusercontent.com/MediaAI-AT/seedance-skill/main/skill/SKILL.md
```

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

The **Video** category and **Seedance 2.0 Prompt Builder** card appear automatically — no config needed.

### Step 3 — Use it

1. Open RUBRIC → **Skill Hub** tab
2. Click **Video** in the sidebar
3. Click **Seedance 2.0 Prompt Builder**
4. Enter your brief in the input field
5. Click **Run with Claude** → your structured prompt appears instantly

---

## Works best with

- **[CineFlow Studio Standalone](https://github.com/MediaAI-AT/cineflow-studio-standalone)** — AI music video pipeline with built-in Seedance 2.0 support and an "✨ Enhance for Seedance" button that uses this skill's format
- **[RUBRIC Console](https://github.com/robonuggets/rubric)** — the agent command centre this skill is built for
- **[WaveSpeed](https://wavespeed.ai)** — the API that runs Seedance 2.0

---

## Repo structure

```
seedance-skill/
├── skill/
│   ├── SKILL.md          ← Claude Code version (auto-triggers on video briefs)
│   └── skill-hub.md      ← RUBRIC Skill Hub card version
└── README.md
```

---

---

## Credits

Prompt structure and effects breakdown format based on the work of **[Rourke Heath](https://www.youtube.com/@RourkeHeath)** — check out his YouTube channel for in-depth Seedance 2.0 tutorials and prompt techniques.

---

Built by [Media AI](https://github.com/MediaAI-AT) · Works with RUBRIC · Powered by Seedance 2.0
