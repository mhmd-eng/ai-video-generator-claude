---
name: seedance-food-beverage
description: Generate appetite-driven food and beverage video prompts for Seedance 2.0 on Higgsfield. Use for restaurant and cafe content, menu item hero shots, cocktail and coffee videos, recipe and cooking clips, bakery and dessert reveals, packaged food (CPG) ads, food delivery creative, or any content where the product is edible. Triggers on food, drink, beverage, restaurant, cafe, coffee, cocktail, bar, menu, dish, recipe, cooking, chef, kitchen, bakery, dessert, snack, sizzle, pour, ASMR food, mukbang, tasting, plating.
---

# Food & Beverage — Appetite-Driven Video Prompts

Food video does not sell a product. It triggers a reflex. The viewer's mouth waters before their brain decides to watch, and every technical choice in the prompt exists to shorten the distance between the first frame and that reflex.

This skill generates Seedance 2.0 prompts engineered around the appetite response: gloss, heat, motion, and sound — in that order of priority.

---

## 1. Input Specifications

**Required inputs:**
- Subject (the dish, drink, or product being filmed)
- Temperature state (hot / cold / ambient — this drives every lighting and effect decision)
- Category (restaurant, cafe, bar, bakery, CPG package, home cooking, delivery)

**Optional inputs:**
- Cuisine or brand context (specialty coffee, izakaya, third-wave bakery, fast casual, fine dining)
- Hero texture (crisp, molten, flaky, creamy, effervescent, charred, glazed)
- Intended placement (Reels, TikTok, in-store menu screen, delivery app tile, website hero)
- Human presence (hands only / chef visible / no human)

**Output format:**
- One complete Seedance 2.0 prompt block per request
- Duration note (6s / 8s / 10s recommended for food; 4s for single-action ASMR)
- Lighting preset label
- Sound stack specification

---

## 2. Material References

- **Images:** Up to 9 — dish photos, plating references, packaging, restaurant interior, ingredient shots
- **Videos:** Up to 3 — existing kitchen footage, motion references, brand b-roll
- **Audio:** Up to 3 — ambient kitchen or cafe tone, music bed, ASMR texture recording
- **Max assets:** 12 total combined
- **Reference syntax:** `@material[name]` within prompts
- **Output:** 4-15 seconds, 720p with synchronized audio

Standard mapping for this skill:
- `@material[image1]` — hero dish or drink reference
- `@material[image2]` — environment / table setting / restaurant interior
- `@material[image3]` — packaging or branding
- `@material[audio1]` — ambient or music bed

---

## 3. The Appetite Response: Why Food Video Is Different

Every other category in this skill set sells an idea. Food sells a physical craving, and craving is triggered by a short list of visual cues the brain reads as *fresh, hot, and safe to eat*.

| Cue | What the brain reads | How to prompt it |
|---|---|---|
| **Gloss** | Moisture = fresh, not stale | "wet sheen on surface, specular highlights catching key light, glossy glaze" |
| **Steam** | Hot = cooked, safe, just-made | "visible steam rising in backlit wisps, curling upward slowly" |
| **Motion** | Being made now = for me | "sauce still settling, cheese still stretching, liquid still swirling" |
| **Sound** | Texture confirmation | "crisp amplified crunch, sizzle, fizz, pour" |
| **Deformation** | Softness, yield, richness | "fork breaking crust, cream collapsing, bread tearing open" |

**The rule that governs everything:** food must look *in progress*, never finished. A static perfect plate reads as a photograph. A plate where sauce is still spreading reads as a meal. Every prompt should contain at least one element still in motion at the final frame.

**The second rule:** never light food from the front. Flat frontal light kills gloss, kills steam, kills texture. Food is lit from behind or from a hard side, always.

---

## 4. 2-Second Hook Patterns

Food hooks are physical events, not concepts. Each of these lands the appetite reflex inside 2 seconds.

### 4.1 Liquid Hooks

