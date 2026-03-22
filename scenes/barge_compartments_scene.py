from manim import *

from scenes.barge_geometry import BargeSceneBase, create_dimension_arrow


class BargeCompartmentsScene(BargeSceneBase):
    """Shows the profile view with watertight compartmentation."""

    def construct(self):
        self.setup_barge_geometry()

        intro_text = Text("Lekteren har 3 vanntette avdelinger", font_size=38).move_to(ORIGIN)

        profile = self.create_profile_view(color=GREEN)
        profile.scale(1.3)
        profile.move_to(ORIGIN)

        profile_label = MathTex(r"\text{Profilsnitt}", font_size=28).next_to(profile, DOWN, buff=0.45)
        ap_label = Tex(r"AP", font_size=14).next_to(profile.get_corner(DL), DOWN + LEFT, buff=0.05)
        fp_label = Tex(r"FP", font_size=14).next_to(profile.get_corner(DR), DOWN + RIGHT, buff=0.05)

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

        self.add(intro_text)
        self.wait(0.8)
        self.play(FadeOut(intro_text))

        self.play(
            FadeIn(profile),
            Write(profile_label),
            Write(ap_label),
            Write(fp_label),
        )
        self.play(FadeIn(dividers, comp_labels))
        self.play(FadeIn(comp_arrows, comp_dim_labels))
        self.wait(1)

