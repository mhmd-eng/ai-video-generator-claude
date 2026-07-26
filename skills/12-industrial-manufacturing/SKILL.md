---
name: seedance-industrial-manufacturing
description: Generate B2B industrial and manufacturing video prompts for Seedance 2.0 on Higgsfield. Use for factory tours, production line footage, machinery and equipment showcases, company profile videos, export and capability films, trade show loops, quality control and certification content, or any video where the buyer is another business rather than a consumer. Triggers on factory, manufacturing, production line, industrial, machinery, equipment, plant, workshop, assembly, CNC, welding, injection molding, packaging line, warehouse, logistics, export, ISO, HACCP, quality control, capacity, B2B, company profile, trade show.
---

# Industrial Manufacturing — B2B Capability Video Prompts

Consumer video sells desire. Industrial video sells **capability and trust**. The buyer is a procurement manager, an importer, or a factory owner deciding whether you can deliver 40,000 units on time to a specification. Nothing about appetite, aspiration, or lifestyle moves that decision.

This skill generates Seedance 2.0 prompts engineered around the trust response: scale, precision, cleanliness, continuity, and control.

---

## 1. Input Specifications

**Required inputs:**
- Product or process (what is being made, and at which stage)
- Sector (see §5 playbooks — food, metal, machinery, furniture, minerals, plastics, print, textile, jewelry)
- Buyer type (domestic B2B / importer / export market / distributor)

**Optional inputs:**
- Certifications to imply visually (ISO 9001, HACCP, CE, halal, organic)
- Production scale (artisanal workshop / mid-size plant / high-volume line)
- Human presence (operators visible / hands only / unmanned automation)
- Intended placement (LinkedIn, website hero, WhatsApp, trade show loop, email, investor deck)

**Output format:**
- One complete Seedance 2.0 prompt block per request
- Duration note (6s / 8s / 10s for single-process; 12-15s for capability films)
- Lighting preset label
- Sound stack specification
- Explicit note on where text will be added in post (never generated)

---

## 2. Material References

- **Images:** Up to 9 — factory floor photos, machine references, product shots, packaging, facility exterior
- **Videos:** Up to 3 — existing plant footage, machine motion references
- **Audio:** Up to 3 — real machine sound, ambient plant tone, music bed
- **Max assets:** 12 total combined
- **Reference syntax:** `@material[name]` within prompts
- **Output:** 4-15 seconds, 720p with synchronized audio

Standard mapping for this skill:
- `@material[image1]` — the product or component
- `@material[image2]` — the machine or production line
- `@material[image3]` — facility, floor, or environment
- `@material[image4]` — packaging or branding (for post-production reference, not in-frame text)

---

## 3. The Trust Response: What Industrial Buyers Read

A procurement buyer scans a supplier video for risk signals, not beauty. Five cues do the work:

| Cue | What the buyer reads | How to prompt it |
|---|---|---|
| **Scale** | You can handle my volume | "wide shot revealing the full length of the line, repeating units receding into depth" |
| **Precision** | Your tolerances are real | "macro on the cutting edge, consistent kerf, no burr, repeated identically" |
| **Cleanliness** | You will pass my audit | "spotless floor, no debris, no oil pooling, surfaces recently wiped" |
| **Continuity** | You will not stop mid-order | "uninterrupted flow of product through frame, no gaps in the line, steady rhythm" |
| **Control** | Someone is accountable | "operator observing the gauge, hand adjusting a dial, deliberate and unhurried" |

**The rule that governs everything:** industrial video must read as **a normal day, not a special day**. Consumer video stages a perfect moment. Industrial video must look like this happens every shift, unremarkably. Over-staging destroys credibility — a factory that looks like a commercial looks like it was rented.

**The second rule:** the line never stops. At least one element must still be in motion at the final frame — a conveyor still advancing, a spindle still turning, product still flowing. A stopped line reads as a shut plant.

**The third rule, specific to this sector:** **never show unsafe practice**. An operator without eye protection near a grinder, an unguarded nip point, a person reaching into a running machine — any buyer with an audit function will notice, and it destroys the video's purpose. Prompt safety explicitly, every time.

---

## 4. 2-Second Hook Patterns

Industrial hooks are demonstrations of capability. Each lands inside 2 seconds.

