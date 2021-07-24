from abc import ABC

import numpy as np

from manim import *


class Intro(Scene):
    def construct(self):
        title = Tex("Overview")
        title.to_edge(UP)
        title.set_color(YELLOW)
        self.play(Write(title))
        self.wait()

        tops = BulletedList("Bounds on the age of the universe", "Estimate from the expansion rate",
                            "Views from General Relativity","Addon: some corner stones")
        tops[0].set_color(RED)
        tops[1].set_color(GREEN)
        tops[2].set_color(BLUE)

        self.play(Write(tops[0]))
        self.wait(1)
        self.play(Write(tops[1]))
        self.wait(1)
        self.play(Write(tops[2]))
        self.wait(1)
        self.play(Write(tops[3]))
        self.wait(1)


class Bounds(Scene):
    def construct(self):
        title = Tex("Bounds on the age of the Universe")
        title.to_edge(UP)
        title.set_color(RED)
        self.play(Write(title))
        self.wait()

        # table = SVGMobject("periodic_table_semi_trans.svg")
        # table.scale(3)
        # self.play(GrowFromCenter(table))

        background0 = ImageMobject("periodic_table.png")
        background0.scale(0.9)
        self.add(background0)
        self.wait(3)

        background = ImageMobject("periodic_table_semi_trans.png")
        background.scale(0.9)
        self.play(FadeOut(background0), FadeIn(background))
        self.wait()

        tops = BulletedList(r"We are star dust,\\the remnants of a burnt out star:\\ca. 6 - 10 billion years",
                            "Oldest rocks on earth$^*$: 4.4 billion years")

        tops.set_color(YELLOW)
        conclusion = CustomizedBulletedList("The universe at least 10 billion years old")
        conclusion.set_color(RED)
        conclusion.next_to(tops, DOWN)
        conclusion.align_to(tops, LEFT)

        self.play(Write(tops[0]))
        self.wait(3)
        footnote = Tex("$^*$ a zircon mineral in the Jack Hills, Australia")
        footnote.scale(0.7)
        footnote.to_corner(DR)

        self.play(Write(tops[1]))
        self.play(Write(footnote))
        self.wait(3)

        self.play(Write(conclusion))
        self.wait(3)

        self.wait(10)


class Expansion(Scene):
    def construct(self):
        title = Tex("Estimate from the Expansion")
        title.to_edge(UP)
        title.set_color(GREEN)
        self.play(Write(title))
        self.wait(3)

        hubbleP = ImageMobject("Hubble.png")
        hubbleP.to_corner(UR)
        self.play(FadeIn(hubbleP))

        expansionrate = MathTex(r"H_0 = 70 \frac{\frac{km}{s}}{Mpc}")
        expansionrate.shift(2 * UP + 2 * LEFT)
        expansionrate.set_color(YELLOW)
        self.play(Write(expansionrate))
        self.wait(2)

        mpc = MathTex(
            r"1Mpc = 3.3 \text{ million light years} = 31 \text{ million trillion kilometers} = 3.1\cdot 10^{19} km")
        mpc.scale(0.7)
        mpc.next_to(expansionrate, DOWN)
        mpc.to_edge(LEFT, buff=LARGE_BUFF)
        self.play(Write(mpc))
        self.wait(2)

        expansionrate2 = MathTex(r"H_0=2.3\cdot 10^{-18} \frac{1}{s}")
        expansionrate2.set_color(YELLOW)
        expansionrate2.next_to(mpc, DOWN)
        expansionrate2.align_to(expansionrate, LEFT)
        self.play(Write(expansionrate2))
        self.wait(2)

        inv_expansion = MathTex(r"H_0^{-1} = 4.4 \cdot 10^{17} s = 14\text{ billion years}")
        inv_expansion.set_color(YELLOW)
        inv_expansion.next_to(expansionrate2, DOWN)
        inv_expansion.align_to(expansionrate, LEFT)
        self.play(Write(inv_expansion))
        self.wait(10)


class GR(Scene):
    def construct(self):
        title = Tex("General Relativity")
        title.to_edge(UP)
        title.set_color(BLUE)
        self.play(Write(title))
        self.wait(3)

        einsteinP = ImageMobject("Einstein.png")
        einsteinP.to_corner(UR)
        self.play(FadeIn(einsteinP))

        einstein = MathTex(r"G_{\mu\nu} =  8 \pi G \cdot  T_{\mu\nu}")
        einstein.scale(2)
        einstein.shift(1 * UP)
        einstein.set_color(YELLOW)
        self.play(Write(einstein))
        self.wait(2)

        teaser1 = ImageMobject("bh.png")
        teaser2 = ImageMobject("gw.png")
        teaser3 = ImageMobject("hubble_neu.png")
        teaser1.scale(0.75)
        teaser2.scale(0.75)
        teaser3.scale(0.75)

        teaser1.next_to(einstein, DOWN)
        teaser1.to_edge(LEFT, buff=SMALL_BUFF)
        teaser2.next_to(teaser1, RIGHT, buff=4 * SMALL_BUFF)
        teaser3.next_to(teaser2, RIGHT, buff=4 * SMALL_BUFF)

        self.play(FadeIn(teaser1))
        self.wait(2)
        self.play(FadeIn(teaser2))
        self.wait(2)
        self.play(FadeIn(teaser3))
        self.wait(2)

        self.wait(10)


