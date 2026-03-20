from manim import *

from barge_geometry import BargeSceneBase, create_dimension_arrow


class BargeCompartmentsScene(BargeSceneBase):
    """Shows the profile view with watertight compartmentation."""

    def construct(self):
        self.setup_barge_geometry()

        profile = self.create_profile_view(color=GREEN)
        profile.shift(UP * 0.6)

        profile_label = MathTex(r"\text{Profilsnitt}", font_size=28).next_to(profile, DOWN, buff=0.45)
        ap_label = Tex(r"AP", font_size=14).next_to(profile.get_corner(DL), DOWN + LEFT, buff=0.05)
        fp_label = Tex(r"FP", font_size=14).next_to(profile.get_corner(DR), DOWN + RIGHT, buff=0.05)

        wl_y = profile.get_bottom()[1] + self.water_y
        profile_waterline = Line(
            start=[profile.get_left()[0] - 0.2, wl_y, 0],
            end=[profile.get_right()[0] + 0.2, wl_y, 0],
            color=BLUE,
            stroke_width=2,
        )
        profile_waterline.set_dash([0.1, 0.1])
        wl_label = Tex(r"WL", font_size=14).next_to(
            np.array([profile.get_right()[0] + 0.2, wl_y, 0]), RIGHT, buff=0.05
        )

        dividers, spacing = self.create_compartment_dividers(profile)

        # Compartment number labels centred in each bay
        left = profile.get_left()[0]
        mid_y = profile.get_center()[1]
        comp_labels = VGroup()
        for index in range(3):
            label = Tex(str(index + 1), font_size=40)
            label.move_to([left + (index + 0.5) * spacing, mid_y, 0])
            comp_labels.add(label)

        # L/3 dimension arrows above the profile
        arrow_y = profile.get_top()[1] + 0.3
        comp_arrows = VGroup()
        comp_dim_labels = VGroup()
        for index in range(3):
            start = np.array([left + index * spacing, arrow_y, 0])
            end = np.array([left + (index + 1) * spacing, arrow_y, 0])
            arrow = create_dimension_arrow(start, end)
            comp_arrows.add(arrow)
            dim_label = Tex(r"L/3", font_size=28).next_to(arrow, UP, buff=0.1)
            comp_dim_labels.add(dim_label)

        title = self.top_text("Vanntett inndeling i tre avdelinger", font_size=34)

        self.play(
            FadeIn(profile, profile_waterline),
            Write(title),
            Write(profile_label),
            Write(ap_label),
            Write(fp_label),
            Write(wl_label),
        )
        self.play(FadeIn(dividers, comp_labels))
        self.play(FadeIn(comp_arrows, comp_dim_labels))
        self.wait(1)
