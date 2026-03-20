from manim import *

from barge_geometry import ShipParameters, scaled, create_section_rect, create_dimension_arrow


class BargeDamageHydrostaticsScene(Scene):
    """Skeleton scene: damaged barge, KB shift, waterplane-area loss, and BM_T change."""

    def construct(self):
        self.camera.background_color = WHITE
        self.params = ShipParameters()
        self.scale = 0.1

        self.setup_side_view_baseline()
        self.phase_1_set_damaged_baseline()
        self.phase_2_define_effective_buoyant_volume()
        self.phase_3_show_vertical_shift_in_kb()
        self.phase_4_explain_kb_cause()
        self.phase_5_switch_to_plan_view_and_waterplane_loss()
        self.phase_6_link_to_it_and_bmt()
        self.phase_7_wrap_up_stability_message()

    def setup_side_view_baseline(self):
        long_width = scaled(self.params.LPP, self.scale)
        section_height = scaled(self.params.D, self.scale)
        water_y = scaled(self.params.T, self.scale)
        new_water_y = water_y * 1.5

        self.long_section = create_section_rect(long_width, section_height, color=BLACK)
        self.long_section.shift(LEFT * 3)

        self.long_left = self.long_section.get_left()[0]
        self.long_right = self.long_section.get_right()[0]
        self.divider_spacing = (self.long_right - self.long_left) / 3

        self.compartment_dividers = VGroup()
        for i in range(1, 3):
            divider_x = self.long_left + i * self.divider_spacing
            divider = Line(
                start=[divider_x, self.long_section.get_bottom()[1], 0],
                end=[divider_x, self.long_section.get_top()[1], 0],
                color=BLACK,
                stroke_width=2,
            )
            self.compartment_dividers.add(divider)

        self.waterline_original = Line(
            start=[self.long_left - 0.5, water_y, 0],
            end=[self.long_right + 0.2, water_y, 0],
            color=GREY,
            stroke_width=1,
        ).set_dash([0.1, 0.1])

        self.waterline_damaged = Line(
            start=[self.long_left - 0.5, new_water_y, 0],
            end=[self.long_right + 0.2, new_water_y, 0],
            color=BLACK,
            stroke_width=2,
        ).set_dash([0.1, 0.1])

        comp2_left = self.long_left + self.divider_spacing
        comp2_right = self.long_left + 2 * self.divider_spacing
        comp2_width = comp2_right - comp2_left

        self.flooded_compartment = Rectangle(
            width=comp2_width,
            height=new_water_y,
            fill_color=GREY,
            fill_opacity=0.45,
            stroke_opacity=0,
        )
        self.flooded_compartment.move_to([(comp2_left + comp2_right) / 2, new_water_y / 2, 0])

        self.comp1_active = Rectangle(
            width=self.divider_spacing,
            height=new_water_y,
            fill_color=GREEN,
            fill_opacity=0.2,
            stroke_opacity=0,
        ).move_to([self.long_left + 0.5 * self.divider_spacing, new_water_y / 2, 0])

        self.comp3_active = Rectangle(
            width=self.divider_spacing,
            height=new_water_y,
            fill_color=GREEN,
            fill_opacity=0.2,
            stroke_opacity=0,
        ).move_to([self.long_left + 2.5 * self.divider_spacing, new_water_y / 2, 0])

        self.comp2_lost = Rectangle(
            width=self.divider_spacing,
            height=new_water_y,
            fill_color=RED,
            fill_opacity=0.22,
            stroke_opacity=0,
        ).move_to([self.long_left + 1.5 * self.divider_spacing, new_water_y / 2, 0])

        self.kb_initial = Dot(point=[self.long_left + 1.5 * self.divider_spacing, water_y / 2, 0], color=BLUE)
        self.kb_damaged = Dot(point=[self.long_left + 1.5 * self.divider_spacing, new_water_y * 0.62, 0], color=BLUE)

        self.side_group = VGroup(
            self.long_section,
            self.compartment_dividers,
            self.waterline_original,
            self.waterline_damaged,
            self.flooded_compartment,
        )

    def phase_1_set_damaged_baseline(self):
        title = Text("Fase 1: Skadet baseline", font_size=34, color=BLACK).to_edge(UP, buff=0.4)

        T_arrow = create_dimension_arrow(
            np.array([self.long_left, self.waterline_original.get_center()[1], 0]),
            np.array([self.long_left, 0, 0]),
        ).shift(LEFT * 0.3)
        T_arrow.set_color(GREY)
        T_label = MathTex(r"T", font_size=30, color=GREY).next_to(T_arrow, LEFT, buff=0.08)

        Ts_arrow = create_dimension_arrow(
            np.array([self.long_left - 0.35, self.waterline_damaged.get_center()[1], 0]),
            np.array([self.long_left - 0.35, 0, 0]),
        ).shift(LEFT * 0.3)
        Ts_arrow.set_color(BLACK)
        Ts_label = MathTex(r"T_S", font_size=30, color=BLACK).next_to(Ts_arrow, LEFT, buff=0.08)

        self.play(FadeIn(self.side_group), Write(title))
        self.play(FadeIn(T_arrow, T_label, Ts_arrow, Ts_label))
        self.wait(1.0)

        self.phase_1_title = title
        self.phase_1_dims = VGroup(T_arrow, T_label, Ts_arrow, Ts_label)

    def phase_2_define_effective_buoyant_volume(self):
        text = Text("Fase 2: Effektivt oppdriftsvolum", font_size=30, color=BLACK).to_edge(UP, buff=0.4)
        self.play(Transform(self.phase_1_title, text))
        self.play(FadeIn(self.comp1_active, self.comp3_active, self.comp2_lost))
        self.wait(1.0)

    def phase_3_show_vertical_shift_in_kb(self):
        text = Text("Fase 3: Vertikal forskyvning av KB", font_size=30, color=BLACK).to_edge(UP, buff=0.4)
        self.play(Transform(self.phase_1_title, text))

        kb_label = MathTex(r"KB", font_size=28, color=BLUE).next_to(self.kb_initial, RIGHT, buff=0.08)
        kbs_label = MathTex(r"KB_S", font_size=28, color=BLUE).next_to(self.kb_damaged, RIGHT, buff=0.08)

        self.play(FadeIn(self.kb_initial, kb_label))
        self.play(Transform(self.kb_initial, self.kb_damaged), Transform(kb_label, kbs_label))

        kb_eq = MathTex(r"KB = \frac{\int z\,dV}{\nabla}", font_size=32, color=BLACK).to_edge(DOWN, buff=0.5)
        self.play(Write(kb_eq))
        self.wait(1.2)

        self.kb_graphics = VGroup(self.kb_initial, kb_label, kb_eq)

    def phase_4_explain_kb_cause(self):
        text = Text("Fase 4: Hvorfor KB flytter seg", font_size=30, color=BLACK).to_edge(UP, buff=0.4)
        self.play(Transform(self.phase_1_title, text))

        callout = Text(
            "Tyngdepunktet til oppdriftsgivende volum endres\n"
            "når geometri og neddykket volum fordeles annerledes.",
            font_size=24,
            color=BLACK,
        ).to_edge(RIGHT, buff=0.6)

        pulse = SurroundingRectangle(VGroup(self.comp1_active, self.comp3_active), color=BLUE, buff=0.08)
        self.play(FadeIn(callout), Create(pulse))
        self.wait(1.2)
        self.play(FadeOut(pulse))

        self.phase_4_callout = callout

    def phase_5_switch_to_plan_view_and_waterplane_loss(self):
        text = Text("Fase 5: Planvisning og tap av vannlinjeareal", font_size=30, color=BLACK).to_edge(UP, buff=0.4)
        self.play(Transform(self.phase_1_title, text))

        plan_width = scaled(self.params.LPP, self.scale)
        plan_height = scaled(self.params.B, self.scale)
        plan_box = Rectangle(width=plan_width, height=plan_height, color=BLACK, stroke_width=3)
        plan_box.shift(RIGHT * 3)

        plan_left = plan_box.get_left()[0]
        spacing = plan_width / 3

        plan_comp1 = Rectangle(width=spacing, height=plan_height, fill_color=GREEN, fill_opacity=0.2, stroke_opacity=0)
        plan_comp1.move_to([plan_left + 0.5 * spacing, plan_box.get_center()[1], 0])

        plan_comp2_lost = Rectangle(width=spacing, height=plan_height, fill_color=RED, fill_opacity=0.25, stroke_opacity=0)
        plan_comp2_lost.move_to([plan_left + 1.5 * spacing, plan_box.get_center()[1], 0])

        plan_comp3 = Rectangle(width=spacing, height=plan_height, fill_color=GREEN, fill_opacity=0.2, stroke_opacity=0)
        plan_comp3.move_to([plan_left + 2.5 * spacing, plan_box.get_center()[1], 0])

        plan_dividers = VGroup(
            Line(
                start=[plan_left + spacing, plan_box.get_bottom()[1], 0],
                end=[plan_left + spacing, plan_box.get_top()[1], 0],
                color=BLACK,
            ),
            Line(
                start=[plan_left + 2 * spacing, plan_box.get_bottom()[1], 0],
                end=[plan_left + 2 * spacing, plan_box.get_top()[1], 0],
                color=BLACK,
            ),
        )

        aw_text = MathTex(r"A_{W,eff} < A_W", font_size=32, color=BLACK).next_to(plan_box, DOWN, buff=0.3)

        self.play(FadeIn(plan_box, plan_dividers, plan_comp1, plan_comp2_lost, plan_comp3, aw_text))
        self.wait(1.2)

        self.plan_group = VGroup(plan_box, plan_dividers, plan_comp1, plan_comp2_lost, plan_comp3, aw_text)

    def phase_6_link_to_it_and_bmt(self):
        text = Text("Fase 6: Konsekvens for I_T og BM_T", font_size=30, color=BLACK).to_edge(UP, buff=0.4)
        self.play(Transform(self.phase_1_title, text))

        it_before = Line(start=[1.4, -1.7, 0], end=[4.6, -1.7, 0], color=GREY, stroke_width=10)
        it_after = Line(start=[2.2, -1.7, 0], end=[3.8, -1.7, 0], color=BLACK, stroke_width=10)

        it_label = MathTex(r"I_T\downarrow", font_size=30, color=BLACK).next_to(it_after, DOWN, buff=0.2)
        bm_eq = MathTex(r"BM_T = \frac{I_T}{\nabla}", font_size=34, color=BLACK).to_edge(DOWN, buff=0.5)
        bm_change = MathTex(r"BM_T\downarrow", font_size=34, color=BLACK).next_to(bm_eq, RIGHT, buff=0.4)

        self.play(FadeIn(it_before))
        self.play(Transform(it_before, it_after), FadeIn(it_label))
        self.play(Write(bm_eq), Write(bm_change))
        self.wait(1.2)

        self.phase_6_group = VGroup(it_before, it_label, bm_eq, bm_change)

    def phase_7_wrap_up_stability_message(self):
        text = Text("Fase 7: Oppsummering", font_size=30, color=BLACK).to_edge(UP, buff=0.4)
        self.play(Transform(self.phase_1_title, text))

        summary = VGroup(
            MathTex(r"KB\uparrow", font_size=36, color=BLACK),
            MathTex(r"BM_T\downarrow", font_size=36, color=BLACK),
            MathTex(r"GM_T = KB + BM_T - KG", font_size=36, color=BLACK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        summary.to_edge(LEFT, buff=0.6).shift(DOWN * 0.6)

        conclusion = Text("Redusert initial tverrskips stabilitetsmargin", font_size=28, color=BLACK)
        conclusion.to_edge(DOWN, buff=0.25)

        self.play(Write(summary))
        self.wait(1.0)
        self.play(Write(conclusion))
        self.wait(1.8)


if __name__ == "__main__":
    print("Run with:")
    print("  manim -ql barge_damage_hydrostatics_scene.py BargeDamageHydrostaticsScene")