class GR2(Scene):
    def construct(self):
        title = Tex("General Relativity")
        title.to_edge(UP)
        title.set_color(BLUE)
        self.play(Write(title))
        self.wait(3)

        friedmannP = ImageMobject("Friedmann.png")
        friedmannP.to_corner(UR)
        self.play(FadeIn(friedmannP))

        friedmann = MathTex(r"3\left(\frac{\dot a}{a}\right)^2", "=", r"8\pi G\cdot \rho")
        friedmann.shift(2 * UP)
        friedmann.set_color(YELLOW)
        self.play(Write(friedmann))
        self.wait(2)

        footnote = MathTex(r"\dot a=\frac{{\rm d}a}{{\rm d}t}")
        footnote.scale(0.7)
        footnote.set_color(YELLOW)
        footnote.to_corner(DR)
        self.play(Write(footnote))
        self.wait(3)

        friedmann0 = MathTex("3 H_0^2", "=", r"8\pi G\cdot \rho_0")
        friedmann0.next_to(friedmann, DOWN)
        friedmann0[1].align_to(friedmann[1], LEFT)
        friedmann0[0].next_to(friedmann0[1], LEFT)
        friedmann0[2].next_to(friedmann0[1], RIGHT)
        self.play(Write(friedmann0))
        self.wait(2)

        line_l = Line(LEFT, RIGHT)
        line_l.next_to(friedmann[0], DOWN, buff=2 * SMALL_BUFF)

        line_r = Line(LEFT, RIGHT)
        line_r.next_to(line_l, RIGHT, buff=MED_LARGE_BUFF)
        self.play(GrowFromCenter(line_l), GrowFromCenter(line_r))
        self.wait(2)

        friedmann1 = MathTex(r"H_0^{-2} \left(\frac{\dot a}{a}\right)^2", "=", r"\frac{\rho}{\rho_0}", "=",
                             r"\frac{a_0^3}{a^3}")
        friedmann1.scale(0.7)
        friedmann1.next_to(friedmann0, DOWN, buff=2 * SMALL_BUFF)
        friedmann1[4].set_color(BLUE)
        friedmann1[1].align_to(friedmann0[1], LEFT)
        friedmann1[0].next_to(friedmann1[1], LEFT)
        friedmann1[2].next_to(friedmann1[1], RIGHT)
        friedmann1[3].next_to(friedmann1[2], RIGHT, buff=SMALL_BUFF)
        friedmann1[4].next_to(friedmann1[3], RIGHT)
        self.play(Write(friedmann1[0:3]))
        self.wait(2)

        color_palette = [BLUE, RED]
        # pie chart

        weights = np.array([0.999, 0.001])
        weights /= weights.sum()

        angles = weights * TAU
        angles_offset = np.cumsum((0, *angles[:-1]))

        sectors1 = [
            MySector(start_angle=ao, angle=a,
                     stroke_width=DEFAULT_STROKE_WIDTH,
                     fill_opacity=0)
            for ao, a in zip(angles_offset, angles)
        ]

        sectors2 = [
            MySector(start_angle=ao, angle=a,
                     stroke_width=DEFAULT_STROKE_WIDTH,
                     fill_color=color_palette[i % len(color_palette)], fill_opacity=0.5)
            for i, (ao, a) in enumerate(zip(angles_offset, angles))
        ]

        weights = np.array([3., 7.])
        weights /= weights.sum()

        angles = weights * TAU
        angles_offset = np.cumsum((0, *angles[:-1]))

        sectors3 = [
            MySector(start_angle=ao, angle=a,
                     stroke_width=DEFAULT_STROKE_WIDTH,
                     fill_color=color_palette[i % len(color_palette)], fill_opacity=0.5)
            for i, (ao, a) in enumerate(zip(angles_offset, angles))
        ]

        group = VGroup(*sectors1, *sectors2, *sectors3)
        group.to_corner(UL)

        matter = Tex("matter")
        matter.set_color(BLUE)
        matter.next_to(group, UP, buff=SMALL_BUFF)

        self.play(
            *(Create(a1, run_time=1) for a1 in sectors1)
        )

        self.play(
            *(Transform(a1, a2, runtime=1) for (a1, a2) in zip(sectors1, sectors2)),
            Write(matter)
        )

        self.wait(2)

        self.play(Write(friedmann1[3:5]))
        self.wait(2)

        self.play(ApplyMethod(friedmann1[0].set_color, BLUE))
        self.wait(2)

        friedmann2 = MathTex(r"\frac{1}{\sqrt{a_0^3} H_0 }", r"\int\limits_0^{a_0}", r"\sqrt{a}", r"{\rm d}a", "=",
                             r"\int\limits_0^{t_0}", r"{\rm d}t")
        friedmann2.scale(0.7)
        friedmann2.next_to(friedmann1, DOWN, buff=2 * SMALL_BUFF)
        friedmann2.set_color(BLUE)
        friedmann2[4].align_to(friedmann1[1], LEFT)
        friedmann2[3].next_to(friedmann2[4], LEFT)
        friedmann2[2].next_to(friedmann2[3], LEFT)
        friedmann2[1].next_to(friedmann2[2], LEFT)
        friedmann2[0].next_to(friedmann2[2], LEFT)
        friedmann2[5].next_to(friedmann2[4], RIGHT)
        friedmann2[6].next_to(friedmann2[4], RIGHT)
        self.play(Write(friedmann2[0]), Write(friedmann2[2:5]), Write(friedmann2[6]))
        self.wait(2)

        friedmann2[0].generate_target()
        friedmann2[0].next_to(friedmann2[1], LEFT)
        friedmann2[0].target = friedmann2[0]
        friedmann2[6].generate_target()
        friedmann2[6].next_to(friedmann2[5], RIGHT)
        friedmann2[6].target = friedmann2[6]
        self.play(MoveToTarget(friedmann2[0]), MoveToTarget(friedmann2[6]), Write(friedmann2[1]), Write(friedmann2[5]))

        self.wait(2)

        friedmann3 = MathTex("t_0", "=", r"\frac{2}{3}", " H_0^{-1}", r"\approx ", "9.3", r"\text{ billion years}")
        friedmann3.next_to(friedmann2, DOWN, buff=2 * SMALL_BUFF)
        friedmann3.set_color(BLUE)
        friedmann3[1].align_to(friedmann2[4], LEFT)
        friedmann3[0].next_to(friedmann3[1], LEFT)
        friedmann3[2].next_to(friedmann3[1], RIGHT)
        friedmann3[3].next_to(friedmann3[2], RIGHT)
        friedmann3[4].next_to(friedmann3[3], RIGHT)
        friedmann3[5].next_to(friedmann3[4], RIGHT)
        friedmann3[6].next_to(friedmann3[5], RIGHT)

        self.play(Write(friedmann3[0:4]))
        self.wait(2)

        hubble = ImageMobject("hubble_neu.png")
        hubble.scale(0.66)
        hubble.next_to(friedmann2, RIGHT, buff=1.5 * LARGE_BUFF)

        self.remove(footnote)
        self.play(FadeIn(hubble))
        self.wait()

        self.play(Write(friedmann3[4:7]))
        self.wait(2)

        dark_energy = Tex("dark energy")
        dark_energy.set_color(RED)
        dark_energy.next_to(group, DOWN, buff=SMALL_BUFF)

        self.play(
            *(Transform(a1, a2, runtime=1) for (a1, a2) in zip(sectors1, sectors3)),
            Write(dark_energy)
        )
        self.wait(2)

        friedmann1[4].generate_target()
        friedmann1[4].target = MathTex(r"0.3\frac{a_0^3}{a^3}+0.7")
        friedmann1[4].target.set_color(RED)
        friedmann1[4].target.scale(0.7)
        friedmann1[4].target.next_to(friedmann1[3], RIGHT)

        self.play(MoveToTarget(friedmann1[4]))
        self.wait(2)

        friedmann2[2].generate_target()
        friedmann2[2].target = MathTex(r"\frac{1}{\sqrt{0.3a^{-1}a_0^3+0.7a^2}}")
        friedmann2[2].target.set_color(RED)
        friedmann2[2].target.scale(0.7)
        friedmann2[2].target.next_to(friedmann2[3], LEFT)

        friedmann2[1].generate_target()
        friedmann2[1].target = friedmann2[1]
        friedmann2[1].target.next_to(friedmann2[2].target, LEFT)
        friedmann2[0].generate_target()
        friedmann2[0].target = MathTex(r"\frac{1}{H_0}")
        friedmann2[0].target.set_color(BLUE)
        friedmann2[0].target.scale(0.7)
        friedmann2[0].target.next_to(friedmann2[1].target, LEFT)

        self.play(MoveToTarget(friedmann2[0]), MoveToTarget(friedmann2[1]), MoveToTarget(friedmann2[2]))
        self.wait(2)

        friedmann3[2].generate_target()
        friedmann3[2].target = MathTex("0.96")
        friedmann3[2].target.next_to(friedmann3[1], RIGHT)
        friedmann3[2].target.set_color(RED)

        for i in range(3, 7):
            friedmann3[i].generate_target()
            if i == 5:
                friedmann3[i].target = MathTex("14")
                friedmann3[i].target.set_color(RED)
            else:
                friedmann3[i].target = friedmann3[i]
            friedmann3[i].target.next_to(friedmann3[i - 1].target)

        self.play(MoveToTarget(friedmann3[2]), *[MoveToTarget(friedmann3[i]) for i in range(3, 7)])
        self.wait(2)

        self.wait(10)


class MySector(Sector, ABC):
    """ Circular sector shape with a custom interpolation method. """

    def interpolate(self, mobject1, mobject2, alpha, path_func=straight_path):
        if not (isinstance(mobject1, MySector) and isinstance(mobject2, MySector)):
            return super().interpolate(mobject1, mobject2, alpha, path_func=path_func)

        for attr in (
                'start_angle', 'angle',
                'inner_radius', 'outer_radius',
        ):
            v1 = getattr(mobject1, attr)
            v2 = getattr(mobject2, attr)
            setattr(self, attr, path_func(v1, v2, alpha))

        self.arc_center = path_func(
            mobject1.get_arc_center(),
            mobject2.get_arc_center(),
            alpha
        )
        self.interpolate_color(mobject1, mobject2, alpha)
        self.clear_points()
        self.generate_points()
        return self


class Details(Scene):
    def construct(self):
        title = Tex("From Einstein to Friedmann")
        title.to_corner(UL)
        title.set_color(WHITE)
        self.play(Write(title))
        self.wait(3)

        calculations = ImageMobject("calculations.png")
        calculations.scale(0.4)
        calculations.to_edge(RIGHT)
        self.play(FadeIn(calculations))
        self.wait(2)

        palette = [YELLOW, RED, GREEN, BLUE, PURPLE]
        liste = BulletedList("a metric for an expanding universe", "Christoffel symbols", "Ricci tensor",
                             "Einstein tensor", "energy--momentum tensor")
        liste.to_edge(LEFT)

        lines = []
        line = Line(UP, DOWN)
        line.scale(0.275)
        line.shift(1.5 * RIGHT + 3.5 * UP)
        line.set_style(stroke_width=10)
        lines.append(line)

        line = Line(UP, DOWN)
        line.scale(1.75)
        line.shift(1.5 * RIGHT + 1.5 * UP)
        line.set_style(stroke_width=10)
        lines.append(line)

        line = Line(UP, DOWN)
        line.scale(1.15)
        line.shift(1.5 * RIGHT + 1.5 * DOWN)
        line.set_style(stroke_width=10)
        lines.append(line)

        line = Line(UP, DOWN)
        line.scale(0.45)
        line.shift(1.5 * RIGHT + 3.2 * DOWN)
        line.set_style(stroke_width=10)
        lines.append(line)

        for i in range(0, len(liste)):
            liste[i].set_color(palette[i])
            if i < len(lines):
                lines[i].set_color(palette[i])
                self.play(Write(liste[i]), GrowFromCenter(lines[i]))
            else:
                self.play(Write(liste[i]))

            self.wait(2)

        self.wait(10)


