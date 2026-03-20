from manim import *

from barge_geometry import ShipParameters, scaled, create_section_rect, create_dimension_arrow


class BargeFloating(Scene):
    """PNG Illustration 1: Barge floating with dimensions"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.camera.background_color = WHITE

    def construct(self):
        params = ShipParameters()
        scale = 0.1

        # Longitudinal section (side view)
        long_width = scaled(params.LPP, scale)
        section_height = scaled(params.D, scale)
        long_section = create_section_rect(long_width, section_height, color=BLACK)
        long_section.shift(LEFT * 3)

        # Transverse section (end view)
        trans_width = scaled(params.B, scale)
        trans_section = create_section_rect(trans_width, section_height, color=BLACK)
        trans_section.shift(RIGHT * 3)

        # Calculate boundaries
        long_left = long_section.get_left()[0]
        long_right = long_section.get_right()[0]
        trans_left = trans_section.get_left()[0]
        trans_right = trans_section.get_right()[0]

        # Waterline
        water_y = scaled(params.T, scale)
        waterline_left = Line(
            start=[long_left - 0.2, water_y, 0],
            end=[long_right + 0.2, water_y, 0],
            color=BLACK,
            stroke_width=2,
        )
        waterline_left.set_dash([0.1, 0.1])

        waterline_right = Line(
            start=[trans_left - 0.2, water_y, 0],
            end=[trans_right + 0.2, water_y, 0],
            color=BLACK,
            stroke_width=2,
        )
        waterline_right.set_dash([0.1, 0.1])

        # Dimension arrows - Length (L)
        L_arrow = create_dimension_arrow(
            long_section.get_left() + UP * (section_height / 2),
            long_section.get_right() + UP * (section_height / 2),
        )
        L_arrow.shift(UP * 0.3)
        L_arrow.set_color(BLACK)
        L_label = Tex(r"L", font_size=36, color=BLACK).next_to(L_arrow, UP, buff=0.1)

        # Dimension arrows - Breadth (B)
        B_arrow = create_dimension_arrow(
            trans_section.get_left() + UP * (section_height / 2),
            trans_section.get_right() + UP * (section_height / 2),
        )
        B_arrow.shift(UP * 0.3)
        B_arrow.set_color(BLACK)
        B_label = Tex(r"B", font_size=36, color=BLACK).next_to(B_arrow, UP, buff=0.1)

        # Dimension arrows - Depth (D)
        D_arrow = create_dimension_arrow(
            trans_section.get_bottom() + LEFT * (trans_width / 2),
            trans_section.get_top() + LEFT * (trans_width / 2),
        )
        D_arrow.shift(LEFT * 0.3)
        D_arrow.set_color(BLACK)
        D_label = Tex(r"D", font_size=36, color=BLACK).next_to(D_arrow, LEFT, buff=0.1)

        # Dimension arrows - Draft (T)
        T_arrow = create_dimension_arrow(
            np.array([long_section.get_left()[0], water_y, 0]),
            np.array([long_section.get_left()[0], 0, 0]),
        )
        T_arrow.shift(LEFT * 0.3)
        T_arrow.set_color(BLACK)
        T_label = Tex(r"T", font_size=36, color=BLACK).next_to(T_arrow, LEFT, buff=0.1)

        # Section labels
        long_label = MathTex(r"\text{Profilsnitt}", font_size=28, color=BLACK).next_to(long_section, DOWN, buff=0.5)
        trans_label = MathTex(r"\text{Tverrsnitt}", font_size=28, color=BLACK).next_to(trans_section, DOWN, buff=0.5)

        # Add all elements
        self.add(
            long_section,
            trans_section,
            waterline_left,
            waterline_right,
            L_arrow,
            L_label,
            B_arrow,
            B_label,
            D_arrow,
            D_label,
            T_arrow,
            T_label,
            long_label,
            trans_label,
        )
