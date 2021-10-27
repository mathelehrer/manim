from abc import ABC

import numpy as np
from manim import *
from typing import Iterable


class Discs(Scene):
    def construct(self):
        title = Tex("Colorful discs")
        title.to_edge(UP)
        title.set_color(YELLOW)
        self.play(Write(title))
        self.wait()

        ax = Axes(
            x_range=[-1.5, 1.5],
            y_range=[-1.5, 1.5],
            x_length=4.5,
            y_length=4.5,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-1, 1.1, 1),
                "color": GREEN
            },
            y_axis_config={
                "numbers_to_include": np.arange(-1, 1.1, 1),
                "color": GREEN
            },
            tips=False,
        )
        labels = ax.get_axis_labels(x_label="x", y_label="y")
        labels[0].shift(0.4 * DOWN)
        labels[1].shift(0.4 * LEFT)
        labels.set_color(GREEN)
        ax.add(labels)
        ax.set_color(GREEN)

        origin = ax.coords_to_point(0, 0)
        screen = Square(4.5)
        screen.move_to(origin)
        self.play(GrowFromPoint(screen, ax.coords_to_point(-3.5, -3.5)))

        lines = []
        for row in range(0, 3):
            start = ax.coords_to_point(-1.5, -1.5 + row)
            end = ax.coords_to_point(1.5, -1.5 + row)
            line = Line(start, end)
            line.set_color(GRAY)
            line.set_style(stroke_opacity=0.7)
            lines.append(line)
        for col in range(0, 3):
            start = ax.coords_to_point(-1.5 + col, -1.5)
            end = ax.coords_to_point(-1.5 + col, 1.5)
            line = Line(start, end)
            line.set_color(GRAY)
            line.set_style(stroke_opacity=0.7)
            lines.append(line)

        self.play(*[Create(lines[line]) for line in range(0, len(lines))])
        self.wait(2)

        circle = Circle(2.25)
        circle.set_color(YELLOW)
        circle.move_to(origin)
        self.play(GrowFromCenter(circle))

        self.wait(2)

        self.play(Create(ax))
        self.wait()

        dots = []
        labels = []
        arrows = []
        squares = []
        for row in range(0, 3):
            for col in range(0, 3):
                y = 1 - row
                x = -1 + col
                text = "(%s|%s)" % (str(x), str(y))
                label = MathTex(text)
                label.scale(0.8)
                arrow = MathTex(r"\rightarrow")
                square = Square(4.5 / 9)
                if x * x + y * y <= 1:
                    square.set_style(fill_color=YELLOW, fill_opacity=0.8)
                else:
                    square.set_style(fill_color=WHITE, fill_opacity=0.8)
                pos = ax.coords_to_point(x, y)
                square.move_to(pos)
                dot = Dot(pos)
                dots.append(dot)
                labels.append(label)
                squares.append(square)
                arrows.append(arrow)

        prev = Tex("(x|y)")
        prev.set_color(GREEN)
        prev.to_corner(UR)
        prev.shift(2 * LEFT + 0.5 * DOWN)
        self.play(Write(prev))

        for dot, label in zip(dots, labels):
            label.next_to(prev, DOWN)
            label.align_to(prev, RIGHT)
            prev = label
            self.play(Create(dot), Write(label))

        self.wait(2)

        first = True
        prev_arrow = arrows[0]
        prev_square = squares[0]
        for dot, label, arrow, square in zip(dots, labels, arrows, squares):
            if first:
                first = False
                arrow.next_to(label, RIGHT)
                square.next_to(arrow, RIGHT)
            else:
                arrow.next_to(label, RIGHT)
                square.next_to(arrow, RIGHT)
                arrow.align_to(prev_arrow, LEFT)
                square.align_to(prev_square, LEFT)
                prev_square = square
                prev_arrow = arrow

            square_copy = square.copy()
            square_copy.scale(3)
            square_copy.move_to(dot)
            self.play(Write(arrow), Create(square))
            self.play(TransformFromCopy(dot, square_copy))

        self.wait(2)

        prev = MathTex(r"x^2+y^2 \le 1")
        prev.set_color(YELLOW)
        prev.to_corner(UL)
        prev.shift(1 * RIGHT + 0.5 * DOWN)
        self.play(Write(prev))
        prev = prev.copy()
        prev.shift(1 * LEFT)

        new_labels = []
        for label in labels:
            label = label.copy()
            new_labels.append(label)
            label.next_to(prev, DOWN)
            label.align_to(prev, RIGHT)
            prev = label
            self.play(Write(label))

        self.wait(2)

        values = [2, 1, 2, 1, 0, 1, 2, 1, 2]
        for (label, arrow, value) in zip(new_labels, arrows, values):
            arrow = arrow.copy()
            arrow.next_to(label, RIGHT)
            val = Tex(value)
            val.scale(0.8)
            if value <= 1:
                val.set_color(YELLOW)
            else:
                val.set_color(WHITE)
            val.next_to(arrow, RIGHT)
            self.play(Write(arrow), Write(val))

        self.wait(10)


