from manim import *

from barge_geometry import BargeSceneBase, create_dimension_arrow


class BargeDamageKBScene(BargeSceneBase):
    """Shows how KB shifts upward after damage flooding of compartment 2."""

    def construct(self):
        self.setup_barge_geometry()

        intro_text = Text("Vertikal forflytning av oppdriftsenteret B", font_size=36).move_to(ORIGIN)

        sf = 1.5   # visual scale factor for sections
        sw = self.breadth_width * sf      # scaled width  = 3.0
        sh = self.depth_height * sf       # scaled height = 1.5
        wy = self.water_y * sf            # scaled draft T = 0.6
        descent = 0.3 * sf               # scaled sinking = 0.45
        T_s = wy + descent               # scaled T_S = 1.05
        KB   = wy / 2                    # visual KB
        KB_s = T_s / 2                   # visual KB_S

        cx_left  = -3.0
        cx_right =  3.0
        base_y   =  0.0   # keel y

        # ── helper: waterline dash line ───────────────────────────────────────
        def make_wl(x_left, x_right, y, col=BLUE):
            l = Line([x_left - 0.2, y, 0], [x_right + 0.2, y, 0], color=col, stroke_width=2)
            l.set_dash([0.1, 0.1])
            return l

        # ── left section: before damage ───────────────────────────────────────
        sect_l = Rectangle(
            width=sw, height=sh,
            stroke_color=GREEN, stroke_width=3, fill_opacity=0,
        ).move_to([cx_left, base_y + sh / 2, 0])

        wl_y_l = base_y + wy
        wl_l = make_wl(sect_l.get_left()[0], sect_l.get_right()[0], wl_y_l)
        wl_label_l = Tex(r"WL", font_size=14).next_to(
            np.array([sect_l.get_right()[0] + 0.2, wl_y_l, 0]), RIGHT, buff=0.05
        )

        cl_l = DashedLine(sect_l.get_top() + UP * 0.2, sect_l.get_bottom() + DOWN * 0.2,
                          color=GREY, dashed_ratio=0.6)
        cl_label_l = Text("\U00002104", font_size=14).next_to(cl_l, DOWN, buff=0.05)

        kb_dot_l = Dot([cx_left, base_y + KB, 0], color=YELLOW, radius=0.08)
        kb_label_l = MathTex(r"B", font_size=28, color=YELLOW).next_to(kb_dot_l, RIGHT, buff=0.1)

        kb_arrow_l = create_dimension_arrow(
            np.array([sect_l.get_left()[0] - 0.4, base_y, 0]),
            np.array([sect_l.get_left()[0] - 0.4, base_y + KB, 0]),
        )
        kb_arr_label_l = MathTex(r"K\!B", font_size=22).next_to(kb_arrow_l, LEFT, buff=0.08)
        kb_guide_l = Line(
            start=[kb_arrow_l.get_center()[0], base_y + KB, 0],
            end=[cx_left, base_y + KB, 0],
            color=GREY,
            stroke_width=1.5,
        )

        sect_l_title = MathTex(r"\text{Før skade}", font_size=28).next_to(sect_l, UP, buff=0.3)
        sect_l_sublabel = MathTex(r"\text{Tverrsnitt}", font_size=24).next_to(sect_l, DOWN, buff=0.55)

        # ── right section: after damage ───────────────────────────────────────
        sect_r = Rectangle(
            width=sw, height=sh,
            stroke_color=GREEN, stroke_width=3, fill_opacity=0,
        ).move_to([cx_right, base_y + sh / 2, 0])

        wl_y_r = base_y + T_s
        wl_r = make_wl(sect_r.get_left()[0], sect_r.get_right()[0], wl_y_r)
        wl_label_r = MathTex(r"WL_S", font_size=14).next_to(
            np.array([sect_r.get_right()[0] + 0.2, wl_y_r, 0]), RIGHT, buff=0.05
        )

        cl_r = DashedLine(sect_r.get_top() + UP * 0.2, sect_r.get_bottom() + DOWN * 0.2,
                          color=GREY, dashed_ratio=0.6)
        cl_label_r = Text("\U00002104", font_size=14).next_to(cl_r, DOWN, buff=0.05)

        kb_dot_r = Dot([cx_right, base_y + KB_s, 0], color=YELLOW, radius=0.08)
        kb_label_r = MathTex(r"B_S", font_size=28, color=YELLOW).next_to(kb_dot_r, RIGHT, buff=0.1)

        kb_arrow_r = create_dimension_arrow(
            np.array([sect_r.get_left()[0] - 0.4, base_y, 0]),
            np.array([sect_r.get_left()[0] - 0.4, base_y + KB_s, 0]),
        )
        kb_arr_label_r = MathTex(r"K\!B_S", font_size=22).next_to(kb_arrow_r, LEFT, buff=0.08)
        kb_guide_r = Line(
            start=[kb_arrow_r.get_center()[0], base_y + KB_s, 0],
            end=[cx_right, base_y + KB_s, 0],
            color=GREY,
            stroke_width=1.5,
        )

        sect_r_title = MathTex(r"\text{Etter skade}", font_size=28).next_to(sect_r, UP, buff=0.3)
        sect_r_sublabel = MathTex(r"\text{Tverrsnitt}", font_size=24).next_to(sect_r, DOWN, buff=0.55)

        # ── equation at bottom ────────────────────────────────────────────────
        eq_text = Text("For rektangulær lekter", font_size=24).move_to([0, -2.0, 0])
        eq = MathTex(
            r"K\!B = \frac{T}{2} < K\!B_S = \frac{T_S}{2}",
            font_size=34,
        ).move_to([0, -2.5, 0])

        # ── animation ─────────────────────────────────────────────────────────
        self.add(intro_text)
        self.wait(0.8)
        self.play(FadeOut(intro_text))

        self.play(
            FadeIn(sect_l, cl_l, wl_l),
            Write(sect_l_title),
            Write(sect_l_sublabel),
            Write(cl_label_l),
            Write(wl_label_l),
        )
        self.play(FadeIn(kb_dot_l, kb_label_l, kb_arrow_l, kb_arr_label_l, kb_guide_l))

        self.play(
            FadeIn(sect_r, cl_r, wl_r),
            Write(sect_r_title),
            Write(sect_r_sublabel),
            Write(cl_label_r),
            Write(wl_label_r),
        )
        self.play(FadeIn(kb_dot_r, kb_label_r, kb_arrow_r, kb_arr_label_r, kb_guide_r))
        self.wait(1.5)

        self.play(Write(eq_text), Write(eq))
        self.wait(1.5)

