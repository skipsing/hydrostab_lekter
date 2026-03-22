from manim import *

from scenes.barge_geometry import BargeSceneBase, create_dimension_arrow


class PngSceneBase(BargeSceneBase):
    def setup_png(self):
        self.setup_barge_geometry()
        self.camera.background_color = WHITE

    @staticmethod
    def blacken(*mobs):
        for mob in mobs:
            mob.set_color(BLACK)

    @staticmethod
    def dim_arrow(start: np.ndarray, end: np.ndarray):
        arr = create_dimension_arrow(start, end)
        arr.set_color(BLACK)
        return arr


class Hoveddimensjoner_for_en_rektangulaer_lekter(PngSceneBase):
    def construct(self):
        self.setup_png()

        profile = self.create_profile_view(color=BLACK).scale(1.15).shift(UP * 1.0 + RIGHT * 1.0)
        transverse = self.create_transverse_view(color=BLACK).scale(1.15).shift(UP * 1.0 + RIGHT * 0.5)
        plan = self.create_plan_view(color=BLACK).scale(1.15).next_to(profile, DOWN, buff=1.1).align_to(profile, LEFT)

        profile_label = MathTex(r"\text{Profilsnitt}", font_size=28, color=BLACK).next_to(profile, DOWN, buff=0.45)
        transverse_label = MathTex(r"\text{Tverrsnitt}", font_size=28, color=BLACK).next_to(transverse, DOWN, buff=0.45)
        plan_label = MathTex(r"\text{Plansnitt}", font_size=28, color=BLACK).next_to(plan, DOWN, buff=0.25)

        ap_label = Tex(r"AP", font_size=16, color=BLACK).next_to(profile.get_corner(DL), DOWN + LEFT, buff=0.05)
        fp_label = Tex(r"FP", font_size=16, color=BLACK).next_to(profile.get_corner(DR), DOWN + RIGHT, buff=0.05)

        transverse_cl = DashedLine(
            start=transverse.get_top() + UP * 0.2,
            end=transverse.get_bottom() + DOWN * 0.2,
            color=BLACK,
            dashed_ratio=0.6,
        )
        transverse_cl_label = Tex(r"CL", font_size=16, color=BLACK).next_to(transverse_cl, DOWN, buff=0.05)

        plan_cl = Line(
            start=plan.get_left() + LEFT * 0.2,
            end=plan.get_right() + RIGHT * 0.2,
            color=BLACK,
            stroke_width=2,
        )
        plan_cl_label = Tex(r"CL", font_size=16, color=BLACK).next_to(plan_cl.get_right(), RIGHT, buff=0.05)

        ap_plan_label = Tex(r"AP", font_size=16, color=BLACK).next_to(plan.get_left() + DOWN * 0.2, LEFT, buff=0.05)
        fp_plan_label = Tex(r"FP", font_size=16, color=BLACK).next_to(plan.get_right() + DOWN * 0.2, RIGHT, buff=0.05)

        l_arrow = self.dim_arrow(profile.get_left() + UP * (self.depth_height / 2), profile.get_right() + UP * (self.depth_height / 2)).shift(UP * 0.3)
        l_label = Tex(r"L", font_size=34, color=BLACK).next_to(l_arrow, UP, buff=0.1)

        d_arrow = self.dim_arrow(transverse.get_bottom() + LEFT * (self.breadth_width / 2), transverse.get_top() + LEFT * (self.breadth_width / 2)).shift(LEFT * 0.3)
        d_label = Tex(r"D", font_size=34, color=BLACK).next_to(d_arrow, LEFT, buff=0.1)

        b_arrow = self.dim_arrow(plan.get_bottom() + LEFT * (plan.width / 2), plan.get_top() + LEFT * (plan.width / 2)).shift(LEFT * 0.3)
        b_label = Tex(r"B", font_size=30, color=BLACK).next_to(b_arrow, LEFT, buff=0.08)

        self.add(
            profile,
            transverse,
            plan,
            profile_label,
            transverse_label,
            plan_label,
            ap_label,
            fp_label,
            ap_plan_label,
            fp_plan_label,
            transverse_cl,
            transverse_cl_label,
            plan_cl,
            plan_cl_label,
            l_arrow,
            l_label,
            d_arrow,
            d_label,
            b_arrow,
            b_label,
        )
        self.wait(0.2)