class Metric(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            y_min=0,
            y_max=5,
            x_min=0,
            x_max=5,
            # y_labeled_nums= np.arange(0, 5, 1),
            # x_labeled_nums=np.arange(0, 7, 1),
            x_axis_label='',
            y_axis_label='',
            graph_origin=np.array([-6, -3, 0]),
            include_tip=True,
            x_axis_width=6,
            y_axis_height=6,
            **kwargs
        )

    def construct(self):
        title = Tex("The metric --- The measurement of distances")
        title.to_edge(UP)
        title.set_color(YELLOW)
        self.play(Write(title))
        self.wait(3)

        self.setup_axes()

        grid = []
        for x in range(1, 6):
            line = Line(self.coords_to_point(x, 0), self.coords_to_point(x, 5))
            line.set_color(BLUE)
            line.set_style(stroke_width=0.75)
            grid.append(line)

        for y in range(1, 6):
            line = Line(self.coords_to_point(0, y), self.coords_to_point(5, y))
            line.set_color(BLUE)
            line.set_style(stroke_width=0.75)
            grid.append(line)

        self.play(*[GrowFromCenter(grid[i]) for i in range(0, len(grid))])
        self.wait(2)

        dot_A = Dot().move_to(self.coords_to_point(0, 0))
        self.add(dot_A)
        dot_B = Dot().move_to(self.coords_to_point(4, 3))
        self.add(dot_B)
        self.wait(2)

        label_a = MathTex("A(0|0)")
        label_b = MathTex("B(4|3)")
        label_a.scale(0.7)
        label_b.scale(0.7)
        label_a.next_to(dot_A, DOWN, buff=SMALL_BUFF)
        label_b.next_to(dot_B, LEFT, buff=4 * SMALL_BUFF)
        self.play(Write(label_a), Write(label_b))
        self.wait(2)

        line = Line(dot_A.get_center(), dot_B.get_center())
        line.set_color(YELLOW)
        line.add_tip(at_start=True)
        line.add_tip()

        question = MathTex(r"\text{distance } \Delta s")
        question.scale(0.7)
        question.set_color(YELLOW)
        question.rotate(0.64, OUT)
        question.shift(self.coords_to_point(1.8, 1.65))

        self.play(Write(question), GrowFromCenter(line))
        self.wait()

        dot_C = Dot().move_to(self.coords_to_point(4, 0))
        line_x = Line(dot_A.get_center(), dot_C.get_center())
        line_x.set_color(BLUE)
        delta_x = MathTex(r"\Delta x =4")
        delta_x.set_color(BLUE)
        delta_x.scale(0.7)
        delta_x.move_to(self.coords_to_point(2, -0.3))
        self.play(Write(delta_x), GrowFromCenter(line_x))
        self.wait()

        line_y = Line(dot_C.get_center(), dot_B.get_center())
        line_y.set_color(BLUE)
        delta_y = MathTex(r"\Delta y =3")
        delta_y.set_color(BLUE)
        delta_y.scale(0.7)
        delta_y.rotate(3.141 / 2, OUT)
        delta_y.move_to(self.coords_to_point(4.3, 1.5))
        self.play(Write(delta_y), GrowFromCenter(line_y))
        self.wait()

        pyt = MathTex(r"\Delta s^2 ", "=", r" \Delta x^2", "+", r"\Delta y^2")
        pyt[0].set_color(YELLOW)
        pyt[2].set_color(BLUE)
        pyt[4].set_color(BLUE)
        pyt2 = MathTex(r"\Delta s^2", "=", r" \left(\begin{array}{c c} \Delta x & \Delta y\end{array}\right)",
                       r"\left(\begin{array}{c c} 1 & 0 \\ 0 &1 \end{array}\right)",
                       r"\left(\begin{array}{c} \Delta x \\ \Delta y\end{array}\right)")
        pyt.scale(0.7)
        pyt2.scale(0.7)
        pyt.next_to(title, DOWN, buff=LARGE_BUFF)
        pyt.shift(2 * RIGHT)
        pyt2.next_to(pyt, DOWN)
        pyt2[1].align_to(pyt[1], LEFT)
        pyt2[0].next_to(pyt2[1], LEFT)
        pyt2[2].next_to(pyt2[1], RIGHT)
        pyt2[2].set_color(BLUE)
        pyt2[4].set_color(BLUE)
        pyt2[3].next_to(pyt2[2], RIGHT)
        pyt2[4].next_to(pyt2[3], RIGHT)
        pyt3 = MathTex(r"5^2", "=", "4^2", "+", "3^2")
        pyt3.scale(0.7)
        pyt3[0].set_color(YELLOW)
        pyt3.next_to(pyt2, DOWN)
        pyt3[1].align_to(pyt2[1], LEFT)
        pyt3[0].next_to(pyt3[1], LEFT)
        pyt3[2].next_to(pyt3[1], RIGHT)
        pyt3[3].next_to(pyt3[2], RIGHT)
        pyt3[4].next_to(pyt3[3], RIGHT)
        pyt3[2].set_color(BLUE)
        pyt3[4].set_color(BLUE)

        self.play(Write(pyt))
        self.wait(2)
        self.play(Write(pyt2))
        self.wait(2)
        self.play(Write(pyt3))
        self.wait(2)

        # transform grid

        for x in range(0, 5):
            grid[x].generate_target()
            r = self.coords_to_point(x + 1, 0)[0] - self.coords_to_point(0, 0)[0]
            grid[x].target = Arc(radius=r, angle=TAU / 4, arc_center=self.coords_to_point(0, 0))
            grid[x].target.set_color(RED)
            grid[x].target.set_style(stroke_width=0.75)

        labels = []
        for y in range(1, 6):
            grid[y + 4].generate_target()
            grid[y + 4].target = Line(self.coords_to_point(0, 0), self.coords_to_point(5 * np.cos(np.radians(y * 18)),
                                                                                       5 * np.sin(np.radians(y * 18))))
            grid[y + 4].target.set_color(RED)
            grid[y + 4].target.set_style(stroke_width=0.75)
            degree = 18 * y
            text = MathTex(str(degree), r"^\circ")
            text.scale(0.7)
            text.move_to(self.coords_to_point(5.25 * np.cos(np.radians(degree)), 5.25 * np.sin(np.radians(degree))))
            text.set_color(RED)
            labels.append(text)

        label_b.generate_target()
        label_b.target = MathTex(r"B(5|36.9^\circ)")
        label_b.target.scale(0.7)
        label_b.target.move_to(label_b.get_center())
        label_b.target.set_color(RED)
        label_b.target.shift(0.2 * LEFT)
        label_a.generate_target()
        label_a.target = MathTex(r"A(0|36.9^\circ)")
        label_a.target.scale(0.7)
        label_a.target.set_color(RED)
        label_a.target.move_to(label_a.get_center())

        self.play(*[MoveToTarget(grid[x]) for x in range(0, 5)],
                  *[MoveToTarget(grid[y + 4]) for y in range(1, 6)],
                  FadeOut(self.axes[1]), FadeOut(delta_x), FadeOut(delta_y), FadeOut(line_x), FadeOut(line_y),
                  *[Write(labels[label]) for label in range(0, len(labels))], MoveToTarget(label_b),
                  MoveToTarget(label_a))

        self.wait(2)

        pyt4 = MathTex(r"\Delta s^2", r"\neq", "\Delta r^2", "+", r"\Delta \varphi^2")
        pyt4.next_to(pyt3, DOWN)
        pyt4.scale(0.7)
        pyt4[1].align_to(pyt3[1], LEFT)
        pyt4[0].next_to(pyt4[1], LEFT)
        pyt4[0].set_color(YELLOW)
        pyt4[2].next_to(pyt4[1], RIGHT)
        pyt4[2].set_color(RED)
        pyt4[4].set_color(RED)
        pyt4[3].next_to(pyt4[2], RIGHT)
        pyt4[4].next_to(pyt4[3], RIGHT)

        self.play(Write(pyt4))
        self.wait(2)

        dot_A.generate_target()
        dot_A.target = Dot().move_to(self.coords_to_point(np.cos(np.radians(18)), np.sin(np.radians(18))))
        dot_B.generate_target()
        dot_B.target = Dot().move_to(self.coords_to_point(2 * np.cos(np.radians(36)), 2 * np.sin(np.radians(36))))

        label_b.generate_target()
        label_b.target = MathTex(r"B(2|36^\circ)")
        label_b.target.scale(0.7)
        label_b.target.next_to(dot_B.target.get_center(), UP)
        label_b.target.set_color(RED)
        label_b.target.shift(0.2 * LEFT)
        label_a.generate_target()
        label_a.target = MathTex(r"A(1|18^\circ)")
        label_a.target.scale(0.7)
        label_a.target.set_color(RED)
        label_a.target.next_to(dot_A.target.get_center(), DOWN, buff=LARGE_BUFF)

        question.generate_target()
        question.target = MathTex(r"{\rm d}s")
        question.target.set_color(YELLOW)
        question.target.rotate(np.radians(52.4))
        question.target.scale(0.7)
        question.target.move_to(self.coords_to_point(1.1, 0.8))

        line.generate_target()
        line.target = Line(dot_A.target.get_center(), dot_B.target.get_center())
        line.target.set_color(YELLOW)

        self.play(MoveToTarget(line), MoveToTarget(dot_A), MoveToTarget(dot_B), MoveToTarget(question),
                  MoveToTarget(label_a), MoveToTarget(label_b))
        self.wait(2)

        label_b.generate_target()
        label_b.target = MathTex(r"B\left(2|\frac{\pi}{5}\right)")
        label_b.target.scale(0.7)
        label_b.target.next_to(dot_B.target.get_center(), UP)
        label_b.target.set_color(RED)
        label_b.target.shift(0.2 * LEFT)
        label_a.generate_target()
        label_a.target = MathTex(r"A\left(1|\frac{\pi}{10}\right)")
        label_a.target.scale(0.7)
        label_a.target.set_color(RED)
        label_a.target.next_to(dot_A.target.get_center(), DOWN, buff=0.5 * LARGE_BUFF)

        delta_r = MathTex(r"{\rm d}r")
        delta_r.set_color(RED)
        delta_r.scale(0.7)
        delta_r.rotate(np.radians(18))
        delta_r.move_to(self.coords_to_point(1.5, 0.25))

        delta_p = MathTex(r"r{\rm d}\varphi")
        delta_p.set_color(RED)
        delta_p.scale(0.7)
        delta_p.rotate(-np.radians(72))
        delta_p.move_to(self.coords_to_point(2, 1))

        dot_C = Dot().move_to(self.coords_to_point(2 * np.cos(np.radians(18)), 2 * np.sin(np.radians(18))))
        line_r = Line(dot_A.target, dot_C)
        line_r.set_color(RED)
        dot_C.set_color(RED)

        r = self.coords_to_point(2, 0)[0] - self.coords_to_point(0, 0)[0]
        line_p = Arc(angle=TAU / 20, radius=r, arc_center=self.coords_to_point(0, 0), start_angle=TAU / 20)
        line_p.set_color(RED)

        ls = [r"\frac{\pi}{10}", r"\frac{\pi}{5}", r"\frac{3\pi}{10}", r"\frac{2\pi}{5}", r"\frac{\pi}{2}"]
        for i, l in enumerate(labels):
            l.generate_target()
            l.target = MathTex(ls[i])
            l.target.set_color(RED)
            l.target.scale(0.5)
            l.target.move_to(l.get_center())

        self.play(Create(dot_C), GrowFromCenter(line_p), GrowFromCenter(line_r), Write(delta_r), Write(delta_p),
                  MoveToTarget(label_a), MoveToTarget(label_b),
                  *[MoveToTarget(labels[_]) for _ in range(0, len(labels))])
        self.wait(2)

        pyt5 = MathTex(r"{\rm d} s^2", "=", r"{\rm d} r^2", "+", r"r^2{\rm d} \varphi^2")
        pyt5.next_to(pyt4, DOWN)
        pyt5.scale(0.7)
        pyt5[1].align_to(pyt5[1], LEFT)
        pyt5[0].next_to(pyt5[1], LEFT)
        pyt5[0].set_color(YELLOW)
        pyt5[2].next_to(pyt5[1], RIGHT)
        pyt5[2].set_color(RED)
        pyt5[4].set_color(RED)
        pyt5[3].next_to(pyt5[2], RIGHT)
        pyt5[4].next_to(pyt5[3], RIGHT)

        self.play(Write(pyt5))
        self.wait(2)

        pyt6 = MathTex(r"{\rm d} s^2", "=", r" \left(\begin{array}{c c} {\rm d} r & {\rm d}\varphi \end{array}\right)",
                       r"\left(\begin{array}{c c} 1 & 0 \\ 0 &r^2 \end{array}\right)",
                       r"\left(\begin{array}{c} {\rm d} r \\ {\rm d}\varphi \end{array}\right)")
        pyt6.scale(0.7)
        pyt6.next_to(pyt5, DOWN)
        pyt6[1].align_to(pyt5[1], LEFT)
        pyt6[0].next_to(pyt6[1], LEFT)
        pyt6[2].next_to(pyt6[1], RIGHT)
        pyt6[2].set_color(RED)
        pyt6[4].set_color(RED)
        pyt6[3].next_to(pyt6[2], RIGHT)
        pyt6[4].next_to(pyt6[3], RIGHT)
        pyt6[0].set_color(YELLOW)

        self.play(Write(pyt6))
        self.wait(2)

        self.wait(10)


