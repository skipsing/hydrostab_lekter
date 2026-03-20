from manim import *

from barge_geometry import ShipParameters, scaled, create_section_rect


class BargeWithDamage(Scene):
    """PNG Illustration 2: Barge with damage indicator and X"""

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

        # Original waterline (reference, faded)
        water_y = scaled(params.T, scale)
        waterline_original = Line(
            start=[long_left - 0.5, water_y, 0],
            end=[long_right + 0.2, water_y, 0],
            color=GREY,
            stroke_width=1,
        )
        waterline_original.set_dash([0.1, 0.1])

        # New waterline (T_S = 1.5 * T) - showing flooded state
        new_water_y = water_y * 1.5
        waterline_new = Line(
            start=[long_left - 0.5, new_water_y, 0],
            end=[long_right + 0.2, new_water_y, 0],
            color=BLACK,
            stroke_width=2,
        )
        waterline_new.set_dash([0.1, 0.1])

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

        # Compartment 2 damage
        comp2_left = long_left + divider_spacing
        comp2_right = long_left + 2 * divider_spacing
        comp2_width = comp2_right - comp2_left
        comp2_center_x = (comp2_left + comp2_right) / 2
        comp2_bottom_y = long_section.get_bottom()[1]

        # Water fill in compartment 2 (up to new waterline T_S)
        water_fill = Rectangle(
            width=comp2_width,
            height=new_water_y,
            fill_color=GREY,
            fill_opacity=0.5,
            stroke_opacity=0,
        )
        water_fill.move_to([(comp2_left + comp2_right) / 2, new_water_y / 2, 0])

        # Damage triangle
        triangle = Polygon(
            np.array([comp2_center_x, -2, 0]),
            np.array([comp2_center_x - 0.15, -1.8, 0]),
            np.array([comp2_center_x + 0.15, -1.8, 0]),
            color=BLACK,
            fill_opacity=0.8,
        )
        triangle.rotate(PI)
        triangle.move_to([comp2_center_x, comp2_bottom_y, 0])

        # X through compartment 2
        x_line1 = Line(
            start=[comp2_left, long_section.get_top()[1], 0],
            end=[comp2_right, long_section.get_bottom()[1], 0],
            color=BLACK,
            stroke_width=4,
        )
        x_line2 = Line(
            start=[comp2_right, long_section.get_top()[1], 0],
            end=[comp2_left, long_section.get_bottom()[1], 0],
            color=BLACK,
            stroke_width=4,
        )

        # Add all elements
        self.add(long_section, waterline_new, compartment_dividers, triangle, x_line1, x_line2)