class Discs2(Scene):
    def construct(self):
        title = Tex("Colorful discs")
        title.to_edge(UP)
        title.set_color(YELLOW)
        self.add(title)
        self.wait()

        ax = Axes(
            x_range=[-3.5, 3.5],
            y_range=[-3.5, 3.5],
            x_length=4.5,
            y_length=4.5,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-3, 3.1, 1),
                "color": GREEN
            },
            y_axis_config={
                "numbers_to_include": np.arange(-3, 3.1, 1),
                "color": GREEN
            },
            tips=False,
        )
        labels = ax.get_axis_labels(x_label="x", y_label="y")
        labels[0].shift(0.4 * DOWN)
        labels[1].shift(0.4 * LEFT)
        labels.set_color(GREEN)
        ax.add(labels)
        ax.set_color(GREEN)

        origin = ax.coords_to_point(0, 0)
        screen = Square(4.5)
        screen.move_to(origin)
        self.play(GrowFromPoint(screen, ax.coords_to_point(-1.5, -1.5)))

        lines = []
        for row in range(0, 7):
            start = ax.coords_to_point(-3.5, -3.5 + row)
            end = ax.coords_to_point(3.5, -3.5 + row)
            line = Line(start, end)
            line.set_color(GRAY)
            line.set_style(stroke_opacity=0.7)
            lines.append(line)
        for col in range(0, 7):
            start = ax.coords_to_point(-3.5 + col, -3.5)
            end = ax.coords_to_point(-3.5 + col, 3.5)
            line = Line(start, end)
            line.set_color(GRAY)
            line.set_style(stroke_opacity=0.7)
            lines.append(line)

        self.play(*[Create(lines[line]) for line in range(0, len(lines))])
        self.wait(2)

        circle = Circle(2.25)
        circle.set_color(YELLOW)
        circle.move_to(origin)
        self.play(GrowFromCenter(circle))

        self.wait(2)

        self.play(Create(ax))
        self.wait()

        header = MathTex(r"x^2+y^2 \le 3^2")
        header.set_color(YELLOW)
        header.to_corner(UL)
        header.shift(RIGHT + 0.5 * DOWN)
        self.play(Write(header))

        first = True
        last_label = Tex("")
        last_arrow = Tex("")
        last_val = Tex("")
        for row in range(0, 7):
            for col in range(0, 7):

                y = 3 - row
                x = -3 + col
                text = "(" + str(x) + "|" + str(y) + ")"
                print(text)
                value = x * x + y * y
                label = MathTex(text)
                label.scale(0.8)
                arrow = MathTex(r"\rightarrow")
                val = MathTex(str(value))
                val.scale(0.8)
                square = Square(4.5 / 7)
                if x * x + y * y <= 9:
                    square.set_style(fill_color=YELLOW, fill_opacity=0.8)
                    val.set_color(YELLOW)
                else:
                    square.set_style(fill_color=WHITE, fill_opacity=0.8)

                pos = ax.coords_to_point(x, y)
                square.move_to(pos)
                if not first:
                    self.remove(last_val, last_arrow, last_label)

                label.next_to(header, DOWN)
                label.align_to(header, RIGHT)
                label.shift(1.4 * LEFT)
                arrow.next_to(label, RIGHT)
                val.next_to(arrow, RIGHT)
                self.play(Write(label), Write(arrow), Write(val), Create(square))
                last_label = label
                last_arrow = last_arrow
                last_val = val
                first = False

        self.wait(2)

        self.wait(10)


