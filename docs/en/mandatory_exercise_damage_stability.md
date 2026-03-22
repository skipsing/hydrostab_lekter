# Mandatory Exercise: Compartment 2 Flooded (Unsymmetric Damage)

## Task

A rectangular barge has 5 equal longitudinal watertight compartments. Compartment 2 (from AP) is fully flooded.

Compute the damaged equilibrium and final drafts, and verify that the trim is counterclockwise with $T_A > T_F$.

## Given

- $L = 80.0\ \mathrm{m}$
- $B = 18.0\ \mathrm{m}$
- $D = 10.0\ \mathrm{m}$
- Initial draft: $T = 3.20\ \mathrm{m}$
- $KG = 3.80\ \mathrm{m}$
- Seawater density: $\rho = 1.025\ \mathrm{t/m^3}$
- $LCG = 40.0\ \mathrm{m}$ from AP (midship)
- 5 equal compartments, so one compartment length is $L/5=16.0\ \mathrm{m}$
- Damaged compartment: No. 2 from AP, spanning $x=16$ to $x=32\ \mathrm{m}$

## Deliverables

1. Initial displacement volume $\nabla$ and displacement $\Delta$
2. Symmetric damaged draft $T_S$ from lost buoyant length
3. Damaged hydrostatic geometry terms: $LCB_S$, $LCF_S$, $I_{WL_S}$, $I_{F_S}$
4. Updated stability terms: $BM_{T_S}$, $BM_{L_S}$, $GM_S$
5. Trimming moment $M_T$ and total trim $t$
6. Trim components $t_a$ and $t_f$ (in cm), and final drafts $T_A$, $T_F$
7. Acceptance checks: $GM_S > 0$ and $\max(T_A,T_F) < D$

## Notes

- Use the same AP-based sign convention as the module.
- Show sign handling clearly for the counterclockwise trim case.
- Expected directional result: final aft draft is larger than final forward draft ($T_A > T_F$).

