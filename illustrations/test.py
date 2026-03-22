"""Entry point that re-exports the currently supported Manim scenes."""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scenes.barge_geometry_scene import BargeGeometryScene as _BargeGeometryScene
from scenes.barge_hydrostatics_scene import BargeHydrostaticsScene as _BargeHydrostaticsScene
from scenes.barge_compartments_scene import BargeCompartmentsScene as _BargeCompartmentsScene
from scenes.barge_damage_submergence_scene import BargeDamageSubmergenceScene as _BargeDamageSubmergenceScene
from scenes.barge_damage_kb_scene import BargeDamageKBScene as _BargeDamageKBScene
from scenes.barge_damage_bm_scene import BargeDamageBMScene as _BargeDamageBMScene
from scenes.barge_damage_hydrostatics_scene import BargeDamageHydrostaticsScene as _BargeDamageHydrostaticsScene
from scenes.barge_damage_trim_scene import BargeDamageTrimScene as _BargeDamageTrimScene


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


if __name__ == "__main__":
    print("Run with:")
    print("  manim -ql illustrations/test.py BargeGeometryScene")
    print("  manim -ql illustrations/test.py BargeHydrostaticsScene")
    print("  manim -ql illustrations/test.py BargeCompartmentsScene")
    print("  manim -ql illustrations/test.py BargeDamageSubmergenceScene")
    print("  manim -ql illustrations/test.py BargeDamageKBScene")
    print("  manim -ql illustrations/test.py BargeDamageBMScene")
    print("  manim -ql illustrations/test.py BargeDamageHydrostaticsScene")
    print("  manim -ql illustrations/test.py BargeDamageTrimScene")