### 4.1 Precision Hooks

| Pattern | Mechanism | Prompt Template |
|---|---|---|
| **The Tolerance Close** | Extreme accuracy is inherently impressive | "Extreme macro on [cutting tool / nozzle / press] meeting [material]. The cut or form happens in one clean pass with zero deviation. Shallow depth of field, hard directional light raking the surface to show the edge quality. Sound: the single precise machine note, no music." |
| **The Repeat** | Identical output = process control | "Locked-off macro. [Component] is formed, then a second identical one, then a third — each occupying the exact same frame position, indistinguishable from the last. Rhythm is metronomic. Sound: the same mechanical cycle repeating exactly." |
| **The Gauge** | Measurement implies standards | "Macro on a caliper, dial indicator or scale closing on a finished part. The needle settles precisely on the target mark. An operator's gloved hand steadies the part. Sound: near-silence, a single soft click as the measurement lands." |
| **The Robot Arm** | Automation reads as modern and consistent | "Robotic arm executes a pick-and-place in one fluid movement, decelerating precisely at the endpoint with no overshoot. Camera tracks the end effector. Industrial LED lighting, cool 5000K. Sound: servo whine and pneumatic release." |

### 4.2 Scale Hooks

| Pattern | Mechanism | Prompt Template |
|---|---|---|
| **The Line Reveal** | Depth = capacity | "Camera begins tight on a single unit on the conveyor, then pulls back steadily over 2.5 seconds to reveal the full line extending into depth — dozens of identical units, machinery on both sides, the far end lost in perspective. Sound: plant ambience rising with the reveal." |
| **The Overhead Grid** | Order at scale | "Locked-off overhead top-down at 90 degrees over the production floor or finished stock. Product arranged in a perfect repeating grid filling the frame edge to edge. Slight movement as the conveyor advances the grid. High-bay lighting, even and shadowless." |
| **The Warehouse Push** | Inventory = readiness | "Camera pushes forward down an aisle between high racking stacked with palletized finished goods. Racking recedes symmetrically on both sides. Wide lens, deep focus. Cool overhead LED. Sound: the hollow reverberant ambience of a large space." |
| **The Stack** | Volume made physical | "Wide shot of finished product stacked or palletized, filling the lower two-thirds of frame. A forklift crosses the background in soft focus. Static camera. The scale of the stack is the entire message." |

### 4.3 Process Hooks

| Pattern | Mechanism | Prompt Template |
|---|---|---|
| **The Spark** | Fire and energy are primal attention | "Side angle on [welding / grinding / cutting]. At 0.5s the arc strikes and sparks fan outward in an arc, briefly lighting the operator and the surrounding darkness. Operator fully masked with proper PPE. Everything outside the spark light falls to black. Sound: the sharp electrical crack of the arc." |
| **The Molten Pour** | Transformation of raw material | "Molten [metal / glass] pours in a continuous glowing stream from [crucible / furnace] into the mold. The stream is the brightest object in frame, throwing orange light onto the surrounding dark plant. 0.5x slow motion. Sound: deep furnace roar, low and continuous." |
| **The Synchronized Line** | Choreography implies engineering | "Multiple stations of the line operating simultaneously in visible rhythm — filling, capping, labeling — each timed to the same beat. Camera tracks laterally along the line at constant speed, passing each station. Sound: the composite mechanical rhythm of the whole line, layered." |
| **The Transformation Cut** | Raw to finished in one frame | "Split or match cut: raw input material [coil / pellet / plank / grain] occupies frame-left, the finished product occupies frame-right, identical camera treatment on both. The transition happens on a hard cut at the midpoint. Sound: an impact hit on the cut." |

---

## 5. Sector Playbooks

Mapped to the sectors that dominate the Lebanese industrial directory.

### 5.1 Food Processing (B2B — not consumer)
This is **not** the food & beverage skill. That one sells appetite to a consumer. This sells **capacity and compliance** to an importer.