class Volumdeplasement_for_rektangulaer_lekter(PngSceneBase):
    def construct(self):
        self.setup_png()

        profile = self.create_profile_view(color=BLACK).scale(1.2)
        transverse = self.create_transverse_view(color=BLACK).scale(1.2)

        pair = VGroup(profile, transverse).arrange(RIGHT, buff=1.5).move_to([0, 0.4, 0])

        profile_label = MathTex(r"\text{Profilsnitt}", font_size=28, color=BLACK).next_to(profile, DOWN, buff=0.45)
        transverse_label = MathTex(r"\text{Tverrsnitt}", font_size=28, color=BLACK).next_to(transverse, DOWN, buff=0.45)

        ap_label = Tex(r"AP", font_size=16, color=BLACK).next_to(profile.get_corner(DL), DOWN + LEFT, buff=0.05)
        fp_label = Tex(r"FP", font_size=16, color=BLACK).next_to(profile.get_corner(DR), DOWN + RIGHT, buff=0.05)

        wl_y = profile.get_bottom()[1] + self.water_y * 1.2
        wl_profile = Line([profile.get_left()[0] - 0.2, wl_y, 0], [profile.get_right()[0] + 0.2, wl_y, 0], color=BLACK, stroke_width=2)
        wl_profile.set_dash([0.1, 0.1])
        wl_trans = Line([transverse.get_left()[0] - 0.2, wl_y, 0], [transverse.get_right()[0] + 0.2, wl_y, 0], color=BLACK, stroke_width=2)
        wl_trans.set_dash([0.1, 0.1])

        wl_profile_label = Tex(r"WL", font_size=14, color=BLACK).next_to([profile.get_right()[0] + 0.2, wl_y, 0], RIGHT, buff=0.05)
        wl_trans_label = Tex(r"WL", font_size=14, color=BLACK).next_to([transverse.get_right()[0] + 0.2, wl_y, 0], RIGHT, buff=0.05)

        trans_cl = DashedLine(
            start=transverse.get_top() + UP * 0.2,
            end=transverse.get_bottom() + DOWN * 0.2,
            color=BLACK,
            dashed_ratio=0.6,
        )
        trans_cl_label = Tex(r"CL", font_size=16, color=BLACK).next_to(trans_cl, DOWN, buff=0.05)

        l_arrow = self.dim_arrow(profile.get_left() + UP * (profile.height / 2), profile.get_right() + UP * (profile.height / 2)).shift(UP * 0.28)
        l_label = Tex(r"L", font_size=32, color=BLACK).next_to(l_arrow, UP, buff=0.08)

        b_arrow = self.dim_arrow(transverse.get_left() + UP * (transverse.height / 2), transverse.get_right() + UP * (transverse.height / 2)).shift(UP * 0.28)
        b_label = Tex(r"B", font_size=32, color=BLACK).next_to(b_arrow, UP, buff=0.08)

        t_arrow = self.dim_arrow(
            np.array([profile.get_left()[0] - 0.35, wl_y, 0]),
            np.array([profile.get_left()[0] - 0.35, profile.get_bottom()[1], 0]),
        )
        t_label = Tex(r"T", font_size=32, color=BLACK).next_to(t_arrow, LEFT, buff=0.08)

        self.add(
            profile,
            transverse,
            profile_label,
            transverse_label,
            ap_label,
            fp_label,
            wl_profile,
            wl_trans,
            wl_profile_label,
            wl_trans_label,
            trans_cl,
            trans_cl_label,
            l_arrow,
            l_label,
            b_arrow,
            b_label,
            t_arrow,
            t_label,
        )
        self.wait(0.2)


class _CompartmentsBasePng(PngSceneBase):
    n_compartments = 3
    title_text = "Lekteren har 3 vanntette avdelinger"

    def construct(self):
        self.setup_png()
        profile = self.create_profile_view(color=BLACK).scale(1.35).move_to([0, 0.0, 0])
        left = profile.get_left()[0]
        right = profile.get_right()[0]
        spacing = (right - left) / self.n_compartments

        profile_label = MathTex(r"\text{Profilsnitt}", font_size=28, color=BLACK).next_to(profile, DOWN, buff=0.45)
        ap_label = Tex(r"AP", font_size=16, color=BLACK).next_to(profile.get_corner(DL), DOWN + LEFT, buff=0.05)
        fp_label = Tex(r"FP", font_size=16, color=BLACK).next_to(profile.get_corner(DR), DOWN + RIGHT, buff=0.05)

        dividers = VGroup()
        for i in range(1, self.n_compartments):
            x = left + i * spacing
            dividers.add(Line([x, profile.get_bottom()[1], 0], [x, profile.get_top()[1], 0], color=BLACK, stroke_width=2))

        comp_labels = VGroup()
        for i in range(self.n_compartments):
            comp_labels.add(Tex(str(i + 1), font_size=36, color=BLACK).move_to([left + (i + 0.5) * spacing, profile.get_center()[1], 0]))

        arrow_y = profile.get_top()[1] + 0.35
        comp_arrows = VGroup()
        comp_dim_labels = VGroup()
        for i in range(self.n_compartments):
            start = np.array([left + i * spacing, arrow_y, 0])
            end = np.array([left + (i + 1) * spacing, arrow_y, 0])
            arr = self.dim_arrow(start, end)
            comp_arrows.add(arr)
            comp_dim_labels.add(Tex(rf"L/{self.n_compartments}", font_size=24, color=BLACK).next_to(arr, UP, buff=0.08))

        self.add(profile, profile_label, ap_label, fp_label, dividers, comp_labels, comp_arrows, comp_dim_labels)
        self.wait(0.2)