class Discs3(Scene):
    def construct(self):
        title = Tex("Colorful discs")
        title.to_edge(UP)
        title.set_color(YELLOW)
        self.add(title)
        self.wait()

        ax = Axes(
            x_range=[-10, 10],
            y_range=[-10, 10],
            x_length=4.5,
            y_length=4.5,
            axis_config={"color": YELLOW},
            x_axis_config={
                "numbers_to_include": np.arange(-3, 3.1, 1),
                "color": YELLOW
            },
            y_axis_config={
                "numbers_to_include": np.arange(-3, 3.1, 1),
                "color": YELLOW
            },
        )

        origin = ax.coords_to_point(0, 0)
        screen = Square(4.5)
        screen.move_to(origin)
        self.play(GrowFromPoint(screen, ax.coords_to_point(-10, -10)))

        lines = []
        for row in range(0, 21):
            start = ax.coords_to_point(-10, -10 + row)
            end = ax.coords_to_point(10, -10 + row)
            line = Line(start, end)
            line.set_color(GRAY)
            line.set_style(stroke_opacity=0.7, stroke_width=1)
            lines.append(line)
        for col in range(0, 21):
            start = ax.coords_to_point(-10 + col, -10)
            end = ax.coords_to_point(-10 + col, 10)
            line = Line(start, end)
            line.set_color(GRAY)
            line.set_style(stroke_opacity=0.7, stroke_width=1)
            lines.append(line)

        self.play(*[Create(lines[line]) for line in range(0, len(lines))])
        self.wait(2)

        circle = Circle(2.25)
        circle.set_color(YELLOW)
        circle.move_to(origin)
        self.play(GrowFromCenter(circle))

        self.wait(2)

        for row in range(0, 20):
            for col in range(0, 20):

                y = 9.5 - row
                x = -9.5 + col
                square = Square(4.5 / 20)
                if x * x + y * y <= 100:
                    square.set_style(fill_color=YELLOW, stroke_color=YELLOW, fill_opacity=0.8)
                else:
                    square.set_style(fill_color=WHITE, stroke_color=WHITE, fill_opacity=0.8)

                pos = ax.coords_to_point(x, y)
                square.move_to(pos)
                self.play(Create(square), run_time=0.01)

        self.wait(2)

        self.wait(10)