| Pattern | Mechanism | Prompt Template |
|---|---|---|
| **The Pour** | Continuous liquid motion is involuntarily watchable | "Extreme close-up, macro lens. [Liquid — espresso, milk, syrup, batter] pours in a continuous ribbon from frame-top into [vessel]. Backlit so the stream glows translucent. 0.5x slow motion. Surface rises and folds. Sound: pure pour, no music. Camera locked off." |
| **The Fizz Bloom** | Carbonation = cold, sharp, refreshing | "Macro on glass rim. [Carbonated liquid] hits ice at 0.3s, explosive bubble bloom races up the glass wall. Condensation beads already on exterior. Hard backlight makes bubbles read as white sparks against dark background. Sound: crisp effervescent hiss." |
| **The Drip** | Anticipation — the brain waits for it to fall | "Extreme macro, shallow depth of field. Single drop of [honey / sauce / chocolate / yolk] hangs at the edge of [subject], stretching under its own weight for 1.2s. At 1.4s it releases and falls. Camera does not move. Sound: near-silence, then a single soft impact." |
| **The Swirl** | Two liquids meeting reads as craft | "Overhead top-down. [Milk / cream / syrup] enters [coffee / soup / cocktail] and blooms outward in a slow fractal swirl. 0.4x speed. Warm key from hard left rakes the surface to show viscosity. Sound: quiet liquid movement only." |

### 4.2 Heat Hooks

| Pattern | Mechanism | Prompt Template |
|---|---|---|
| **The Sizzle Drop** | Sound and steam arrive simultaneously | "Tight macro on hot cast-iron surface, heat shimmer visible. At 0.4s [protein / vegetable] drops into frame and hits the pan. Instant violent sizzle, oil scatter, steam burst rising into hard backlight. Camera flinches 2 degrees on impact. Sound: explosive sizzle at full level, no music." |
| **The Steam Rise** | Heat made visible | "Static macro, dark background. [Dish] center frame. Steam rises in slow curling ribbons, strongly backlit so vapor glows white against black. Camera imperceptibly pushes in over 2s. No other movement. Sound: room tone and faint bubbling only." |
| **The Flame Kiss** | Fire is a primal attention trigger | "Side angle on [grill / pan / torch]. At 0.6s a flame flares upward across the subject for 0.4s, then recedes. Char marks and blistering visible in the flame's light. Everything else in deep shadow. Sound: gas roar and fat crackle, sharp attack." |
| **The Cheese Pull** | Elastic deformation = richness | "Macro, backlit. Hands lift [slice / portion] slowly upward out of frame-top. Molten cheese stretches into long glossy strands that catch rim light and slowly thin. 0.5x slow motion. Steam escapes from the break. Sound: soft tearing and a low ambient hum." |

### 4.3 Texture Hooks

| Pattern | Mechanism | Prompt Template |
|---|---|---|
| **The Cut Reveal** | Interior state is the payoff | "Overhead macro. Knife enters [subject] at 0.5s and passes through in one clean slow stroke. Interior revealed — [molten center / layered crumb / pink medium-rare / custard]. Filling moves or flows outward after the cut. Hard raking sidelight. Sound: crust crack, then blade against board." |
| **The Crunch** | Audio-first hook | "Extreme close-up on [crisp subject]. At 0.8s it snaps or shatters, fragments scattering in slow motion. Crumbs suspended mid-air. Hard directional light picks out every edge and shard. Sound: hyper-close amplified crunch, binaural, no music at all." |
| **The Frost Bloom** | Cold made visible | "Macro on [glass / can / bottle] straight from the freezer. Frost crystals visible on the surface, condensation beads forming and running down. Backlit rim light makes the ice read blue-white. Camera slow vertical tilt following one droplet's descent. Sound: soft ice crackle." |
| **The Dust Fall** | Slow-motion particulate is hypnotic | "Backlit macro. [Powdered sugar / cocoa / flour / grated cheese / chili flake] falls through a shaft of hard light onto [subject] below. 0.25x slow motion. Individual particles glow against a black background. Camera locked off. Sound: near-silence, faint granular patter." |

---

## 5. Category Playbooks

### 5.1 Hot Food & Restaurant Dishes
- **Priority cues:** steam, gloss, char, sauce motion
- **Lighting:** hard backlight for steam separation, warm key at 3200K from the side
- **Camera:** slow push-in, 45-degree hero angle, overhead for composed plates
- **Background:** dark wood, slate, or deep shadow — never white
- **Anchor phrases:** "steam backlit against dark background", "glossy sauce catching raking light", "charred edges with visible blistering", "cast iron still radiating heat"

### 5.2 Coffee & Cafe
- **Priority cues:** pour, crema, milk texture, steam, ceramic
- **Lighting:** soft window daylight from one side, 5600K, gentle falloff
- **Camera:** overhead top-down for latte art, macro side angle for pour, rack focus from cup to barista
- **Background:** warm wood, matte ceramic, unfocused cafe interior with bokeh
- **Anchor phrases:** "espresso crema forming tiger-striping", "microfoam folding into the pour", "steam wand vapor in window light", "top-down latte art rosetta pouring in one motion"

