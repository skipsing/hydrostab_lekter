# Notes â€” BargeDamageKBScene

## Scene metadata
- Scene: `BargeDamageKBScene`
- Source: `scenes/barge_damage_kb_scene.py`
- Learning objective (overall): Show that the center of buoyancy moves upward when the draft increases after damage, and relate this to the rectangular-section relation `KB = T/2`.
- Output tags: `outline`, `latex`, `html`, `slides`

## Assumptions used in narration
- The transverse section is rectangular.
- The damaged condition is represented by a deeper draft `T_S` than the intact draft `T`.
- The section remains symmetric, so `B` and the centerline stay unchanged.
- For a rectangular section, the center of buoyancy is located halfway between keel and waterline.

---

## Phase 1 â€” Introduce intact transverse section
- Goal: Establish the reference section before damage.
- Visual cue:
  - Fade in the left transverse section with centerline and waterline.
  - Show labels `FÃ¸r skade`, `Tverrsnitt`, `WL`, and centerline marker.
- Narration (short):
  - We start with the intact transverse section.
  - The waterline and keel define the vertical range of the submerged volume.
- Key equations: *(none in this phase)*
- Given values:
  - `Draft before damage = T`
- Unit check:
  - Vertical distances in meters.
- Common pitfall: Confusing the transverse centerline with a vertical measurement line.
- Takeaway: The intact submerged geometry is the baseline for locating `B`.

---

## Phase 2 â€” Show `KB` and buoyancy center before damage
- Goal: Identify the buoyancy center position in the intact condition.
- Visual cue:
  - Show yellow point `B` in the submerged area.
  - Show `KB` dimension arrow from keel to `B`.
  - Show horizontal guide line from the arrow to the buoyancy point.
- Narration (short):
  - The center of buoyancy lies at the centroid of the submerged rectangular area.
  - For the intact condition, this gives the vertical distance `KB`.
- Key equations:
  - `$K\!B$`
- Given values:
  - `$T$`
- Unit check:
  - `KB` in meters.
- Common pitfall: Measuring `KB` from the waterline downward instead of from the keel upward.
- Takeaway: `KB` is a vertical distance from keel to center of buoyancy.

---

## Phase 3 â€” Introduce damaged transverse section
- Goal: Compare the intact and damaged conditions side by side.
- Visual cue:
  - Fade in the right transverse section.
  - Show labels `Etter skade`, `Tverrsnitt`, `WL_S`, and centerline marker.
  - The new waterline is higher than the original due to increased draft.
- Narration (short):
  - After damage, the barge sinks deeper in the water.
  - The new waterline `WL_S` gives a larger draft than before.
- Key equations: *(none in this phase)*
- Given values:
  - `Draft after damage = T_S`
- Unit check:
  - `T_S` in meters.
- Common pitfall: Treating `WL` and `WL_S` as the same equilibrium condition.
- Takeaway: The damaged section has greater immersion and therefore a different buoyancy-center height.

---

## Phase 4 â€” Show `KB_S` and buoyancy center after damage
- Goal: Locate the new buoyancy center in the damaged condition.
- Visual cue:
  - Show yellow point `B_S` in the deeper submerged region.
  - Show `KB_S` arrow from keel to `B_S`.
  - Show horizontal guide line from the arrow to the buoyancy point.
- Narration (short):
  - The center of buoyancy moves upward because the submerged rectangle becomes deeper.
  - In the damaged condition, the corresponding vertical distance is `KB_S`.
- Key equations:
  - `$K\!B_S$`
- Given values:
  - `$T_S$`
- Unit check:
  - `KB_S` in meters.
- Common pitfall: Assuming `B` stays fixed when only the draft changes.
- Takeaway: Increased draft shifts the center of buoyancy upward.

---

## Phase 5 â€” Compare the intact and damaged `KB` relations
- Goal: State the rectangular-section rule and compare the two conditions directly.
- Visual cue:
  - Write `For rektangulÃ¦r lekter` below the sections.
  - Write `K\!B = \frac{T}{2} < K\!B_S = \frac{T_S}{2}`.
- Narration (short):
  - For a rectangular section, the buoyancy center is at half the draft.
  - Since `T_S > T`, it follows directly that `KB_S > KB`.
- Key equations:
  - `$K\!B = \frac{T}{2}$`
  - `$K\!B_S = \frac{T_S}{2}$`
  - `$K\!B < K\!B_S$`
- Given values:
  - `$T_S > T$`
- Unit check:
  - All vertical quantities are in meters.
- Worked step (optional):
  - If `$T = 4.0\,\mathrm{m}$` and `$T_S = 5.0\,\mathrm{m}$`, then
  - `$KB = 2.0\,\mathrm{m}$` and `$KB_S = 2.5\,\mathrm{m}$`.
- Common pitfall: Forgetting that the comparison relies on the rectangular-section centroid rule.
- Takeaway: A deeper rectangular draft moves the buoyancy center vertically upward.

---

## Reuse blocks

### LaTeX handout seed
```tex
\subsection*{Upward shift of the buoyancy center after damage}
For a rectangular transverse section, the center of buoyancy lies at the centroid of the
submerged area. Therefore,
\[
KB = \frac{T}{2}.
\]
After damage, the vessel sinks to a larger draft $T_S$, giving
\[
KB_S = \frac{T_S}{2}.
\]
Since $T_S > T$, it follows that
\[
KB_S > KB.
\]
```

### HTML outline seed
```html
<h3>Vertical Shift of the Buoyancy Center</h3>
<ul>
  <li>Left section: intact condition with draft T and buoyancy center B.</li>
  <li>Right section: damaged condition with larger draft T_S and buoyancy center B_S.</li>
  <li>For a rectangular section, KB = T/2.</li>
  <li>Therefore, a larger draft implies a larger KB value.</li>
</ul>
```
