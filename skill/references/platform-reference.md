# Seedance 2.0 Platform Reference

## Camera Language

### Basic Movements
| Term | Description |
|---|---|
| Push in / Slow push | Camera moves toward subject |
| Pull back / Pull away | Camera moves away from subject |
| Pan left / Pan right | Camera rotates horizontally |
| Tilt up / Tilt down | Camera rotates vertically |
| Track / Follow shot | Camera follows subject movement |
| Orbit / Revolve | Camera circles around subject |
| One-take / Oner | Continuous shot, no cuts |

### Advanced Techniques
| Term | Description |
|---|---|
| Hitchcock zoom (dolly zoom) | Push in + zoom out (or vice versa) — creates vertigo/disorientation |
| Fisheye lens | Ultra-wide distorted lens |
| Low angle / High angle | Camera below or above subject eyeline |
| Bird's eye / Overhead | Top-down view |
| First-person POV | Subjective camera from character's perspective |
| Whip pan | Very fast horizontal pan creating motion blur smear |
| Crane shot | Vertical camera movement like a crane arm |

### Shot Sizes
| Term | Description |
|---|---|
| Extreme close-up (ECU) | Eyes, mouth, or small detail only |
| Close-up (CU) | Face fills frame |
| Medium close-up (MCU) | Head and shoulders |
| Medium shot (MS) | Waist up |
| Full shot (FS) | Entire body visible |
| Wide / Establishing shot | Full environment context |

---

## Style and Quality Modifiers

Append these to prompts to enhance output quality.

### Visual Style
- `Cinematic quality, film grain, shallow depth of field`
- `2.35:1 widescreen, 24fps`
- `Ink wash painting style`
- `Anime style`
- `Photorealistic`
- `High saturation neon colors, cool-warm contrast`
- `4K medical CGI, semi-transparent visualization`

### Mood / Atmosphere
- `Tense and suspenseful`
- `Warm and healing`
- `Epic and grand`
- `Comedy with exaggerated expressions`
- `Documentary tone, restrained narration`

### Audio Direction
- `Background music: grand and majestic`
- `Sound effects: footsteps, crowd noise, car sounds`
- `Voice tone reference @Video1`
- `Beat-synced transitions matching music rhythm`

---

## Use-Case Prompt Patterns

### 1. Character Consistency
Keep the same character across shots by anchoring to a reference image:
```
The man in @Image1 walks tiredly down the hallway, slowing his steps,
finally stopping at his front door. Close-up on his face — he takes a
deep breath, adjusts his emotions, replaces the weariness with a relaxed
expression. Close-up of him finding his keys, inserting into the lock.
After entering, his daughter and a pet dog run to greet him.
The interior is warm and cozy. Natural dialogue throughout.
```

### 2. Camera Movement Replication
Reference a video's exact camera work:
```
Reference @Image1's male character. He is in @Image2's elevator.
Completely reference @Video1's camera movements and the protagonist's
facial expressions. Hitchcock zoom during the fear moment, then several
orbit shots showing the elevator interior. Elevator doors open, follow
shot walking out. Exterior scene references @Image3.
```

### 3. Effects / Style Replication
Replicate transitions, ad styles, or visual effects from a reference video:
```
Replace @Video1's character with @Image1. @Image1 as the first frame.
Character puts on VR sci-fi glasses. Reference @Video1's camera work —
close orbit shot transitions from third-person to character's subjective POV.
Travel through the VR glasses into @Image2's deep blue universe.
Several spaceships shuttle toward the distance.
```

### 4. Video Extension (Forward)
Extend an existing video by adding new footage after it:
```
Extend @Video1 by 10 seconds.
1–4s: Light and shadow slowly slide across wooden table and cup.
5–8s: A coffee bean drifts down from the top of frame. Camera pushes in.
9–10s: English text appears — "Lucky Coffee / AM 7:00–10:00".
```
Set generation duration to match the extension length (extend 10s → select 10s).

### 5. Video Extension (Backward / Prepend)
Add footage before an existing video:
```
Extend backward 8s. In warm afternoon light, camera starts from the corner
with awning fluttering in the breeze, slowly tilting down to daisies
peeking out at the wall base, then pulling back to reveal the full café exterior.
```

### 6. Video Editing / Plot Subversion
Change specific elements of an existing video:
```
Subvert @Video1's plot — the man's expression shifts from tenderness to
icy cruelty. In an unguarded moment, he shoves the female lead off the bridge.
The action is decisive, without hesitation. She surfaces and screams:
"You've been lying to me from the start!"
```

### 7. Music Beat-Matching
Sync visuals to audio rhythm:
```
@Image1 @Image2 @Image3 @Image4 @Image5 @Image6 — match the keyframe
positions and overall rhythm of @Video1 for beat-synced cuts.
Characters should have more dynamic movement. Overall visual style more
dreamlike with strong visual tension.
```

### 8. Dialogue and Voice Acting
Include character dialogue with voice direction:
```
In the "Cat & Dog Roast Show" — emotionally expressive comedy:
Cat host (licking paw, rolling eyes): "Who understands my suffering?
This one next to me does nothing but wag his tail and destroy sofas..."
Dog host (head tilted, tail wagging): "You're one to talk?
You sleep 18 hours a day, wake up just to con humans out of canned food..."
```

### 9. One-Take / Long Take
Continuous single-shot sequences:
```
@Image1 @Image2 @Image3 @Image4 — one-take tracking shot following a runner
from the street, up stairs, through a corridor, onto a rooftop,
finally overlooking the city. No cuts throughout.
```

### 10. E-Commerce / Product Showcase
Product-focused advertising:
```
Deconstruct the reference image. Static camera. Hamburger suspended and rotating
mid-air. Ingredients gently separate while maintaining shape and proportion.
Smooth motion, no extra effects. Hamburger splits apart — golden sesame bun,
fresh lettuce, dewy tomato slices, two thick beef patties with melting cheddar —
all slowly descend and perfectly reassemble. Cheese continues melting
and dripping throughout. Maintain ultimate food aesthetics.
```

### 11. Educational / Scientific Visualization
Medical or science content:
```
15-second health educational clip.
0–5s: Transparent blue human upper body. Camera slowly pushes into a clear artery.
Blood flows smoothly, clean blue color.
5–10s: Symbolic sugar and fat particles enter the bloodstream. Blood gradually
thickens, yellowish lipid deposits form on vessel walls.
10–15s: Vessel lumen visibly narrows, flow speed decreases.
Before/after comparison creates visual contrast. Colors darken.
Style: 4K medical CGI, semi-transparent visualization.
```