class Discs4(Scene):
    def construct(self):
        title = Tex("Colorful discs")
        title.to_edge(UP)
        title.set_color(YELLOW)
        self.add(title)
        self.wait()

        ax = Axes(
            x_range=[-10, 10],
            y_range=[-10, 10],
            x_length=4.5,
            y_length=4.5,
            axis_config={"color": YELLOW},
            x_axis_config={
                "numbers_to_include": np.arange(-3, 3.1, 1),
                "color": YELLOW
            },
            y_axis_config={
                "numbers_to_include": np.arange(-3, 3.1, 1),
                "color": YELLOW
            },
            tips=False,
        )
        ax.shift(3 * RIGHT)

        origin = ax.coords_to_point(0, 0)

        ax2 = Axes(
            x_range=[-10, 11],
            y_range=[0., 1.2],
            x_length=6,
            y_length=3,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.1, 5),
                "color": GREEN,
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 1.1, 0.2),
                "color": GREEN,
                "decimal_number_config": {
                    "num_decimal_places": 1,
                }
            },
            tips=True,
        )
        ax2.shift(3 * LEFT)

        origin = ax.coords_to_point(0, 0)
        screen = Square(4.5)
        screen.move_to(origin)
        self.play(GrowFromPoint(screen, ax.coords_to_point(-10, -10)))
        ax2.align_to(screen, DOWN)

        lines = []
        for row in range(0, 21):
            start = ax.coords_to_point(-10, -10 + row)
            end = ax.coords_to_point(10, -10 + row)
            line = Line(start, end)
            line.set_color(GRAY)
            line.set_style(stroke_opacity=0.7, stroke_width=1)
            lines.append(line)
        for col in range(0, 21):
            start = ax.coords_to_point(-10 + col, -10)
            end = ax.coords_to_point(-10 + col, 10)
            line = Line(start, end)
            line.set_color(GRAY)
            line.set_style(stroke_opacity=0.7, stroke_width=1)
            lines.append(line)

        self.play(*[Create(lines[line]) for line in range(0, len(lines))])
        self.wait(2)

        circle = Circle(2.25)
        circle.set_color(YELLOW)
        circle.move_to(origin)
        self.play(GrowFromCenter(circle))

        self.wait(2)

        header0 = Tex("$(x,y)$-dependent opacity:").scale(0.7)
        header = MathTex(r"o(x,y)=e^{-\frac{x^2+y^2}{100}}")
        header.set_color(YELLOW)
        header0.to_corner(UL)
        header0.shift(RIGHT + 0.5 * DOWN)
        header.next_to(header0, DOWN)
        header.align_to(header0, LEFT)

        self.play(Write(header0))
        self.play(Write(header))

        self.wait(2)

        self.play(Create(ax2))
        self.wait(2)

        axes_labels = ax2.get_axis_labels()
        bell1_graph = ax2.get_graph(lambda x: np.exp(-x ** 2 / 1), color=BLUE)
        bell2_graph = ax2.get_graph(lambda x: np.exp(-x ** 2 / 25), color=RED)

        bell1_label = ax2.get_graph_label(
            bell1_graph, r"e^{-x^2}", x_val=-10, direction=UP)
        bell2_label = ax2.get_graph_label(bell2_graph, label=r"e^{-\tfrac{x^2}{25}}", x_val=10, direction=UP)

        self.play(Create(bell1_graph), Create(bell1_label))
        self.wait(2)

        self.play(Create(bell2_graph), Create(bell2_label))
        self.wait(2)

        for row in range(0, 20):
            for col in range(0, 20):

                y = 9.5 - row
                x = -9.5 + col
                opacity = np.exp(-(x * x + y * y) / 200)
                if x * x + y * y > 100:
                    opacity = 0

                square = Square(4.5 / 20)
                square.set_style(fill_color=YELLOW, stroke_color=YELLOW, fill_opacity=opacity, stroke_width=opacity)

                pos = ax.coords_to_point(x, y)
                square.move_to(pos)
                self.play(Create(square), run_time=0.01)

        self.wait(2)

        self.wait(10)