class Lekteren_har_3_vanntette_avdelinger(_CompartmentsBasePng):
    n_compartments = 3
    title_text = "Lekteren har 3 vanntette avdelinger"


class Lekteren_har_4_vanntette_avdelinger(_CompartmentsBasePng):
    n_compartments = 4
    title_text = "Lekteren har 4 vanntette avdelinger"


class Lekteren_har_5_vanntette_avdelinger(_CompartmentsBasePng):
    n_compartments = 5
    title_text = "Lekteren har 5 vanntette avdelinger"


class Lekteren_har_6_vanntette_avdelinger(_CompartmentsBasePng):
    n_compartments = 6
    title_text = "Lekteren har 6 vanntette avdelinger"


class Flytestilling_ved_symmetrisk_skade(PngSceneBase):
    def construct(self):
        self.setup_png()

        profile = self.create_profile_view(color=BLACK).scale(1.45).move_to([1.0, -0.2, 0])
        dividers, spacing = self.create_compartment_dividers(profile, color=BLACK)

        left = profile.get_left()[0]
        right = profile.get_right()[0]
        bottom = profile.get_bottom()[1]
        wl_y = bottom + self.water_y * 1.45

        wl = Line([left - 0.2, wl_y, 0], [right + 0.2, wl_y, 0], color=BLACK, stroke_width=2)
        wl.set_dash([0.1, 0.1])
        wl_label = MathTex(r"WL_S", font_size=16, color=BLACK).next_to([right + 0.2, wl_y, 0], RIGHT, buff=0.05)

        comp_labels = VGroup()
        for i in range(3):
            comp_labels.add(Tex(str(i + 1), font_size=34, color=BLACK).move_to([left + (i + 0.5) * spacing, profile.get_center()[1], 0]))

        comp2_left = left + spacing
        comp2_right = left + 2 * spacing
        flooded = Rectangle(
            width=comp2_right - comp2_left,
            height=wl_y - bottom,
            fill_color=BLACK,
            fill_opacity=0.14,
            stroke_opacity=0,
        ).move_to([(comp2_left + comp2_right) / 2, (wl_y + bottom) / 2, 0])

        ap_label = Tex(r"AP", font_size=16, color=BLACK).next_to(profile.get_corner(DL), DOWN + LEFT, buff=0.05)
        fp_label = Tex(r"FP", font_size=16, color=BLACK).next_to(profile.get_corner(DR), DOWN + RIGHT, buff=0.05)

        t_s_arrow = self.dim_arrow(np.array([left - 0.5, wl_y, 0]), np.array([left - 0.5, bottom, 0]))
        t_s_label = MathTex(r"T_S", font_size=30, color=BLACK).next_to(t_s_arrow, LEFT, buff=0.1)

        self.add(profile, dividers, comp_labels, wl, wl_label, flooded, ap_label, fp_label, t_s_arrow, t_s_label)
        self.wait(0.2)