- **Priority cues:** hygiene, stainless steel, packaging speed, batch consistency, cold chain
- **Lighting:** bright, even, cool-neutral 5000K — food plants are lit flat and clean, and that is the point
- **Camera:** lateral track along the filling line, overhead on the packing grid, macro on the seal
- **Show:** hairnets, gloves, clean stainless, sealed packaging, date coding, palletized export cartons
- **Never show:** bare hands touching product, wooden surfaces, cluttered floors
- **Anchor phrases:** "stainless steel filling line, spotless and recently sanitized", "sealed packages advancing in an unbroken line", "operator in hairnet and gloves observing the fill level", "export cartons palletized and stretch-wrapped"

### 5.2 Metal Products
- **Priority cues:** sparks, precision cuts, weld quality, surface finish, stock volume
- **Lighting:** dark workshop with the process as the light source — arc, sparks, molten
- **Camera:** macro on the cut, orbit around the finished part, wide on the press
- **Anchor phrases:** "CNC plasma cutting a clean kerf through steel plate", "weld bead with even consistent ripple, no spatter", "sparks fanning from the grinder into darkness", "brushed surface finish catching raking light"

### 5.3 Machinery & Electrical Equipment
- **Priority cues:** assembly complexity, component density, testing, cable management
- **Lighting:** bright even workshop, 5000K, clean and technical
- **Camera:** macro on the assembly, rack focus across a control panel, slow orbit on the finished unit
- **Anchor phrases:** "gloved hands seating a component onto the board with tweezers", "control cabinet with disciplined cable management, every run parallel", "finished unit under test, indicator lamps sequencing", "slow orbit around the assembled machine on the test stand"

### 5.4 Non-Metallic Minerals (glass, cement, ceramics, stone)
- **Priority cues:** heat, mass, raw material transformation, surface
- **Lighting:** furnace glow as key, otherwise dark; or harsh daylight for quarry and yard
- **Camera:** locked-off on the furnace mouth, slow push on the slab, wide on the kiln
- **Anchor phrases:** "molten glass gathering on the pipe, glowing orange against a dark plant", "stone slab emerging from the cutter, water sheeting off the surface", "kiln mouth radiating heat, product advancing on the roller bed"

### 5.5 Furniture & Wood
- **Priority cues:** craft, grain, joinery, finish, hand skill
- **Lighting:** warm workshop light, hard raking sidelight to show grain relief
- **Camera:** macro drift along the grain, hands working in shallow focus, slow orbit on the finished piece
- **Anchor phrases:** "hard raking light across open wood grain, every fibre casting relief", "dovetail joint closing with a precise fit", "finish coat leveling out to an even sheen", "shavings curling from the plane in slow motion"

### 5.6 Paper, Cardboard & Printing
- **Priority cues:** speed, registration, web tension, color accuracy
- **Lighting:** bright press hall, cool and even
- **Camera:** track along the press, macro on the sheet exiting, overhead on the stack
- **Anchor phrases:** "printed web travelling through the press at speed, perfectly registered", "sheets fanning into the delivery stack in even rhythm", "macro on the print surface, color dense and consistent edge to edge"

### 5.7 Textiles & Garments
- **Priority cues:** loom motion, thread tension, fabric handling, finishing
- **Lighting:** bright hall, or hard sidelight for weave texture
- **Camera:** macro on the shuttle, lateral track along the loom bank, slow drift over folded stock
- **Anchor phrases:** "loom beating up the weft in steady rhythm, warp threads under even tension", "fabric emerging and folding onto the batch roll", "macro on the weave structure, hard sidelight showing every interlacing"

### 5.8 Chemicals & Plastics
- **Priority cues:** containment, automation, molding cycle, cleanliness
- **Lighting:** bright, clinical, cool — chemical plants must read as controlled
- **Camera:** locked-off on the mold opening, macro on the part ejecting, wide on the reactor
- **Anchor phrases:** "injection mold opening and ejecting the part in one clean cycle", "pellets flowing into the hopper in a steady stream", "sealed reactor vessels with clean insulated pipework, no leaks or staining"

### 5.9 Jewelry & Precious Metals
Combine with the `seedance-luxury-aesthetic` skill — this sector rewards that treatment.

- **Priority cues:** hand craft, magnification, material value, finish
- **Lighting:** single hard source, deep black surround, strong specular
- **Camera:** extreme macro, static with subject motion, slow orbit
- **Anchor phrases:** "jeweller's loupe view of the setting, stone seating precisely into the prongs", "polished surface throwing a hard specular highlight against black", "hands working under the bench lamp, everything else in darkness"

