from manim import *

from barge_geometry import ShipParameters, scaled, create_section_rect, create_dimension_arrow


class BargeFlooded(Scene):
    """PNG Illustration 3: Barge flooded with new draft T_S"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.camera.background_color = WHITE

    def construct(self):
        params = ShipParameters()
        scale = 0.1

        # Longitudinal section
        long_width = scaled(params.LPP, scale)
        section_height = scaled(params.D, scale)
        long_section = create_section_rect(long_width, section_height, color=BLACK)
        long_section.shift(LEFT * 3)

        long_left = long_section.get_left()[0]
        long_right = long_section.get_right()[0]

        # Original waterline (reference)
        water_y = scaled(params.T, scale)
        waterline_original = Line(
            start=[long_left - 0.5, water_y, 0],
            end=[long_right + 0.2, water_y, 0],
            color=GREY,
            stroke_width=1,
        )
        waterline_original.set_dash([0.1, 0.1])

        # Compartment dividers
        divider_spacing = (long_right - long_left) / 3
        compartment_dividers = VGroup()
        for i in range(1, 3):
            divider_x = long_left + i * divider_spacing
            divider = Line(
                start=[divider_x, long_section.get_bottom()[1], 0],
                end=[divider_x, long_section.get_top()[1], 0],
                color=BLACK,
                stroke_width=2,
            )
            compartment_dividers.add(divider)

        # Flooded compartment 2
        comp2_left = long_left + divider_spacing
        comp2_right = long_left + 2 * divider_spacing
        comp2_width = comp2_right - comp2_left
        comp2_height = water_y

        water_fill = Rectangle(
            width=comp2_width,
            height=comp2_height,
            fill_color=GREY,
            fill_opacity=0.5,
            stroke_opacity=0,
        )
        water_fill.move_to([(comp2_left + comp2_right) / 2, comp2_height / 2, 0])

        # New waterline (T_S = 1.5 * T)
        new_water_y = water_y * 1.5
        waterline_new = Line(
            start=[long_left - 0.5, new_water_y, 0],
            end=[long_right + 0.2, new_water_y, 0],
            color=BLACK,
            stroke_width=2,
        )
        waterline_new.set_dash([0.1, 0.1])

        # Original draft dimension (faded)
        T_arrow_orig = create_dimension_arrow(
            np.array([long_left, water_y, 0]),
            np.array([long_left, 0, 0]),
        )
        T_arrow_orig.shift(LEFT * 0.3)
        T_arrow_orig.set_opacity(0.5)
        T_arrow_orig.set_color(GREY)
        T_label_orig = Tex(r"T", font_size=32, color=GREY).next_to(T_arrow_orig, LEFT, buff=0.1)

        # New draft dimension (highlighted)
        T_skade_arrow = create_dimension_arrow(
            np.array([long_left, new_water_y, 0]),
            np.array([long_left, 0, 0]),
        )
        T_skade_arrow.shift(LEFT * 0.3)
        T_skade_arrow.set_color(BLACK)
        T_skade_label = MathTex(r"T_S", font_size=32, color=BLACK).next_to(T_skade_arrow, LEFT, buff=0.1)

        # Add all elements
        self.add(
            long_section,
            waterline_new,
            compartment_dividers,
            water_fill,
            T_skade_arrow,
            T_skade_label,
        )