class Reduksjon_av_tverrskips_BM(PngSceneBase):
    def construct(self):
        self.setup_png()

        plan = self.create_plan_view(color=BLACK).scale(1.35).move_to([0.9, 0.1, 0])
        left = plan.get_left()[0]
        right = plan.get_right()[0]
        spacing = (right - left) / 3
        d1 = left + spacing
        d2 = left + 2 * spacing

        plan_label = MathTex(r"\text{Plansnitt}", font_size=28, color=BLACK).next_to(plan, DOWN, buff=0.3)
        ap_label = Tex(r"AP", font_size=16, color=BLACK).next_to(plan.get_left() + DOWN * 0.2, LEFT, buff=0.05)
        fp_label = Tex(r"FP", font_size=16, color=BLACK).next_to(plan.get_right() + DOWN * 0.2, RIGHT, buff=0.05)

        cl = Line(start=plan.get_left() + LEFT * 0.2, end=plan.get_right() + RIGHT * 0.2, color=BLACK, stroke_width=2)
        cl_label = Text("â„„", font_size=16, color=BLACK).next_to(cl.get_right(), RIGHT, buff=0.05)

        divider_1 = Line([d1, plan.get_bottom()[1], 0], [d1, plan.get_top()[1], 0], color=BLACK, stroke_width=2)
        divider_2 = Line([d2, plan.get_bottom()[1], 0], [d2, plan.get_top()[1], 0], color=BLACK, stroke_width=2)

        lost_zone = Rectangle(
            width=spacing,
            height=plan.height,
            fill_color=BLACK,
            fill_opacity=0.12,
            stroke_opacity=0,
        ).move_to([left + 1.5 * spacing, plan.get_center()[1], 0])

        lost_cross = VGroup(
            Line([d1, plan.get_top()[1], 0], [d2, plan.get_bottom()[1], 0], color=BLACK, stroke_width=3),
            Line([d2, plan.get_top()[1], 0], [d1, plan.get_bottom()[1], 0], color=BLACK, stroke_width=3),
        )

        b_arrow = self.dim_arrow(np.array([left - 0.45, plan.get_bottom()[1], 0]), np.array([left - 0.45, plan.get_top()[1], 0]))
        b_label = Tex(r"B", font_size=30, color=BLACK).next_to(b_arrow, LEFT, buff=0.08)

        l13 = self.dim_arrow(np.array([left, plan.get_top()[1] + 0.35, 0]), np.array([d1, plan.get_top()[1] + 0.35, 0]))
        l13_label = Tex(r"L/3", font_size=24, color=BLACK).next_to(l13, UP, buff=0.08)
        r13 = self.dim_arrow(np.array([d2, plan.get_top()[1] + 0.35, 0]), np.array([right, plan.get_top()[1] + 0.35, 0]))
        r13_label = Tex(r"L/3", font_size=24, color=BLACK).next_to(r13, UP, buff=0.08)

        self.add(
            plan,
            plan_label,
            ap_label,
            fp_label,
            cl,
            cl_label,
            divider_1,
            divider_2,
            lost_zone,
            lost_cross,
            b_arrow,
            b_label,
            l13,
            l13_label,
            r13,
            r13_label,
        )
        self.wait(0.2)


class Vertikal_forflytning_av_oppdriftsenteret_B(PngSceneBase):
    def construct(self):
        self.setup_png()

        sf = 1.5
        sw = self.breadth_width * sf
        sh = self.depth_height * sf
        wy = self.water_y * sf
        descent = 0.3 * sf
        t_s = wy + descent

        cx_left, cx_right = -2.6, 2.6
        base_y = -0.5

        sect_l = Rectangle(width=sw, height=sh, stroke_color=BLACK, stroke_width=3, fill_opacity=0).move_to([cx_left, base_y + sh / 2, 0])
        sect_r = Rectangle(width=sw, height=sh, stroke_color=BLACK, stroke_width=3, fill_opacity=0).move_to([cx_right, base_y + sh / 2, 0])

        wl_l = Line([sect_l.get_left()[0] - 0.2, base_y + wy, 0], [sect_l.get_right()[0] + 0.2, base_y + wy, 0], color=BLACK, stroke_width=2)
        wl_l.set_dash([0.1, 0.1])
        wl_r = Line([sect_r.get_left()[0] - 0.2, base_y + t_s, 0], [sect_r.get_right()[0] + 0.2, base_y + t_s, 0], color=BLACK, stroke_width=2)
        wl_r.set_dash([0.1, 0.1])

        wl_l_label = Tex(r"WL", font_size=14, color=BLACK).next_to([sect_l.get_right()[0] + 0.2, base_y + wy, 0], RIGHT, buff=0.05)
        wl_r_label = MathTex(r"WL_S", font_size=14, color=BLACK).next_to([sect_r.get_right()[0] + 0.2, base_y + t_s, 0], RIGHT, buff=0.05)

        cl_l = DashedLine(sect_l.get_top() + UP * 0.2, sect_l.get_bottom() + DOWN * 0.2, color=BLACK, dashed_ratio=0.6)
        cl_r = DashedLine(sect_r.get_top() + UP * 0.2, sect_r.get_bottom() + DOWN * 0.2, color=BLACK, dashed_ratio=0.6)
        cl_l_label = Tex(r"CL", font_size=14, color=BLACK).next_to(cl_l, DOWN, buff=0.05)
        cl_r_label = Tex(r"CL", font_size=14, color=BLACK).next_to(cl_r, DOWN, buff=0.05)

        b_l = Dot([cx_left, base_y + wy / 2, 0], color=BLACK, radius=0.06)
        b_r = Dot([cx_right, base_y + t_s / 2, 0], color=BLACK, radius=0.06)
        b_l_label = MathTex(r"B", font_size=26, color=BLACK).next_to(b_l, RIGHT, buff=0.1)
        b_r_label = MathTex(r"B_S", font_size=26, color=BLACK).next_to(b_r, RIGHT, buff=0.1)

        b_l_line = DashedLine(
            [sect_l.get_left()[0], base_y + wy / 2, 0],
            [cx_left, base_y + wy / 2, 0],
            color=BLACK, stroke_width=1.5, dashed_ratio=0.5,
        )
        b_r_line = DashedLine(
            [sect_r.get_left()[0], base_y + t_s / 2, 0],
            [cx_right, base_y + t_s / 2, 0],
            color=BLACK, stroke_width=1.5, dashed_ratio=0.5,
        )

        kb_l = self.dim_arrow(np.array([sect_l.get_left()[0] - 0.35, base_y, 0]), np.array([sect_l.get_left()[0] - 0.35, base_y + wy / 2, 0]))
        kb_l_label = MathTex(r"KB", font_size=24, color=BLACK).next_to(kb_l, LEFT, buff=0.08)
        kb_r = self.dim_arrow(np.array([sect_r.get_left()[0] - 0.35, base_y, 0]), np.array([sect_r.get_left()[0] - 0.35, base_y + t_s / 2, 0]))
        kb_r_label = MathTex(r"KB_S", font_size=24, color=BLACK).next_to(kb_r, LEFT, buff=0.08)

        self.add(
            sect_l,
            sect_r,
            wl_l,
            wl_r,
            wl_l_label,
            wl_r_label,
            cl_l,
            cl_r,
            cl_l_label,
            cl_r_label,
            b_l_line,
            b_r_line,
            b_l,
            b_r,
            b_l_label,
            b_r_label,
            kb_l,
            kb_l_label,
            kb_r,
            kb_r_label,
        )
        self.wait(0.2)