class Discs5(Scene):
    def construct(self):
        title = Tex("Colorful discs")
        title.to_edge(UP)
        title.set_color(YELLOW)
        self.add(title)
        self.wait()

        ax = Axes(
            x_range=[-10, 10],
            y_range=[-10, 10],
            x_length=4.5,
            y_length=4.5,
            axis_config={"color": YELLOW},
            x_axis_config={
                "numbers_to_include": np.arange(-3, 3.1, 1),
                "color": YELLOW
            },
            y_axis_config={
                "numbers_to_include": np.arange(-3, 3.1, 1),
                "color": YELLOW
            },
            tips=False,
        )
        ax.shift(3 * RIGHT)

        origin = ax.coords_to_point(0, 0)

        ax2 = Axes(
            x_range=[-10, 10],
            y_range=[0., 1.2],
            x_length=6,
            y_length=3,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.1, 5),
                "color": GREEN,
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 1.1, 0.2),
                "color": GREEN,
                "decimal_number_config": {
                    "num_decimal_places": 1,
                }
            },
            tips=True,
        )
        ax2.shift(3 * LEFT)

        origin = ax.coords_to_point(0, 0)
        screen = Square(4.5)
        screen.move_to(origin)
        self.play(GrowFromPoint(screen, ax.coords_to_point(-10, -10)))
        ax2.align_to(screen, DOWN)

        lines = []
        for row in range(0, 21):
            start = ax.coords_to_point(-10, -10 + row)
            end = ax.coords_to_point(10, -10 + row)
            line = Line(start, end)
            line.set_color(GRAY)
            line.set_style(stroke_opacity=0.7, stroke_width=1)
            lines.append(line)
        for col in range(0, 21):
            start = ax.coords_to_point(-10 + col, -10)
            end = ax.coords_to_point(-10 + col, 10)
            line = Line(start, end)
            line.set_color(GRAY)
            line.set_style(stroke_opacity=0.7, stroke_width=1)
            lines.append(line)

        self.play(*[Create(lines[line]) for line in range(0, len(lines))])
        self.wait(2)

        circle = Circle(2.25)
        circle.set_color(YELLOW)
        circle.move_to(origin)
        self.play(GrowFromCenter(circle))

        self.wait(2)

        header0 = Tex(r"$\varphi$-dependent hue:").scale(0.7)
        header = MathTex(r"\tan\varphi = \tfrac{y}{x}")
        header.set_color(YELLOW)
        header0.to_corner(UL)
        header0.shift(RIGHT + DOWN)
        header.next_to(header0, DOWN)
        header.align_to(header0, LEFT)

        self.play(Write(header0))
        self.play(Write(header))

        self.wait(2)

        color_wheel = ImageMobject("colorwheel.png")
        color_wheel.scale(1.5)
        color_wheel.next_to(header, DOWN)
        color_wheel.shift(3*RIGHT)
        self.play(FadeIn(color_wheel))
        self.wait(2)

        phi = ValueTracker(0)
        r=1.7
        phi.add_updater(lambda mob, dt: mob.increment_value(360*dt/5))
        label = always_redraw(lambda: MathTex(r"\varphi=", str(np.floor(phi.get_value()))).set_color(hsv_to_hex([phi.get_value()/360,1,1])).next_to(header,RIGHT,buff = LARGE_BUFF))
        dyn_dot = always_redraw(lambda: Dot().scale(1.4).set_color(hsv_to_hex([phi.get_value()/360,1,1])).move_to(color_wheel.get_center()+  r * (np.cos(phi.get_value() / 180 * np.pi) * RIGHT + np.sin(phi.get_value() / 180 * np.pi) * UP)))
        self.add(phi,label,dyn_dot)
        self.wait(5)
        phi.clear_updaters()

        for row in range(0, 20):
            for col in range(0, 20):

                y = 9.5 - row
                x = -9.5 + col
                hue = np.arctan2(-y, -x) / np.pi / 2 + 0.5

                if x * x + y * y > 100:
                    opacity = 0
                else:
                    opacity = 1

                square = Square(4.5 / 20)
                col = hsv_to_hex([hue, 1, 1])
                square.set_style(stroke_color=col, fill_color=col, fill_opacity=opacity, stroke_width=opacity)

                pos = ax.coords_to_point(x, y)
                square.move_to(pos)
                self.play(Create(square), run_time=0.01)

        self.wait(2)
        self.wait(10)


