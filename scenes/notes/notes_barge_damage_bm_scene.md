# Notes â€” BargeDamageBMScene

## Scene metadata
- Scene: `BargeDamageBMScene`
- Source: `scenes/barge_damage_bm_scene.py`
- Learning objective (overall): Show that flooding a middle compartment reduces the effective waterplane area and, consequently, reduces the transverse metacentric radius `BM_T`.
- Output tags: `outline`, `latex`, `html`, `slides`

## Assumptions used in narration
- The vessel is a rectangular barge divided into three equal compartments of length `L/3`.
- The middle compartment (compartment 2) is open to the sea and contributes no waterplane area after damage.
- Displacement volume `âˆ‡` is unchanged (parallel sinkage is handled separately in `BargeDamageSubmergenceScene`).
- The intact waterplane area is `A_WL = L Â· B`; after damage only two-thirds remains.
- The moment of inertia of the waterplane area is taken **about the longitudinal (foreâ€“aft) axis** through the centroid of the waterplane, which is the relevant axis for transverse (`BM_T`) calculations.

---

## Phase 1 â€” Intact plan view and waterplane area
- Goal: Establish the reference waterplane before damage and introduce `A_WL`.
- Visual cue:
  - Fade in the plan view (top view) of the barge with the centerline and `AP`/`FP` labels.
  - Show the `B`-dimension arrow on the port side.
  - Fade in the two transverse bulkhead dividers and compartment numbers 1, 2, 3.
  - Write label "Vannlinjeareal fÃ¸r skade" and equation `A_WL = L Â· B`.
- Narration (short):
  - The full waterplane spans the entire length `L` and beam `B`.
  - This gives the intact waterplane area as the product `L Â· B`.
- Key equations:
  - `$A_{WL} = L \cdot B$`
- Given values:
  - `$L = 60\,\mathrm{m}$`, `$B = 20\,\mathrm{m}$`
  - `$A_{WL} = 60 \times 20 = 1200\,\mathrm{m}^2$`
- Unit check:
  - `A_WL` in mÂ².
- Common pitfall: Confusing the plan area (waterplane) with the transverse cross-sectional area.
- Takeaway: The intact waterplane covers the full `L Â· B` area.

---

## Phase 2 â€” Damaged plan view and effective waterplane area
- Goal: Show that flooding the middle compartment removes its contribution to the waterplane.
- Visual cue:
  - Shade compartments 1 and 3 green (effective) and compartment 2 red (lost), with a red cross.
  - Show `L/3` dimension arrows above compartments 1 and 3.
  - Write label "Effektivt vannlinjeareal etter skade" and equation `A_WL_S = (2/3) L Â· B`.
- Narration (short):
  - A flooded open compartment is in free communication with the sea.
  - Its waterplane area no longer contributes to the vessel's restoring geometry.
  - Only the two intact thirds (compartments 1 and 3) remain effective.
- Key equations:
  - `$A_{WL_S} = \tfrac{2}{3}\,L \cdot B$`
- Given values:
  - `$A_{WL_S} = \tfrac{2}{3} \times 60 \times 20 = 800\,\mathrm{m}^2$`
- Unit check:
  - `A_WL_S` in mÂ².
- Common pitfall: Forgetting to exclude the flooded compartment from the waterplane calculation.
- Takeaway: The flooded compartment removes one-third of the original waterplane area.

---

## Phase 3 â€” Second moment of area of the damaged waterplane
- Goal: Compute `I_WL_S`, the second moment of the effective (two-thirds) waterplane area about the **longitudinal centroidal axis**.
- Visual cue:
  - Write label "Vannlinjearealets treghetsmoment" and equation
    `I_WL_S = (1/12) Â· (2L/3) Â· BÂ³`.
- Narration (short):
  - The transverse metacentric radius `BM_T` depends on the second moment of the waterplane area about the **longitudinal axis** (the foreâ€“aft axis), not the transverse axis.
  - For each intact rectangular strip of length `L/3` and beam `B`, this moment of inertia is `(1/12) Â· (L/3) Â· BÂ³`. With two such strips the result doubles.
  - The longitudinal axis convention means we integrate `yÂ²` across the beam, giving the `BÂ³` term.