class Symmetries(Scene):
    def construct(self):
        title = Tex("Coordinate transformations")
        title.to_edge(UP)
        title.set_color(YELLOW)
        self.play(Write(title))
        self.wait(3)

        y_min = 0
        y_max = 5
        x_min = 0
        x_max = 5
        graph_origin = np.array([-6, -3, 0])
        x_axis_width = 6
        y_axis_height = 6

        def coords_to_point(x, y):
            return graph_origin + np.array(
                (x_axis_width * (x - x_min) / (x_max - x_min), y_axis_height * (y - y_min) / (y_max - y_min), 0))

        x_axis = NumberLine(length=x_axis_width, include_ticks=True, include_tip=True, x_range=[x_min, x_max])
        x_axis.shift(graph_origin + x_axis.width / 2 * RIGHT)

        y_axis = NumberLine(length=y_axis_height, include_ticks=True, include_tip=True, x_range=[y_min, y_max],
                            rotation=TAU / 4)
        y_axis.shift(graph_origin + y_axis.height / 2 * UP)

        # setup coordinate system and grid
        self.add(x_axis, y_axis)
        grid = []
        for x in range(1, 6):
            line = Line(coords_to_point(x, 0), coords_to_point(x, 5))
            line.set_color(BLUE)
            line.set_style(stroke_width=0.75)
            grid.append(line)

        for y in range(1, 6):
            line = Line(coords_to_point(0, y), coords_to_point(5, y))
            line.set_color(BLUE)
            line.set_style(stroke_width=0.75)
            grid.append(line)

        self.add(*grid)

        dot_a = Dot().move_to(coords_to_point(0, 0))
        self.add(dot_a)
        dot_b = Dot().move_to(coords_to_point(4, 3))
        self.add(dot_b)

        decimal_b = DecimalNumber(4, num_decimals=2)
        decimal_b.scale(0.7)

        label_a = MathTex("A(", "0.00", "|0.00)")
        label_b = MathTex("B(", "4.00", "|", "3.00", ")")
        label_a.scale(0.7)
        label_b.scale(0.7)
        label_a.next_to(dot_a, DOWN, buff=SMALL_BUFF)
        label_a.shift(0.5 * RIGHT)
        label_b.next_to(dot_b, LEFT, buff=4 * SMALL_BUFF)

        decimal_a = DecimalNumber(0, num_decimals=2)
        decimal_a.scale(0.7)
        decimal_a.move_to(label_a[1])

        decimal_b1 = DecimalNumber(4, num_decimals=2)
        decimal_b1.scale(0.7)
        decimal_b1.move_to(label_b[1])

        decimal_b2 = DecimalNumber(3, num_decimals=2)
        decimal_b2.scale(0.7)
        decimal_b2.move_to(label_b[3])

        self.add(label_a, label_b)

        line = Line(dot_a.get_center(), dot_b.get_center())
        line.set_color(YELLOW)
        line.add_tip(at_start=True)
        line.add_tip()

        question = MathTex(r"\Delta s")
        question.scale(0.7)
        question.set_color(YELLOW)
        question.rotate(0.64, OUT)
        question.shift(coords_to_point(1.8, 1.65))

        self.add(question, line)

        dot_c = Dot().move_to(coords_to_point(4, 0))
        dot_c.set_color(BLUE)
        dot_c.scale(0.7)
        line_x = Line(dot_a.get_center(), dot_c.get_center())
        line_x.set_color(BLUE)
        delta_x = MathTex(r"\Delta x =4")
        delta_x.set_color(BLUE)
        delta_x.scale(0.7)
        delta_x.move_to(coords_to_point(2, -0.3))
        self.add(delta_x, line_x)

        line_y = Line(dot_c.get_center(), dot_b.get_center())
        line_y.set_color(BLUE)
        delta_y = MathTex(r"\Delta y =3")
        delta_y.set_color(BLUE)
        delta_y.scale(0.7)
        delta_y.rotate(3.141 / 2, OUT)
        delta_y.move_to(coords_to_point(4.3, 1.5))
        self.add(delta_y, line_y)

        pyt = MathTex(r"\Delta s^2 ", "=", r" \Delta x^2", "+", r"\Delta y^2")
        pyt[0].set_color(YELLOW)
        pyt[2].set_color(BLUE)
        pyt[4].set_color(BLUE)
        pyt2 = MathTex(r"\Delta s^2", "=", r" \left(\begin{array}{c c} \Delta x & \Delta y\end{array}\right)",
                       r"\left(\begin{array}{c c} 1 & 0 \\ 0 &1 \end{array}\right)",
                       r"\left(\begin{array}{c} \Delta x \\ \Delta y\end{array}\right)")
        pyt.scale(0.7)
        pyt2.scale(0.7)
        pyt.next_to(title, DOWN, buff=LARGE_BUFF)
        pyt.shift(2 * RIGHT)
        pyt2.next_to(pyt, DOWN)
        pyt2[1].align_to(pyt[1], LEFT)
        pyt2[0].next_to(pyt2[1], LEFT)
        pyt2[2].next_to(pyt2[1], RIGHT)
        pyt2[2].set_color(BLUE)
        pyt2[4].set_color(BLUE)
        pyt2[3].next_to(pyt2[2], RIGHT)
        pyt2[4].next_to(pyt2[3], RIGHT)
        pyt3 = MathTex(r"5.00^2", "=", "4.00","2", "+", "3.00","2")
        pyt3.scale(0.7)
        pyt3[3].scale(0.7)
        pyt3[6].scale(0.7)
        pyt3[0].set_color(YELLOW)
        pyt3.next_to(pyt2, DOWN)
        pyt3[1].align_to(pyt2[1], LEFT)
        pyt3[0].next_to(pyt3[1], LEFT)
        pyt3[2].next_to(pyt3[1], RIGHT)
        pyt3[3].next_to(pyt3[2], RIGHT,buff =0)
        pyt3[4].next_to(pyt3[3], RIGHT)
        pyt3[5].next_to(pyt3[4], RIGHT)
        pyt3[6].next_to(pyt3[5], RIGHT,buff = 0)
        pyt3[3].shift(0.15 * UP)
        pyt3[6].shift(0.15 * UP)
        pyt3[2].set_color(BLUE)
        pyt3[3].set_color(BLUE)
        pyt3[6].set_color(BLUE)
        pyt3[5].set_color(BLUE)

        self.add(pyt)
        self.add(pyt2)

        decimal_b11 = decimal_b1.copy()
        decimal_b11.move_to(pyt3[2])
        decimal_b11.set_color(BLUE)
        decimal_b21 = DecimalNumber(number = 3,num_decimal_places=2)
        decimal_b21.scale(0.7)
        decimal_b21.move_to(pyt3[5])
        decimal_b21.set_color(BLUE)

        self.wait(3)

        self.play(Write(pyt3), FadeOut(delta_x, delta_y))

        #replace string objects by DecimalNumbers
        self.add(decimal_a, decimal_b1, decimal_b2, decimal_b11, decimal_b21)
        self.play(FadeOut(label_a[1]), FadeOut(label_b[1]), FadeOut(label_b[3]),FadeOut(pyt3[2]),FadeOut(pyt3[5]))

        coord_grid = VGroup(x_axis, y_axis, *grid)

        # updater
        def shift_x_forth(mobject, dt):
            mobject.shift(dt * LEFT)

        def shift_x_back(mobject, dt):
            mobject.shift(-dt * LEFT)

        decimal_a.add_updater(lambda d, dt: d.increment_value(dt * (x_max - x_min) / x_axis_width))
        decimal_b1.add_updater(lambda d, dt: d.increment_value(dt * (x_max - x_min) / x_axis_width))
        coord_grid.add_updater(shift_x_forth)
        self.add(coord_grid)  # it's important to add object again, after adding an updater
        self.add(decimal_a,decimal_b1)
        self.wait(2)
        coord_grid.remove_updater(shift_x_forth)
        decimal_a.clear_updaters()
        decimal_b1.clear_updaters()

        decimal_a.add_updater(lambda d, dt: d.increment_value(-dt * (x_max - x_min) / x_axis_width))
        decimal_b1.add_updater(lambda d, dt: d.increment_value(-dt * (x_max - x_min) / x_axis_width))
        coord_grid.add_updater(shift_x_back)
        self.add(coord_grid)
        self.add(decimal_a)
        self.wait(2)
        label_a[0].shift(0.25 * LEFT)
        decimal_a.shift(0.25 * LEFT)
        self.wait(2)
        decimal_a.clear_updaters()
        decimal_b1.clear_updaters()
        coord_grid.remove_updater(shift_x_back)

        self.wait(2)

        decimal_a.add_updater(lambda d, dt: d.increment_value(dt * (x_max - x_min) / x_axis_width))
        decimal_b1.add_updater(lambda d, dt: d.increment_value(dt * (x_max - x_min) / x_axis_width))
        coord_grid.add_updater(shift_x_forth)
        self.add(coord_grid)  # it's important to add object again, after adding an updater
        self.add(decimal_a)
        self.wait(2)

        decimal_a.set_value(0)

        coord_grid.remove_updater(shift_x_forth)
        decimal_a.clear_updaters()
        decimal_b1.clear_updaters()
        label_a[0].shift(0.25 * RIGHT)
        decimal_a.shift(0.25 * RIGHT)

        self.wait(3)

        def get_line_x():
            line = Line(dot_a, dot_c)
            line.set_color(BLUE)
            return line

        def get_line_y():
            line = Line(dot_b, dot_c)
            line.set_color(BLUE)
            return line

        dyn_line_x = always_redraw(get_line_x)
        dyn_line_y = always_redraw(get_line_y)

        # rotations
        angle = DecimalNumber(0.6435)  # initial angle, auxiliary decimal to track the absolute value of rotation
        angle.add_updater(lambda d, dt: d.increment_value(0.2 * dt))
        angle.shift(10 * LEFT)  # make it invisible
        coord_grid.add_updater(lambda d, dt: d.rotate(angle=-0.2 * dt, axis=OUT, about_point=graph_origin))
        decimal_b1.add_updater(lambda d, dt: d.set_value(np.cos(angle.get_value()) * 5))
        decimal_b11.add_updater(lambda d, dt: d.set_value(np.cos(angle.get_value()) * 5))
        decimal_b2.add_updater(lambda d, dt: d.set_value(np.sin(angle.get_value()) * 5))
        decimal_b21.add_updater(lambda d, dt: d.set_value(np.sin(angle.get_value()) * 5))
        dot_c.add_updater(lambda d: d.move_to(
            coords_to_point(decimal_b1.get_value() * np.cos(0.6435 - angle.get_value()),
                            decimal_b1.get_value() * np.sin(0.6435 - angle.get_value()))))
        self.add(decimal_b1, decimal_b2,decimal_b11, decimal_b21, dot_c)
        self.add(dyn_line_x, dyn_line_y)
        self.remove(line_x, line_y)
        self.add(angle)
        self.add(coord_grid)
        self.wait(2)
        coord_grid.clear_updaters()
        decimal_b1.clear_updaters()
        decimal_b11.clear_updaters()
        decimal_b2.clear_updaters()
        decimal_b21.clear_updaters()
        dot_c.clear_updaters()
        angle.clear_updaters()

        angle.add_updater(lambda d, dt: d.increment_value(-0.2 * dt))
        decimal_b1.add_updater(lambda d, dt: d.set_value(np.cos(angle.get_value()) * 5))
        decimal_b11.add_updater(lambda d, dt: d.set_value(np.cos(angle.get_value()) * 5))
        decimal_b2.add_updater(lambda d, dt: d.set_value(np.sin(angle.get_value()) * 5))
        decimal_b21.add_updater(lambda d, dt: d.set_value(np.sin(angle.get_value()) * 5))
        dot_c.add_updater(lambda d: d.move_to(
            coords_to_point(decimal_b1.get_value() * np.cos(0.6435 - angle.get_value()),
                            decimal_b1.get_value() * np.sin(0.6435 - angle.get_value()))))

        self.add(decimal_b1, decimal_b2,decimal_b11, decimal_b21, dot_c)
        self.add(angle)
        coord_grid.add_updater(lambda d, dt: d.rotate(angle=0.2 * dt, axis=OUT, about_point=graph_origin))
        self.add(coord_grid)
        self.add(dyn_line_x, dyn_line_y)
        self.remove(line_x, line_y)
        self.wait(2)
        coord_grid.clear_updaters()
        decimal_b1.clear_updaters()
        decimal_b11.clear_updaters()
        decimal_b2.clear_updaters()
        decimal_b21.clear_updaters()
        dot_c.clear_updaters()
        angle.clear_updaters()

        self.wait(10)


