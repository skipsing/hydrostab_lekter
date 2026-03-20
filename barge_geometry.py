from manim import *


class ShipParameters:
    """Defines the physical parameters of the vessel."""

    LPP = 60
    B = 20
    D = 10
    T = 4

    @property
    def displacement(self):
        return self.LPP * self.B * self.T


def scaled(value: float, scale: float = 0.1) -> float:
    return value * scale


def create_section_rect(width: float, height: float, color=BLUE, stroke_width=3) -> Rectangle:
    rect = Rectangle(
        width=width,
        height=height,
        stroke_color=color,
        stroke_width=stroke_width,
        fill_opacity=0.0,
    )
    rect.shift(UP * (height / 2))
    return rect


def create_waterline(y: float, width: float, color=BLUE, overhang: float = 0.0) -> Line:
    line = Line(
        start=[-width / 2 - overhang, y, 0],
        end=[width / 2 + overhang, y, 0],
        color=color,
        stroke_width=2,
    )
    line.set_dash([0.1, 0.1])
    return line


def create_dimension_arrow(start: np.ndarray, end: np.ndarray) -> DoubleArrow:
    return DoubleArrow(start=start, end=end, buff=0, stroke_width=2)


class BargeSceneBase(Scene):
    """Shared geometry builders for the lecture scenes."""

    def setup_barge_geometry(self):
        self.params = ShipParameters()
        self.scale = 0.1
        self.profile_width = scaled(self.params.LPP, self.scale)
        self.breadth_width = scaled(self.params.B, self.scale)
        self.depth_height = scaled(self.params.D, self.scale)
        self.water_y = scaled(self.params.T, self.scale)

    def create_profile_view(self, color=GREEN):
        profile = create_section_rect(self.profile_width, self.depth_height, color=color)
        profile.shift(LEFT * 3)
        return profile

    def create_transverse_view(self, color=GREEN):
        transverse = create_section_rect(self.breadth_width, self.depth_height, color=color)
        transverse.shift(RIGHT * 3)
        return transverse

    def create_plan_view(self, color=GREEN):
        plan = Rectangle(
            width=self.profile_width,
            height=self.breadth_width,
            stroke_color=color,
            stroke_width=3,
            fill_opacity=0.0,
        )
        return plan

    def create_compartment_dividers(self, profile, color=GREY):
        left = profile.get_left()[0]
        right = profile.get_right()[0]
        spacing = (right - left) / 3
        dividers = VGroup()
        for index in range(1, 3):
            divider_x = left + index * spacing
            dividers.add(
                Line(
                    start=[divider_x, profile.get_bottom()[1], 0],
                    end=[divider_x, profile.get_top()[1], 0],
                    color=color,
                    stroke_width=2,
                )
            )
        return dividers, spacing

    def create_compartment_labels(self, profile, spacing, color=WHITE):
        left = profile.get_left()[0]
        labels = VGroup()
        for index in range(3):
            label = Tex(str(index + 1), font_size=40, color=color)
            label.move_to([left + (index + 0.5) * spacing, self.depth_height / 2, 0])
            labels.add(label)
        return labels

    def top_text(self, text: str, font_size: int = 32, color=WHITE):
        label = Text(text, font_size=font_size, color=color)
        label.to_edge(UP, buff=0.5)
        label.move_to([0, label.get_y(), 0])
        return label