# Notes â€” BargeDamageSubmergenceScene

## Scene metadata
- Scene: `BargeDamageSubmergenceScene`
- Source: `scenes/barge_damage_submergence_scene.py`
- Learning objective (overall): Show how a damaged rectangular barge establishes a new symmetric floating condition and derive the new equilibrium draft `T_S` from unchanged displacement volume.
- Output tags: `outline`, `latex`, `html`, `slides`

## Assumptions used in narration
- Flooding is symmetric, so the vessel sinks without trim or heel in this scene.
- The damaged compartment occupies one-third of the barge length.
- The simplified hydrostatic model is rectangular, so displacement is expressed with `L`, `B`, and draft.
- The displaced volume is unchanged when setting the new equilibrium condition.

---

## Phase 1 â€” Centered intro text only
- Goal: State the purpose of the scene before the geometry appears.
- Visual cue:
  - Add centered intro text at scene start.
  - Hold briefly, then fade it out.
- Narration (short):
  - We now establish the new floating condition after symmetric flooding.
  - The aim is to determine the new equilibrium draft.
- Key equations: *(none in this phase)*
- Given values: *(none in this phase)*
- Unit check: N/A
- Common pitfall: Jumping directly to formulas before the physical situation is clear.
- Takeaway: Students know the scene is about re-establishing equilibrium after flooding.

---

## Phase 2 â€” Reveal damaged profile and reference labels
- Goal: Establish the damaged vessel profile and the initial waterline reference.
- Visual cue:
  - Fade in `profile`, compartment dividers, waterline, compartment numbers, and labels.
  - Show `Profilsnitt`, `AP`, `FP`, and `WL`.
  - Layout note: the full profile block is placed toward the upper-left area, with the derivation column to the right.
- Narration (short):
  - We start from the original floating condition and mark the compartment arrangement.
  - The waterline is the fixed external reference used during the sinking motion.
- Key equations: *(none in this phase)*
- Given values: *(none in this phase)*
- Unit check: Waterline and draft are interpreted in meters.
- Common pitfall: Forgetting that `WL` is the reference line while the hull moves downward relative to it.
- Takeaway: The geometry and reference frame are established for the flooding sequence.

---

## Phase 3 â€” Indicate damage location
- Goal: Identify the damaged compartment before flooding begins.
- Visual cue:
  - Show a red triangle in compartment 2.
  - Hold briefly, then fade it out.
- Narration (short):
  - The red triangle marks the damaged compartment.
  - This is the space that becomes flooded in the next step.
- Key equations: *(none in this phase)*
- Given values: Damaged length fraction `L/3`
- Unit check: N/A
- Common pitfall: Losing track of which compartment is flooded once the water fill appears.
- Takeaway: The damage location is clearly identified before the re-equilibrium process starts.

---

## Phase 4 â€” Flooding and sinking with live `T_S`
- Goal: Show the physical re-equilibrium process and define the new equilibrium draft.
- Visual cue:
  - Fill compartment 2 with water.
  - Show the `T_S` arrow and label before the sinking motion.
  - During the downward motion, the top of the `T_S` arrow stays on the waterline while the bottom follows the keel.
- Narration (short):
  - Floodwater enters the damaged compartment, increasing immersion.
  - Because the flooding is symmetric, the vessel sinks bodily instead of trimming.
  - The new equilibrium draft is denoted `T_S`.
- Key equations:
  - `$T_S$`
- Given values:
  - `Flooded length = L/3`
- Unit check:
  - `T_S` in meters.
- Common pitfall: Letting the draft arrow move with the vessel instead of measuring from waterline to keel.
- Takeaway: Students can read `T_S` as the new equilibrium draft after symmetric flooding.

---

## Phase 5 â€” Write equilibrium before damage
- Goal: Recall the initial displacement relation for the intact rectangular barge.
- Visual cue:
  - Write heading `Likevekt fÃ¸r skade`.
  - Write `\nabla = L \cdot B \cdot T`.
- Narration (short):
  - Before damage, the full barge displacement is the rectangular volume based on `L`, `B`, and `T`.
- Key equations:
  - `$\nabla = L \cdot B \cdot T$`
- Given values:
  - `$L, B, T$`
- Unit check:
  - `$\nabla$ in $\mathrm{m^3}$`
- Common pitfall: Mixing initial draft `T` with new equilibrium draft `T_S`.
- Takeaway: The intact equilibrium expression is the reference equation.

---