---

## 6. Camera Movement Library

Industrial camera work is **steady and observational**. Handheld reads as amateur; fast moves read as hiding something.

| Move | Duration | Purpose | Prompt Phrasing |
|---|---|---|---|
| **Lateral Line Track** | 3-4s | Show the whole process | "Camera tracks laterally alongside the production line at constant speed, matching the product's travel direction. Each station passes through frame in sequence. No acceleration." |
| **Pull-Back Scale Reveal** | 2-3s | Single unit to full capacity | "Begin tight on one unit, pull back steadily over 3 seconds revealing the full line and the scale of the floor. Smooth dolly, no jitter." |
| **Slow Machine Orbit** | 3-4s | Dimensionality of equipment | "Camera orbits 45 degrees around the machine at fixed distance and a slightly low angle, so the equipment reads as substantial." |
| **Overhead Top-Down** | static | Order, grid, volume | "Locked-off overhead at 90 degrees. Product in a repeating grid. Only the conveyor moves." |
| **Macro Process Hold** | 2-3s | Precision proof | "Locked-off extreme macro on the working point. The camera does not move; the process provides all motion. Shallow depth of field." |
| **Aisle Push** | 3s | Inventory and readiness | "Slow forward push down the centre of the aisle, racking receding symmetrically both sides, wide lens, deep focus." |
| **Rack Focus Handoff** | 1-2s | Machine to operator | "Focus pulls from the working tool in foreground to the operator's face behind it, connecting process to person." |
| **Gantry Descend** | 3s | Plant overview to detail | "Camera descends slowly from a high vantage over the floor toward a single station, maintaining a level horizon." |

**Avoid in industrial:** whip pans, snap zooms, dutch angles, handheld shake, speed ramps, drone swoops. All of them read as advertising, and advertising reads as compensation.

**Speed:** real time to 0.5x. Unlike food, industrial does **not** live in slow motion — real-time machine rhythm is itself the credibility signal. Reserve slow motion for a single hero moment.

---

## 7. Lighting Presets

### High-Bay Industrial
The honest default. Most real plants look like this, and looking real is the objective.

```
"Overhead high-bay LED lighting, cool 5000K, even and shadowless across the
floor. No dramatic pools or theatrical falloff. Surfaces read accurately. The
space is bright, clean and legible. Slight specular on stainless and painted
machine guards."
```

### Process-As-Key
For welding, molten metal, glass, furnace work. The process itself lights the frame.

```
"The [arc / molten stream / furnace mouth] is the only significant light source.
It throws warm orange light onto nearby surfaces and the operator, falling off
rapidly to deep black. No fill. High contrast, dramatic without being staged."
```

### Clean Room
Food, pharma, electronics.

```
"Bright, even, cool-neutral 5000K. Every surface stainless or white, no shadows
in corners. The lighting itself communicates hygiene compliance. Slight sheen on
wiped stainless. Nothing is dim or ambiguous."
```

### Workshop Task Light
Craft sectors — furniture, jewelry, bespoke fabrication.

```
"Single warm task lamp over the bench, 3200K, creating a pool of light on the
work surface with the workshop falling into soft darkness beyond. Hands and
work fully lit; environment implied rather than shown."
```

### Facility Daylight
Exteriors, yards, loading bays, quarries.

```
"Natural daylight, slightly overcast for even exposure and no blown highlights.
Facility reads clean and maintained. Neutral grade, accurate colour on painted
surfaces and signage."
```

---

## 8. The Arabic Text Problem

**Critical constraint. Read before writing any prompt for a Lebanese or Arab-market client.**

Seedance 2.0 — like every current video model — renders **Arabic script as malformed, disconnected, meaningless glyphs**. Arabic is cursive and context-dependent, and the models do not reproduce letter joining correctly. The output looks like broken text to any Arabic reader, and on a corporate video it is worse than having no text at all.

**Latin text is only marginally better** and still frequently garbled at small sizes.

### The rule

**Never generate text in-frame. Ever.** Not company names, not slogans, not certification marks, not packaging labels, not signage, not screen readouts.

### How to prompt it

Add this suppression to every prompt:

