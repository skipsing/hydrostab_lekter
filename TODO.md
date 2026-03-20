TODO

Goal

Refresh the project into smaller lecture-oriented scenes that are also useful as PNG figures for notes, example calculations, and exercises.

Recommended structure

- Keep the project flat at the repo root for now.
- Use `barge_geometry.py` as the shared geometry/helper module.
- Use one topic-focused scene file per concept.

Current status

- Done: `barge_geometry.py`
- Done: `barge_geometry_scene.py`
- Done: `barge_hydrostatics_scene.py`
- Done: `barge_compartments_scene.py`
- Done: `barge_damage_submergence_scene.py`
- Done: `barge_damage_kb_scene.py`
- Done: `barge_damage_bm_scene.py`
- Done: `barge_damage_longitudinal_bm_scene.py`
- Done: `barge_damage_hydrostatics_scene.py`
- Done: `barge_damage_trim_scene.py`
- Done: legacy `LekterSkadeDypgang*` scenes retired from supported structure

Scene review order

- Review `BargeGeometryScene`
- Review `BargeHydrostaticsScene`
- Review `BargeCompartmentsScene`
- Review `BargeDamageSubmergenceScene`
- Review `BargeDamageKBScene`
- Review `BargeDamageBMScene`
- Review `BargeDamageLongitudinalBMScene`
- Review `BargeDamageHydrostaticsScene`
- Review `BargeDamageTrimScene`

Scene intent

- `barge_geometry_scene.py`
    - Show the barge in 3 projections with dimensions.
    - Place the plane view below the profile view.
- `barge_hydrostatics_scene.py`
    - Show the two existing projections with waterline and the displacement equation.
- `barge_compartments_scene.py`
    - Show only the profile view with compartment labels and dimensions.
- `barge_damage_submergence_scene.py`
    - Phase 1: Show damage to the central compartment.
    - Phase 2: Show flooding and sinking from `T` to `T_S`.
    - Phase 3: Show the damaged position and equation for `T_S`.
- `barge_damage_kb_scene.py`
    - Phase 1: Show three transverse sections, one for each compartment, with `KB` before damage.
    - Phase 2: Show sinking/flooding and move `KB` to `KB_S`.
- `barge_damage_bm_scene.py`
    - Phase 1: Show plane view.
    - Phase 2: Show loss of effective waterplane area.
    - Phase 3: Link reduced `I_T` to reduced transverse `BM_T`.
- `barge_damage_trim_scene.py`
    - Separate trim case with damage in compartment 3.
    - Do not include the `KB` and `BM` scenes here.
    - Show `LCB`, `LCG`, `LCB_T`, trimming moment `TM_S`, rotation about `LCF`, and trim measures `t_a` and `t_f`.

Next implementation batch: PNG-only lecture/exercise scenes

Global requirements for all new PNG scenes

- All scenes use white background.
- All text, lines, arrows, and geometry are black unless a pedagogical color is strictly required.
- Export one PNG at scene end.
- Output filename is based on the scene title text:
    - replace spaces with `_`
    - use ASCII when practical
    - no quotes in file names

Tasks

1) Based on `BargeGeometryScene`
- Create a new scene for PNG export.
- Save PNG at the end.
- Use title-based filename.


2) Based on `BargeHydrostaticsScene`
- Create a new scene for PNG export.
- In final animation, move sections with all dimensions down to center.
- Remove text `\nabla =` (keep only right-hand expression if needed).
- Save PNG with title-based filename.

3) Based on `BargeCompartmentsScene`
- Create a new scene for PNG export.
- Save PNG with title-based filename.

4) Variant set based on task 3
- Create separate scenes with 4, 5, and 6 compartments.
- Update compartment dimensions accordingly.
- Keep total barge length within screen limits.
- Update title text to reflect actual number of compartments.
- Save one PNG per variant using title-based filename.
- Purpose: generate multiple exercise versions with different inputs.

5) Based on `BargeDamageSubmergenceScene`
- Create a new scene for PNG export.
- In final animation, remove all equations and text.
- Move geometry with all dimensions right and down to center.
- Increase size to fill more of the frame.
- Save PNG with title-based filename.

6) Based on `BargeDamageBMScene`
- Create a new scene for PNG export.
- In final animation, remove all equations and text.
- Move geometry with all dimensions right and down to center.
- Increase size to fill more of the frame.
- Save PNG with title-based filename.

7) Based on `BargeDamageKBScene`
- Create a new scene for PNG export.
- In final animation, remove all equations and text.
- Move geometry with all dimensions down to center.
- Increase size to fill more of the frame.
- Save PNG with title-based filename.

8) Based on `BargeDamageLongitudinalBMScene`
- Create a new scene for PNG export.
- In final animation, remove all equations and text.
- Centerline Line is missing 
- Move geometry with all dimensions right and down to center.
- Increase size to fill more of the frame.
- Save PNG with title-based filename.

9) Based on `BargeDamageTrimScene` (trim setup figure)
- Create a new scene for PNG export.
- Stop before text/equation derivation starts.
- Remove top text.
- The png be taken when B has moved aft to B_S and lenght l_k is shown. AP, FP and WL_S is missing
- Move geometry with dimensions plus `B` and `G` arrows right and center.
- Increase size.
- Save PNG with title-based filename.

10) Based on `BargeDamageTrimScene` (trim distribution figure)
- Create a new scene for PNG export.
- In final animation, remove top text and all equations/text.
- The lines for t are rotated.
- Move geometry with dimensions plus `B`, `G`, and `LCF_S` arrows right and center.
- Increase size.
- Save PNG as `Fordeling_av_trim`.
- Reword top text in original trim scene to `Fordeling av trim`.







