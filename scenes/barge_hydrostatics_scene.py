from manim import *

from scenes.barge_geometry import BargeSceneBase, create_dimension_arrow


class BargeHydrostaticsScene(BargeSceneBase):
    """Shows the floating barge, the waterline, and the displacement relation."""

    def construct(self):
        self.setup_barge_geometry()

        intro_text = Text("Volumdeplasement for rektangulÃ¦r lekter", font_size=38).move_to(ORIGIN)

        profile = self.create_profile_view(color=GREEN)
        profile.scale(1.15)
        profile.shift(UP * 1.0 + RIGHT * 1.0)
        transverse = self.create_transverse_view(color=GREEN)
        transverse.scale(1.15)
        transverse.shift(UP * 1.0 + RIGHT * 0.5)

        profile_label = MathTex(r"\text{Profilsnitt}", font_size=28).next_to(profile, DOWN, buff=0.45)
        transverse_label = MathTex(r"\text{Tverrsnitt}", font_size=28).next_to(transverse, DOWN, buff=0.45)

        ap_label = Tex(r"AP", font_size=14).next_to(profile.get_corner(DL), DOWN + LEFT, buff=0.05)
        fp_label = Tex(r"FP", font_size=14).next_to(profile.get_corner(DR), DOWN + RIGHT, buff=0.05)

        transverse_cl = DashedLine(
            start=transverse.get_top() + UP * 0.2,
            end=transverse.get_bottom() + DOWN * 0.2,
            color=GREY,
            dashed_ratio=0.6,
        )
        transverse_cl_label = Text("\U00002104", font_size=14).next_to(transverse_cl, DOWN, buff=0.05)

        # Waterline y relative to shifted profiles
        wl_y = profile.get_bottom()[1] + self.water_y

        profile_waterline = Line(
            start=[profile.get_left()[0] - 0.2, wl_y, 0],
            end=[profile.get_right()[0] + 0.2, wl_y, 0],
            color=BLUE,
            stroke_width=2,
        )
        profile_waterline.set_dash([0.1, 0.1])

        transverse_waterline = Line(
            start=[transverse.get_left()[0] - 0.2, wl_y, 0],
            end=[transverse.get_right()[0] + 0.2, wl_y, 0],
            color=BLUE,
            stroke_width=2,
        )
        transverse_waterline.set_dash([0.1, 0.1])

        wl_profile_label = Tex(r"WL", font_size=14).next_to(
            np.array([profile.get_right()[0] + 0.2, wl_y, 0]), RIGHT, buff=0.05
        )
        wl_transverse_label = Tex(r"WL", font_size=14).next_to(
            np.array([transverse.get_right()[0] + 0.2, wl_y, 0]), RIGHT, buff=0.05
        )

        draft_arrow = create_dimension_arrow(
            np.array([profile.get_left()[0], wl_y, 0]),
            np.array([profile.get_left()[0], profile.get_bottom()[1], 0]),
        )
        draft_arrow.shift(LEFT * 0.3)
        draft_label = Tex(r"T", font_size=34).next_to(draft_arrow, LEFT, buff=0.1)

        L_arrow = create_dimension_arrow(
            profile.get_left() + UP * (self.depth_height / 2),
            profile.get_right() + UP * (self.depth_height / 2),
        )
        L_arrow.shift(UP * 0.3)
        L_label = Tex(r"L", font_size=34).next_to(L_arrow, UP, buff=0.1)

        B_arrow = create_dimension_arrow(
            transverse.get_left() + UP * (self.depth_height / 2),
            transverse.get_right() + UP * (self.depth_height / 2),
        )
        B_arrow.shift(UP * 0.3)
        B_label = Tex(r"B", font_size=34).next_to(B_arrow, UP, buff=0.1)

        eq_y = -2.0  # midpoint between centre (0) and bottom (~-4)
        equation = MathTex(r"\nabla = L \times B \times T", font_size=36, color=WHITE)
        equation.move_to([0, eq_y, 0])

        self.add(intro_text)
        self.wait(0.8)
        self.play(FadeOut(intro_text))

        self.play(
            FadeIn(profile, transverse, transverse_cl),
            Write(profile_label),
            Write(transverse_label),
            Write(ap_label),
            Write(fp_label),
            Write(transverse_cl_label),
        )
        self.play(FadeIn(profile_waterline, transverse_waterline), Write(wl_profile_label), Write(wl_transverse_label))
        self.play(FadeIn(L_arrow, L_label))
        self.play(FadeIn(B_arrow, B_label))
        self.play(FadeIn(draft_arrow, draft_label))
        self.play(Write(equation))
        self.wait(1)