```
"No legible text anywhere in frame. Packaging, signage, screens and labels are
blank, abstract, or turned away from camera. No lettering of any kind."
```

### Design for post instead

Prompt deliberate **clean plates** where text will be added in editing:

```
"Leave the upper third of frame as clean uncluttered background — even tone, no
detail — as a plate for graphics added in post."
```

This is not a workaround, it is the correct professional workflow: Arabic typography, logos, certification marks and data overlays all belong in After Effects or Premiere where they can be set correctly, kerned, and made RTL-accurate.

**Price it.** Post-production text and graphics is real labour on every single deliverable in this market. It is not absorbed into the generation cost.

---

## 9. Sound Design Stack

Industrial sound must read as **the real plant**. Over-produced sound design undermines the authenticity the video depends on.

**The four layers:**

1. **Machine layer (primary)** — the actual process: servo, hydraulic, pneumatic, press, conveyor, arc
2. **Ambient layer** — plant room tone, the reverberant hollowness of a large space
3. **Impact layer** — the single hit synced to the hero moment: the press, the cut, the stamp
4. **Music layer (optional, last)** — a restrained corporate bed, entering after 2s, always below the machine layer

| Content type | Sound design | Prompt phrasing |
|---|---|---|
| **Capability film** | Machine-led, music underneath | "Audio: plant ambience and machine rhythm foreground throughout. Restrained corporate music bed enters at 2s, kept clearly below the machine sound. No voiceover." |
| **Process / precision** | Machine only | "Audio: the single machine process at full level — servo, cut, cycle. No music at all. The mechanical precision of the sound is the message." |
| **Trade show loop** | Ambient only or silent | "Audio: low plant ambience only, no music, no impacts. Designed to loop silently on a stand where nobody can hear it." |
| **Heavy process** | Impact-led | "Audio: deep furnace roar or press impact, low frequency dominant. Sparse. Sub-bass on each cycle. No melodic content." |

**On voiceover:** for Arabic-market delivery, record voiceover in post with a real speaker. Do not attempt generated Arabic speech — pronunciation and dialect errors are immediately obvious to a Lebanese listener and cost more credibility than they save in budget.

---

## 10. Colour & Grade

- **Neutral and accurate.** Industrial credibility comes from looking true, not graded. "Neutral grade, accurate colour, no stylised look."
- **Cool for clean sectors** — food, pharma, electronics, plastics: "cool-neutral, clean whites, slightly desaturated."
- **Warm only for craft and heat** — furniture, jewelry, foundry, glass: "warm amber where the process is the light source."
- **Never crush blacks in a bright plant.** A dark, moody factory reads as concealing something. Keep shadows open and detailed.
- **Never oversaturate.** Saturated industrial footage reads as a stock library clip, which reads as not your factory.
- **Safety colours must be correct** — yellow guarding, red stops, green exits. "Safety markings render in accurate standard colours."

---

## 11. Platform Optimization

**LinkedIn (16:9 or 1:1)** — the primary B2B channel. Hook by 3s; the audience is more patient than consumer feeds. Sound-off by default, so the visual must carry alone. Capability and scale outperform craft close-ups here.

**WhatsApp (1:1 or 9:16)** — dominant in Lebanese business communication. Files must be small, the first frame must work as a static thumbnail, and the video must be legible on a phone at arm's length. Keep the subject large in frame.

**Website hero (16:9, silent loop)** — no hard cuts, seamless loop, no text dependency, works with sound off. Usually a single continuous move.

**Trade show loop (16:9)** — plays silently for hours to passers-by. Slow, seamless, no jarring transitions, readable from three metres.

**Email and proposal embeds (16:9)** — short, under 15s, opens on the most impressive frame because many viewers never press play.

**Instagram / TikTok (9:16)** — mostly irrelevant for industrial B2B. Exception: employer branding and recruitment, where factory content performs surprisingly well.

---

## 12. Failure Modes

Industrial AI video fails in specific, credibility-destroying ways. Name the failure in the prompt to suppress it.