def hsv_to_hex(hsv: Iterable[float]) -> str:
    h = hsv[0]
    s = hsv[1]
    v = hsv[2]

    hi = np.floor(6 * h)
    f = 6 * h - hi

    p = v * (1 - s)
    q = v * (1 - s * f)
    t = v * (1 - s * (1 - f))

    rgb = []
    if hi == 0 or hi == 6:
        rgb = [v, t, p]
    if hi == 1:
        rgb = [q, v, p]
    if hi == 2:
        rgb = [p, v, t]
    if hi == 3:
        rgb = [p, q, v]
    if hi == 4:
        rgb = [t, p, v]
    if hi == 5:
        rgb = [v, p, q]
    return "#" + "".join("%02x" % int(255 * x) for x in rgb)


class UVCoordinates(ThreeDScene):
    def construct(self):
        title = Tex("UV-coordinates of a sphere")
        title.to_edge(UP)
        title.set_color(YELLOW)
        self.play(Write(title))
        self.wait()

        u_color = PURPLE
        v_color = BLUE

        ax = Axes(
            x_range=[0, 1],
            y_range=[0., 1],
            x_length=3,
            y_length=3,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": np.arange(-0, 1.1, 1),
                "color": WHITE,
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 1.1, 1),
                "color": WHITE,
            },
            tips=False,
        )
        ax.shift(5*LEFT+UP)
        labels = ax.get_axis_labels(x_label="u", y_label="v")
        labels[0].set_color(u_color)
        labels[1].set_color(v_color)
        ax.add(labels)

        ax2 = Axes(
            x_range=[0, 2 * np.pi],
            y_range=[0, np.pi],
            x_length=6,
            y_length=3,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": np.arange(-0, 6.1, 1),
                "color": WHITE,
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 3.1, 1),
                "color": WHITE,
            },
            tips=False,
        )

        labels = ax2.get_axis_labels(x_label=r"\varphi", y_label=r"\vartheta")
        labels[0].set_color(u_color)
        labels[1].set_color(v_color)
        ax2.add(labels)

        self.play(Create(ax))
        self.wait(2)

        group1 =[ax,ax2]

        x_lines=[]
        for x in range(0,11):
            line = Line(ax.coords_to_point(x/10,0),ax.coords_to_point(x/10,1))
            line.set_color(u_color)
            group1.append(line)
            x_lines.append(line)
            self.play(Create(line),run_time=0.2)
        self.wait(2)

        y_lines=[]
        for y in range(0,11):
            line = Line(ax.coords_to_point(0,y/10),ax.coords_to_point(1,y/10))
            line.set_color(v_color)
            y_lines.append(line)
            group1.append(line)
            self.play(Create(line),run_time=0.2)

        first_Group = VGroup(ax,*x_lines,*y_lines)

        self.wait(2)

        trans = [MathTex(r"\varphi = 2\pi\cdot u"), MathTex(r"\vartheta =\pi\cdot v")]
        trans[0].set_color(u_color)
        trans[1].set_color(v_color)
        trans[0].next_to(ax,RIGHT)
        trans[0].shift(0.25*UP)
        trans[1].next_to(trans[0], DOWN)
        trans[1].align_to(trans[0], LEFT)

        group1.append(trans[0])
        group1.append(trans[1])

        self.play(*[Write(trans[i]) for i in range(0, len(trans))])
        self.wait(2)

        self.play(ApplyMethod(first_Group.scale, 0.3333))
        self.wait(2)

        ax2.next_to(trans[0],RIGHT)
        ax2.shift(0.5*DOWN)
        self.play(Create(ax2))

        self.wait(2)

        for x in range(0, 11):
            line = Line(ax2.coords_to_point(2*np.pi* x / 10 , 0), ax2.coords_to_point(2*np.pi*x / 10, np.pi))
            line.set_color(u_color)
            group1.append(line)
            self.play(TransformFromCopy(x_lines[x].copy(),line), run_time=0.4)

        self.wait(2)

        for y in range(0, 11):
            line = Line(ax2.coords_to_point(0, np.pi*y / 10), ax2.coords_to_point(2 * np.pi, np.pi* y / 10))
            line.set_color(v_color)
            group1.append(line)
            self.play(TransformFromCopy(y_lines[y],line), run_time=0.4)

        self.wait(2)

        trans2 = [MathTex(r"x=\sin",r"\vartheta",r"\cos",r"\varphi"),MathTex(r"y=\sin",r"\vartheta",r"\sin",r"\varphi"),MathTex(r"z=\cos",r"\vartheta")]
        for i in range(0,3):
            trans2[i][1].set_color(v_color)
        for i in range(0,2):
            trans2[i][3].set_color(u_color)

        trans2[0].shift(1.5*DOWN)
        for i in range(1,3):
            trans2[i].next_to(trans2[i-1], DOWN)
            trans2[i].align_to(trans2[i-1], LEFT)

        self.play(*[Write(trans2[i]) for i in range(0, len(trans2))])
        self.wait(2)

        vgroup1 = VGroup(*group1)
        vgroup2 = VGroup(*trans2)

        self.play(ApplyMethod(vgroup1.scale,0.7),ApplyMethod(vgroup2.scale,0.7))
        self.wait(2)

        self.play(ApplyMethod(vgroup1.shift,2*LEFT+0.75*UP))
        self.play(ApplyMethod(vgroup2.next_to,vgroup1,RIGHT,buff= 2*LARGE_BUFF))

        self.wait(10)