class ThreeD(Scene):
    def construct(self):
        title = Tex("In three dimensions")
        title.to_edge(UP)
        title.set_color(YELLOW)
        self.play(Write(title))
        self.wait(3)

        line = MathTex(r"{\rm d}s^2","=",r"{\rm d}x^2+{\rm d}y^2+{\rm d}z^2={\rm d}x_1^2+{\rm d}x_2^2+{\rm d}x_3^2")
        line2 = MathTex(r"{\rm d}s^2","=",r"\left(\begin{array}{c c c} {\rm d}x_1 & {\rm d}x_2 & {\rm d}x_3 \end{array}\right)\left(\begin{array}{c c c} 1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & 1 \end{array}\right)\left(\begin{array}{c} {\rm d}x_1 \\ {\rm d}x_2 \\{\rm d}x_3 \end{array}\right)")

        line3 = MathTex(r"{\rm d}s^2","=",r"\sum_{m,n=1}^3 \delta_{mn}dx^m dx^n=\delta_{mn}dx^m dx^n")
        line2.scale(0.7)
        line3.set_color(YELLOW)
        line.next_to(title,DOWN)
        line2.next_to(line,DOWN)
        line2[1].align_to(line[1],LEFT)
        line2[0].next_to(line2[1],LEFT)
        line2[2].next_to(line2[1],RIGHT)
        line3.next_to(line2, DOWN)
        line3[1].align_to(line2[1], LEFT)
        line3[0].next_to(line3[1], LEFT)
        line3[2].next_to(line3[1], RIGHT)

        self.play(Write(line))
        self.wait(2)
        self.play(Write(line2))
        self.wait(2)
        self.play(Write(line3))
        self.wait(2)

        liste = BulletedList("applicable for all observers at rest","independent of their position", "independent of their orientation")
        liste.next_to(line3,DOWN)
        liste.set_color(YELLOW)

        for i in range(0,len(liste)):
            self.play(Write(liste[i]))
            self.wait(2)

        self.wait(10)