| Failure | What it looks like | Prompt correction |
|---|---|---|
| **Garbled text** | Meaningless glyphs on signage, packaging, screens | "No legible text anywhere in frame. Labels blank or turned away." |
| **Impossible machinery** | Mechanisms that could not function, parts connected to nothing | "Machinery is mechanically plausible — visible drive, guarding, and fixings consistent with the motion shown." |
| **Unsafe practice** | Operator without PPE, hands near unguarded moving parts | "Operator in correct PPE — safety glasses, gloves, hearing protection where appropriate. Hands never inside the machine envelope." |
| **Floating product** | Items hovering above the conveyor | "Product rests physically on the conveyor with contact shadows, advancing with the belt at matched speed." |
| **Wrong scale** | Machine size inconsistent with the operator | "Human figure included for scale reference, correctly proportioned to the equipment." |
| **Too clean to be true** | Showroom, not a working plant | "A working plant, not a showroom — clean and maintained, but with normal signs of use." |
| **Dead line** | Everything stationary | "At the final frame the line is still running — conveyor advancing, spindle turning, product still flowing." |
| **Stock-footage look** | Oversaturated, generic, anonymous | "Neutral accurate grade, unstylised, documentary rather than advertising." |

---

## 13. Complete Example Prompts

### Example 1: Food Processing Line — Export Capability (10s)

```
SEEDANCE 2.0 PROMPT:

Bright, even high-bay LED lighting at 5000K across a stainless steel filling
line. Spotless floor, no debris, no pooling. Cool-neutral grade, clean whites.
Working plant, clean and maintained but with normal signs of use.

0-2.5s: Extreme macro on a single container advancing on the stainless conveyor
as it passes the filling head. The fill completes cleanly with no spill. Camera
locked off. Sound: the filling line's mechanical rhythm at full level, plant
ambience beneath.

2.5-5.5s: Camera pulls back steadily over 3 seconds, revealing the full line
extending into depth — dozens of identical containers advancing in an unbroken
sequence, capping and sealing stations on both sides, the far end lost in
perspective. Sound: plant ambience rises with the reveal; restrained corporate
music bed enters at 3s, clearly below the machine sound.

5.5-8s: Camera tracks laterally alongside the line at constant speed, matching
the product's travel direction. Each station passes through frame in sequence —
fill, cap, seal — every one timed to the same beat. An operator in hairnet,
gloves and safety glasses observes a gauge, adjusting a dial without hurry.

8-10s: Overhead top-down at 90 degrees on the packing station, sealed units
arranged in a perfect repeating grid, advancing as the conveyor moves. Export
cartons palletized and stretch-wrapped in the background. The line is still
running at the final frame.

Sound: machine rhythm and plant ambience foreground throughout. Music bed from
3s, well below. No voiceover.

Grade: neutral and accurate, cool-neutral, clean whites, shadows open and
detailed. Unstylised, documentary rather than advertising.

Suppress: no legible text anywhere in frame — packaging, signage and screens are
blank or turned away. Product rests physically on the conveyor with contact
shadows. Operator in correct PPE throughout, hands never inside the machine
envelope.

Post plate: leave the upper third as clean even background for Arabic and
English graphics added in post.

Material references: @material[image1] product, @material[image2] the line,
@material[image3] the facility.
```

---

### Example 2: Metal Fabrication — Precision & Power (8s)

```
SEEDANCE 2.0 PROMPT:

Dark fabrication workshop. The process is the only significant light source,
throwing warm orange light onto nearby surfaces and falling off rapidly to deep
black. High contrast, dramatic without being staged.

0-1s: Black frame with faint machine ambience. At 0.5s the plasma arc strikes.
Sparks fan outward in a wide arc, briefly lighting the steel plate, the cutting
head, and the guarding beyond. Sound: the sharp electrical crack of the arc at
full level, no music.

1-3.5s: Locked-off extreme macro on the cutting head travelling through steel
plate. The kerf is clean and consistent, molten edge glowing then cooling to
grey behind the head. Zero deviation from the programmed path. The camera does
not move; the process provides all motion. Sound: the sustained cutting note,
steady and unwavering.

3.5-5.5s: Cut to the finished part lifted clear. Slow orbit 45 degrees around
it at a slightly low angle, so the piece reads as substantial. Hard raking light
across the brushed surface finish. Cut edge shows no burr. Sound: sparks decay,
low sustained bass bed enters.

5.5-8s: Rack focus pulls from the finished edge in foreground to the operator
behind it — fully masked, safety glasses and gloves, observing the next cut
beginning. Behind them the machine is already running again. Sparks continue at
the final frame.

Sound: 0-1s silence then the arc crack. 1-3.5s cutting note foreground. 3.5s low
bass bed enters, machine sound stays above it. No voiceover.

Grade: neutral where lit, deep black surround, warm only where the arc provides
the light. Safety markings in accurate standard colours. No oversaturation.

Suppress: no legible text in frame. Machinery mechanically plausible with
visible guarding and drive. Operator in correct PPE, hands never inside the
machine envelope.

Material references: @material[image1] the part, @material[image2] the machine.
```

