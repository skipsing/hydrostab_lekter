# Skadestabilitet (Manim)

Dette prosjektet inneholder Manim-scener for å illustrere skadestabilitet.

## Kjøring

Fra prosjektmappen:

- Støttede forelesningsscener via samlet entry point:
  - `manim -ql illustrations/main.py BargeGeometryScene`
  - `manim -ql illustrations/main.py BargeHydrostaticsScene`
  - `manim -ql illustrations/main.py BargeCompartmentsScene`
  - `manim -ql illustrations/main.py BargeDamageSubmergenceScene`
  - `manim -ql illustrations/main.py BargeDamageKBScene`
  - `manim -ql illustrations/main.py BargeDamageBMScene`
  - `manim -ql illustrations/main.py BargeDamageLongitudinalBMScene`
  - `manim -ql illustrations/main.py BargeDamageHydrostaticsScene`
  - `manim -ql illustrations/main.py BargeDamageTrimScene`
- PNG-eksportscener (hvit bakgrunn, svart geometri/tekst):
  - `manim -s illustrations/main.py Hoveddimensjoner_for_en_rektangulaer_lekter`
  - `manim -s illustrations/main.py Volumdeplasement_for_rektangulaer_lekter`
  - `manim -s illustrations/main.py Lekteren_har_3_vanntette_avdelinger`
  - `manim -s illustrations/main.py Lekteren_har_4_vanntette_avdelinger`
  - `manim -s illustrations/main.py Lekteren_har_5_vanntette_avdelinger`
  - `manim -s illustrations/main.py Lekteren_har_6_vanntette_avdelinger`
  - `manim -s illustrations/main.py Flytestilling_ved_symmetrisk_skade`
  - `manim -s illustrations/main.py Reduksjon_av_tverrskips_BM`
  - `manim -s illustrations/main.py Vertikal_forflytning_av_oppdriftsenteret_B`
  - `manim -s illustrations/main.py Langskips_BM_og_LCF_ved_usymmetrisk_skade`
  - `manim -s illustrations/main.py Trimoppsett`
  - `manim -s illustrations/main.py Fordeling_av_trim`
- Direktekjøring av enkeltfiler fungerer også ved behov.

## Scene-filer

Scene-koden ligger nå i `scenes/`.

- `scenes/barge_geometry.py`:
  - `ShipParameters`
  - `BargeSceneBase`
- `illustrations/main.py`:
  - Samlet entry point for de støttede scenene
- `scenes/barge_geometry_scene.py`:
  - `BargeGeometryScene`
- `scenes/barge_hydrostatics_scene.py`:
  - `BargeHydrostaticsScene`
- `scenes/barge_compartments_scene.py`:
  - `BargeCompartmentsScene`
- `scenes/barge_damage_submergence_scene.py`:
  - `BargeDamageSubmergenceScene`
- `scenes/barge_damage_kb_scene.py`:
  - `BargeDamageKBScene`
- `scenes/barge_damage_bm_scene.py`:
  - `BargeDamageBMScene`
- `scenes/barge_damage_longitudinal_bm_scene.py`:
  - `BargeDamageLongitudinalBMScene`
- `scenes/barge_damage_hydrostatics_scene.py`:
  - `BargeDamageHydrostaticsScene`
- `scenes/barge_damage_trim_scene.py`:
  - `BargeDamageTrimScene`
- `scenes/barge_png_export_scenes.py`:
  - PNG-eksportscener for forelesnings- og oppgavemateriell

## Illustrasjonsverktøy

Skript for rendering og etterbehandling ligger i `illustrations/`:

- `illustrations/main.py`:
  - Samlet Manim entry point for forelesnings- og PNG-scener
- `illustrations/test.py`:
  - Alternativt test-entry point
- `illustrations/speed_up_gifs.py`:
  - Lager raske GIF-varianter i `exports/`
- `illustrations/crop_pngs.py`:
  - Beskjærer PNG-er i `exports/` for mindre whitespace

## Dokumentstruktur

- Norske hovedfiler ligger i prosjektroten:
  - `skadestabilitet_teori.md`
  - `skadestabilitet_oppgaver.md`
  - `skadestabilitet_obligatorisk_oppgave.md`
  - `skadestabilitet_obligatorisk_oppgave_losning.md`
- Engelske oversettelser ligger i `docs/en/`:
  - `docs/en/damage_stability_module.md`
  - `docs/en/damage_stability_exercises.md`
  - `docs/en/mandatory_exercise_damage_stability.md`
  - `docs/en/mandatory_exercise_damage_stability_solution.md`
- Delte figurer/notebooks for begge språk ligger i `exports/`.

## Scene-notater

Notatfiler for gjenbruk i forelesningsdisposisjon, LaTeX og HTML:

- `scenes/notes/notes_barge_geometry_scene.md`
- `scenes/notes/notes_barge_hydrostatics_scene.md`
- `scenes/notes/notes_barge_damage_submergence_scene.md`
- `scenes/notes/notes_barge_damage_kb_scene.md`
- `scenes/notes/notes_barge_damage_bm_scene.md`

## Notat

Den anbefalte strukturen er å bygge videre på `scenes/`, med `illustrations/main.py` som samlet entry point. Eldre eksperimentelle og erstattede animasjonsfiler er tatt ut av den støttede strukturen.

## Publisering til GitHub Pages

Bruk `publish.ps1` til å committe og publisere endringer i `docs/`:

```powershell
# Med commit-melding direkte:
.\publish.ps1 -Message "docs: oppdater teori-side"

# La skriptet spørre om melding:
.\publish.ps1
```

Skriptet stager kun `docs/`, committer og pusher. Det stopper med feil hvis noe går galt.

## Git-strategi (anbefalt)

- En commit per tema:
  - Én sceneendring = én commit.
  - Dokumentasjonsendring = egen commit.
  - Render-filer (`media/`) skal ikke committes.
- Navngiving av commits:
  - `scene: improve trim equations and labels`
  - `docs: update run commands in README`
  - `chore: adjust gitignore for manim outputs`
- Foreslått arbeidsflyt:
  1. `git status`
  2. `git add <relevante filer>`
  3. `git commit -m "<type>: <kort beskrivelse>"`
  4. Kjør aktuell scene raskt med `-ql` før neste commit.

## Render-index

Siste genererte filer (for rask visuell gjennomgang):

- Videoer:
  - [BargeGeometryScene](media/videos/main/480p15/BargeGeometryScene.mp4)
  - [BargeHydrostaticsScene](media/videos/main/480p15/BargeHydrostaticsScene.mp4)
  - [BargeCompartmentsScene](media/videos/main/480p15/BargeCompartmentsScene.mp4)
  - [BargeDamageSubmergenceScene](media/videos/main/480p15/BargeDamageSubmergenceScene.mp4)
  - [BargeDamageKBScene](media/videos/main/480p15/BargeDamageKBScene.mp4)
  - [BargeDamageBMScene](media/videos/main/480p15/BargeDamageBMScene.mp4)
  - [BargeDamageLongitudinalBMScene](media/videos/main/480p15/BargeDamageLongitudinalBMScene.mp4)
  - [BargeDamageHydrostaticsScene](media/videos/main/480p15/BargeDamageHydrostaticsScene.mp4)
  - [BargeDamageTrimScene](media/videos/main/480p15/BargeDamageTrimScene.mp4)



