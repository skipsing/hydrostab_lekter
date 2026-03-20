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
  - `manim -ql main.py BargeDamageLongitudinalBMScene`
  - `manim -ql main.py BargeDamageHydrostaticsScene`
  - `manim -ql main.py BargeDamageTrimScene`
- PNG-eksportscener (hvit bakgrunn, svart geometri/tekst):
  - `manim -s main.py Hoveddimensjoner_for_en_rektangulaer_lekter`
  - `manim -s main.py Volumdeplasement_for_rektangulaer_lekter`
  - `manim -s main.py Lekteren_har_3_vanntette_avdelinger`
  - `manim -s main.py Lekteren_har_4_vanntette_avdelinger`
  - `manim -s main.py Lekteren_har_5_vanntette_avdelinger`
  - `manim -s main.py Lekteren_har_6_vanntette_avdelinger`
  - `manim -s main.py Flytestilling_ved_symmetrisk_skade`
  - `manim -s main.py Reduksjon_av_tverrskips_BM`
  - `manim -s main.py Vertikal_forflytning_av_oppdriftsenteret_B`
  - `manim -s main.py Langskips_BM_og_LCF_ved_usymmetrisk_skade`
  - `manim -s main.py Trimoppsett`
  - `manim -s main.py Fordeling_av_trim`
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
- `barge_damage_longitudinal_bm_scene.py`:
  - `BargeDamageLongitudinalBMScene`
- `barge_damage_hydrostatics_scene.py`:
  - `BargeDamageHydrostaticsScene`
- `barge_damage_trim_scene.py`:
  - `BargeDamageTrimScene`
- `barge_png_export_scenes.py`:
  - PNG-eksportscener for forelesnings- og oppgavemateriell

## Scene-notater

Notatfiler for gjenbruk i forelesningsdisposisjon, LaTeX og HTML:

- `notes_barge_geometry_scene.md`
- `notes_barge_hydrostatics_scene.md`
- `notes_barge_damage_submergence_scene.md`
- `notes_barge_damage_kb_scene.md`
- `notes_barge_damage_bm_scene.md`

## Notat

Den anbefalte strukturen er å bygge videre på `barge_geometry.py`, de tematiske `barge_*`-scenefilene og `main.py` som samlet entry point. Eldre eksperimentelle og erstattede animasjonsfiler er tatt ut av den støttede strukturen.

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