class Langskips_BM_og_LCF_ved_usymmetrisk_skade(PngSceneBase):
    def construct(self):
        self.setup_png()

        plan = self.create_plan_view(color=BLACK).scale(1.35).move_to([0.9, 0.1, 0])
        left = plan.get_left()[0]
        right = plan.get_right()[0]
        spacing = (right - left) / 3
        d1 = left + spacing
        d2 = left + 2 * spacing

        ap_label = Tex(r"AP", font_size=16, color=BLACK).next_to(plan.get_left() + DOWN * 0.2, LEFT, buff=0.05)
        fp_label = Tex(r"FP", font_size=16, color=BLACK).next_to(plan.get_right() + DOWN * 0.2, RIGHT, buff=0.05)
        plan_label = MathTex(r"\text{Plansnitt}", font_size=28, color=BLACK).next_to(plan, DOWN, buff=0.3)

        divider_1 = Line([d1, plan.get_bottom()[1], 0], [d1, plan.get_top()[1], 0], color=BLACK, stroke_width=2)
        divider_2 = Line([d2, plan.get_bottom()[1], 0], [d2, plan.get_top()[1], 0], color=BLACK, stroke_width=2)

        cl = Line(start=plan.get_left() + LEFT * 0.2, end=plan.get_right() + RIGHT * 0.2, color=BLACK, stroke_width=2)
        cl_label = Tex(r"CL", font_size=16, color=BLACK).next_to(cl.get_right(), RIGHT, buff=0.05)

        lost_zone = Rectangle(width=spacing, height=plan.height, fill_color=BLACK, fill_opacity=0.12, stroke_opacity=0).move_to([left + 2.5 * spacing, plan.get_center()[1], 0])
        lost_cross = VGroup(
            Line([d2, plan.get_top()[1], 0], [right, plan.get_bottom()[1], 0], color=BLACK, stroke_width=3),
            Line([right, plan.get_top()[1], 0], [d2, plan.get_bottom()[1], 0], color=BLACK, stroke_width=3),
        )

        lcf_s_x = left + spacing
        lcf_axis = DashedLine([lcf_s_x, plan.get_bottom()[1] - 0.2, 0], [lcf_s_x, plan.get_top()[1] + 0.2, 0], color=BLACK, dashed_ratio=0.6)
        lcf_dim = self.dim_arrow(np.array([left, plan.get_center()[1], 0]), np.array([lcf_s_x, plan.get_center()[1], 0]))
        lcf_label = MathTex(r"LCF_S = L/3", font_size=24, color=BLACK).next_to(lcf_dim, UP, buff=0.08)

        l13 = self.dim_arrow(np.array([left, plan.get_top()[1] + 0.35, 0]), np.array([d1, plan.get_top()[1] + 0.35, 0]))
        l13_label = Tex(r"L/3", font_size=24, color=BLACK).next_to(l13, UP, buff=0.08)
        m13 = self.dim_arrow(np.array([d1, plan.get_top()[1] + 0.35, 0]), np.array([d2, plan.get_top()[1] + 0.35, 0]))
        m13_label = Tex(r"L/3", font_size=24, color=BLACK).next_to(m13, UP, buff=0.08)

        b_arrow = self.dim_arrow(np.array([left - 0.45, plan.get_bottom()[1], 0]), np.array([left - 0.45, plan.get_top()[1], 0]))
        b_label = Tex(r"B", font_size=30, color=BLACK).next_to(b_arrow, LEFT, buff=0.08)

        self.add(
            plan,
            plan_label,
            ap_label,
            fp_label,
            cl,
            cl_label,
            divider_1,
            divider_2,
            lost_zone,
            lost_cross,
            lcf_axis,
            lcf_dim,
            lcf_label,
            l13,
            l13_label,
            m13,
            m13_label,
            b_arrow,
            b_label,
        )
        self.wait(0.2)