---

### Example 3: Machinery Assembly — Technical Credibility (10s)

```
SEEDANCE 2.0 PROMPT:

Bright even workshop, 5000K, clean and technical. Assembly bench with organized
tooling. Neutral accurate grade, shadows open. Working environment, not a
showroom.

0-2s: Extreme macro on gloved hands seating a component onto an assembly with
tweezers. The placement is deliberate and lands precisely. Shallow depth of
field, hard directional light raking the surface. Sound: near-silence, a single
soft click as the component seats.

2-4.5s: Camera drifts laterally across a control cabinet under assembly.
Disciplined cable management — every run parallel, every bundle dressed. The
density of correct detail is the message. Sound: quiet workshop ambience,
restrained corporate bed enters at 3s below it.

4.5-7s: Macro on a dial indicator closing on a finished assembly. The needle
settles precisely on the target mark. A gloved hand steadies the part. Sound:
the soft click of the measurement landing, clearly above the music.

7-10s: Slow orbit 45 degrees around the completed unit on the test stand at a
slightly low angle. Indicator lamps sequence through their startup pattern. An
operator in safety glasses observes from frame-right. The unit is still running
its test cycle at the final frame.

Sound: workshop ambience and process sound foreground. Corporate bed from 3s,
well below. No voiceover.

Grade: neutral, accurate, unstylised. Cool-neutral. Safety colours correct.

Suppress: no legible text anywhere — control panels, labels and screens blank or
turned away. Machinery mechanically plausible. Operator in correct PPE.

Post plate: clean even background frame-left through the orbit for specification
callouts added in post.

Material references: @material[image1] the product, @material[image2] the
assembly area.
```

---

### Example 4: Furniture Workshop — Craft at Scale (8s)

```
SEEDANCE 2.0 PROMPT:

Warm workshop, single task lamp over the bench at 3200K creating a pool of light
on the work surface, the workshop falling into soft darkness beyond. Hard raking
sidelight across the timber to show grain relief.

0-2s: Macro drift along open wood grain, every fibre casting relief in the
raking light. Shavings from an earlier cut rest on the surface. Sound: workshop
room tone only, no music.

2-4s: Hands guide a plane along the edge in one continuous stroke. A shaving
curls up and away in slow motion, catching the task light. 0.5x speed. Sound:
the clean sustained cut of the blade, hyper-close.

4-6s: Cut to a dovetail joint closing — the two halves meeting with a precise
fit, no gap. Locked-off macro. Sound: the soft knock of the joint seating, then
silence.

6-8s: Pull back to reveal the finished piece under the bench lamp, finish coat
leveling to an even sheen. Behind it, in soft focus, a rack of identical
completed pieces recedes into the darker workshop — craft repeated at volume.
Camera settles. Dust still drifting through the lamp beam at the final frame.

Sound: workshop ambience and tool sound only. No music at any point. The
craftsmanship of the sound is the message.

Grade: warm amber where the lamp reaches, neutral elsewhere, shadows open not
crushed. Wood tones accurate and unsaturated.

Suppress: no legible text in frame. Naturally imperfect — a shaving off the edge
of the bench, tooling not perfectly aligned. A working shop, not a showroom.

Material references: @material[image1] the finished piece, @material[image2]
the workshop.
```

---

### Example 5: Glass or Stone — Raw Material Transformation (8s)