## Phase 6 â€” Write equilibrium after damage
- Goal: Express the remaining displacement volume in the damaged condition.
- Visual cue:
  - Write heading `Likevekt etter skade`.
  - Show two `L/3` arrows above compartments 1 and 3.
  - Write `\nabla_S = (\tfrac{1}{3} + \tfrac{1}{3}) L \cdot B \cdot T_S`.
- Narration (short):
  - After damage, only the two undamaged thirds contribute to intact displacement volume.
  - The damaged equilibrium is therefore based on `2/3` of the original length.
- Key equations:
  - `$\nabla_S = \left(\tfrac{1}{3} + \tfrac{1}{3}\right) L \cdot B \cdot T_S$`
- Given values:
  - `Effective intact length = 2L/3`
- Unit check:
  - Keep `L`, `B`, and `T_S` in meters.
- Common pitfall: Forgetting that the flooded compartment does not contribute as intact buoyant volume in this simplified derivation.
- Takeaway: The damaged displacement relation is reduced to two intact thirds.

---

## Phase 7 â€” Use unchanged displacement volume
- Goal: Link intact and damaged equilibrium through constant displacement volume.
- Visual cue:
  - Write `Volumdeplasementet er uendret`.
  - Write `\nabla = \nabla_S`.
- Narration (short):
  - To solve for the new floating condition, we set the displacement volume before and after damage equal.
  - This gives the bridge between `T` and `T_S`.
- Key equations:
  - `$\nabla = \nabla_S$`
- Given values: *(none beyond previous phases)*
- Unit check:
  - Both sides must represent the same unit: `$\mathrm{m^3}$`.
- Common pitfall: Interpreting â€œunchangedâ€ as unchanged draft rather than unchanged displacement volume.
- Takeaway: The governing equilibrium condition is equality of displacement volume.

---

## Phase 8 â€” Solve for new equilibrium draft
- Goal: Derive the explicit expression for the new equilibrium draft `T_S`.
- Visual cue:
  - Show the downward implication arrow.
  - Write `L \cdot B \cdot T = \tfrac{2}{3} L \cdot B \cdot T_S`.
  - Write heading `Ny likevektsposisjon ved`.
  - Write final equation `T_S = \frac{\nabla}{\tfrac{2}{3} L \cdot B}`.
- Narration (short):
  - Equating the two displacement expressions gives the new equilibrium draft condition.
  - The result is the draft required for the reduced intact length to displace the same volume.
- Key equations:
  - `$L \cdot B \cdot T = \tfrac{2}{3} L \cdot B \cdot T_S$`
  - `$T_S = \frac{\nabla}{\tfrac{2}{3} L \cdot B}$`
- Given values:
  - `$\nabla$ from the intact condition`
- Unit check:
  - Numerator in `$\mathrm{m^3}$`, denominator in `$\mathrm{m^2}$`, result in `$\mathrm{m}$`.
- Worked step (optional):
  - If `$\nabla = 4800\,\mathrm{m^3}$`, `$L = 60\,\mathrm{m}$`, and `$B = 20\,\mathrm{m}$`, then
  - `$T_S = \frac{4800}{(2/3)\cdot 60 \cdot 20} = 6.0\,\mathrm{m}$`.
- Common pitfall: Losing the `2/3` factor when simplifying.
- Takeaway: Reduced intact length requires a larger equilibrium draft.

---

## Reuse blocks

### LaTeX handout seed
```tex
\subsection*{New equilibrium draft after symmetric flooding}
For a rectangular barge with one flooded compartment of length $L/3$, the remaining intact
buoyant length is $2L/3$. Assuming symmetric flooding, the vessel sinks without trim, and the
new equilibrium draft is denoted by $T_S$.

Using unchanged displacement volume,
\[
\nabla = \nabla_S,
\]
with
\[
\nabla = LBT, \qquad \nabla_S = \tfrac{2}{3}LBT_S.
\]
Hence,
\[
T_S = \frac{\nabla}{\tfrac{2}{3}LB}.
\]
```

### HTML outline seed
```html
<h3>New Floating Condition After Symmetric Flooding</h3>
<ul>
  <li>Damage is indicated in the middle compartment.</li>
  <li>Flooding is symmetric, so the barge sinks without trim.</li>
  <li>The new equilibrium draft is measured as T_S from waterline to keel.</li>
  <li>Only two thirds of the original barge length remain intact for buoyancy.</li>
  <li>Use unchanged displacement volume to solve for the new equilibrium draft.</li>
</ul>
```