class Trimoppsett(PngSceneBase):
    def construct(self):
        self.setup_png()

        profile = self.create_profile_view(color=BLACK).scale(1.45).move_to([1.0, -0.15, 0])
        dividers, spacing = self.create_compartment_dividers(profile, color=BLACK)

        left = profile.get_left()[0]
        right = profile.get_right()[0]
        bottom = profile.get_bottom()[1]
        top = profile.get_top()[1]
        wl_y = bottom + self.water_y * 1.45

        ap_label = Tex(r"AP", font_size=16, color=BLACK).next_to(profile.get_corner(DL), DOWN + LEFT, buff=0.05)
        fp_label = Tex(r"FP", font_size=16, color=BLACK).next_to(profile.get_corner(DR), DOWN + RIGHT, buff=0.05)

        wl = Line([left - 0.2, wl_y, 0], [right + 0.2, wl_y, 0], color=BLACK, stroke_width=2)
        wl.set_dash([0.1, 0.1])
        wl_label = MathTex(r"WL_S", font_size=14, color=BLACK).next_to([right + 0.2, wl_y, 0], RIGHT, buff=0.05)

        comp3_left = left + 2 * spacing
        flooded_3 = Rectangle(
            width=spacing,
            height=wl_y - bottom,
            fill_color=BLACK,
            fill_opacity=0.14,
            stroke_opacity=0,
        ).move_to([(comp3_left + right) / 2, (wl_y + bottom) / 2, 0])

        g_x = left + 1.5 * spacing
        g_y = top - 0.25 * (top - bottom)
        b_x = left + spacing
        b_y = bottom + (wl_y - bottom) / 2

        g_dot = Dot([g_x, g_y, 0], color=BLACK, radius=0.07)
        b_dot = Dot([b_x, b_y, 0], color=BLACK, radius=0.07)
        g_label = MathTex(r"G", font_size=28, color=BLACK).next_to(g_dot, RIGHT, buff=0.1)
        b_label = MathTex(r"B_S", font_size=28, color=BLACK).next_to(b_dot, LEFT, buff=0.1)

        g_arrow = Arrow([g_x, g_y + 0.45, 0], [g_x, g_y, 0], color=BLACK, stroke_width=4, buff=0, tip_length=0.2)
        b_arrow = Arrow([b_x, b_y - 0.45, 0], [b_x, b_y, 0], color=BLACK, stroke_width=4, buff=0, tip_length=0.2)

        lcg = self.dim_arrow(np.array([left, top + 0.45, 0]), np.array([g_x, top + 0.45, 0]))
        lcg_label = MathTex(r"LCG", font_size=24, color=BLACK).next_to(lcg, UP, buff=0.1)

        lcb = self.dim_arrow(np.array([left, bottom - 0.45, 0]), np.array([b_x, bottom - 0.45, 0]))
        lcb_label = MathTex(r"LCB_S", font_size=24, color=BLACK).next_to(lcb, DOWN, buff=0.1)

        l_k_y = (g_y + b_y) / 2
        l_k_line = Line([b_x, l_k_y, 0], [g_x, l_k_y, 0], color=BLACK, stroke_width=2)
        l_k_label = MathTex(r"\ell_k", font_size=28, color=BLACK).next_to(l_k_line, DOWN, buff=0.08)

        self.add(profile, dividers, ap_label, fp_label, wl, wl_label, flooded_3, g_dot, b_dot, g_label, b_label, g_arrow, b_arrow, lcg, lcg_label, lcb, lcb_label, l_k_line, l_k_label)
        self.wait(0.2)