- Key equations:
  - `$I_{WL_S} = 2 \times \tfrac{1}{12}\,\tfrac{L}{3}\,B^3 = \tfrac{1}{12}\,\tfrac{2L}{3}\,B^3$`
- Given values:
  - `$I_{WL_S} = \tfrac{1}{12} \times 40 \times 20^3 = \tfrac{1}{12} \times 40 \times 8000$`
  - `$I_{WL_S} \approx 26\,667\,\mathrm{m}^4$`
- Unit check:
  - `I_WL_S` in mâ´.
- Common pitfall:
  - Using `LÂ³` instead of `BÂ³` â€” the longitudinal axis runs foreâ€“aft, so it is the **beam** dimension `B` that appears cubed.
  - Forgetting that the second moment is about the **longitudinal** (not the transverse) axis; the transverse axis would give `BM_L` (longitudinal metacentric radius), not `BM_T`.
- Takeaway: `I_WL_S` is always calculated about the foreâ€“aft axis for transverse stability; this yields the `BÂ³` dependence.

---

## Phase 4 â€” Transverse metacentric radius after damage
- Goal: Compute `BM_T_S` and compare with the intact value.
- Visual cue:
  - Write label "Tverrskips BM etter skade" and equation `BM_T_S = I_WL_S / âˆ‡`.
  - Write comparison equation `BM_T_S < BM_T`.
- Narration (short):
  - The metacentric radius is the ratio of the waterplane second moment (longitudinal axis) to the displacement volume.
  - Because `I_WL_S` is reduced while `âˆ‡` is unchanged, `BM_T_S` is smaller than in the intact condition.
  - This represents a direct loss of transverse stability margin.
- Key equations:
  - `$BM_{T_S} = \dfrac{I_{WL_S}}{\nabla}$`
  - `$BM_{T_S} < BM_T$`
- Given values:
  - `$\nabla = L \cdot B \cdot T = 60 \times 20 \times 4 = 4800\,\mathrm{m}^3$`
  - `$BM_{T_S} = 26\,667 / 4800 \approx 5.56\,\mathrm{m}$`
  - Intact: `$BM_T = I_{WL}/\nabla = (1/12 \times 60 \times 20^3)/4800 = 40\,000/4800 \approx 8.33\,\mathrm{m}$`
- Unit check:
  - `BM_T_S` in meters.
- Common pitfall: Changing `âˆ‡` when computing `BM_T_S` â€” the displacement volume equals the intact draft times intact length times beam (parallel sinkage is separate).
- Takeaway: Flooding a compartment reduces `BM_T` because it cuts the waterplane second moment while leaving `âˆ‡` unchanged.

---

## Reuse blocks

### LaTeX handout seed
```tex
\subsection*{Reduction of transverse metacentric radius after damage}

The transverse metacentric radius is
\[
BM_T = \frac{I_{WL}}{\nabla},
\]
where $I_{WL}$ is the \emph{second moment of the waterplane area about the longitudinal
(foreâ€“aft) centroidal axis} and $\nabla$ is the displacement volume.

After damage to the middle compartment (length $L/3$), the effective waterplane area
reduces from $L \cdot B$ to $\tfrac{2}{3}L \cdot B$, and its second moment about the
longitudinal axis becomes
\[
I_{WL_S} = \frac{1}{12}\,\frac{2L}{3}\,B^3.
\]
Since the displacement volume $\nabla$ is unchanged,
\[
BM_{T_S} = \frac{I_{WL_S}}{\nabla} < BM_T.
\]
This reduces the transverse stability margin of the vessel.
```

### HTML outline seed
```html
<h3>Loss of Transverse BM After Damage</h3>
<ul>
  <li>Intact waterplane: A_WL = L Â· B &rarr; I_WL = (1/12) L BÂ³ (about longitudinal axis).</li>
  <li>Damaged waterplane: middle compartment flooded, A_WL_S = (2/3) L Â· B.</li>
  <li>Damaged second moment (longitudinal axis): I_WL_S = (1/12)(2L/3)BÂ³.</li>
  <li>Displacement volume âˆ‡ is unchanged.</li>
  <li>Therefore BM_T_S = I_WL_S / âˆ‡ &lt; BM_T.</li>
</ul>
```