class PolarCoordinates(ThreeDScene):
    def construct(self):
        u_color = PURPLE
        v_color = BLUE

        axes = ThreeDAxes(tips=False,x_range=[-4,4,1.5],y_range=[-4,4,1.5],z_range=[-4,4,1.5],x_length=8,y_length=8,z_length=8)
        self.add(axes)

        self.set_camera_orientation(phi=75*DEGREES, theta=-30*DEGREES)

        self.begin_ambient_camera_rotation(rate=0.25)

        for x in range(0,10):
            theta = np.pi*x/10
            curve = ParametricFunction(lambda t: np.array(
                [3*np.sin(theta) * np.cos(2 * np.pi * t), 3*np.sin(theta) * np.sin(2 * np.pi * t), 3*np.cos(theta)]),
                                       t_range=[0, 2 * np.pi])
            curve.set_color(v_color)
            self.play(Create(curve))

        for x in range(0,10):
            phi = 2*np.pi*x/10
            curve = ParametricFunction(lambda t: np.array(
                [3*np.sin(t) * np.cos(phi), 3*np.sin(t) * np.sin(phi), 3*np.cos(t)]),
                                       t_range=[0, np.pi])
            curve.set_color(u_color)
            self.play(Create(curve))

        self.wait(10)


class PolarCoordinates2(ThreeDScene):
    def construct(self):
        u_color = PURPLE
        v_color = BLUE

        axes = ThreeDAxes(tips=False,x_range=[-4,4,1.5],y_range=[-4,4,1.5],z_range=[-4,4,1.5],x_length=8,y_length=8,z_length=8)
        self.add(axes)

        self.set_camera_orientation(phi=75*DEGREES, theta=-30*DEGREES)

        self.begin_ambient_camera_rotation(rate=0.125)

        x_curves=[]
        for x in range(0,11):
            u = -0.5+x/10
            curve = ParametricFunction(lambda t: np.array(
                [u, t,0]),
                                       t_range=[-0.5, 0.5])
            curve.set_color(v_color)
            x_curves.append(curve)

        self.play(*[Create(x_curves[i]) for i in range(0,len(x_curves))])

        y_curves = []
        for y in range(0, 11):
            v = -0.5 + y / 10
            curve = ParametricFunction(lambda t: np.array(
                [ t, v,0]), t_range=[-0.5, 0.5])
            curve.set_color(u_color)
            y_curves.append(curve)

        self.play(*[Create(y_curves[i]) for i in range(0,len(y_curves))])

        self.wait(5)

        new_x_curves=[]
        for x in range(0, 11):
            u = -np.pi/2 + np.pi*x / 10
            curve = ParametricFunction(lambda t: np.array(
                [u, t,0]), t_range=[-np.pi, np.pi])
            curve.set_color(v_color)
            new_x_curves.append(curve)

        new_y_curves=[]
        for y in range(0, 11):
            v = -np.pi + np.pi*y / 5
            curve = ParametricFunction(lambda t: np.array(
                [t, v,0]), t_range=[-np.pi/2, np.pi/2])
            curve.set_color(u_color)
            new_y_curves.append(curve)

        self.play(*[Transform(x_curves[i],new_x_curves[i]) for i in range(0,len(x_curves))],*[Transform(y_curves[i],new_y_curves[i]) for i in range(0,len(y_curves))],run_time=5)

        self.wait(5)

        for x in range(0,11):
            theta = -np.pi/2+np.pi*x/10
            curve = ParametricFunction(lambda t: np.array(
                [3*np.cos(theta) * np.cos(2 * np.pi * t), 3*np.cos(theta) * np.sin(2 * np.pi * t), 3*np.sin(theta)]),
                                       t_range=[-np.pi,  np.pi])
            curve.set_color(v_color)
            self.play(Transform(x_curves[x],curve))

        for y in range(0,11):
            phi = 2*np.pi*y/10
            curve = ParametricFunction(lambda t: np.array(
                [3*np.cos(t) * np.cos(phi), 3*np.cos(t) * np.sin(phi), 3*np.sin(t)]),
                                       t_range=[-np.pi/2, np.pi/2])
            curve.set_color(u_color)
            self.play(Transform(y_curves[y],curve))

        self.wait(10)