```
SEEDANCE 2.0 PROMPT:

Dark plant interior. The furnace mouth is the only significant light source,
radiating warm orange onto nearby surfaces and equipment, falling off rapidly to
black. High contrast.

0-2s: Locked-off on the furnace mouth. Heat shimmer distorts the air above it.
Molten material glows within. Camera does not move. Sound: deep continuous
furnace roar, low frequency dominant, no music.

2-4.5s: Molten glass gathers on the pipe and is drawn out in a continuous
glowing stream — the brightest object in frame by a wide margin, throwing moving
orange light across the dark plant. 0.5x slow motion. Operator in full heat PPE,
face shielded. Sound: furnace roar sustains, a low sub-bass pulse on the gather.

4.5-6.5s: Cut to the formed piece cooling on the bed, colour shifting from
orange through deep red toward its final state. Camera pushes in slowly. Heat
still visibly radiating. Sound: roar recedes, sparse low bass enters.

6.5-8s: Wide shot revealing the scale of the operation — multiple stations
working simultaneously along the hall, each an isolated pool of orange light in
the darkness, receding into depth. The nearest station is still working at the
final frame.

Sound: furnace roar foreground throughout. Sparse sub-bass from 4.5s. No
melodic content, no voiceover.

Grade: deep black surround, warm orange only where the process provides light.
Shadows detailed, not crushed to nothing. Unstylised.

Suppress: no legible text in frame. Operator in correct heat PPE with face
shielded at all times. Machinery mechanically plausible. Human figure included
for scale.

Material references: @material[image1] the product, @material[image2] the plant.
```

---

### Example 6: Company Capability Film — Facility to Owner (15s)

```
SEEDANCE 2.0 PROMPT:

Overcast natural daylight for the exterior, transitioning to bright high-bay
5000K LED interior. Neutral accurate grade throughout. Facility clean and
maintained.

0-3s: Wide exterior of the facility, overcast daylight, even exposure with no
blown highlights. A truck is being loaded at the bay in the background. Camera
pushes forward slowly toward the entrance. Sound: exterior ambience, distant
plant hum. Restrained corporate bed enters at 2s, low.

3-6s: Interior. Camera descends slowly from a high vantage over the production
floor toward a single station, maintaining a level horizon. The full scale of
the floor is visible during the descent — multiple lines running in parallel,
operators at stations, forklift crossing in the mid-ground. Sound: plant ambience
rises and takes foreground.

6-9s: Lateral track alongside the main line at constant speed, passing three
stations in sequence, product advancing steadily through every one. Operators in
correct PPE working unhurriedly. Nothing is staged for the camera.

9-12s: Aisle push down the centre of the finished-goods warehouse, high racking
stacked with palletized stock receding symmetrically on both sides. Wide lens,
deep focus, cool overhead LED. Sound: the hollow reverberant ambience of the
large space.

12-15s: Rack focus handoff — from a pallet of finished stock in foreground to
the owner standing in the aisle behind it, in workwear, looking toward the line
rather than at camera. Held. Behind them the plant continues running. Nothing
stops at the final frame.

Sound: plant ambience and machine rhythm foreground throughout. Corporate bed
from 2s, always below. No voiceover — Arabic voiceover to be recorded in post
with a real speaker.

Grade: neutral and accurate, unstylised, documentary. Safety colours correct.
Shadows open.

Suppress: no legible text anywhere in frame — no signage, no branding, no
screens. All operators in correct PPE. Human figures included for scale. A
working plant, not a showroom.

Post plate: the exterior wide (0-3s) and the final aisle shot leave clean even
background regions for the company name, certifications and contact details to
be added in post, set correctly in Arabic and English.

Material references: @material[image1] facility exterior, @material[image2] the
production floor, @material[image3] finished product, @material[image4] the
owner.
```

---

## 14. Quick Reference

**Before generating any industrial prompt, confirm:**

1. Buyer type established (domestic B2B / importer / export) — it changes what must be shown
2. Sector playbook selected from §5
3. Camera is steady and observational — no handheld, no whip pans, no drone swoops
4. Speed is real time, with slow motion reserved for one hero moment only
5. At least one element still running at the final frame
6. **Text suppression stated explicitly** — no legible lettering anywhere
7. **PPE and safe practice stated explicitly** — every shot with a human in it
8. Post plate identified where Arabic or English graphics will be added
9. Grade specified as neutral and accurate, not stylised
10. Sound stack specified with the machine layer foreground
11. At least one failure mode suppressed by name
12. Material references mapped to `@material[imageN]`
