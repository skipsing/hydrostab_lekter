# Notes — BargeGeometryScene

## Scene metadata
- Scene: `BargeGeometryScene`
- Source: `barge_geometry_scene.py`
- Learning objective (overall): Identify the three geometric views and the principal dimensions `L`, `B`, and `D`.
- Output tags: `outline`, `latex`, `html`, `slides`

---

## Phase 1 — Centered intro text only
- Goal: Set context before any geometry appears.
- Visual cue:
  - Add centered title text immediately at scene start.
  - Keep it static briefly, then fade it out.
- Narration (short):
  - This scene introduces the main geometric dimensions of a rectangular barge.
  - We first present the context, then reveal the geometric views.
- Key equations: *(none in this phase)*
- Given values: *(none in this phase)*
- Unit check: N/A
- Common pitfall: Starting with too much visual information before the title context is clear.
- Takeaway: Students know what the scene will establish before details appear.

---

## Phase 2 — Reveal views and reference labels
- Goal: Establish profile, transverse, and plan view as the geometric basis for later scenes.
- Visual cue:
  - Fade in `profile`, `transverse`, `plan` after intro fade-out.
  - Show centerline markers (`℄`) and AP/FP labels.
  - Show section labels (`Profilsnitt`, `Tverrsnitt`, `Plansnitt`).
  - Layout note: views are scaled up and shifted upward; transverse view shifted right to avoid overlap.
- Narration (short):
  - We now show the three standard projections of the same barge.
  - AP/FP and centerlines provide consistent geometric references.
- Key equations: *(none in this phase)*
- Given values: *(none in this phase)*
- Unit check: N/A
- Common pitfall: Mixing up profile and plan AP/FP usage.
- Takeaway: Students can map each view to a physical vessel direction.

---

## Phase 3 — Introduce `L` and `D`
- Goal: Define the principal longitudinal and vertical dimensions.
- Visual cue:
  - Show `L` dimension arrow over profile view
  - Show `D` dimension arrow at transverse view
- Narration (short):
  - `L` is the longitudinal reference dimension in profile view.
  - `D` is the total molded depth shown in transverse view.
  - These dimensions anchor later displacement and damage calculations.
- Key equations:
  - `$L$`
  - `$D$`
- Given values:
  - `$L = \ldots\ \mathrm{m}$`
  - `$D = \ldots\ \mathrm{m}$`
- Unit check:
  - Both `L` and `D` must be in meters.
- Worked step (optional):
  - Convert any input dimension from cm to m before use in hydrostatic formulas.
- Common pitfall: Treating `D` as draft `T`.
- Takeaway: `L` and `D` are geometric dimensions, not equilibrium-dependent quantities.

---

## Phase 4 — Introduce `B` in plan view
- Goal: Complete the geometric triplet `L`, `B`, `D`.
- Visual cue:
  - Show beam arrow in plan view with label `B`
- Narration (short):
  - The plan view gives the breadth `B` directly.
  - Together with `L` and `D`, this defines the base rectangular hull geometry used throughout the lecture sequence.
- Key equations:
  - `$B$`
- Given values:
  - `$B = \ldots\ \mathrm{m}$`
- Unit check:
  - `B` in meters; keep consistent with `L` and `D`.
- Common pitfall: Using transverse-view width instead of plan-view breadth reference in later formulas.
- Takeaway: After this phase, all principal geometric dimensions are established.

---

## Reuse blocks

### LaTeX handout seed
```tex
\subsection*{Barge geometry basis}
The rectangular barge is introduced in profile, transverse, and plan views.
The principal dimensions are denoted by $L$ (length), $B$ (breadth), and $D$ (depth).
These dimensions define the geometric foundation used in the subsequent hydrostatic and damage-stability derivations.
```

### HTML outline seed
```html
<h3>Barge Geometry (Foundation Scene)</h3>
<ul>
  <li>Three views: profile, transverse, plan.</li>
  <li>Reference markers: AP/FP and centerlines.</li>
  <li>Main dimensions introduced: L, D, B.</li>
</ul>
<p>This scene establishes the geometric vocabulary for all later calculations.</p>
```
