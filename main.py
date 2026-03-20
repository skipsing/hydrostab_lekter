"""Entry point that re-exports the currently supported Manim scenes."""

from barge_geometry_scene import BargeGeometryScene as _BargeGeometryScene
from barge_hydrostatics_scene import BargeHydrostaticsScene as _BargeHydrostaticsScene
from barge_compartments_scene import BargeCompartmentsScene as _BargeCompartmentsScene
from barge_damage_submergence_scene import BargeDamageSubmergenceScene as _BargeDamageSubmergenceScene
from barge_damage_kb_scene import BargeDamageKBScene as _BargeDamageKBScene
from barge_damage_bm_scene import BargeDamageBMScene as _BargeDamageBMScene
from barge_damage_hydrostatics_scene import BargeDamageHydrostaticsScene as _BargeDamageHydrostaticsScene
from barge_damage_trim_scene import BargeDamageTrimScene as _BargeDamageTrimScene
from barge_floating import BargeFloating as _BargeFloating
from barge_with_damage import BargeWithDamage as _BargeWithDamage
from barge_flooded import BargeFlooded as _BargeFlooded


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


class BargeDamageHydrostaticsScene(_BargeDamageHydrostaticsScene):
    pass


class BargeDamageTrimScene(_BargeDamageTrimScene):
    pass


class BargeFloating(_BargeFloating):
    pass


class BargeWithDamage(_BargeWithDamage):
    pass


class BargeFlooded(_BargeFlooded):
    pass


if __name__ == "__main__":
    print("Run with:")
    print("  manim -ql main.py BargeGeometryScene")
    print("  manim -ql main.py BargeHydrostaticsScene")
    print("  manim -ql main.py BargeCompartmentsScene")
    print("  manim -ql main.py BargeDamageSubmergenceScene")
    print("  manim -ql main.py BargeDamageKBScene")
    print("  manim -ql main.py BargeDamageBMScene")
    print("  manim -ql main.py BargeDamageHydrostaticsScene")
    print("  manim -ql main.py BargeDamageTrimScene")
    print("  manim -s main.py BargeFloating")
    print("  manim -s main.py BargeWithDamage")
    print("  manim -s main.py BargeFlooded")
    print("  manim -s barge_floating.py BargeFloating")
    print("  manim -s barge_with_damage.py BargeWithDamage")
    print("  manim -s barge_flooded.py BargeFlooded")