### 5.3 Cocktails & Bar
- **Priority cues:** ice clarity, layering, garnish, condensation, colored liquid
- **Lighting:** dark bar with a single hard key or neon accent, deep shadow, strong specular hits on glass
- **Camera:** locked-off hero, slow orbit around the glass, macro on ice crack
- **Background:** near-black with a single practical light source
- **Anchor phrases:** "large clear ice cube with visible internal clarity", "spirit layering over ice in slow ribbons", "citrus twist expressing oils in a fine mist", "neon rim light through amber liquid"

### 5.4 Bakery & Pastry
- **Priority cues:** flake, crumb, lamination, steam from the tear, sugar
- **Lighting:** hard raking sidelight at a low angle to exaggerate surface relief
- **Camera:** macro, extremely shallow depth of field, slow drift across the surface
- **Background:** flour-dusted stone, linen, matte neutral
- **Anchor phrases:** "visible lamination layers in cross-section", "shattering flake fragments falling", "open irregular crumb structure", "steam escaping from a torn interior"

### 5.5 Desserts & Chocolate
- **Priority cues:** molten flow, glaze, gloss, temperature contrast
- **Lighting:** single hard source, high contrast, dark surround
- **Camera:** macro static with subject motion, or slow tilt down the pour
- **Anchor phrases:** "molten center flowing outward after the spoon breaks the surface", "mirror glaze poured in one continuous sheet", "tempered chocolate snap with a clean fracture edge"

### 5.6 Fresh Produce & Health
- **Priority cues:** water droplets, saturated green, crispness, natural daylight
- **Lighting:** bright diffused daylight, high key, cool-neutral 5600K — the one category where bright and clean works
- **Camera:** overhead top-down, slow lateral slider, water impact in slow motion
- **Anchor phrases:** "water droplets beading on a waxy leaf surface", "produce dropping into water with a slow-motion crown splash", "crisp fracture on the bite"

### 5.7 Packaged Food (CPG)
- **Priority cues:** package legibility, product escaping the package, brand color
- **Lighting:** clean studio with controlled specular highlights, product-photography discipline
- **Camera:** locked-off hero with product motion, or 90-degree tilt reveal from package to contents
- **Note:** the package must be readable in the final frame and the product must be shown *outside* the package by the midpoint
- **Anchor phrases:** "package center frame with controlled specular highlight on the label", "contents cascading from the opened package in slow motion", "hero product suspended in front of the pack"

### 5.8 Restaurant Atmosphere & Chef
- **Priority cues:** human craft, motion, environment, warmth
- **Lighting:** practical lights in frame (pendants, pass lamps, candles), warm and moody
- **Camera:** gimbal push through the pass, rack focus from chef's hands to face, handheld is permitted here only
- **Anchor phrases:** "gimbal push through the kitchen pass, heat lamps flaring", "rack focus from plating hands to the chef's face", "warm practical pendants in the background bokeh"

---

## 6. Camera Movement Library

Food camera work is macro-dominant. Distance kills appetite.

| Move | Duration | Purpose | Prompt Phrasing |
|---|---|---|---|
| **Macro Push-In** | 2-3s | Intimacy, texture reveal | "Extremely slow macro push-in toward [subject], covering 15% of frame width over 3 seconds. Focus holds on the hero texture. No jitter." |
| **Overhead Top-Down** | static or 2s | Composition, pours, plating | "Locked-off overhead top-down at 90 degrees. Subject centered. Slight rotation of the surface rather than the camera." |
| **The 90-Degree Tilt Reveal** | 2s | Package to contents, table to dish | "Camera begins at flat overhead, tilts down to a level 0-degree side angle over 2 seconds, revealing the height and layering of the subject." |
| **Tabletop Slider** | 3s | Ingredient reveal, sequence | "Smooth lateral slider left-to-right across the surface at constant speed, passing foreground ingredients in soft bokeh before settling on the hero." |
| **Probe Lens Fly-Through** | 2-3s | Impossible intimacy | "Snorkel probe lens travels forward at surface level, passing between [ingredients / glasses / garnish] and arriving at the hero subject. Ultra-wide macro perspective, everything in deep focus." |
| **Slow Plate Orbit** | 3-4s | Dimensionality | "Camera orbits 45 degrees around the plate at a fixed low angle, maintaining constant distance. Lighting shifts across the surface as the angle changes." |
| **Rack Focus Pull** | 1-2s | Shift attention, add depth | "Focus plane pulls from foreground garnish to the hero subject behind it over 1.2 seconds. Shallow depth of field, f/1.8 equivalent, creamy bokeh." |
| **Impact Flinch** | 0.2s | Physicality on a drop or hit | "Camera shifts 2 degrees and settles at the moment of impact, as if reacting to the force. Subtle — not a shake." |
| **Follow the Fall** | 1-2s | Pours, drops, dust | "Camera tilts downward at the exact speed of the falling [liquid / particle], keeping it fixed in frame while the background travels upward." |

