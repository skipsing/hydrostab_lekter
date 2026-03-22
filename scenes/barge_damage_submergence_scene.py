from manim import *

from scenes.barge_geometry import BargeSceneBase, create_dimension_arrow


class BargeDamageSubmergenceScene(BargeSceneBase):
    """Shows damage, flooding, sinking, and the equation for T_S."""

    def construct(self):
        self.setup_barge_geometry()

        layout_shift_x = 0.45

        intro_text = Text("Etablere ny flytestilling ved symmetrisk skade", font_size=38).move_to(ORIGIN)

        profile = self.create_profile_view(color=GREEN)
        profile.scale(1.15)
        profile.shift(UP * 1.0 + RIGHT * layout_shift_x)

        profile_label = MathTex(r"\text{Profilsnitt}", font_size=28).next_to(profile, DOWN, buff=0.45)
        ap_label = Tex(r"AP", font_size=14).next_to(profile.get_corner(DL), DOWN + LEFT, buff=0.05)
        fp_label = Tex(r"FP", font_size=14).next_to(profile.get_corner(DR), DOWN + RIGHT, buff=0.05)

        dividers, spacing = self.create_compartment_dividers(profile)

        left = profile.get_left()[0]
        mid_y = profile.get_center()[1]
        comp_number_labels = VGroup()
        for index in range(3):
            lbl = Tex(str(index + 1), font_size=40)
            lbl.move_to([left + (index + 0.5) * spacing, mid_y, 0])
            comp_number_labels.add(lbl)

        wl_y = profile.get_bottom()[1] + self.water_y
        waterline = Line(
            start=[profile.get_left()[0] - 0.2, wl_y, 0],
            end=[profile.get_right()[0] + 0.2, wl_y, 0],
            color=BLUE,
            stroke_width=2,
        )
        waterline.set_dash([0.1, 0.1])
        wl_label = Tex(r"WL", font_size=14).next_to(
            np.array([profile.get_right()[0] + 0.2, wl_y, 0]), RIGHT, buff=0.05
        )

        comp2_left = left + spacing
        comp2_right = left + 2 * spacing
        comp2_center_x = (comp2_left + comp2_right) / 2
        comp2_width = comp2_right - comp2_left
        comp2_bottom_y = profile.get_bottom()[1]

        self.add(intro_text)
        self.wait(0.8)
        self.play(FadeOut(intro_text))

        # --- Phase 1: initial scene ---
        self.play(
            FadeIn(profile, dividers, waterline, comp_number_labels),
            Write(profile_label),
            Write(ap_label),
            Write(fp_label),
            Write(wl_label),
        )

        # --- Phase 2: stationary damage triangle, then fade out ---
        triangle = Polygon(
            np.array([comp2_center_x, comp2_bottom_y, 0]),
            np.array([comp2_center_x - 0.2, comp2_bottom_y + 0.4, 0]),
            np.array([comp2_center_x + 0.2, comp2_bottom_y + 0.4, 0]),
            color=RED,
            fill_opacity=0.8,
        )
        self.play(FadeIn(triangle))
        self.wait(0.5)
        self.play(FadeOut(triangle))

        # --- Phase 3: flooding and sinking ---
        water_fill = Rectangle(
            width=comp2_width,
            height=self.water_y,
            fill_color=BLUE,
            fill_opacity=0.5,
            stroke_opacity=0,
        )
        water_fill.move_to([comp2_center_x, comp2_bottom_y + self.water_y / 2, 0])
        self.play(FadeIn(water_fill))

        t_s_arrow = always_redraw(
            lambda: create_dimension_arrow(
                np.array([profile.get_left()[0], wl_y, 0]),
                np.array([profile.get_left()[0], profile.get_bottom()[1], 0]),
            ).shift(LEFT * 0.3)
        )
        t_s_label = always_redraw(
            lambda: MathTex(r"T_S", font_size=32).next_to(t_s_arrow, LEFT, buff=0.1)
        )
        self.play(FadeIn(t_s_arrow, t_s_label))

        descent = 0.3
        self.play(
            profile.animate.shift(DOWN * descent),
            dividers.animate.shift(DOWN * descent),
            comp_number_labels.animate.shift(DOWN * descent),
            profile_label.animate.shift(DOWN * descent),
            ap_label.animate.shift(DOWN * descent),
            fp_label.animate.shift(DOWN * descent),
            water_fill.animate.shift(DOWN * descent).stretch_to_fit_height(
                self.water_y + descent, about_edge=DOWN
            ),
            run_time=2,
        )

        # --- Phase 4: equation sequence, centred at eq_cx ---
        eq_cx = 3.2 + layout_shift_x   # horizontal centre of the text column
        eq_top = 2.5  # top y of first item

        def cx(mob):
            """Re-centre mob horizontally at eq_cx after positioning."""
            mob.set_x(eq_cx)
            return mob

        txt1 = cx(Text("Likevekt fÃ¸r skade", font_size=20).move_to([eq_cx, eq_top, 0]))
        eq1  = cx(MathTex(r"\nabla = L \cdot B \cdot T", font_size=30).next_to(txt1, DOWN, buff=0.12))

        # L/3 dimension arrows above compartments 1 and 3
        arrow_y = profile.get_top()[1] + 0.35
        comp1_arrow = create_dimension_arrow(
            np.array([left, arrow_y, 0]),
            np.array([left + spacing, arrow_y, 0]),
        )
        comp3_arrow = create_dimension_arrow(
            np.array([left + 2 * spacing, arrow_y, 0]),
            np.array([left + 3 * spacing, arrow_y, 0]),
        )
        comp1_dim_label = Tex(r"L/3", font_size=22).next_to(comp1_arrow, UP, buff=0.08)
        comp3_dim_label = Tex(r"L/3", font_size=22).next_to(comp3_arrow, UP, buff=0.08)

        txt2 = cx(Text("Likevekt etter skade", font_size=20).next_to(eq1, DOWN, buff=0.3))
        eq2  = cx(MathTex(
            r"\nabla_S = \left(\tfrac{1}{3} + \tfrac{1}{3}\right) L \cdot B \cdot T_S",
            font_size=28,
        ).next_to(txt2, DOWN, buff=0.12))

        txt3 = cx(Text("Volumdeplasementet er uendret", font_size=20).next_to(eq2, DOWN, buff=0.3))
        eq3  = cx(MathTex(r"\nabla = \nabla_S", font_size=30).next_to(txt3, DOWN, buff=0.12))

        down_arrow = Arrow(
            start=eq3.get_bottom() + DOWN * 0.05,
            end=eq3.get_bottom() + DOWN * 0.45,
            buff=0,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.25,
        ).set_x(eq_cx)

        eq4 = cx(MathTex(
            r"L \cdot B \cdot T = \tfrac{2}{3}\,L \cdot B \cdot T_S",
            font_size=28,
        ).next_to(down_arrow, DOWN, buff=0.1))

        txt5 = cx(Text("Ny likevektsposisjon ved", font_size=20).next_to(eq4, DOWN, buff=0.3))
        eq5  = cx(MathTex(
            r"T_S = \frac{\nabla}{\tfrac{2}{3}\,L \cdot B}",
            font_size=30,
        ).next_to(txt5, DOWN, buff=0.12))

        self.play(Write(txt1), Write(eq1))
        self.wait(1.0)
        self.play(
            Write(txt2),
            FadeIn(comp1_arrow, comp1_dim_label, comp3_arrow, comp3_dim_label),
        )
        self.play(Write(eq2))
        self.wait(1.0)
        self.play(Write(txt3), Write(eq3))
        self.wait(1.0)
        self.play(FadeIn(down_arrow))
        self.play(Write(eq4))
        self.wait(1.0)
        self.play(Write(txt5))
        self.play(Write(eq5))
        self.wait(1.5)