class Transformations(Scene):
    def construct(self):
        u_color = PURPLE
        v_color = BLUE

        trans = [MathTex(r"-\tfrac{1}{2}\le u \le \tfrac{1}{2}"),MathTex(r"-\tfrac{1}{2}\le v \le \tfrac{1}{2}")]
        trans[0].set_color(u_color)
        trans[1].set_color(v_color)

        trans[0].to_corner(UL)
        trans[1].next_to(trans[0],DOWN)

        self.play(Write(trans[0]))
        self.play(Write(trans[1]))

        self.wait(5)

        trans2 = [MathTex(r"-\pi\le \varphi \le \pi"), MathTex(r"-\tfrac{\pi}{2} \le \vartheta \le \tfrac{\pi}{2}")]
        trans2[0].set_color(u_color)
        trans2[1].set_color(v_color)

        trans2[0].to_corner(UL)
        trans2[1].next_to(trans2[0], DOWN)

        self.play(Transform(trans[0],trans2[0]))
        self.play(Transform(trans[1],trans2[1]))

        self.wait(5)

        trans2 = [MathTex(r"-\pi\le \varphi \le \pi"), MathTex(r"-\tfrac{\pi}{2} \le \vartheta \le \tfrac{\pi}{2}"),]
        trans2[0].set_color(u_color)
        trans2[1].set_color(v_color)

        for i in range(0,2):
            trans2[i].move_to(trans[i])
            self.play(Transform(trans[i], trans2[i]))

        self.wait(5)

        trans3 = [MathTex(r"x=\cos",r"\vartheta",r"\cos",r"\varphi"),MathTex(r"y=\cos",r"\vartheta",r"\sin",r"\varphi"),MathTex(r"z=\sin",r"\vartheta") ]
        for i in range(0,3):
            trans3[i][1].set_color(v_color)
        for i in range(0,2):
            trans3[i][3].set_color(u_color)

        trans3[0].to_corner(UL)
        for i in range(1,3):
            trans3[i].next_to(trans3[i-1], DOWN)
            trans3[i].align_to(trans3[i-1], LEFT)

        for i in range(0,2):
            self.play(Transform(trans[i], trans3[i]))
        self.play(Write(trans3[2]))

        self.wait(5)