class Fordeling_av_trim(PngSceneBase):
    def construct(self):
        self.setup_png()

        profile = self.create_profile_view(color=BLACK)
        profile.shift(UP * 1.0)
        dividers, spacing = self.create_compartment_dividers(profile, color=BLACK)

        left_x = profile.get_left()[0]
        right_x = profile.get_right()[0]
        bottom_y = profile.get_bottom()[1]
        top_y = profile.get_top()[1]
        wl_y = bottom_y + self.water_y

        ap_label = Tex(r"AP", font_size=14, color=BLACK).next_to(profile.get_corner(DL), DOWN + LEFT, buff=0.05)
        fp_label = Tex(r"FP", font_size=14, color=BLACK).next_to(profile.get_corner(DR), DOWN + RIGHT, buff=0.05)

        wl = Line(
            start=[left_x - 0.2, wl_y, 0],
            end=[right_x + 0.2, wl_y, 0],
            color=BLACK,
            stroke_width=2,
        )
        wl.set_dash([0.1, 0.1])
        wl_label = MathTex(r"WL_S", font_size=14, color=BLACK).next_to([right_x + 0.2, wl_y, 0], RIGHT, buff=0.05).shift(UP * 0.17)

        descent = 0.2
        rot_angle = -5 * DEGREES
        comp2_center_x = left_x + 1.5 * spacing
        rot_about = np.array([comp2_center_x, wl_y, 0.0])

        profile_group = VGroup(profile, dividers, ap_label, fp_label)
        profile_group.shift(DOWN * descent)
        profile_group.rotate(rot_angle, about_point=rot_about)

        def rotate_point(point, angle, about):
            c = np.cos(angle)
            s = np.sin(angle)
            p = np.array(point) - about
            r = np.array([c * p[0] - s * p[1], s * p[0] + c * p[1], 0.0])
            return r + about

        def x_at_horizontal_y(p_bottom, p_top, y_target):
            t = (y_target - p_bottom[1]) / (p_top[1] - p_bottom[1])
            return p_bottom[0] + t * (p_top[0] - p_bottom[0])

        def intersect_lines(p1, d1, p2, d2):
            a = np.array([[d1[0], -d2[0]], [d1[1], -d2[1]]], dtype=float)
            b = np.array([p2[0] - p1[0], p2[1] - p1[1]], dtype=float)
            t, _ = np.linalg.solve(a, b)
            return p1 + t * d1

        hull_left_bottom = np.array([left_x, bottom_y - descent, 0.0])
        hull_left_top = np.array([left_x, top_y - descent, 0.0])
        hull_right_bottom = np.array([right_x, bottom_y - descent, 0.0])
        hull_right_top = np.array([right_x, top_y - descent, 0.0])

        hull_left_bottom_r = rotate_point(hull_left_bottom, rot_angle, rot_about)
        hull_left_top_r = rotate_point(hull_left_top, rot_angle, rot_about)
        hull_right_bottom_r = rotate_point(hull_right_bottom, rot_angle, rot_about)
        hull_right_top_r = rotate_point(hull_right_top, rot_angle, rot_about)

        comp3_left = left_x + 2 * spacing
        comp3_right = right_x
        left_bottom = np.array([comp3_left, bottom_y - descent, 0.0])
        left_top = np.array([comp3_left, top_y - descent, 0.0])
        right_bottom = np.array([comp3_right, bottom_y - descent, 0.0])
        right_top = np.array([comp3_right, top_y - descent, 0.0])

        left_bottom_r = rotate_point(left_bottom, rot_angle, rot_about)
        left_top_r = rotate_point(left_top, rot_angle, rot_about)
        right_bottom_r = rotate_point(right_bottom, rot_angle, rot_about)
        right_top_r = rotate_point(right_top, rot_angle, rot_about)

        left_wl_x = x_at_horizontal_y(left_bottom_r, left_top_r, wl_y)
        right_wl_x = x_at_horizontal_y(right_bottom_r, right_top_r, wl_y)
        water_fill_rot = Polygon(
            np.array([left_wl_x, wl_y, 0.0]),
            np.array([right_wl_x, wl_y, 0.0]),
            right_bottom_r,
            left_bottom_r,
            fill_color=BLACK,
            fill_opacity=0.14,
            stroke_opacity=0,
        )

        g_y = top_y - (top_y - bottom_y) * 0.25
        g_sink_pt = np.array([comp2_center_x, g_y - descent, 0.0])
        g_rot_pt = rotate_point(g_sink_pt, rot_angle, rot_about)

        x_b = left_x + 0.5 * (right_x - left_x)
        b_y = bottom_y + self.water_y / 2
        b_pt = np.array([x_b, b_y, 0.0])

        g_dot = Dot(g_rot_pt, color=BLACK, radius=0.08)
        b_dot = Dot(b_pt, color=BLACK, radius=0.08)
        g_label = MathTex(r"G", font_size=28, color=BLACK).next_to(g_dot, LEFT, buff=0.1)
        b_label = MathTex(r"B_S", font_size=28, color=BLACK).next_to(b_dot, LEFT, buff=0.1)

        g_arrow = Arrow(
            start=[g_rot_pt[0], g_rot_pt[1] + 0.45, 0],
            end=[g_rot_pt[0], g_rot_pt[1], 0],
            color=BLACK,
            stroke_width=4,
            buff=0,
            tip_length=0.28,
        )
        b_arrow = Arrow(
            start=[x_b, b_y - 0.45, 0],
            end=[x_b, b_y, 0],
            color=BLACK,
            stroke_width=4,
            buff=0,
            tip_length=0.28,
        )

        long_vec = hull_right_bottom_r - hull_left_bottom_r
        long_unit = long_vec / np.linalg.norm(long_vec)
        normal_unit = np.array([-long_unit[1], long_unit[0], 0.0])

        right_hull_wl_x = x_at_horizontal_y(hull_right_bottom_r, hull_right_top_r, wl_y)
        upper_right_pt = np.array([right_hull_wl_x, wl_y, 0.0])
        left_hull_wl_x = x_at_horizontal_y(hull_left_bottom_r, hull_left_top_r, wl_y)
        lower_level_pt = np.array([left_hull_wl_x, wl_y, 0.0])

        aft_side_p = hull_right_bottom_r
        aft_side_d = hull_right_top_r - hull_right_bottom_r
        left_side_p = hull_left_bottom_r
        left_side_d = hull_left_top_r - hull_left_bottom_r

        lower_right_hull = intersect_lines(lower_level_pt, long_unit, aft_side_p, aft_side_d)

        divider12_bottom = np.array([left_x + spacing, bottom_y - descent, 0.0])
        divider12_top = np.array([left_x + spacing, top_y - descent, 0.0])
        divider12_bottom_r = rotate_point(divider12_bottom, rot_angle, rot_about)
        divider12_top_r = rotate_point(divider12_top, rot_angle, rot_about)
        divider12_wl_x = x_at_horizontal_y(divider12_bottom_r, divider12_top_r, wl_y)
        middle_anchor_pt = np.array([divider12_wl_x, wl_y, 0.0])
        middle_left_hull = intersect_lines(middle_anchor_pt, -long_unit, left_side_p, left_side_d)
        middle_right_hull = intersect_lines(middle_anchor_pt, long_unit, aft_side_p, aft_side_d)

        extension = 0.6
        upper_right_ext = upper_right_pt + long_unit * extension
        lower_right_ext = lower_right_hull + long_unit * extension
        middle_right_ext = middle_right_hull + long_unit * extension
        lower_left_ext = lower_level_pt - long_unit * extension

        fore_trim_line = DashedLine(
            start=upper_right_pt,
            end=upper_right_ext,
            color=BLACK,
            stroke_width=2,
            dashed_ratio=0.6,
        )
        middle_trim_line = DashedLine(
            start=middle_left_hull - long_unit * 0.72,
            end=middle_right_hull + long_unit * 0.72,
            color=BLACK,
            stroke_width=2,
            dashed_ratio=0.6,
        )
        aft_distribution_line = DashedLine(
            start=lower_left_ext,
            end=lower_level_pt,
            color=BLACK,
            stroke_width=2,
            dashed_ratio=0.6,
        )

        t_f = np.dot(upper_right_pt - middle_right_hull, normal_unit)
        t_f_base = middle_right_hull + long_unit * 0.06
        t_f_dim_arrow = self.dim_arrow(t_f_base, t_f_base + normal_unit * t_f)
        t_f_dim_label = MathTex(r"t_f", font_size=28, color=BLACK).move_to(t_f_dim_arrow.get_center() + long_unit * 0.10)

        t_a = np.dot(middle_left_hull - lower_level_pt, normal_unit)
        t_a_base = lower_level_pt - long_unit * 0.06
        t_a_dim_arrow = self.dim_arrow(t_a_base, t_a_base + normal_unit * t_a)
        t_a_dim_label = MathTex(r"t_a", font_size=28, color=BLACK).move_to(t_a_dim_arrow.get_center() - normal_unit * 0.14 - long_unit * 0.08)

        lcf_s_dim_y = max(hull_left_top_r[1], hull_right_top_r[1]) + 0.45
        lcf_s_profile_arrow = self.dim_arrow(
            np.array([hull_left_bottom_r[0], lcf_s_dim_y, 0.0]),
            np.array([divider12_wl_x, lcf_s_dim_y, 0.0]),
        )
        lcf_s_profile_label = MathTex(r"LCF_S", font_size=26, color=BLACK).next_to(lcf_s_profile_arrow, UP, buff=0.1)

        self.add(
            profile_group,
            wl,
            wl_label,
            water_fill_rot,
            g_dot,
            b_dot,
            g_label,
            b_label,
            g_arrow,
            b_arrow,
            fore_trim_line,
            middle_trim_line,
            aft_distribution_line,
            t_f_dim_arrow,
            t_f_dim_label,
            t_a_dim_arrow,
            t_a_dim_label,
            lcf_s_profile_arrow,
            lcf_s_profile_label,
        )
        self.wait(0.2)


if __name__ == "__main__":
    print("Run with, for example:")
    print("  manim -s barge_png_export_scenes.py Hoveddimensjoner_for_en_rektangulaer_lekter")
    print("  manim -s barge_png_export_scenes.py Fordeling_av_trim")

