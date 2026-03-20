"""Entry point that re-exports the currently supported Manim scenes."""

from barge_geometry_scene import BargeGeometryScene as _BargeGeometryScene
from barge_hydrostatics_scene import BargeHydrostaticsScene as _BargeHydrostaticsScene
from barge_compartments_scene import BargeCompartmentsScene as _BargeCompartmentsScene
from barge_damage_submergence_scene import BargeDamageSubmergenceScene as _BargeDamageSubmergenceScene
from barge_damage_kb_scene import BargeDamageKBScene as _BargeDamageKBScene
from barge_damage_bm_scene import BargeDamageBMScene as _BargeDamageBMScene
from barge_damage_longitudinal_bm_scene import BargeDamageLongitudinalBMScene as _BargeDamageLongitudinalBMScene
from barge_damage_hydrostatics_scene import BargeDamageHydrostaticsScene as _BargeDamageHydrostaticsScene
from barge_damage_trim_scene import BargeDamageTrimScene as _BargeDamageTrimScene
from barge_png_export_scenes import Hoveddimensjoner_for_en_rektangulaer_lekter as _Hoveddimensjoner_for_en_rektangulaer_lekter
from barge_png_export_scenes import Volumdeplasement_for_rektangulaer_lekter as _Volumdeplasement_for_rektangulaer_lekter
from barge_png_export_scenes import Lekteren_har_3_vanntette_avdelinger as _Lekteren_har_3_vanntette_avdelinger
from barge_png_export_scenes import Lekteren_har_4_vanntette_avdelinger as _Lekteren_har_4_vanntette_avdelinger
from barge_png_export_scenes import Lekteren_har_5_vanntette_avdelinger as _Lekteren_har_5_vanntette_avdelinger
from barge_png_export_scenes import Lekteren_har_6_vanntette_avdelinger as _Lekteren_har_6_vanntette_avdelinger
from barge_png_export_scenes import Flytestilling_ved_symmetrisk_skade as _Flytestilling_ved_symmetrisk_skade
from barge_png_export_scenes import Reduksjon_av_tverrskips_BM as _Reduksjon_av_tverrskips_BM
from barge_png_export_scenes import Vertikal_forflytning_av_oppdriftsenteret_B as _Vertikal_forflytning_av_oppdriftsenteret_B
from barge_png_export_scenes import Langskips_BM_og_LCF_ved_usymmetrisk_skade as _Langskips_BM_og_LCF_ved_usymmetrisk_skade
from barge_png_export_scenes import Trimoppsett as _Trimoppsett
from barge_png_export_scenes import Fordeling_av_trim as _Fordeling_av_trim


class BargeGeometryScene(_BargeGeometryScene):
    pass


class BargeHydrostaticsScene(_BargeHydrostaticsScene):
    pass


class BargeCompartmentsScene(_BargeCompartmentsScene):
    pass


class BargeDamageSubmergenceScene(_BargeDamageSubmergenceScene):
    pass


class BargeDamageKBScene(_BargeDamageKBScene):
    pass


class BargeDamageBMScene(_BargeDamageBMScene):
    pass


class BargeDamageLongitudinalBMScene(_BargeDamageLongitudinalBMScene):
    pass


class BargeDamageHydrostaticsScene(_BargeDamageHydrostaticsScene):
    pass


class BargeDamageTrimScene(_BargeDamageTrimScene):
    pass


class Hoveddimensjoner_for_en_rektangulaer_lekter(_Hoveddimensjoner_for_en_rektangulaer_lekter):
    pass


class Volumdeplasement_for_rektangulaer_lekter(_Volumdeplasement_for_rektangulaer_lekter):
    pass


class Lekteren_har_3_vanntette_avdelinger(_Lekteren_har_3_vanntette_avdelinger):
    pass


class Lekteren_har_4_vanntette_avdelinger(_Lekteren_har_4_vanntette_avdelinger):
    pass


class Lekteren_har_5_vanntette_avdelinger(_Lekteren_har_5_vanntette_avdelinger):
    pass


class Lekteren_har_6_vanntette_avdelinger(_Lekteren_har_6_vanntette_avdelinger):
    pass


class Flytestilling_ved_symmetrisk_skade(_Flytestilling_ved_symmetrisk_skade):
    pass


class Reduksjon_av_tverrskips_BM(_Reduksjon_av_tverrskips_BM):
    pass


class Vertikal_forflytning_av_oppdriftsenteret_B(_Vertikal_forflytning_av_oppdriftsenteret_B):
    pass


class Langskips_BM_og_LCF_ved_usymmetrisk_skade(_Langskips_BM_og_LCF_ved_usymmetrisk_skade):
    pass


class Trimoppsett(_Trimoppsett):
    pass


class Fordeling_av_trim(_Fordeling_av_trim):
    pass


if __name__ == "__main__":
    print("Run with:")
    print("  manim -ql main.py BargeGeometryScene")
    print("  manim -ql main.py BargeHydrostaticsScene")
    print("  manim -ql main.py BargeCompartmentsScene")
    print("  manim -ql main.py BargeDamageSubmergenceScene")
    print("  manim -ql main.py BargeDamageKBScene")
    print("  manim -ql main.py BargeDamageBMScene")
    print("  manim -ql main.py BargeDamageLongitudinalBMScene")
    print("  manim -ql main.py BargeDamageHydrostaticsScene")
    print("  manim -ql main.py BargeDamageTrimScene")
    print("  manim -s main.py Hoveddimensjoner_for_en_rektangulaer_lekter")
    print("  manim -s main.py Volumdeplasement_for_rektangulaer_lekter")
    print("  manim -s main.py Lekteren_har_3_vanntette_avdelinger")
    print("  manim -s main.py Lekteren_har_4_vanntette_avdelinger")
    print("  manim -s main.py Lekteren_har_5_vanntette_avdelinger")
    print("  manim -s main.py Lekteren_har_6_vanntette_avdelinger")
    print("  manim -s main.py Flytestilling_ved_symmetrisk_skade")
    print("  manim -s main.py Reduksjon_av_tverrskips_BM")
    print("  manim -s main.py Vertikal_forflytning_av_oppdriftsenteret_B")
    print("  manim -s main.py Langskips_BM_og_LCF_ved_usymmetrisk_skade")
    print("  manim -s main.py Trimoppsett")
    print("  manim -s main.py Fordeling_av_trim")