**Avoid in food:** whip pans, snap zooms, dutch angles, drone moves, anything above 1x speed. Food lives in slow motion — 0.25x to 0.5x is the working range.

---

## 7. Lighting Presets

### Backlit Steam
The default for anything hot. Key light is behind and slightly above the subject, aimed back toward camera. Vapor scatters the light and reads as glowing white; the dish itself is shaped by a weak bounce from camera-front.

```
"Hard key light positioned behind and above the subject, aimed toward camera.
Steam and vapor glow bright against a deep shadow background. Small white bounce
card at camera-front lifts the front of the dish just enough for detail.
Background falls to near-black. Contrast ratio 8:1."
```

### Raking Sidelight
The texture preset. A hard source almost parallel to the surface exaggerates every crumb, flake, char mark, and grain.

```
"Single hard light source at 85 degrees to the side, nearly parallel to the
surface. Every surface irregularity casts a long shadow — crumb, char, flake,
and grain read at maximum relief. No fill on the shadow side. Warm 3200K."
```

### Window Daylight
The cafe and fresh-food preset. Soft, directional, believable.

```
"Large soft window source from camera-left, 5600K daylight. Gentle falloff
across the table surface. Single white bounce from camera-right lifting shadows
to a 3:1 ratio. Natural, unstyled, warm neutral grade."
```

### Dark Restaurant
Moody hospitality. Practicals in frame do the storytelling.

```
"Low-key restaurant interior. Practical pendant light directly above the table
acting as key, warm 2700K, creating a pool of light with hard falloff into
darkness. Background tables visible only as warm bokeh points. No fill."
```

### Clean Studio Product
CPG and packaged goods only.

```
"Two large softboxes at 45 degrees either side, plus a controlled overhead strip
for the top specular highlight. Seamless neutral background with a subtle
gradient. Specular highlights placed deliberately on the package edge and the
product's glossy surface. No unmotivated shadows."
```

### Neon Bar
Cocktails and nightlife.

```
"Deep black bar environment. Single neon source [magenta / cyan / amber] from
behind the glass, transmitting through the liquid and making it glow from within.
Hard rim light on the glass edge. Everything outside the glass falls to black."
```

---

## 8. Texture & Physics Vocabulary

Seedance 2.0 responds to material-specific language far better than to adjectives like "delicious" or "tasty." Never use taste words — they carry no visual information. Use these instead:

| Domain | Words that work |
|---|---|
| **Surface** | glossy, matte, lacquered, glazed, wet sheen, specular, tacky, dusted, blistered |
| **Structure** | flaky, laminated, open crumb, dense, aerated, fibrous, gelatinous, brittle |
| **Heat** | charred, seared, blistered, caramelized, molten, bubbling, rendered, radiant |
| **Cold** | frosted, condensating, beaded, crystalline, slushy, set, firm |
| **Liquid** | viscous, thin, ribboning, cascading, emulsified, effervescent, foamed, syrupy |
| **Motion** | settling, spreading, collapsing, stretching, folding, blooming, cascading, yielding |

**Replace:** "delicious pasta" → "glossy sauce clinging to fresh pasta, still steaming, sauce settling into the ridges"
**Replace:** "tasty burger" → "seared patty with rendered fat, molten cheese draping the edge, glazed brioche with a wet sheen"

---

## 9. Sound Design Stack

Food is the only category where sound can carry the entire hook. In many food videos the correct music track is *no music*.

**The four layers:**

1. **Texture layer (primary)** — the food's own sound, recorded hyper-close: sizzle, crunch, pour, fizz, crack, tear, bubble
2. **Ambient layer** — kitchen room tone, cafe murmur, bar background, or true silence
3. **Impact layer** — the single hit synced to the hero moment: the drop, the cut, the snap
4. **Music layer (optional, last)** — enters after 2s if at all; never competes with the texture layer

