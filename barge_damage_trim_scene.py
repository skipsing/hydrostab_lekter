from manim import *

from barge_geometry import BargeSceneBase, create_dimension_arrow


class BargeDamageTrimScene(BargeSceneBase):
    """Shows trim response to damage in compartment 3 and longitudinal hydrostatics."""

    def construct(self):
        self.setup_barge_geometry()

        # ─────────────────────────────────────────────────────────────────────
        # PROFILE VIEW - shows GG (center of gravity) and BB (buoyancy) before
        # ─────────────────────────────────────────────────────────────────────
        profile = self.create_profile_view(color=GREEN)
        profile.shift(UP * 1.0)

        profile_label = MathTex(r"\text{Profilsnitt}", font_size=28).next_to(profile, DOWN, buff=0.45)
        ap_label = Tex(r"AP", font_size=14).next_to(profile.get_corner(DL), DOWN + LEFT, buff=0.05)
        fp_label = Tex(r"FP", font_size=14).next_to(profile.get_corner(DR), DOWN + RIGHT, buff=0.05)

        dividers, spacing = self.create_compartment_dividers(profile)

        left_x = profile.get_left()[0]
        right_x = profile.get_right()[0]
        bottom_y = profile.get_bottom()[1]
        top_y = profile.get_top()[1]

        comp_labels = VGroup()
        for index in range(3):
            label = Tex(str(index + 1), font_size=36)
            label.move_to([left_x + (index + 0.5) * spacing, profile.get_center()[1], 0])
            comp_labels.add(label)

        wl_y = bottom_y + self.water_y

        # Waterline before damage
        wl_0 = Line(
            start=[left_x - 0.2, wl_y, 0],
            end=[right_x + 0.2, wl_y, 0],
            color=BLUE,
            stroke_width=2,
        )
        wl_0.set_dash([0.1, 0.1])
        wl_0_label = Tex(r"WL", font_size=14).next_to([right_x + 0.2, wl_y, 0], RIGHT, buff=0.05)
        wl_s_label = MathTex(r"WL_S", font_size=14).next_to([right_x + 0.2, wl_y, 0], RIGHT, buff=0.05).shift(UP * 0.17)

        # G: center of gravity at midship of compartment 2 (center point vertically in top 1/3)
        comp2_left = left_x + spacing
        comp2_right = left_x + 2 * spacing
        comp2_center_x = (comp2_left + comp2_right) / 2
        g_y = top_y - (top_y - bottom_y) * 0.25  # upper 1/4 of profile
        
        g_dot = Dot([comp2_center_x, g_y, 0], color=ORANGE, radius=0.08)
        g_label = MathTex(r"G", font_size=28, color=WHITE).next_to(g_dot, LEFT, buff=0.1)

        # B: buoyancy center at centerline, at T/2 below waterline
        x_b = left_x + 0.5 * (right_x - left_x)
        b_y = bottom_y + self.water_y / 2
        
        b_dot = Dot([x_b, b_y, 0], color=YELLOW, radius=0.08)
        b_label = MathTex(r"B", font_size=28, color=WHITE).next_to(b_dot, LEFT, buff=0.1)

        # LCB dimension: from AP down to B level, then horizontal distance to B
        lcb_arrow = create_dimension_arrow(
            np.array([left_x, bottom_y + 0.1, 0]),
            np.array([x_b, bottom_y + 0.1, 0]),
        )
        lcb_arrow.shift(DOWN * 0.35)
        lcb_label = MathTex(r"LCB", font_size=28).next_to(lcb_arrow, DOWN, buff=0.12)

        # LCG dimension: from top-left corner to G
        lcg_arrow = create_dimension_arrow(
            np.array([left_x, top_y + 0.1, 0]),
            np.array([comp2_center_x, top_y + 0.1, 0]),
        )
        lcg_arrow.shift(UP * 0.35)
        lcg_label = MathTex(r"LCG", font_size=28).next_to(lcg_arrow, UP, buff=0.12)

        # GG arrow pointing down to G
        g_arrow = Arrow(
            start=[comp2_center_x, g_y + 0.45, 0],
            end=[comp2_center_x, g_y, 0],
            color=ORANGE,
            stroke_width=4,
            buff=0,
            tip_length=0.28,
        )

        # BB arrow pointing up to B
        b_arrow = Arrow(
            start=[x_b, b_y - 0.45, 0],
            end=[x_b, b_y, 0],
            color=YELLOW,
            stroke_width=4,
            buff=0,
            tip_length=0.28,
        )

        # Horizontal distance between G and B: l_k (trimming lever)
        l_k_y = (g_y + b_y) / 2
        l_k_line = Line(
            start=[comp2_center_x, l_k_y, 0],
            end=[x_b, l_k_y, 0],
            color=WHITE,
            stroke_width=2,
        )
        l_k_label = MathTex(r"\ell_k", font_size=28, color=WHITE).next_to(l_k_line, DOWN, buff=0.1)

        # Damage in compartment 3
        comp3_left = left_x + 2 * spacing
        comp3_right = right_x
        comp3_center_x = (comp3_left + comp3_right) / 2

        damage_triangle = Polygon(
            [comp3_center_x, bottom_y, 0],
            [comp3_center_x - 0.18, bottom_y + 0.35, 0],
            [comp3_center_x + 0.18, bottom_y + 0.35, 0],
            color=RED,
            fill_opacity=0.8,
        )

        # Water filling in compartment 3 (polygon form gives cleaner transforms)
        water_fill = Polygon(
            np.array([comp3_left, wl_y, 0.0]),
            np.array([comp3_right, wl_y, 0.0]),
            np.array([comp3_right, bottom_y, 0.0]),
            np.array([comp3_left, bottom_y, 0.0]),
            fill_color=BLUE,
            fill_opacity=0.5,
            stroke_opacity=0,
        )

        # Parallel sinking amount (waterline remains fixed in global frame)
        descent = 0.2

        # End drafts after parallel sinking (equal fore/aft)
        wl_a_y = wl_y
        wl_f_y = wl_y

        # B_S: new buoyancy after damage (moves aft to divider between compartments 1 and 2)
        x_b_s = left_x + spacing
        b_s_y = b_y - 0.5 * descent
        
        b_s_dot = Dot([x_b_s, b_s_y, 0], color=YELLOW, radius=0.08)
        b_s_label = MathTex(r"B_S", font_size=28, color=WHITE).next_to(b_s_dot, LEFT, buff=0.1)
        b_s_arrow = Arrow(
            start=[x_b_s, b_s_y - 0.45, 0],
            end=[x_b_s, b_s_y, 0],
            color=YELLOW,
            stroke_width=4,
            buff=0,
            tip_length=0.28,
        )
        g_s_y = g_y - descent
        l_k_s_y = (g_s_y + b_s_y) / 2
        l_k_s_line = Line(
            start=[x_b_s, l_k_s_y, 0],
            end=[comp2_center_x, l_k_s_y, 0],
            color=WHITE,
            stroke_width=2,
        )
        l_k_s_label = MathTex(r"\ell_k", font_size=28, color=WHITE).next_to(l_k_s_line, DOWN, buff=0.1)

        # Flooded-water shapes for sinking and rotation; tops stay on fixed WL_S.
        rot_angle = -5 * DEGREES
        rot_about = np.array([comp2_center_x, wl_y, 0.0])

        water_fill_sink = Polygon(
            np.array([comp3_left, wl_y, 0.0]),
            np.array([comp3_right, wl_y, 0.0]),
            np.array([comp3_right, bottom_y - descent, 0.0]),
            np.array([comp3_left, bottom_y - descent, 0.0]),
            fill_color=BLUE,
            fill_opacity=0.5,
            stroke_opacity=0,
        )

        def rotate_point(point, angle, about):
            c = np.cos(angle)
            s = np.sin(angle)
            p = np.array(point) - about
            r = np.array([c * p[0] - s * p[1], s * p[0] + c * p[1], 0.0])
            return r + about

        def x_at_horizontal_y(p_bottom, p_top, y_target):
            t = (y_target - p_bottom[1]) / (p_top[1] - p_bottom[1])
            return p_bottom[0] + t * (p_top[0] - p_bottom[0])

        left_bottom = np.array([comp3_left, bottom_y - descent, 0.0])
        left_top = np.array([comp3_left, top_y - descent, 0.0])
        right_bottom = np.array([comp3_right, bottom_y - descent, 0.0])
        right_top = np.array([comp3_right, top_y - descent, 0.0])

        # Full barge side points after sinking (used for trim references)
        hull_left_bottom = np.array([left_x, bottom_y - descent, 0.0])
        hull_left_top = np.array([left_x, top_y - descent, 0.0])
        hull_right_bottom = np.array([right_x, bottom_y - descent, 0.0])
        hull_right_top = np.array([right_x, top_y - descent, 0.0])

        left_bottom_r = rotate_point(left_bottom, rot_angle, rot_about)
        left_top_r = rotate_point(left_top, rot_angle, rot_about)
        right_bottom_r = rotate_point(right_bottom, rot_angle, rot_about)
        right_top_r = rotate_point(right_top, rot_angle, rot_about)

        hull_left_bottom_r = rotate_point(hull_left_bottom, rot_angle, rot_about)
        hull_left_top_r = rotate_point(hull_left_top, rot_angle, rot_about)
        hull_right_bottom_r = rotate_point(hull_right_bottom, rot_angle, rot_about)
        hull_right_top_r = rotate_point(hull_right_top, rot_angle, rot_about)

        left_wl_x = x_at_horizontal_y(left_bottom_r, left_top_r, wl_y)
        right_wl_x = x_at_horizontal_y(right_bottom_r, right_top_r, wl_y)

        water_fill_rot = Polygon(
            np.array([left_wl_x, wl_y, 0.0]),
            np.array([right_wl_x, wl_y, 0.0]),
            right_bottom_r,
            left_bottom_r,
            fill_color=BLUE,
            fill_opacity=0.5,
            stroke_opacity=0,
        )

        g_sink_pt = np.array([comp2_center_x, g_s_y, 0.0])
        g_rot_pt = rotate_point(g_sink_pt, rot_angle, rot_about)
        g_arrow_rot = Arrow(
            start=[g_rot_pt[0], g_rot_pt[1] + 0.45, 0],
            end=[g_rot_pt[0], g_rot_pt[1], 0],
            color=ORANGE,
            stroke_width=4,
            buff=0,
            tip_length=0.28,
        )

        # During rotation, move B_S back toward initial B location.
        b_back_dot = Dot([x_b, b_y, 0], color=YELLOW, radius=0.08)
        b_back_label = MathTex(r"B_S", font_size=28, color=WHITE).next_to(b_back_dot, LEFT, buff=0.1)
        b_back_arrow = Arrow(
            start=[x_b, b_y - 0.45, 0],
            end=[x_b, b_y, 0],
            color=YELLOW,
            stroke_width=4,
            buff=0,
            tip_length=0.28,
        )
        l_k_back_y = (g_s_y + b_y) / 2
        l_k_back_line = Line(
            start=[x_b, l_k_back_y, 0],
            end=[comp2_center_x, l_k_back_y, 0],
            color=WHITE,
            stroke_width=2,
        )
        l_k_back_label = MathTex(r"\ell_k", font_size=28, color=WHITE).next_to(l_k_back_line, DOWN, buff=0.1)

        # Trim-reference construction in rotated state:
        # two dashed lines parallel to rotated longitudinal axis, each ending at aft side.
        long_vec = right_bottom_r - left_bottom_r
        long_unit = long_vec / np.linalg.norm(long_vec)
        normal_unit = np.array([-long_unit[1], long_unit[0], 0.0])

        def intersect_lines(p1, d1, p2, d2):
            """2D intersection of two infinite lines p1+t*d1 and p2+s*d2."""
            a = np.array([[d1[0], -d2[0]], [d1[1], -d2[1]]], dtype=float)
            b = np.array([p2[0] - p1[0], p2[1] - p1[1]], dtype=float)
            t, _ = np.linalg.solve(a, b)
            return p1 + t * d1

        # Upper line anchor at right-side WL intersection on full hull.
        right_hull_wl_x = x_at_horizontal_y(hull_right_bottom_r, hull_right_top_r, wl_y)
        upper_right_pt = np.array([right_hull_wl_x, wl_y, 0.0])

        # Lower line anchor: WL intersection on full left hull side.
        left_hull_wl_x = x_at_horizontal_y(hull_left_bottom_r, hull_left_top_r, wl_y)
        lower_level_pt = np.array([left_hull_wl_x, wl_y, 0.0])

        aft_side_p = hull_right_bottom_r
        aft_side_d = hull_right_top_r - hull_right_bottom_r

        left_side_p = hull_left_bottom_r
        left_side_d = hull_left_top_r - hull_left_bottom_r

        upper_left_hull = intersect_lines(upper_right_pt, -long_unit, left_side_p, left_side_d)
        lower_right_hull = intersect_lines(lower_level_pt, long_unit, aft_side_p, aft_side_d)

        divider12_bottom = np.array([left_x + spacing, bottom_y - descent, 0.0])
        divider12_top = np.array([left_x + spacing, top_y - descent, 0.0])
        divider12_bottom_r = rotate_point(divider12_bottom, rot_angle, rot_about)
        divider12_top_r = rotate_point(divider12_top, rot_angle, rot_about)
        divider12_wl_x = x_at_horizontal_y(divider12_bottom_r, divider12_top_r, wl_y)
        middle_anchor_pt = np.array([divider12_wl_x, wl_y, 0.0])
        middle_left_hull = intersect_lines(middle_anchor_pt, -long_unit, left_side_p, left_side_d)
        middle_right_hull = intersect_lines(middle_anchor_pt, long_unit, aft_side_p, aft_side_d)

        # Extend both reference lines beyond the aft side.
        extension = 0.6
        upper_right_ext = upper_right_pt + long_unit * extension
        lower_right_ext = lower_right_hull + long_unit * extension
        middle_right_ext = middle_right_hull + long_unit * extension
        lower_left_ext = lower_level_pt - long_unit * extension

        fore_trim_line = DashedLine(
            start=upper_right_pt,
            end=upper_right_ext,
            color=WHITE,
            stroke_width=2,
            dashed_ratio=0.6,
        )

        aft_trim_line = DashedLine(
            start=lower_level_pt,
            end=lower_right_ext,
            color=WHITE,
            stroke_width=2,
            dashed_ratio=0.6,
        )

        t_signed = np.dot(upper_right_ext - lower_right_ext, normal_unit)
        t_base = lower_right_ext + long_unit * 0.12
        t_dim_arrow = create_dimension_arrow(t_base, t_base + normal_unit * t_signed)
        t_dim_label = MathTex(r"t", font_size=28, color=WHITE).next_to(t_dim_arrow, RIGHT, buff=0.08)

        t_f_signed = np.dot(upper_right_ext - middle_right_ext, normal_unit)
        t_f_base = middle_right_ext + long_unit * 0.12
        t_f_dim_arrow = create_dimension_arrow(t_f_base, t_f_base + normal_unit * t_f_signed)
        t_f_dim_label = MathTex(r"t_f", font_size=28, color=WHITE).next_to(t_f_dim_arrow, RIGHT, buff=0.08)

        t_a_signed = np.dot(middle_left_hull - lower_left_ext, normal_unit)
        t_a_base = lower_left_ext - long_unit * 0.12
        t_a_dim_arrow = create_dimension_arrow(t_a_base, t_a_base + normal_unit * t_a_signed)
        t_a_dim_label = MathTex(r"t_a", font_size=28, color=WHITE).next_to(t_a_dim_arrow, LEFT, buff=0.08)

        lcf_s_dim_y = max(hull_left_top_r[1], hull_right_top_r[1]) + 0.45
        lcf_s_profile_arrow = create_dimension_arrow(
            np.array([hull_left_bottom_r[0], lcf_s_dim_y, 0.0]),
            np.array([divider12_wl_x, lcf_s_dim_y, 0.0]),
        )
        lcf_s_profile_label = MathTex(r"LCF_S", font_size=26, color=WHITE).next_to(lcf_s_profile_arrow, UP, buff=0.1)

        middle_trim_line = DashedLine(
            start=middle_left_hull - long_unit * 0.72,
            end=middle_right_hull + long_unit * 0.72,
            color=WHITE,
            stroke_width=2,
            dashed_ratio=0.6,
        )
        aft_distribution_line = DashedLine(
            start=lower_left_ext,
            end=lower_level_pt,
            color=WHITE,
            stroke_width=2,
            dashed_ratio=0.6,
        )

        # T_S dimension
        t_s_arrow = create_dimension_arrow(
            np.array([left_x - 0.55, wl_y, 0]),
            np.array([left_x - 0.55, bottom_y - descent, 0]),
        )
        t_s_label = MathTex(r"T_S", font_size=28).next_to(t_s_arrow, LEFT, buff=0.12)

        # Trim moment equations (right side)
        eq_cx = 3.5
        eq_top = 2.3

        def cx(mob):
            mob.set_x(eq_cx)
            return mob

        txt_trim = cx(Text("Trimmende moment", font_size=22).move_to([eq_cx, eq_top, 0]))
        eq_tm = cx(MathTex(r"M_T = \nabla \cdot \rho \cdot \ell_k", font_size=32).next_to(txt_trim, DOWN, buff=0.15))

        txt_total_trim = cx(Text("Den totale trimmen ved skade", font_size=22).next_to(eq_tm, DOWN, buff=0.45))
        eq_total_trim = cx(MathTex(r"t = \frac{M_T}{MCT_{1cm_S}}", font_size=32).next_to(txt_total_trim, DOWN, buff=0.15))
        profile_rotation_group = VGroup(
            profile,
            dividers,
            ap_label,
            fp_label,
            g_dot,
            g_label,
            l_k_line,
            l_k_label,
        )
        final_profile_group = VGroup(
            profile,
            dividers,
            ap_label,
            fp_label,
        )

        intro_text = Text("Etablere ny flytestilling ved usymmetrisk skade", font_size=36).move_to(ORIGIN)
        title = Text("Fordeling av trim", font_size=28, color=WHITE).to_edge(UP, buff=0.3)

        # ─────────────────────────────────────────────────────────────────────
        # PLAN VIEW - shows LCF and damage in compartment 3
        # ─────────────────────────────────────────────────────────────────────
        plan = self.create_plan_view(color=GREEN)
        plan.next_to(profile, DOWN, buff=1.3).align_to(profile, LEFT)

        plan_label = MathTex(r"\text{Plansnitt}", font_size=28).next_to(plan, DOWN, buff=0.62)
        ap_plan_label = Tex(r"AP", font_size=14).next_to(plan.get_left() + DOWN * 0.2, LEFT, buff=0.05)
        fp_plan_label = Tex(r"FP", font_size=14).next_to(plan.get_right() + DOWN * 0.2, RIGHT, buff=0.05)

        plan_left_x = plan.get_left()[0]
        plan_right_x = plan.get_right()[0]
        plan_top_y = plan.get_top()[1]
        plan_bottom_y = plan.get_bottom()[1]
        plan_center_x = plan.get_center()[0]

        # Centerline in plan view
        plan_cl = Line(
            start=[plan.get_left()[0] - 0.2, plan.get_center()[1], 0],
            end=[plan.get_right()[0] + 0.2, plan.get_center()[1], 0],
            color=GREY,
            stroke_width=2,
        )
        plan_cl_label = Text("\U00002104", font_size=14).next_to(plan_cl.get_right(), RIGHT, buff=0.05)

        # Compartment dividers in plan view
        plan_spacing = (plan_right_x - plan_left_x) / 3
        plan_dividers = VGroup()
        for i in range(1, 3):
            divider_x = plan_left_x + i * plan_spacing
            divider = Line(
                start=[divider_x, plan_bottom_y, 0],
                end=[divider_x, plan_top_y, 0],
                color=GREY,
                stroke_width=2,
            )
            plan_dividers.add(divider)

        plan_comp_labels = VGroup()
        for index in range(3):
            label = Tex(str(index + 1), font_size=32)
            label.move_to([plan_left_x + (index + 0.5) * plan_spacing, plan.get_center()[1], 0])
            plan_comp_labels.add(label)

        # LCF before damage (vertical axis at midship)
        lcf_axis = DashedLine(
            start=[plan_center_x, plan_bottom_y - 0.2, 0],
            end=[plan_center_x, plan_top_y + 0.2, 0],
            color=WHITE,
            stroke_width=2,
            dashed_ratio=0.6,
        )

        # Dimension from AP to LCF along centerline with annotation
        lcf_dim_arrow = create_dimension_arrow(
            np.array([plan_left_x, plan.get_center()[1], 0]),
            np.array([plan_center_x, plan.get_center()[1], 0]),
        )
        lcf_dim_label = MathTex(r"LCF = L/2", font_size=24, color=WHITE).next_to(lcf_dim_arrow, UP, buff=0.08)

        # Damage indication in compartment 3 (plan view)
        comp3_plan_left = plan_left_x + 2 * plan_spacing
        comp3_plan_right = plan_right_x
        comp3_plan_center_x = (comp3_plan_left + comp3_plan_right) / 2

        damage_zone_plan = Rectangle(
            width=(comp3_plan_right - comp3_plan_left),
            height=plan.height,
            fill_color=RED,
            fill_opacity=0.25,
            stroke_opacity=0,
        )
        damage_zone_plan.move_to([comp3_plan_center_x, plan.get_center()[1], 0])

        # Initial filled state in plan view (all compartments intact)
        plan_fill_comp1 = Rectangle(
            width=plan_spacing,
            height=plan.height,
            fill_color=GREEN,
            fill_opacity=0.18,
            stroke_opacity=0,
        ).move_to([plan_left_x + 0.5 * plan_spacing, plan.get_center()[1], 0])
        plan_fill_comp2 = Rectangle(
            width=plan_spacing,
            height=plan.height,
            fill_color=GREEN,
            fill_opacity=0.18,
            stroke_opacity=0,
        ).move_to([plan_left_x + 1.5 * plan_spacing, plan.get_center()[1], 0])
        plan_fill_comp3 = Rectangle(
            width=plan_spacing,
            height=plan.height,
            fill_color=GREEN,
            fill_opacity=0.18,
            stroke_opacity=0,
        ).move_to([plan_left_x + 2.5 * plan_spacing, plan.get_center()[1], 0])

        damage_x_plan = VGroup(
            Line(
                start=[comp3_plan_left, plan_top_y, 0],
                end=[comp3_plan_right, plan_bottom_y, 0],
                color=RED,
                stroke_width=3,
            ),
            Line(
                start=[comp3_plan_right, plan_top_y, 0],
                end=[comp3_plan_left, plan_bottom_y, 0],
                color=RED,
                stroke_width=3,
            ),
        )

        # LCF_S after damage (vertical axis at division between compartments 1 and 2)
        # The division is at plan_left_x + plan_spacing
        lcf_s_x = plan_left_x + plan_spacing
        lcf_s_axis = DashedLine(
            start=[lcf_s_x, plan_bottom_y - 0.2, 0],
            end=[lcf_s_x, plan_top_y + 0.2, 0],
            color=WHITE,
            stroke_width=2,
            dashed_ratio=0.6,
        )
        lcf_dim_arrow_s = create_dimension_arrow(
            np.array([plan_left_x, plan.get_center()[1], 0]),
            np.array([lcf_s_x, plan.get_center()[1], 0]),
        )
        lcf_dim_label_s = MathTex(r"LCF_S = L/3", font_size=24, color=WHITE).next_to(lcf_dim_arrow_s, UP, buff=0.08)

        # Equations for longitudinal stiffness (right side, below trim moment)
        txt_mct = cx(Text("Enhetstrimmomentet ved skade", font_size=22))
        eq_mct = cx(MathTex(r"MCT_{1cm_S} = \frac{\nabla \cdot \rho \cdot BM_{L_S}}{100 \cdot L}", font_size=32))

        txt_bm = cx(Text("Longitudinalt BM", font_size=22).next_to(eq_mct, DOWN, buff=0.25))
        eq_bm = cx(MathTex(r"BM_{L_S} = \frac{I_{F_S}}{\nabla}", font_size=32).next_to(txt_bm, DOWN, buff=0.15))

        txt_if = Text("Treghetsmoment om LCF", font_size=22)
        eq_if = MathTex(r"I_{F_S} = \frac{1}{12} B \left(\frac{2L}{3}\right)^3", font_size=32)

        beam_dim_arrow = create_dimension_arrow(
            np.array([plan_left_x - 0.45, plan_bottom_y, 0]),
            np.array([plan_left_x - 0.45, plan_top_y, 0]),
        )
        beam_dim_label = MathTex(r"B", font_size=24, color=WHITE).next_to(beam_dim_arrow, LEFT, buff=0.08)

        # Dimensions for reduced length in plan view (compartments 1 and 2) — above barge
        reduced_dim_arrows = VGroup()
        reduced_dim_labels = VGroup()
        for idx in [0, 1]:
            start_x = plan_left_x + idx * plan_spacing
            end_x = plan_left_x + (idx + 1) * plan_spacing
            arrow = create_dimension_arrow(
                np.array([start_x, plan_top_y + 0.35, 0]),
                np.array([end_x, plan_top_y + 0.35, 0]),
            )
            reduced_dim_arrows.add(arrow)
            label = Tex(r"L/3", font_size=20).next_to(arrow, UP, buff=0.08)
            reduced_dim_labels.add(label)

        # ─────────────────────────────────────────────────────────────────────
        # ANIMATION
        # ─────────────────────────────────────────────────────────────────────

        self.add(intro_text)
        self.wait(0.8)
        self.play(FadeOut(intro_text))

        # Phase 1: Show profile with compartments and waterline
        self.play(
            FadeIn(profile, dividers, wl_0, comp_labels),
            Write(title),
            Write(profile_label),
            Write(ap_label),
            Write(fp_label),
            Write(wl_0_label),
        )

        # Phase 2: Clear compartment numbers, then show G and B centers
        self.play(FadeOut(comp_labels))
        self.remove(comp_labels)
        self.play(FadeIn(g_dot, g_label, g_arrow, b_dot, b_label, b_arrow))

        # Phase 3: Show dimensions
        self.play(FadeIn(lcg_arrow, lcg_label, lcb_arrow, lcb_label))

        # Phase 4: Show trim lever l_k
        self.play(FadeIn(l_k_line, l_k_label))

        # Phase 5: Show damage triangle briefly
        self.play(FadeIn(damage_triangle))
        self.wait(0.5)
        self.play(FadeOut(damage_triangle))

        # Phase 6: Fade out dimensions (LCG, LCB) before filling
        self.play(FadeOut(lcg_arrow, lcg_label, lcb_arrow, lcb_label))

        # Phase 7: Fill compartment 3 with water (indicates damage)
        self.play(FadeIn(water_fill))

        # Phase 8: Parallel sinking - move vessel down, keep waterline fixed
        self.play(
            profile.animate.shift(DOWN * descent),
            dividers.animate.shift(DOWN * descent),
            profile_label.animate.shift(DOWN * descent),
            ap_label.animate.shift(DOWN * descent),
            fp_label.animate.shift(DOWN * descent),
            g_dot.animate.shift(DOWN * descent),
            g_label.animate.shift(DOWN * descent),
            g_arrow.animate.shift(DOWN * descent),
            Transform(b_arrow, b_s_arrow),
            Transform(l_k_line, l_k_s_line),
            Transform(l_k_label, l_k_s_label),
            Transform(wl_0_label, wl_s_label),
            Transform(water_fill, water_fill_sink),
            b_dot.animate.become(b_s_dot),
            b_label.animate.become(b_s_label),
            run_time=2.8,
        )
        self.wait(0.7)

        # Phase 9: Show T_S dimension
        self.play(FadeIn(t_s_arrow, t_s_label))

        # Phase 10: Show trim moment text, then equation
        self.play(Write(txt_trim))
        self.wait(0.8)
        self.play(Write(eq_tm))
        self.wait(0.8)

        # Phase 11: Remove T_S before rotating
        self.play(FadeOut(t_s_arrow, t_s_label))

        # Phase 12: Small trim rotation of the profile section
        # Keep rotation moderate so the fixed waterline does not cross the deck edge.
        self.play(
            Rotate(
                profile_rotation_group,
                angle=rot_angle,
                about_point=rot_about,
            ),
            Transform(b_dot, b_back_dot),
            Transform(b_label, b_back_label),
            Transform(b_arrow, b_back_arrow),
            Transform(g_arrow, g_arrow_rot),
            Transform(l_k_line, l_k_back_line),
            Transform(l_k_label, l_k_back_label),
            Transform(water_fill, water_fill_rot),
            run_time=3.0,
        )

        # Phase 13: Hide l_k once B_S has moved back, then show trim reference t.
        self.play(FadeOut(l_k_line, l_k_label))
        self.play(FadeIn(fore_trim_line, aft_trim_line, t_dim_arrow, t_dim_label))

        # Phase 14: Show total trim text and equation
        self.play(Write(txt_total_trim))
        self.wait(0.8)
        self.play(Write(eq_total_trim))
        self.wait(0.8)

        # Phase 15: Clear the first equation block and continue directly with trim distribution.
        txt_trim_split = Text("Fordeler den totale trimmen", font_size=22).move_to([3.8, 2.2, 0])
        eq_ta = MathTex(
            r"t_a = t \cdot \frac{LCF_S}{L}",
            font_size=30,
        ).next_to(txt_trim_split, DOWN, buff=0.2).set_x(3.8)
        eq_tf = MathTex(
            r"t_f = t \cdot \frac{L - LCF_S}{L}",
            font_size=30,
        ).next_to(eq_ta, DOWN, buff=0.18).set_x(3.8)
        txt_ta_draft = Text("Dypgang akter", font_size=22).move_to([3.8, -0.15, 0])
        eq_ta_draft = MathTex(
            r"T_A = T_S - \frac{t_a}{100}",
            font_size=30,
        ).next_to(txt_ta_draft, DOWN, buff=0.18).set_x(3.8)
        txt_tf_draft = Text("Dypgang forrut", font_size=22).next_to(eq_ta_draft, DOWN, buff=0.42).set_x(3.8)
        eq_tf_draft = MathTex(
            r"T_F = T_S + \frac{t_f}{100}",
            font_size=30,
        ).next_to(txt_tf_draft, DOWN, buff=0.18).set_x(3.8)

        self.play(FadeOut(txt_trim, eq_tm, txt_total_trim, eq_total_trim))
        self.wait(0.6)
        self.play(FadeOut(fore_trim_line, aft_trim_line, t_dim_arrow, t_dim_label))
        self.wait(0.6)
        self.play(Write(txt_trim_split))
        self.wait(0.6)
        self.play(Write(eq_ta), Write(eq_tf))
        self.wait(0.8)
        self.play(FadeIn(fore_trim_line, middle_trim_line, aft_distribution_line, lcf_s_profile_arrow, lcf_s_profile_label))
        self.wait(0.6)
        self.play(FadeIn(t_f_dim_arrow, t_f_dim_label, t_a_dim_arrow, t_a_dim_label))
        self.wait(0.8)
        self.play(Write(txt_ta_draft), Write(eq_ta_draft))
        self.wait(0.6)
        self.play(Write(txt_tf_draft), Write(eq_tf_draft))

        self.wait(1.5)