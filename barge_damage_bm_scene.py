from manim import *

from barge_geometry import BargeSceneBase, create_dimension_arrow


class BargeDamageBMScene(BargeSceneBase):
    """Shows loss of effective waterplane area and reduced transverse BM."""

    def construct(self):
        self.setup_barge_geometry()

        plan = self.create_plan_view(color=GREEN)
        plan.move_to([-2.4, 0.5, 0])

        plan_label = MathTex(r"\text{Plansnitt}", font_size=28).next_to(plan, DOWN, buff=0.25)
        plan_label.shift(LEFT * 0.2)
        ap_label = Tex(r"AP", font_size=14).next_to(plan.get_left() + DOWN * 0.2, LEFT, buff=0.05)
        fp_label = Tex(r"FP", font_size=14).next_to(plan.get_right() + DOWN * 0.2, RIGHT, buff=0.05)

        plan_cl = Line(
            start=plan.get_left() + LEFT * 0.2,
            end=plan.get_right() + RIGHT * 0.2,
            color=GREY,
            stroke_width=2,
        )
        plan_cl_label = Text("\U00002104", font_size=14).next_to(plan_cl.get_right(), RIGHT, buff=0.05)

        b_arrow = create_dimension_arrow(
            np.array([plan.get_left()[0], plan.get_bottom()[1], 0]),
            np.array([plan.get_left()[0], plan.get_top()[1], 0]),
        )
        b_arrow.shift(LEFT * 0.35)
        b_label = Tex(r"B", font_size=28).next_to(b_arrow, LEFT, buff=0.08)

        left_x = plan.get_left()[0]
        right_x = plan.get_right()[0]
        spacing = (right_x - left_x) / 3
        divider_1_x = left_x + spacing
        divider_2_x = left_x + 2 * spacing

        divider_1 = Line(
            start=[divider_1_x, plan.get_bottom()[1], 0],
            end=[divider_1_x, plan.get_top()[1], 0],
            color=GREY,
            stroke_width=2,
        )
        divider_2 = Line(
            start=[divider_2_x, plan.get_bottom()[1], 0],
            end=[divider_2_x, plan.get_top()[1], 0],
            color=GREY,
            stroke_width=2,
        )

        comp_labels = VGroup()
        for index in range(3):
            label = Tex(str(index + 1), font_size=34)
            label.move_to([left_x + (index + 0.5) * spacing, plan.get_center()[1], 0])
            comp_labels.add(label)

        active_left = Rectangle(
            width=spacing,
            height=plan.height,
            fill_color=GREEN,
            fill_opacity=0.18,
            stroke_opacity=0,
        ).move_to([left_x + spacing / 2, plan.get_center()[1], 0])
        lost_zone = Rectangle(
            width=spacing,
            height=plan.height,
            fill_color=RED,
            fill_opacity=0.28,
            stroke_opacity=0,
        ).move_to([left_x + 1.5 * spacing, plan.get_center()[1], 0])
        active_right = Rectangle(
            width=spacing,
            height=plan.height,
            fill_color=GREEN,
            fill_opacity=0.18,
            stroke_opacity=0,
        ).move_to([left_x + 2.5 * spacing, plan.get_center()[1], 0])

        lost_cross = VGroup(
            Line(
                start=[divider_1_x, plan.get_top()[1], 0],
                end=[divider_2_x, plan.get_bottom()[1], 0],
                color=RED,
                stroke_width=4,
            ),
            Line(
                start=[divider_2_x, plan.get_top()[1], 0],
                end=[divider_1_x, plan.get_bottom()[1], 0],
                color=RED,
                stroke_width=4,
            ),
        )

        left_dim = create_dimension_arrow(
            np.array([left_x, plan.get_top()[1] + 0.35, 0]),
            np.array([divider_1_x, plan.get_top()[1] + 0.35, 0]),
        )
        left_dim_label = Tex(r"L/3", font_size=24).next_to(left_dim, UP, buff=0.08)
        right_dim = create_dimension_arrow(
            np.array([divider_2_x, plan.get_top()[1] + 0.35, 0]),
            np.array([right_x, plan.get_top()[1] + 0.35, 0]),
        )
        right_dim_label = Tex(r"L/3", font_size=24).next_to(right_dim, UP, buff=0.08)

        eq_cx = 3.6
        eq_top = 2.3

        def cx(mob):
            mob.set_x(eq_cx)
            return mob

        txt1 = cx(Text("Vannlinjeareal før skade", font_size=20).move_to([eq_cx, eq_top, 0]))
        eq1 = cx(MathTex(r"A_{WL} = L \cdot B", font_size=30).next_to(txt1, DOWN, buff=0.12))

        txt2 = cx(Text("Effektivt vannlinjeareal etter skade", font_size=20).next_to(eq1, DOWN, buff=0.32))
        eq2 = cx(MathTex(r"A_{WL_S} = \tfrac{2}{3} L \cdot B", font_size=30).next_to(txt2, DOWN, buff=0.12))

        txt3 = cx(Text("Vannlinjearealets treghetsmoment", font_size=20).next_to(eq2, DOWN, buff=0.32))
        eq3 = cx(MathTex(r"I_{WL_S} = \tfrac{1}{12}\left(\tfrac{2}{3}L\right) B^3", font_size=30).next_to(txt3, DOWN, buff=0.12))

        txt4 = cx(Text("Tverrskips BM etter skade", font_size=20).next_to(eq3, DOWN, buff=0.32))
        eq4 = cx(MathTex(r"BM_{T_S} = \frac{I_{WL_S}}{\nabla}", font_size=30).next_to(txt4, DOWN, buff=0.12))
        eq5 = cx(MathTex(r"BM_{T_S} < BM_T", font_size=30).next_to(eq4, DOWN, buff=0.22))

        title = self.top_text("Reduksjon av tverrskips BM ved tap av vannlinjeareal", font_size=30)

        self.play(
            FadeIn(plan, plan_cl, b_arrow, b_label),
            Write(title),
            Write(plan_label),
            Write(ap_label),
            Write(fp_label),
            Write(plan_cl_label),
        )
        self.play(FadeIn(divider_1, divider_2, comp_labels))
        self.play(Write(txt1), Write(eq1))

        self.play(
            FadeIn(active_left, active_right, lost_zone, lost_cross),
            FadeIn(left_dim, left_dim_label, right_dim, right_dim_label),
        )
        self.play(Write(txt2), Write(eq2))
        self.play(Write(txt3), Write(eq3))
        self.play(Write(txt4), Write(eq4))
        self.play(Write(eq5))
        self.wait(1)