class FourD(Scene):
    def construct(self):
        title = Tex("In four dimensions --- special relativity")
        title.to_edge(UP)
        title.set_color(YELLOW)
        self.play(Write(title))
        self.wait(3)

        y_min = -6
        y_max = 6
        x_min = -6
        x_max = 6
        graph_origin = np.array([-6, -5, 0])
        x_axis_width = 8
        y_axis_height = 8

        def coords_to_point(x, y):
            return graph_origin + np.array(
                (x_axis_width * (x - x_min) / (x_max - x_min), y_axis_height * (y - y_min) / (y_max - y_min), 0))

        x_axis = NumberLine(length=x_axis_width, include_ticks=True, include_tip=True, x_range=[x_min, x_max])

        t_axis = NumberLine(length=y_axis_height, include_ticks=True, include_tip=True, x_range=[y_min, y_max],
                            rotation=TAU / 4)

        t_axis.shift(graph_origin + t_axis.height / 2 * UP+x_axis.width/2*RIGHT)
        x_axis.shift(graph_origin + x_axis.width / 2 * RIGHT + t_axis.height / 2 * UP)

        # setup coordinate system and grid
        self.add(x_axis, t_axis)
        grid_x = []
        grid_y = []

        label_x = MathTex("x")
        label_t = MathTex("t")
        label_t.scale(0.7)
        label_x.scale(0.7)
        label_x.move_to(x_axis.get_end()-0.5*RIGHT-0.5*UP)
        label_t.move_to(t_axis.get_end()+0.5*RIGHT-0.5*UP)

        self.play(Write(label_t))
        self.play(Write(label_x))

        self.wait(2)

        for x in range(-6, 7):
            line = Line(coords_to_point(x, y_min), coords_to_point(x, y_max))
            line.set_color(BLUE)
            line.set_style(stroke_width=0.75)
            grid_y.append(line)

        for y in range(-6, 7):
            line = Line(coords_to_point(x_min, y), coords_to_point(x_max, y))
            line.set_color(BLUE)
            line.set_style(stroke_width=0.75)
            grid_x.append(line)

        self.add(*grid_x,*grid_y)
        self.wait(2)

        line = Line(coords_to_point(0,0),coords_to_point(3,3))
        line.set_color(YELLOW)
        line.set_style(stroke_width=4)

        line2 = Line(coords_to_point(0, 0), coords_to_point(-3, 3))
        line2.set_color(YELLOW)
        line2.set_style(stroke_width=4)

        self.play(GrowFromPoint(line2,coords_to_point(0,0)),GrowFromPoint(line,coords_to_point(0,0)),run_time=3)

        dot_a = Dot().move_to(coords_to_point(-3, 3))
        dot_b = Dot().move_to(coords_to_point(3, 3))

        self.play(Create(dot_a), Create(dot_b))
        self.wait(2)

        label_a = MathTex("(","3.0","|","-3.0",")")
        label_b = MathTex("(","3.0","|","3.0",")")
        label_a.scale(0.7)
        label_b.scale(0.7)
        label_a.next_to(dot_a, UP, buff=SMALL_BUFF)
        label_a.shift(0.5 * RIGHT)
        label_b.next_to(dot_b, UP, buff=SMALL_BUFF)

        decimal_at = DecimalNumber(-3, num_decimal_places=1)
        decimal_ax = DecimalNumber(3, num_decimal_places=1)
        decimal_bx = DecimalNumber(3, num_decimal_places=1)
        decimal_bt = DecimalNumber(3, num_decimal_places=1)
        decimal_ax.scale(0.7)
        decimal_ax.move_to(label_a[1])
        decimal_at.scale(0.7)
        decimal_at.move_to(label_a[3])
        decimal_bx.scale(0.7)
        decimal_bx.move_to(label_b[1])
        decimal_bt.scale(0.7)
        decimal_bt.move_to(label_b[3])

        label_a = VGroup(label_a[0],decimal_ax,label_a[2],decimal_at,label_a[4])
        label_b = VGroup(label_b[0],decimal_bx,label_b[2],decimal_bt,label_b[4])

        self.play(Write(label_a),Write(label_b))
        self.wait(2)

        self.play(FadeOut(title))

          # updater
        def shift_grid_x(mobject, dt):
            center = mobject.get_center()
            zero = coords_to_point(0,0)
            center = center -zero
            angle = -1/(1+v.get_value()*v.get_value())*0.2*dt
            rot_mat = np.matrix([[np.cos(angle),-np.sin(angle),0],[np.sin(angle),np.cos(angle),0],[0,0,1]])
            rot_center = rot_mat.dot(center)
            s = rot_center-center
            mobject.shift(s)

        def shift_grid_y(mobject, dt):
            center = mobject.get_center()
            zero = coords_to_point(0,0)
            center = center -zero
            angle = 1/(1+v.get_value()*v.get_value())*0.2*dt
            rot_mat = np.matrix([[np.cos(angle),-np.sin(angle),0],[np.sin(angle),np.cos(angle),0],[0,0,1]])
            rot_center = rot_mat.dot(center)
            s = rot_center-center
            mobject.shift(s)

        # scale coordinate system

        def shift_scale(mobject, dt):
            center = mobject.get_center() - coords_to_point(0, 0)
            scaled_center = center * np.power(np.power(1.45774, 1 / 3), dt)
            s = scaled_center - center
            mobject.shift(s)

        # boost
        v = DecimalNumber(0)  # initial angle, auxiliary decimal to track the absolute value of rotation
        v.add_updater(lambda d, dt: d.increment_value(0.2 * dt))
        v.shift(10 * LEFT)  # make it invisible

        # boost axes
        x_axis.add_updater(
            lambda d, dt: d.rotate(angle=1 / (1 + v.get_value() * v.get_value()) * 0.2 * dt, axis=OUT,
                                   about_point=coords_to_point(0, 0)))
        t_axis.add_updater(
            lambda d, dt: d.rotate(angle=-1 / (1 + v.get_value() * v.get_value()) * 0.2 * dt, axis=OUT,
                                   about_point=coords_to_point(0, 0)))

        x_axis.add_updater(lambda d, dt: d.scale(np.power(np.power(1.45774, 1 / 3), dt)))
        t_axis.add_updater(lambda d, dt: d.scale(np.power(np.power(1.45774, 1 / 3), dt)))

        self.add(x_axis)
        self.add(t_axis)

        label_x.add_updater(lambda d,dt: d.move_to(x_axis.get_end() - 0.5 * RIGHT - 0.5 * UP))
        label_t.add_updater(lambda d,dt: d.move_to(t_axis.get_end() + 0.5 * RIGHT - 0.5 * UP))
        self.add(label_x)
        self.add(label_t)

        # some tweaking until the correct values are achieved

        decimal_bx.add_updater(lambda d, dt: d.increment_value(0.26*dt/np.sqrt(1-v.get_value()*v.get_value())*((-decimal_bt.get_value()+v.get_value()*d.get_value())/(1-v.get_value()*v.get_value()))))
        decimal_bt.add_updater(lambda d, dt: d.set_value(decimal_bx.get_value()))
        self.add(decimal_bx)
        self.add(decimal_bt)

        decimal_at.add_updater(lambda d, dt: d.increment_value(0.26*dt/np.sqrt(1-v.get_value()*v.get_value())*((-decimal_ax.get_value()+v.get_value()*d.get_value())/(1-v.get_value()*v.get_value()))))
        decimal_ax.add_updater(lambda d, dt: d.set_value(-decimal_at.get_value()))
        self.add(decimal_ax)
        self.add(decimal_at)

        # boost grid lines

        for grid in grid_x:
            grid.add_updater(shift_grid_x)
            grid.add_updater(shift_scale)
            grid.add_updater(lambda d, dt: d.scale(np.power(np.power(1.45774, 1 / 3), dt)))
            grid.add_updater(lambda d ,dt: d.rotate(angle=1/(1+v.get_value()*v.get_value()) * 0.2*dt,axis=OUT, about_point=d.get_center()))
            self.add(grid)

        for grid in grid_y:
            grid.add_updater(shift_grid_y)
            grid.add_updater(shift_scale)
            grid.add_updater(lambda d, dt: d.scale(np.power(np.power(1.45774, 1 / 3), dt)))
            grid.add_updater(lambda d ,dt: d.rotate(angle=-1/(1+v.get_value()*v.get_value()) * 0.2*dt,axis=OUT, about_point=d.get_center()))
            self.add(grid)

        # some tweaking until the correct values are achieved

        self.wait(2.7)

        x_axis.clear_updaters()
        t_axis.clear_updaters()
        for grid in grid_x:
            grid.clear_updaters()
        for grid in grid_y:
            grid.clear_updaters()
        label_x.clear_updaters()
        label_t.clear_updaters()
        decimal_ax.clear_updaters()
        decimal_at.clear_updaters()
        decimal_bx.clear_updaters()
        decimal_bt.clear_updaters()

        self.wait(2)

        pyt = MathTex(r"{\rm d} s^2 ", "=", r" -{\rm d} t^2", "+", r"{\rm d} x^2","+",r"{\rm d} y^2","+",r"{\rm d} z^2")
        pyt[0].set_color(YELLOW)
        pyt[2].set_color(BLUE)
        pyt[4].set_color(BLUE)
        pyt[6].set_color(BLUE)
        pyt[8].set_color(BLUE)

        pyt.to_corner(DR)

       # self.play(Write(pyt[0:5]))
        self.wait(2)
       # self.play(Write(pyt[5:9]))
        self.wait(2)

        self.play(FadeOut(line),FadeOut(line2))
        self.wait()

        line.set_color(RED)

        line2a = Line(coords_to_point(0,0),coords_to_point(-0.75,0.75))
        line2b = Line(coords_to_point(-0.75,0.75),coords_to_point(-3,3))
        line2a.set_color(BLUE)
        line2b.set_color(BLUE)

        self.play(GrowFromPoint(line2a,coords_to_point(0,0)),GrowFromPoint(line,coords_to_point(0,0)),run_time=1.5,rate_func=linear)
        self.play(GrowFromPoint(line2b,coords_to_point(-0.75,0.75)),run_time=4.5,rate_func=linear)

        self.wait(2)
        self.wait(10)


