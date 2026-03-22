# Notes â€” BargeHydrostaticsScene

## Scene metadata
- Scene: `BargeHydrostaticsScene`
- Source: `scenes/barge_hydrostatics_scene.py`
- Learning objective (overall): Connect barge geometry and floating draft to the displacement relation $\nabla = L \times B \times T$.
- Output tags: `outline`, `latex`, `html`, `slides`

## Assumptions used in narration
- The barge mass is assumed to be equally distributed longitudinally.
- Therefore, `LCG` is located at the longitudinal center (midship).
- Initial condition is no trim and no heel.

---

## Phase 1 â€” Centered intro text only
- Goal: Set context before geometry appears.
- Visual cue:
  - Add centered title text at scene start.
  - Hold briefly, then fade out.
- Narration (short):
  - This scene introduces hydrostatic volume displacement for a rectangular barge.
  - We first frame the objective, then reveal geometry and waterline references.
- Key equations: *(none in this phase)*
- Given values: *(none in this phase)*
- Unit check: N/A
- Common pitfall: Presenting formulas before the geometric frame is visible.
- Takeaway: Students know the target relation before details are shown.

---

## Phase 2 â€” Reveal profile/transverse views and references
- Goal: Establish geometric and reference frame for hydrostatics.
- Visual cue:
  - Fade in `profile`, `transverse`, centerline marker, AP/FP labels, and section labels.
  - Layout note: views are scaled up, shifted upward, and transverse shifted right to avoid overlap.
- Narration (short):
  - We use profile and transverse sections to define length, breadth, and draft consistently.
  - AP/FP and centerline references ensure consistent direction and symmetry.
  - With uniform mass distribution, we assume `LCG` at midship in this baseline condition.
- Key equations: *(none in this phase)*
- Given values: *(none in this phase)*
- Unit check: N/A
- Common pitfall: Mixing profile and transverse references when defining dimensions.
- Takeaway: Visual frame is set for hydrostatic variables.

---

## Phase 3 â€” Add waterlines and `WL` labels
- Goal: Identify current floating condition in both views.
- Visual cue:
  - Show dashed waterline in profile and transverse views.
  - Add `WL` labels.
- Narration (short):
  - The waterline marks the equilibrium floating plane.
  - Draft is measured vertically from keel to this line.
- Key equations: *(none in this phase)*
- Given values: *(none in this phase)*
- Unit check: Waterline position and draft use meters in calculations.
- Common pitfall: Confusing molded depth `D` with draft `T`.
- Takeaway: Waterline is the reference for defining `T`.

---

## Phase 4 â€” Show `L` and `B`
- Goal: Introduce planform dimensions needed in displacement formula.
- Visual cue:
  - Show `L` arrow in profile.
  - Show `B` arrow in transverse.
- Narration (short):
  - `L` and `B` define the horizontal footprint of the submerged rectangular block.
  - Together with draft `T`, they determine displacement volume.
- Key equations:
  - `$L$`
  - `$B$`
- Given values:
  - `$L = \ldots\ \mathrm{m}$`
  - `$B = \ldots\ \mathrm{m}$`
- Unit check: Both in meters.
- Common pitfall: Using inconsistent units between dimensions.
- Takeaway: Horizontal geometry is now fully specified.

---

## Phase 5 â€” Show draft `T`
- Goal: Define the vertical immersion component in displacement.
- Visual cue:
  - Show vertical draft arrow from waterline to keel and label `T`.
- Narration (short):
  - Draft `T` is the submerged depth of the hull.
  - In the no-trim baseline, this is taken as uniform along the length.
- Key equations:
  - `$T$`
- Given values:
  - `$T = \ldots\ \mathrm{m}$`
- Unit check: `T` in meters.
- Common pitfall: Treating `T` as total depth `D`.
- Takeaway: Vertical term in displacement is established.

---

## Phase 6 â€” Present displacement relation
- Goal: Combine dimensions into the rectangular displacement expression.
- Visual cue:
  - Write equation at lower center of frame:
  - `$\nabla = L \times B \times T$`
- Narration (short):
  - For this simplified rectangular barge model, displacement volume is the product of length, breadth, and draft.
  - This relation is the starting point for damage and re-equilibrium calculations.
- Key equations:
  - `$\nabla = L \times B \times T$`
- Given values:
  - `$L, B, T$ from previous phases`
- Unit check:
  - `$\nabla$ in $\mathrm{m^3}$`
- Worked step (optional):
  - If $L=60\,\mathrm{m}$, $B=20\,\mathrm{m}$, $T=4\,\mathrm{m}$, then
  - `$\nabla = 60 \times 20 \times 4 = 4800\,\mathrm{m^3}$`
- Common pitfall: Unit mismatch (e.g., `cm` for one dimension).
- Takeaway: Students have the core displacement formula and assumptions for later scenes.

---

## Reuse blocks

### LaTeX handout seed
```tex
\subsection*{Hydrostatic baseline for a rectangular barge}
Assuming no trim/heel and uniform longitudinal mass distribution (thus LCG at midship),
the displacement volume is approximated by
\[
\nabla = L B T.
\]
Here, $L$ is length, $B$ is breadth, and $T$ is draft.
```

### HTML outline seed
```html
<h3>Hydrostatic Baseline</h3>
<ul>
  <li>Assumption: uniform mass distribution, LCG at midship.</li>
  <li>Waterline defines equilibrium draft T.</li>
  <li>Rectangular displacement model: âˆ‡ = L Â· B Â· T.</li>
</ul>
```

