TODO

Goal: refresh the project into smaller lecture-oriented scenes that are also useful as PNG figures for notes, example calculations, and exercises.

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
- Review `BargeDamageHydrostaticsScene`
- Review `BargeDamageTrimScene`

Scene intent

- `barge_geometry_scene.py`
    - Show the barge in 3 projections with dimensions.
    - Plane view is placed below the profile view.
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
    - Phase 2: Show sinking/filling and move `KB` to `KB_S`.
- `barge_damage_bm_scene.py`
    - Phase 1: Show plane view.
    - Phase 2: Show loss of effective waterplane area.
    - Phase 3: Link reduced `I_T` to reduced transverse `BM_T`.
- `barge_damage_trim_scene.py`
    - Separate trim case with damage in compartment 3.
    - Do not include the `KB` and `BM` scenes here.
    - Show `LCB`, `LCG`, `LCB_T`, trimming moment `TM_S`, rotation about `LCF`, and trim measures `t_a` and `t_f`.

Open decisions

- Decide whether trim should remain one scene file with several phases or be split further later.
- Review each new scene and tighten the pedagogy before adding more detailed animation.

- next step = review all completed scenes for final polish and consistency