class FourD2(Scene):
    def construct(self):
        title = Tex("In four dimensions --- special relativity")
        title.to_edge(UP)
        title.set_color(YELLOW)
        self.play(Write(title))
        self.wait(3)

        y_min = -6
        y_max = 6
        x_min = -6
        x_max = 6
        graph_origin = np.array([-6, -5, 0])
        x_axis_width = 8
        y_axis_height = 8

        def coords_to_point(x, y):
            return graph_origin + np.array(
                (x_axis_width * (x - x_min) / (x_max - x_min), y_axis_height * (y - y_min) / (y_max - y_min), 0))

        x_axis = NumberLine(length=x_axis_width, include_ticks=True, include_tip=True, x_range=[x_min, x_max])

        t_axis = NumberLine(length=y_axis_height, include_ticks=True, include_tip=True, x_range=[y_min, y_max],
                            rotation=TAU / 4)

        t_axis.shift(graph_origin + t_axis.height / 2 * UP+x_axis.width/2*RIGHT)
        x_axis.shift(graph_origin + x_axis.width / 2 * RIGHT + t_axis.height / 2 * UP)

        # setup coordinate system and grid
        self.add(x_axis, t_axis)
        grid_x = []
        grid_y = []

        label_x = MathTex("x")
        label_t = MathTex("t")
        label_t.scale(0.7)
        label_x.scale(0.7)
        label_x.move_to(x_axis.get_end()-0.5*RIGHT-0.5*UP)
        label_t.move_to(t_axis.get_end()+0.5*RIGHT-0.5*UP)

        self.play(Write(label_t))
        self.play(Write(label_x))

        self.wait(2)

        for x in range(-6, 7):
            line = Line(coords_to_point(x, y_min), coords_to_point(x, y_max))
            line.set_color(BLUE)
            line.set_style(stroke_width=0.75)
            grid_y.append(line)

        for y in range(-6, 7):
            line = Line(coords_to_point(x_min, y), coords_to_point(x_max, y))
            line.set_color(BLUE)
            line.set_style(stroke_width=0.75)
            grid_x.append(line)

        self.add(*grid_x,*grid_y)
        self.wait(2)

        line = Line(coords_to_point(0,0),coords_to_point(3,3))
        line.set_color(YELLOW)
        line.set_style(stroke_width=4)

        line2 = Line(coords_to_point(0, 0), coords_to_point(-3, 3))
        line2.set_color(YELLOW)
        line2.set_style(stroke_width=4)

        self.play(GrowFromPoint(line2,coords_to_point(0,0)),GrowFromPoint(line,coords_to_point(0,0)),run_time=3)

        dot_a = Dot().move_to(coords_to_point(-3, 3))
        dot_b = Dot().move_to(coords_to_point(3, 3))

        self.play(Create(dot_a), Create(dot_b))
        self.wait(2)

        label_a = MathTex("(","3.0","|","-3.0",")")
        label_b = MathTex("(","3.0","|","3.0",")")
        label_a.scale(0.7)
        label_b.scale(0.7)
        label_a.next_to(dot_a, UP, buff=SMALL_BUFF)
        label_a.shift(0.5 * RIGHT)
        label_b.next_to(dot_b, UP, buff=SMALL_BUFF)

        decimal_ax = DecimalNumber(3, num_decimal_places=1)
        decimal_at = DecimalNumber(-3, num_decimal_places=1)
        decimal_bx = DecimalNumber(3, num_decimal_places=1)
        decimal_bt = DecimalNumber(3, num_decimal_places=1)
        decimal_ax.scale(0.7)
        decimal_ax.move_to(label_a[1])
        decimal_at.scale(0.7)
        decimal_at.move_to(label_a[3])
        decimal_bx.scale(0.7)
        decimal_bx.move_to(label_b[1])
        decimal_bt.scale(0.7)
        decimal_bt.move_to(label_b[3])

        label_a = VGroup(label_a[0],decimal_ax,label_a[2],decimal_at,label_a[4])
        label_b = VGroup(label_b[0],decimal_bx,label_b[2],decimal_bt,label_b[4])

        self.play(Write(label_a),Write(label_b))
        self.wait(2)

        self.play(FadeOut(title))

          # updater
        def shift_grid_x(mobject, dt):
            center = mobject.get_center()
            zero = coords_to_point(0,0)
            center = center -zero
            angle = -1/(1+v.get_value()*v.get_value())*0.2*dt
            rot_mat = np.matrix([[np.cos(angle),-np.sin(angle),0],[np.sin(angle),np.cos(angle),0],[0,0,1]])
            rot_center = rot_mat.dot(center)
            s = rot_center-center
            mobject.shift(s)

        def shift_grid_y(mobject, dt):
            center = mobject.get_center()
            zero = coords_to_point(0,0)
            center = center -zero
            angle = 1/(1+v.get_value()*v.get_value())*0.2*dt
            rot_mat = np.matrix([[np.cos(angle),-np.sin(angle),0],[np.sin(angle),np.cos(angle),0],[0,0,1]])
            rot_center = rot_mat.dot(center)
            s = rot_center-center
            mobject.shift(s)

        # scale coordinate system

        def shift_scale(mobject, dt):
            center = mobject.get_center() - coords_to_point(0, 0)
            scaled_center = center * np.power(np.power(1.45774, 1 / 3), dt)
            s = scaled_center - center
            mobject.shift(s)

        # boost
        v = DecimalNumber(0)  # initial angle, auxiliary decimal to track the absolute value of rotation
        v.add_updater(lambda d, dt: d.increment_value(0.2 * dt))
        v.shift(10 * LEFT)  # make it invisible

        # boost axes
        x_axis.add_updater(
            lambda d, dt: d.rotate(angle=1 / (1 + v.get_value() * v.get_value()) * 0.2 * dt, axis=OUT,
                                   about_point=coords_to_point(0, 0)))
        t_axis.add_updater(
            lambda d, dt: d.rotate(angle=-1 / (1 + v.get_value() * v.get_value()) * 0.2 * dt, axis=OUT,
                                   about_point=coords_to_point(0, 0)))

        x_axis.add_updater(lambda d, dt: d.scale(np.power(np.power(1.45774, 1 / 3), dt)))
        t_axis.add_updater(lambda d, dt: d.scale(np.power(np.power(1.45774, 1 / 3), dt)))

        self.add(x_axis)
        self.add(t_axis)

        label_x.add_updater(lambda d,dt: d.move_to(x_axis.get_end() - 0.5 * RIGHT - 0.5 * UP))
        label_t.add_updater(lambda d,dt: d.move_to(t_axis.get_end() + 0.5 * RIGHT - 0.5 * UP))
        self.add(label_x)
        self.add(label_t)

        # some tweaking until the correct values are achieved

        decimal_bx.add_updater(lambda d, dt: d.increment_value(0.26*dt/np.sqrt(1-v.get_value()*v.get_value())*((-decimal_bt.get_value()+v.get_value()*d.get_value())/(1-v.get_value()*v.get_value()))))
        decimal_bt.add_updater(lambda d, dt: d.set_value(decimal_bx.get_value()))
        self.add(decimal_bx)
        self.add(decimal_bt)

        decimal_at.add_updater(lambda d, dt: d.increment_value(0.26*dt/np.sqrt(1-v.get_value()*v.get_value())*((-decimal_ax.get_value()+v.get_value()*d.get_value())/(1-v.get_value()*v.get_value()))))
        decimal_ax.add_updater(lambda d, dt: d.set_value(-decimal_at.get_value()))
        self.add(decimal_ax)
        self.add(decimal_at)

        # boost grid lines

        for grid in grid_x:
            grid.add_updater(shift_grid_x)
            grid.add_updater(shift_scale)
            grid.add_updater(lambda d, dt: d.scale(np.power(np.power(1.45774, 1 / 3), dt)))
            grid.add_updater(lambda d ,dt: d.rotate(angle=1/(1+v.get_value()*v.get_value()) * 0.2*dt,axis=OUT, about_point=d.get_center()))
            self.add(grid)

        for grid in grid_y:
            grid.add_updater(shift_grid_y)
            grid.add_updater(shift_scale)
            grid.add_updater(lambda d, dt: d.scale(np.power(np.power(1.45774, 1 / 3), dt)))
            grid.add_updater(lambda d ,dt: d.rotate(angle=-1/(1+v.get_value()*v.get_value()) * 0.2*dt,axis=OUT, about_point=d.get_center()))
            self.add(grid)

        # some tweaking until the correct values are achieved

        self.wait(2.7)

        x_axis.clear_updaters()
        t_axis.clear_updaters()
        for grid in grid_x:
            grid.clear_updaters()
        for grid in grid_y:
            grid.clear_updaters()
        label_x.clear_updaters()
        label_t.clear_updaters()
        decimal_ax.clear_updaters()
        decimal_at.clear_updaters()
        decimal_bx.clear_updaters()
        decimal_bt.clear_updaters()

        self.wait(2)

        title = Tex("Minkowski metric")
        title.to_edge(RIGHT)
        title.shift(-2*UP)
        title.set_color(YELLOW)
        self.play(Write(title))
        self.wait(3)

        pyt = MathTex(r"{\rm d} s^2 ", "=", r" -{\rm d} t^2", "+", r"{\rm d} x^2","+",r"{\rm d} y^2","+",r"{\rm d} z^2")
        pyt[0].set_color(YELLOW)
        pyt[2].set_color(BLUE)
        pyt[4].set_color(BLUE)
        pyt[6].set_color(BLUE)
        pyt[8].set_color(BLUE)

        pyt.to_corner(DR)

        self.play(Write(pyt[0:5]))
        self.wait(2)
        self.play(Write(pyt[5:9]))
        self.wait(2)

        self.play(FadeOut(line),FadeOut(line2))
        self.wait()

        line.set_color(RED)

        line2a = Line(coords_to_point(0,0),coords_to_point(-0.75,0.75))
        line2b = Line(coords_to_point(-0.75,0.75),coords_to_point(-3,3))
        line2a.set_color(BLUE)
        line2b.set_color(BLUE)

        self.play(GrowFromPoint(line2a,coords_to_point(0,0)),GrowFromPoint(line,coords_to_point(0,0)),run_time=1.5,rate_func=linear)
        self.play(GrowFromPoint(line2b,coords_to_point(-0.75,0.75)),run_time=4.5,rate_func=linear)

        self.wait(2)
        self.wait(10)


