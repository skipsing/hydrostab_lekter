from manim import *

from barge_geometry import BargeSceneBase, create_dimension_arrow


class BargeGeometryScene(BargeSceneBase):
    """Shows the barge in profile, transverse, and plan view with main dimensions."""

    def construct(self):
        self.setup_barge_geometry()

        profile = self.create_profile_view(color=GREEN)
        profile.shift(UP * 0.6)
        transverse = self.create_transverse_view(color=GREEN)
        transverse.shift(UP * 0.6)
        plan = self.create_plan_view(color=GREEN)
        plan.next_to(profile, DOWN, buff=1.1).align_to(profile, LEFT)

        profile_label = MathTex(r"\text{Profilsnitt}", font_size=28).next_to(profile, DOWN, buff=0.45)
        transverse_label = MathTex(r"\text{Tverrsnitt}", font_size=28).next_to(transverse, DOWN, buff=0.45)
        plan_label = MathTex(r"\text{Plansnitt}", font_size=28).next_to(plan, DOWN, buff=0.25)
        ap_label = Tex(r"AP", font_size=14).next_to(profile.get_corner(DL), DOWN + LEFT, buff=0.05)
        fp_label = Tex(r"FP", font_size=14).next_to(profile.get_corner(DR), DOWN + RIGHT, buff=0.05)

        transverse_cl = DashedLine(
            start=transverse.get_top() + UP * 0.2,
            end=transverse.get_bottom() + DOWN * 0.2,
            color=GREY,
            dashed_ratio=0.6,
        )
        transverse_cl_label = Text("\U00002104", font_size=14).next_to(transverse_cl, DOWN, buff=0.05)

        plan_cl = Line(
            start=plan.get_left() + LEFT * 0.2,
            end=plan.get_right() + RIGHT * 0.2,
            color=GREY,
            stroke_width=2,
        )
        plan_cl_label = Text("\U00002104", font_size=14).next_to(plan_cl.get_right(), RIGHT, buff=0.05)
        ap_plan_label = Tex(r"AP", font_size=14).next_to(plan.get_left() + DOWN * 0.2, LEFT, buff=0.05)
        fp_plan_label = Tex(r"FP", font_size=14).next_to(plan.get_right() + DOWN * 0.2, RIGHT, buff=0.05)

        L_arrow = create_dimension_arrow(profile.get_left() + UP * (self.depth_height / 2), profile.get_right() + UP * (self.depth_height / 2))
        L_arrow.shift(UP * 0.3)
        L_label = Tex(r"L", font_size=34).next_to(L_arrow, UP, buff=0.1)

        D_arrow = create_dimension_arrow(transverse.get_bottom() + LEFT * (self.breadth_width / 2), transverse.get_top() + LEFT * (self.breadth_width / 2))
        D_arrow.shift(LEFT * 0.3)
        D_label = Tex(r"D", font_size=34).next_to(D_arrow, LEFT, buff=0.1)

        beam_arrow_plan = create_dimension_arrow(plan.get_bottom() + LEFT * (plan.width / 2), plan.get_top() + LEFT * (plan.width / 2))
        beam_arrow_plan.shift(LEFT * 0.3)
        beam_label_plan = Tex(r"B", font_size=30).next_to(beam_arrow_plan, LEFT, buff=0.08)

        title = self.top_text("Hoveddimensjoner for en rektangulær lekter", font_size=34)

        self.play(
            FadeIn(profile, transverse, plan, transverse_cl, plan_cl),
            Write(title),
            Write(profile_label),
            Write(transverse_label),
            Write(plan_label),
            Write(ap_label),
            Write(fp_label),
            Write(ap_plan_label),
            Write(fp_plan_label),
            Write(transverse_cl_label),
            Write(plan_cl_label),
        )
        self.play(FadeIn(L_arrow, L_label, D_arrow, D_label))
        self.play(FadeIn(beam_arrow_plan, beam_label_plan))
        self.wait(1)