| Content type | Sound design | Prompt phrasing |
|---|---|---|
| **ASMR / texture-led** | Texture only, no music | "Audio: hyper-close binaural recording of [texture sound] at full level. No music, no voiceover. Room tone barely audible beneath. The sound is the content." |
| **Restaurant / atmosphere** | Ambient + light music | "Audio: warm restaurant ambience — distant conversation, cutlery, low kitchen activity. Soft acoustic bed enters at 2s, kept well below the foreground sizzle." |
| **Cafe / lifestyle** | Ambient + mellow beat | "Audio: cafe room tone, espresso machine hiss and grinder in the background. Mellow lo-fi beat enters at 1.5s at low level. Pour sound stays foreground." |
| **Bar / cocktail** | Impact-led + sparse music | "Audio: near-silence, then ice against glass at 0.8s, shaker rhythm, pour. Sparse downtempo bass enters at 3s. Every liquid sound stays above the music." |
| **CPG / ad** | Impact + branded music | "Audio: package crinkle and open at 0.6s, product crunch at 2s, upbeat music bed underneath from 0s. Sound effects sit clearly above the music at every hero beat." |

---

## 10. Color & Grade

Appetite has a color temperature, and it is warm.

- **Push warm:** cooked food, bread, meat, coffee, spirits. Amber, gold, deep red-brown. "Warm grade, amber-forward, lifted reds and oranges."
- **Push cool only for:** fresh produce, seafood on ice, cold drinks, dairy. "Cool-neutral grade, clean whites, saturated greens."
- **Never:** green or blue cast on cooked food or meat — it reads as spoiled. State this explicitly when the environment might introduce it: "no green or blue cast on the food; keep the dish warm even if the ambient light is cool."
- **Saturation:** high on the food, low on everything else. "Food saturated and rich; environment desaturated so the dish is the only source of color in frame."
- **Blacks:** keep them deep. Lifted, milky blacks make food look flat and cheap. "Deep crushed blacks in the background, no lift."

---

## 11. Platform Optimization

**TikTok (9:16)** — Hook by 1.5s, and it must be a sound event. Texture audio over trending music where possible. Keep the dish in the center 80%; bottom 20% is covered by UI. Loop by returning to the opening composition.

**Instagram Reels (9:16)** — Hook by 2s. Higher polish expected; grade matters. The cover frame must survive as a static grid image, so plan one frame with the finished hero at maximum gloss.

**YouTube Shorts (9:16)** — Hook by 2-3s. Process content performs — show the making, not just the result. Longer builds are tolerated.

**Pinterest (2:3 or 9:16)** — Overhead top-down dominates. Bright, clean, high-key. Recipe and ingredient layouts outperform moody restaurant looks here.

**In-store menu screens & delivery apps (16:9 or 1:1)** — Loop seamlessly, no hard cuts, no text dependency, and the dish must be identifiable in a single frame at small size. Keep the whole dish in frame; avoid extreme macro.

**LinkedIn (16:9 or 1:1)** — Hospitality B2B. Lead with the craft and the people, not the close-up. Slower pacing is acceptable.

---

## 12. Failure Modes

AI food video fails in recognizable ways. Name the failure in the prompt to suppress it.

| Failure | What it looks like | Prompt correction |
|---|---|---|
| **Plastic sheen** | Uniform waxy gloss over the whole subject | "Varied surface finish — glossy where sauce or fat pools, matte on dry and floured areas. Not uniformly shiny." |
| **Impossible steam** | Steam with no source, or too much of it | "Steam originates only from the hot surface itself, thin and intermittent, dissipating within 30cm. Not fog." |
| **Floating garnish** | Herbs and toppings hovering, not resting | "Garnish rests physically on the surface with contact shadows, slightly settled into the sauce." |
| **Uncanny hands** | Distorted fingers handling food | "Hands enter frame partially and briefly, seen from behind or above, fingers not fully extended toward camera." Or: "No hands or people in frame." |
| **Over-perfect symmetry** | Machine-plated, lifeless | "Naturally imperfect plating — one element slightly off-center, a single crumb beside the plate, an irregular sauce edge." |
| **Dead final frame** | Everything stops moving | "At the final frame, [steam / sauce / bubbles] is still in motion. The scene never fully settles." |
| **Wrong scale** | Macro that loses the dish | "Frame retains enough context that the dish is identifiable — macro on texture but the silhouette of the whole item stays readable." |

---