class FRW(Scene):
    def construct(self):
        title = Tex("The metric of an expanding universe")
        title.to_edge(UP)
        title.set_color(YELLOW)
        self.play(Write(title))
        self.wait(3)

        metric = MathTex(r"{\rm d}s^2 = -{\rm d}t^2 +a(t)^2 \left({\rm d} x^2+{\rm d} y^2+{\rm d}z^2\right)")
        metric.set_color(BLUE)
        metric.to_edge(LEFT,buff=LARGE_BUFF)
        metric.shift(2*UP)

        self.play(Write(metric))
        self.wait(2)

        label = MathTex("a(t) = ","1.00")
        label.set_color(BLUE)
        label.to_edge(RIGHT,buff=LARGE_BUFF)
        label.shift(2*UP)

        number = DecimalNumber(1, 2)
        number.set_color(BLUE)
        number.move_to(label[1])

        self.play(Write(label[0]))
        self.play(Write(number))
        self.wait(2)

        number.add_updater(lambda d, dt: d.increment_value(0.1*dt))
        self.add(number)
        self.wait(15)
        number.clear_updaters()

        number.add_updater(lambda d, dt: d.increment_value(-0.16 * dt))
        self.add(number)
        self.wait(15)
        number.clear_updaters()

        self.wait(10)


class Christoffel(Scene):
    def construct(self):
        title = Tex("Christoffel symbols")
        title.to_edge(UP)
        title.set_color(RED)
        self.play(Write(title))
        self.wait(3)

        definition=MathTex(r"\Gamma^{\kappa}_{\mu\nu}=\frac{1}{2} g^{\kappa\lambda}\left(g_{\mu\lambda,\nu}+g_{\nu\lambda,\mu}-g_{\mu\nu,\lambda}\right)")
        definition.shift(2*UP)
        self.play(Write(definition))
        self.wait(2)

        nonzero = [MathTex(r"\Gamma^{x}_{tx}=\Gamma^{y}_{ty}=\Gamma^{z}_{tz}=\frac{\dot a}{a}"),
                   MathTex(r"\Gamma^{x}_{xt}=\Gamma^{y}_{yt}=\Gamma^{z}_{zt}=\frac{\dot a}{a}"),
                   MathTex(r"\Gamma^{t}_{xx}=\Gamma^{t}_{yy}=\Gamma^{t}_{yy}=\dot a a")]

        nonzero[0].next_to(definition,DOWN)
        nonzero[0].align_to(definition,LEFT)

        for i in range(1,3):
            nonzero[i].next_to(nonzero[i-1], DOWN)
            nonzero[i].align_to(nonzero[i-1], LEFT)

        self.play(*[Write(nonzero[i]) for i in range(0,3)])

        self.wait(2)

        self.wait(10)


class Ricci(Scene):
    def construct(self):
        title = Tex("Ricci tensor")
        title.to_edge(UP)
        title.set_color(GREEN)
        self.play(Write(title))
        self.wait(3)

        definition=MathTex(r"R_{\mu\nu}=\Gamma^\lambda_{\mu\nu,\lambda}-\Gamma^\lambda_{\mu\lambda,\nu}+\Gamma^\lambda_{\kappa\lambda}\Gamma^\kappa_{\mu\nu}-\Gamma^\lambda_{\kappa\nu}\Gamma^\kappa_{\mu\lambda}")
        definition.shift(2*UP)
        self.play(Write(definition))
        self.wait(2)

        sphere=MathTex(r"R^\mu_{\,\,\nu}=\left(\begin{array}{c  c} \tfrac{1}{r^2} & 0\\ 0 & \tfrac{1}{r^2}\end{array}\right)")
        sphere.to_edge(LEFT,buff=LARGE_BUFF)
        sphere.set_color(BLUE)


        self.play(Write(sphere))
        self.wait(2)

        nonzero = [
                    MathTex(r"R_{tt}=-3\frac{\ddot a}{a}"),
                    MathTex(r"R_{xx}=R_{yy}=R_{zz}=2\dot a^2+a \ddot a"),
                ]


        nonzero[0].next_to(definition,DOWN)
        nonzero[0].align_to(definition,LEFT)
        nonzero[0].shift(3*DOWN)

        for i in range(1,len(nonzero)):
            nonzero[i].next_to(nonzero[i-1], DOWN)
            nonzero[i].align_to(nonzero[i-1], LEFT)

        self.play(*[Write(nonzero[i]) for i in range(0,len(nonzero))])

        self.wait(2)

        self.wait(10)



class Einstein(Scene):
    def construct(self):
        title = Tex("Einstein tensor")
        title.to_corner(UL)
        title.set_color(BLUE)
        self.play(Write(title))
        self.wait(3)

        definition=MathTex(r"G_{\mu\nu}=R_{\mu\nu}-\tfrac{1}{2} R g_{\mu\nu}")
        definition.next_to(title,DOWN)
        definition.align_to(title,LEFT)
        self.play(Write(definition))
        self.wait(2)


        nonzero = [
                    MathTex(r"G_{tt}=",r"3\left(\frac{\dot a}{a}\right)^2"),
                    MathTex(r"G_{xx}=G_{yy}=G_{zz}=-\dot a^2-2a \ddot a"),
                ]

        nonzero[0].next_to(definition,DOWN)
        nonzero[0].align_to(definition,LEFT)

        for i in range(1,len(nonzero)):
            nonzero[i].next_to(nonzero[i-1], DOWN)
            nonzero[i].align_to(nonzero[i-1], LEFT)

        self.play(*[Write(nonzero[i]) for i in range(0,len(nonzero))])

        self.wait(2)

        title = Tex("Energy-momentum tensor")
        title.to_corner(UR)
        title.set_color(PURPLE)
        self.play(Write(title))
        self.wait(3)

        definition = Tex(r"perfect fluid approximation")
        definition.next_to(title, DOWN)
        definition.align_to(title, LEFT)

        self.play(Write(definition))
        self.wait(2)

        nonzero2 = [
            MathTex(r"T_{tt}=",r"\rho"),
            MathTex(r"T_{xx}=T_{yy}=T_{zz}=p"),
        ]

        nonzero2[0].next_to(definition, DOWN,buff=LARGE_BUFF)
        nonzero2[0].align_to(definition, LEFT)

        for i in range(1, len(nonzero2)):
            nonzero2[i].next_to(nonzero2[i - 1], DOWN,buff=0.5*LARGE_BUFF)
            nonzero2[i].align_to(nonzero2[i - 1], LEFT)

        self.play(*[Write(nonzero2[i]) for i in range(0, len(nonzero2))])

        self.wait(2)

        title = Tex("Friedmann equation")
        title.set_color(YELLOW)
        title.shift(DOWN)
        self.play(Write(title))
        self.wait(2);

        eq1 = MathTex(r"G_{\mu\nu}=8\pi G \cdot T_{\mu\nu}")
        eq2 = MathTex(r"3\left(\frac{\dot a}{a}\right)^2 ","=",r"8\pi G","\cdot",r"\rho")
        eq2[0].set_color(YELLOW)
        eq2[4].set_color(YELLOW)

        eq1.next_to(title,DOWN)
        eq2.next_to(eq1,DOWN)
        eq2.align_to(eq1,LEFT)
        eq2.shift(0.8*LEFT)

        self.play(Write(eq1))
        self.play(TransformFromCopy(nonzero[0][1],eq2[0]))
        self.play(Write(eq2[1]))
        self.play(Write(eq2[2]))
        self.play(Write(eq2[3]))
        self.play(TransformFromCopy(nonzero2[0][1],eq2[4]))
        self.wait(2)

        self.wait(10)


class Dedication(Scene):
    def construct(self):
        title = Tex("in memoriam")
        title.to_edge(DOWN,buff=LARGE_BUFF)

        self.play(Write(title))
        self.wait(2)

        kofman = Tex("Lev Kofman (17.06.1957 - 12.11.2009) ")
        kofman.scale(0.7)
        kofman.to_corner(DL)

        self.play(GrowFromCenter(kofman))

        stephani = Tex("Hans Stephani (20.01.1935 - 14.09.2003) ")
        stephani.scale(0.7)
        stephani.to_corner(DR)

        self.play(GrowFromCenter(stephani))

        self.wait(10)
