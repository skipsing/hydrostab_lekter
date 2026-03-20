# Skadestabilitet (Manim)

Dette prosjektet inneholder Manim-scener for å illustrere skadestabilitet.

## Kjøring

Fra prosjektmappen:

- Støttede forelesningsscener via samlet entry point:
  - `manim -ql main.py BargeGeometryScene`
  - `manim -ql main.py BargeHydrostaticsScene`
  - `manim -ql main.py BargeCompartmentsScene`
  - `manim -ql main.py BargeDamageSubmergenceScene`
  - `manim -ql main.py BargeDamageKBScene`
  - `manim -ql main.py BargeDamageBMScene`
  - `manim -ql main.py BargeDamageHydrostaticsScene`
  - `manim -ql main.py BargeDamageTrimScene`
- Statiske illustrasjoner:
  - `manim -s barge_floating.py BargeFloating`
  - `manim -s barge_with_damage.py BargeWithDamage`
  - `manim -s barge_flooded.py BargeFlooded`
- Direktekjøring av enkeltfiler fungerer også ved behov.

## Scene-filer

- `barge_geometry.py`:
  - `ShipParameters`
  - `BargeSceneBase`
- `main.py`:
  - Samlet entry point for de støttede scenene
- `barge_geometry_scene.py`:
  - `BargeGeometryScene`
- `barge_hydrostatics_scene.py`:
  - `BargeHydrostaticsScene`
- `barge_compartments_scene.py`:
  - `BargeCompartmentsScene`
- `barge_damage_submergence_scene.py`:
  - `BargeDamageSubmergenceScene`
- `barge_damage_kb_scene.py`:
  - `BargeDamageKBScene`
- `barge_damage_bm_scene.py`:
  - `BargeDamageBMScene`
- `barge_damage_hydrostatics_scene.py`:
  - `BargeDamageHydrostaticsScene`
- `barge_damage_trim_scene.py`:
  - `BargeDamageTrimScene`
- `barge_floating.py`:
  - `BargeFloating`
- `barge_with_damage.py`:
  - `BargeWithDamage`
- `barge_flooded.py`:
  - `BargeFlooded`

## Notat

Den anbefalte strukturen er å bygge videre på `barge_geometry.py`, de tematiske `barge_*`-scenefilene og `main.py` som samlet entry point. Eldre eksperimentelle og erstattede animasjonsfiler er tatt ut av den støttede strukturen.