## 13. Complete Example Prompts

### Example 1: Specialty Coffee Pour (8s)

```
SEEDANCE 2.0 PROMPT:

Macro side angle on a matte ceramic cup filled with fresh espresso, dark crema
surface with tiger-striping visible. Soft window daylight from camera-left at
5600K, single white bounce from the right lifting shadows to a 3:1 ratio.
Warm wood counter, cafe interior behind in unfocused bokeh.

0-1.5s: Static macro on the crema surface. Micro-movement in the foam as it
settles. Steam rises in thin intermittent wisps, backlit by the window so vapor
glows against the darker background. Camera imperceptibly pushes in. Sound:
cafe room tone, distant grinder, espresso machine hiss.

1.5-3.5s: A steel pitcher enters frame-top. Microfoam begins to pour in a thin
controlled stream, striking the crema off-center and sinking beneath it.
0.5x slow motion. The pour is continuous and uninterrupted. Sound: the pour
becomes the foreground; mellow lo-fi beat enters underneath at low level.

3.5-6s: Camera tilts to an overhead top-down at 90 degrees over 1.5 seconds
as the pour widens. The rosetta forms — foam surfacing in successive folds,
each layer pushing the previous one outward. Surface tension visible at the
edges of each fold. Warm brown and cream, high saturation on the cup contents,
desaturated wood surround.

6-8s: Pitcher lifts away, drawing the final line through the pattern. Camera
holds overhead, locked off. The surface is still settling at the last frame —
one edge of the pattern continues to spread by a millimeter. Steam still rising.

Sound: 0-1.5s cafe ambience only. 1.5s pour foreground. 2s lo-fi bed enters
low. 6-8s music holds, pour sound decays to room tone. No voiceover.

Grade: warm neutral, deep browns, clean cream whites, deep blacks in the
background bokeh. No blue cast.

Material references: @material[image1] for the cup and latte art reference.
@material[image2] for the cafe interior.
```

---

### Example 2: Burger Hero — Sizzle to Cheese Pull (10s)

```
SEEDANCE 2.0 PROMPT:

Extreme macro on a cast-iron skillet radiating visible heat shimmer. Deep
shadow environment, hard key light positioned behind and above the pan aimed
toward camera, small bounce at camera-front. Background falls to near-black.
Contrast ratio 8:1. Warm 3200K.

0-1s: Heat shimmer over empty iron for 0.4s. At 0.4s a seasoned beef patty
drops into frame and hits the surface. Violent immediate sizzle, oil scattering
outward, steam bursting upward into the backlight and glowing white. Camera
shifts 2 degrees on impact and settles. Sound: explosive sizzle at full level,
no music.

1-3s: Macro drift across the sear. Crust forms and darkens — visible Maillard
browning, rendered fat pooling and glossing the edges, irregular charred spots.
Raking backlight exaggerates every ridge of the crust. Sound: sustained sizzle,
fat popping intermittently.

3-5s: A slice of cheese lands on the patty and begins to slump. Time compresses
slightly. The edges soften and drape over the sides, glossy where it melts,
still matte at the center. Steam continues from beneath. Sound: sizzle drops in
level, low bass music bed enters.

5-7.5s: Cut to the assembled burger on a dark slate surface, low 15-degree hero
angle. Glazed brioche with a wet sheen, sesame catching the backlight. Sauce
visibly settling at the edge where the bun meets the patty — still moving.
Camera slow push-in covering 15% of frame width.

7.5-10s: Hands enter from frame-bottom, seen from behind, and lift the top half
slowly upward out of frame. Molten cheese stretches into long glossy strands
catching the rim light, thinning as they extend. 0.5x slow motion. Steam
escapes from the break. Camera follows the lift upward. Final frame: strands
still stretching, not yet broken.

Sound: 0-1s silence then explosive sizzle. 1-3s sustained sizzle foreground.
3s low bass bed enters. 7.5-10s soft tearing and stretch sound over music.
Sizzle stays audible under everything.

Grade: warm amber-forward, lifted reds and oranges, deep crushed blacks in the
background. Food saturated, environment desaturated. No green or blue cast on
the meat.

Suppress: uniform plastic gloss — surface finish varies, glossy where fat pools,
matte on the bun's dry areas. Garnish rests with contact shadows.

Material references: @material[image1] for the burger build reference.
```

---

### Example 3: Cocktail Build (8s)

```
SEEDANCE 2.0 PROMPT:

Deep black bar environment. Single hard magenta neon source positioned behind
the glass, transmitting through the liquid so it glows from within. Hard rim
light picks out the glass edge. Everything outside the glass falls to black.
Locked-off macro, heavy rocks glass center frame.

0-1s: Empty glass, single large clear ice cube with visible internal clarity
and faint fracture lines. Static frame. Sound: near-silence, faint bar ambience,
a single ice-against-glass click at 0.8s.

1-3s: Amber spirit pours from frame-top in a continuous ribbon, backlit so the
stream glows translucent. It strikes the ice and splits, running down the
faces of the cube in thin sheets. Liquid level rises. 0.5x slow motion. The
ice cracks audibly at 2.4s, a hairline fracture propagating through it. Sound:
pour foreground, sharp ice crack at 2.4s.

3-5s: A second liquid — deep red vermouth — enters and layers over the amber,
sinking in slow ribbons and creating visible density stratification before
beginning to blend. Camera begins a slow 45-degree orbit around the glass at
fixed distance. Neon rim shifts across the liquid as the angle changes. Sound:
sparse downtempo bass enters, liquid movement stays above it.

5-6.5s: A citrus twist enters from frame-top, is squeezed above the surface —
a fine mist of oils sprays visibly through the neon backlight — then is dropped
onto the ice. Camera continues the orbit. Sound: the sharp small snap of the
peel.

6.5-8s: Orbit completes and settles at a 45-degree hero angle. Condensation has
formed on the glass exterior, one bead beginning to run down. The liquids are
still blending at the final frame — the stratification not yet resolved.

Sound: 0-1s bar ambience and one ice click. 1s pour. 2.4s ice crack. 3s sparse
downtempo bass at low level. Every liquid sound stays above the music. No
voiceover.

Grade: near-black surround, magenta and amber only, deep blacks with no lift.
Liquid highly saturated, environment fully desaturated.

Material references: @material[image1] for the glassware and drink reference.
@material[audio1] for the music bed.
```

---

### Example 4: Bakery Croissant Macro (6s)

```
SEEDANCE 2.0 PROMPT:

Extreme macro on a laminated croissant resting on flour-dusted stone. Single
hard light source at 85 degrees to the side, nearly parallel to the surface,
warm 3200K. Every flake casts a long shadow. No fill on the shadow side.
Shallow depth of field, f/1.8 equivalent.

0-1.5s: Slow macro drift left-to-right across the exterior. Lamination layers
read as distinct ridges in the raking light. Loose flakes sit on the surface,
one at the edge trembling faintly. Background stone desaturated and dark.
Sound: silence, faint room tone only. No music.

1.5-3s: Two hands enter from either side, seen from above, fingers not extended
toward camera. They grip and pull the croissant apart in one slow motion.
0.4x speed. The crust shatters along the pull — fragments and flakes scatter
outward and fall through the shaft of hard light, glowing against the dark
background. Sound: hyper-close binaural crust shatter at full level. Nothing
else.

3-4.5s: Interior revealed — open irregular honeycomb crumb, visibly moist,
steam escaping in thin wisps from the torn face. Camera pushes in on the
cross-section. The two halves separate slowly, strands of crumb stretching
briefly between them. Sound: soft tearing, then room tone.

4.5-6s: Camera settles on the interior at maximum magnification. Steam still
rising from the crumb. A single flake falls past the lens in the foreground,
out of focus. Frame does not fully settle. Sound: silence returns, a faint
granular patter as flakes land.

Sound: no music at any point. Hyper-close binaural texture recording only —
shatter, tear, flakes landing. The sound is the content.

Grade: warm golden, high saturation on the pastry, desaturated stone surround,
deep blacks. Crushed shadows, no lift.

Suppress: uniform gloss — the exterior is matte and floury, only the interior
crumb reads moist. Naturally imperfect, one flake off the edge of the stone.

Material references: @material[image1] for the croissant reference.
```

---

### Example 5: Restaurant Atmosphere & Chef Plating (12s)

```
SEEDANCE 2.0 PROMPT:

Low-key restaurant kitchen at service. Practical heat lamps above the pass act
as key light, warm 2700K, creating pools of light with hard falloff into
darkness. Background kitchen visible only as warm bokeh and moving silhouettes.
Gimbal-mounted camera, 35mm equivalent.

0-2s: Gimbal push forward through the pass at counter height. Heat lamps flare
directly into the lens creating soft anamorphic streaks. Steam crosses the
frame from an unseen source. Depth of field shallow — foreground tickets and
plates pass in blur. Sound: full kitchen ambience, ticket printer, distant
calls, pan noise.

2-4.5s: Camera arrives and settles on a white plate under the lamps. Chef's
hands enter frame and set the primary element down — a seared protein, glossy
with rendered fat, char marks catching the hard overhead light. Contact shadow
where it meets the plate. Sound: ambience continues, the plate settles with a
soft ceramic click.

4.5-7s: Hands work in sequence — sauce spooned and pulled across the plate in
one motion, still spreading after the spoon lifts; garnish placed with tweezers,
resting and settling slightly into the sauce. Camera holds at a 30-degree
angle, imperceptibly pushing in. Sound: a low acoustic bed enters at 5s, kept
well below the foreground kitchen sound.

7-9.5s: Rack focus pulls from the plating hands up to the chef's face — focused,
lit from below by the lamp bounce off the white plate, background falling to
black. Held for 1.5 seconds. Sound: ambience thins slightly, music holds.

9.5-12s: Focus returns to the plate. Camera rises to a 60-degree angle as the
plate is pushed forward under the lamp. Steam still rising from the protein,
sauce edge still spreading at the final frame. Anamorphic flare from the lamp
crosses the top of the frame.

Sound: 0-5s full kitchen ambience, foreground. 5s soft acoustic bed enters low.
Cutlery, ceramic, and pan sounds stay above the music throughout. No voiceover.

Grade: warm amber, deep crushed blacks, food saturated and rich, kitchen
environment desaturated. Practical lamp highlights allowed to bloom slightly.

Suppress: hands enter partially and from above, fingers never extended toward
camera. Plating is naturally imperfect — one element slightly off-center, an
irregular sauce edge.

Material references: @material[image1] for the dish. @material[image2] for the
kitchen environment. @material[audio1] for the music bed.
```

---

### Example 6: Packaged Snack — CPG Ad (6s)

```
SEEDANCE 2.0 PROMPT:

Clean studio product setup. Two large softboxes at 45 degrees either side plus
a controlled overhead strip creating the top specular highlight. Seamless
background in a subtle brand-colored gradient. Locked-off camera, product-
photography discipline, no unmotivated shadows.

0-1s: Package standing center frame, front label fully legible, controlled
specular highlight running down the package edge. Static. Sound: upbeat music
bed already running from 0s at moderate level.

1-2s: Hands enter from frame-bottom and tear the package open in one motion.
The foil deforms and crinkles visibly. At 1.6s the seal breaks. Camera holds
locked off. Sound: package crinkle and the tear pop at 1.6s, sitting clearly
above the music.

2-4s: The package tips forward and contents cascade out toward camera in 0.3x
slow motion — individual pieces tumbling and rotating, each catching the
overhead specular. They scatter across the surface below and settle. Seasoning
dust falls with them, particles visible against the gradient. Sound: the
cascade and impact, then a single amplified crunch at 3.4s as one piece
fractures.

4-5s: Camera performs a 90-degree tilt from flat overhead down to a level side
angle over 1 second, revealing the height of the scattered pile and the package
standing behind it. Both product and package in frame together, label still
legible.

5-6s: Settle on the hero composition — package upright frame-right, product
scattered frame-left, one piece in sharp foreground macro. A last piece rolls
to a stop at the final frame. Sound: music resolves on a beat, crunch decays.

Sound: upbeat music bed from 0s. Package crinkle 1s, tear pop 1.6s, cascade
2-4s, hero crunch 3.4s. Every sound effect sits clearly above the music at
each hero beat. No voiceover.

Grade: clean and bright, brand color saturated, neutral whites, controlled
contrast. Product warm and appetizing against the cooler background gradient.

Suppress: surface finish varies across pieces — glossier where seasoned oil
pools, matte where dusted. Pieces rest with contact shadows, none floating.

Material references: @material[image1] for the packaging and label.
@material[image2] for the product itself. @material[audio1] for the music bed.
```

---

## 14. Quick Reference

**Before generating any food prompt, confirm:**

1. Temperature state established (hot → backlight + steam; cold → frost + condensation)
2. Light is behind or hard-side, never frontal
3. At least one element still moving at the final frame
4. Sound stack specified, with texture audio as the foreground layer
5. Grade direction stated, with an explicit "no green/blue cast" if the food is cooked
6. At least one failure mode suppressed by name
7. Speed between 0.25x and 0.5x for all hero moments
8. Material references mapped to `@material[imageN]`
