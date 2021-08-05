from abc import ABC

import numpy as np
from manim import *
from colour import Color


class Intro(Scene):
    def construct(self):
        title = Tex("Overview")
        title.to_edge(UP)
        title.set_color(YELLOW)
        self.play(Write(title))
        self.wait()

        tops = BulletedList("Optimal points", "Optimal functions",
                            "Least action principle", "Applications","Technical details")
        tops[0].set_color(RED)
        tops[1].set_color(GREEN)
        tops[2].set_color(YELLOW)
        tops[3].set_color(BLUE)
        tops[4].set_color(WHITE)

        self.play(Write(tops[0]))
        self.wait(1)
        self.play(Write(tops[1]))
        self.wait(1)
        self.play(Write(tops[2]))
        self.wait(1)
        self.play(Write(tops[3]))
        self.wait(1)


class OptimalBox(Scene):

    def construct(self):
        title = Tex("Optimal points")
        title.to_edge(UP)
        title.shift(0.1 * RIGHT)
        title.set_color(RED)
        self.play(Write(title))
        self.wait()

        paper = ImageMobject("paper.png")
        paper.scale(0.7)
        self.add(paper)
        self.wait(3)

        label = Tex("33\,cm")
        label.set_color(RED)
        label.shift(3.5 * DOWN)
        line = DoubleArrow(2.7 * LEFT, 2.7 * RIGHT)
        line.shift(3 * DOWN)
        line.set_color(RED)

        self.play(Write(label), Create(line))
        self.wait(2)

        self.play(FadeOut(paper), FadeOut(label), FadeOut(line))

        volume1 = MathTex("21\,cm\cdot 21\,cm\cdot 6\,cm = 2646\,cm^3=2.6\,l")
        volume1.scale(0.7)
        volume1.to_corner(DL, buff=LARGE_BUFF)

        self.play(Write(volume1))
        self.wait(2)

        ax = Axes(
            x_range=[0, 20],
            y_range=[0, 4],
            x_length=6,
            y_length=4,
            axis_config={"color": GRAY},
            x_axis_config={
                "numbers_to_include": np.arange(0, 20, 5),
                "numbers_with_eleongated_tics": np.arange(0, 15, 5),
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 4, 1),
                "numbers_with_eleongated_tics": np.arange(0, 4, 1),
            },
            include_tip=True,
        )

        ax.shift(3.5 * RIGHT)

        self.play(Create(ax))

        dot_A = Dot().move_to(ax.coords_to_point(6, 2.646))
        label_A = MathTex(r"(6,2.6)")
        label_A.scale(0.7)
        label_A.next_to(dot_A, UP)
        self.play(Create(dot_A), Write(label_A))

        self.wait(2)

        self.play(FadeOut(volume1))

        volume2 = MathTex("27\,cm\cdot 27\,cm\cdot 3\,cm = 2187\,cm^3=2.2\,l")
        volume2.scale(0.7)
        volume2.to_corner(DL, buff=LARGE_BUFF)

        self.play(Write(volume2))
        self.wait(2)

        dot_B = Dot().move_to(ax.coords_to_point(3, 2.187))
        label_B = MathTex(r"(3,2.2)")
        label_B.scale(0.7)
        label_B.next_to(dot_B, UP)
        self.play(Create(dot_B), Write(label_B))

        self.wait(2)

        self.play(FadeOut(volume2))

        volume3 = MathTex("9\,cm\cdot 9\,cm\cdot 12\,cm = 972\,cm^3=0.97\,l")
        volume3.scale(0.7)
        volume3.to_corner(DL, buff=LARGE_BUFF)

        self.play(Write(volume3))
        self.wait(2)

        dot_C = Dot().move_to(ax.coords_to_point(12, 0.972))
        label_C = MathTex(r"(12,0.97)")
        label_C.scale(0.7)
        label_C.next_to(dot_C, UP)
        self.play(Create(dot_C), Write(label_C))
        self.wait(2)

        self.play(FadeOut(volume3))

        box = ImageMobject("box.png")
        box.scale(0.7)
        box.to_edge(LEFT)
        box.shift(UP)
        self.play(GrowFromCenter(box))
        self.wait(2)

        label2 = MathTex("x")
        label2.set_color(RED)
        label2.scale(0.7)
        line2 = DoubleArrow(1.15 * LEFT, 1.15 * RIGHT)
        line2.shift(5.65 * LEFT)
        line2.set_color(RED)
        label2.next_to(line2, DOWN)

        label3 = MathTex("x")
        label3.set_color(RED)
        label3.scale(0.7)
        line3 = DoubleArrow(1.15 * LEFT, 1.15 * RIGHT)
        line3.shift(2.5 * LEFT)
        line3.set_color(RED)
        label3.next_to(line3, DOWN)

        self.play(GrowFromCenter(line2), Write(label2), GrowFromCenter(line3), Write(label3))
        self.wait(2)

        label = MathTex("33-2\cdot x")
        label.set_color(RED)
        label.scale(0.7)
        line = DoubleArrow(0.9 * LEFT, 0.9 * RIGHT)
        line.set_color(RED)
        line.next_to(box, DOWN)
        label.next_to(line, DOWN)

        self.play(GrowFromCenter(line), Write(label))
        self.wait(2)

        volume4 = MathTex("V(x)=(33-2\cdot x)^2\cdot x=4x^3-132x^2+1089x")
        volume4.to_corner(DL, buff=LARGE_BUFF)
        volume4.shift(0.5 * DOWN)
        volume4.set_color(RED)

        func = ax.get_graph(lambda x: (4 * x ** 3 - 132 * x ** 2 + 1089 * x) / 1000, color=RED, x_range=[0, 16.5])
        self.play(Write(volume4), Create(func))
        self.wait(2)

        self.play(FadeOut(box), FadeOut(dot_A), FadeOut(dot_B), FadeOut(dot_C), FadeOut(label_A), FadeOut(label_B),
                  FadeOut(label_C), FadeOut(line), FadeOut(line3), FadeOut(line2), FadeOut(label), FadeOut(label2),
                  FadeOut(label3))

        dot_Max = Dot().move_to(ax.coords_to_point(5.5, 2.662))
        dot_Max.scale(1.5)
        dot_Max.set_color(RED)
        label_Max = MathTex(r"(\hat x,\hat V )")
        label_Max.set_color(RED)
        label_Max.next_to(dot_Max, UP)
        self.play(Create(dot_Max), Write(label_Max))

        self.wait(2)

        vol_prime = MathTex(r"V'(x)=12x^2-264x+1089")
        necessary = MathTex(r"V'(\hat x)=0")
        eq = MathTex(r"\,\,0=12\hat x^2-264\hat x+1089")
        sol1 = MathTex(r"\,\hat x_0=5.5 \Longrightarrow V(\hat x_0)=2.7\,l")
        sol2 = MathTex(r"\,\hat x_1=16.5 \Longrightarrow V(\hat x_1) =0\,l")

        rows = [vol_prime, necessary, eq, sol1, sol2]

        rows[0].to_corner(UL, buff=LARGE_BUFF)
        rows[0].shift(DOWN)

        for i in range(1, len(rows)):
            rows[i].next_to(rows[i - 1], DOWN)
            rows[i].align_to(rows[i - 1], LEFT)

        colors = [WHITE, WHITE, WHITE, RED, BLUE]
        for i in range(0, 2):
            self.play(Write(rows[i]))
            rows[i].set_color(colors[i])

        rect = SurroundingRectangle(necessary)
        rect.set_color(YELLOW)
        self.play(GrowFromCenter(rect))
        self.wait(2)

        # moving tangent

        alpha = ValueTracker(0)  # this is the value we're changing when animating

        # function for drawing the tangent line
        draw_tangent = (lambda:
                        TangentLine(func, alpha.get_value(), length=2, color=YELLOW))

        # always redraw the tangent line, i.e. update when alpha changes
        tangent = always_redraw(draw_tangent)

        self.play(Create(tangent))

        # move the value of alpha around
        for alpha_ in (0, 0.9, 0.43):  # animate range as a fraction of the entire x-range of the graph
            self.play(alpha.animate.set_value(alpha_), run_time=3)

        self.wait()

        for i in range(2, len(rows)):
            self.play(Write(rows[i]))
            rows[i].set_color(colors[i])
            if i < len(rows) - 1:
                self.wait(2)

        dot_Min = Dot().move_to(ax.coords_to_point(16.6, 0))
        dot_Min.scale(1.5)
        dot_Min.set_color(BLUE)
        self.play(Create(dot_Min))
        self.wait(2)

        self.wait(10)


class OptimalFunction(Scene):

    def construct(self):
        title = Tex("Optimal Functions")
        title.to_edge(DOWN)
        title.shift(0.1 * RIGHT)
        title.set_color(GREEN)
        self.play(Write(title))
        self.wait()

        demo = ImageMobject("freeFall.png")
        demo.to_edge(LEFT)
        self.add(demo)

        line = NumberLine(x_range=[0, 5], length=5, include_numbers=True, include_tip=True)
        line.shift(4.25 * LEFT + 1.2 * UP)
        line.rotate(PI / 2)
        line.set_color(GRAY)

        self.play(Create(line))

        self.wait(2)

        ax = Axes(
            x_range=[0, 1., 0.2],
            y_range=[0, 5, 1],
            x_length=5,
            y_length=5,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": [0.2, 0.4, 0.6, 0.8, 1.0],
                "numbers_with_eleongated_tics": np.arange(0, 1.1, 1),
                "label": 't',
                'decimal_number_config': {
                    'num_decimal_places': 1,
                }
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 5, 1),
                "numbers_with_eleongated_tics": np.arange(0, 5, 1),
                "label": 'h(t)',
            },
            include_tip=True,
        )
        labels = ax.get_axis_labels(x_label="t", y_label="h(t)")
        labels[1].shift(0.5 * DOWN - 1.2 * RIGHT)
        labels[0].shift(0.3 * LEFT)
        ax.add(labels)
        ax.shift(3.5 * RIGHT + 0.8 * UP)

        self.play(Create(ax))
        self.wait(2)

        h = lambda t: 5 - 5 * t * t

        alpha = ValueTracker(0)  # this is the value we're changing when animating
        # function for drawing the tangent line

        arrow = always_redraw(lambda: Arrow(start=(h(alpha.get_value()) - 1.5) * UP + 1.5 * LEFT,
                                            end=(h(alpha.get_value()) - 1.5) * UP + 4 * LEFT, stroke_color=RED,
                                            fill_color=RED, stroke_width=2))
        self.add(arrow)
        label = always_redraw(
            lambda: MathTex(r"(", round(alpha.get_value(), 1), ",", round(h(alpha.get_value()), 1), ")").scale(
                0.7).next_to(arrow, RIGHT).set_color(RED))

        parabel = always_redraw(
            lambda: ax.get_graph(lambda x: 5 - 5 * x * x, color=RED, x_range=[0, alpha.get_value()]))

        self.add(label)
        self.add(parabel)

        dot = always_redraw(lambda: Dot(stroke_color=RED, stroke_width=2, fill_color=RED_D).move_to(
            ax.coords_to_point(alpha.get_value(), h(alpha.get_value()))))
        self.add(dot)

        self.play(alpha.animate.set_value(0), run_time=2)
        self.play(alpha.animate.set_value(1), run_time=5, rate_func=linear)
        self.wait(2)

        self.wait(20)


class OptimalFunction2(Scene):
    def construct(self):
        title = Tex("Optimal Functions")
        title.to_edge(DOWN)
        title.shift(0.1 * RIGHT)
        title.set_color(GREEN)

        ax = Axes(
            x_range=[0, 1., 0.2],
            y_range=[0, 5, 1],
            x_length=5,
            y_length=5,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": [0.2, 0.4, 0.6, 0.8, 1.0],
                "numbers_with_eleongated_tics": np.arange(0, 1.1, 1),
                "label": 't',
                'decimal_number_config': {
                    'num_decimal_places': 1,
                }
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 5, 1),
                "numbers_with_eleongated_tics": np.arange(0, 5, 1),
                "label": 'h(t)',
            },
            include_tip=True,
        )
        labels = ax.get_axis_labels(x_label="t", y_label="h(t)")
        labels[1].shift(0.5 * DOWN - 1.2 * RIGHT)
        labels[0].shift(0.3 * LEFT)
        ax.add(labels)
        ax.shift(3.5 * RIGHT + 0.8 * UP)

        parabel = ax.get_graph(lambda x: 5 - 5 * x * x, color=RED, x_range=[0, 1])

        self.add(title, ax, parabel)
        self.wait(2)

        self.play(ApplyMethod(title.to_edge, UP), ApplyMethod(ax.shift, 1.5 * DOWN + 0.5 * RIGHT),
                  ApplyMethod(parabel.shift, 1.5 * DOWN + 0.5 * RIGHT))
        self.wait(2)

        dotA = Dot(ax.coords_to_point(0, 5)).set_color(GREEN).scale(2)
        dotB = Dot(ax.coords_to_point(1, 0)).set_color(GREEN).scale(2)

        self.play(GrowFromCenter(dotA))
        self.play(GrowFromCenter(dotB))

        fcns = [lambda x: 5 - 5 * x ** 32, lambda x: 5 - 5 * x ** 16, lambda x: 5 - 5 * x ** 8,
                lambda x: 5 - 5 * x ** 4, lambda x: 5 - 5 * x ** 2, lambda x: 5 - 5 * x]

        # calculating the mirror images of the above functions, for some reason the functions are not evaluated correctly for too small exponents
        fcns2 = []
        for fcn in fcns:
            fcns2.append(
                ParametricFunction(lambda u: ax.coords_to_point(1 - 1 / 5 * fcn(u), 5 - 5 * u), color=GREEN, t_min=0,
                                   t_max=1))

        functions = []

        for fcn in fcns2:
            self.play(Create(fcn), run_time=0.2)
            functions.append(fcn)

        omitFirstOne = 0
        for fcn in reversed(fcns):
            p = ax.get_graph(fcn, color=GREEN, x_range=[0, 1])
            self.play(Create(p), run_time=0.2)
            if omitFirstOne > 0:
                functions.append(p)
            omitFirstOne = omitFirstOne + 1

        cruncher = ImageMobject("cruncher.png")
        cruncher.scale(0.2)
        self.add(cruncher)
        self.wait(2)

        num_action_values = [-1.53, -3.00, -5.82, -11.6, 1000, -12.5, -16.7, -11.4, 8.89, 56.2, 155]
        action_values = []
        for val in num_action_values:
            if val == 1000:
                action_values.append(r"\infty")
            else:
                action_values.append(str(val))

        ax2 = Axes(
            x_range=[0, 11., 1],
            y_range=[-30, 130, 30],
            x_length=4,
            y_length=7,
            axis_config={"color": WHITE},
            x_axis_config={
            },
            y_axis_config={
                "numbers_to_include": np.arange(-30, 130, 60),
                "numbers_with_eleongated_tics": np.arange(0, 5, 1)
            },
            include_tip=True,
        )
        ax2.shift(3.5 * LEFT - 0.2 * UP)
        self.add(ax2)

        count = 0
        for parabel, action_value in zip(functions, action_values):
            copy = parabel.copy()
            copy.shift(4.1 * LEFT + 0.45 * UP)
            copy.scale(0.25)
            self.play(TransformFromCopy(parabel, copy))
            value = MathTex(action_value)
            value.set_color(RED)
            value.scale(0.7)
            self.play(FadeOut(copy), FadeIn(value), run_time=5)
            dot = Dot()
            dot.set_color(RED)
            self.play(Transform(value, dot))
            self.play(ApplyMethod(value.shift, ax2.coords_to_point(count, num_action_values[count])))
            count = count + 1

        self.wait(2)

        pTwo = lambda n: 2 ** (n - 5)
        solFunc = lambda x: 25 * pTwo(x) * (4 + (pTwo(x) - 7) * pTwo(x)) / 2 / (2 * pTwo(x) ** 2 + pTwo(x) - 1)
        solution = ax2.get_graph(solFunc, color=RED, x_range=[0, 3.9])
        solution2 = ax2.get_graph(solFunc, color=RED, x_range=[4.06, 10])

        self.play(GrowFromPoint(solution, ax2.coords_to_point(0, 0)))
        self.play(GrowFromPoint(solution2, ax2.coords_to_point(4.01, solFunc(4.01))))
        self.wait(2)

        alpha = ValueTracker(1)  # this is the value we're changing when animating

        # function for drawing the tangent line
        draw_tangent = (lambda: TangentLine(solution2, alpha.get_value(), length=2, color=YELLOW))

        # always redraw the tangent line, i.e. update when alpha changes
        tangent = always_redraw(draw_tangent)

        self.play(Create(tangent))

        # move the value of alpha around
        for alpha_ in (0.1, 0.325):  # animate range as a fraction of the entire x-range of the graph
            self.play(alpha.animate.set_value(alpha_), run_time=3)

        self.wait(2)

        dot = Dot(ax2.coords_to_point(6, -16.7))
        dot.set_color(YELLOW)
        dot.scale(1.5)

        emphasize = functions[7]
        self.play(GrowFromCenter(dot), ApplyMethod(emphasize.set_color, YELLOW))
        self.wait(2)

        self.wait(20)


class LeastAction(Scene):
    def construct(self):
        title = Tex("Least Action Principle")
        title.to_edge(UP)
        title.shift(0.1 * RIGHT)
        title.set_color(YELLOW)

        self.play(Write(title))

        cruncher = ImageMobject("cruncher.png")
        cruncher.scale(0.15)
        cruncher.next_to(title, DOWN)

        self.play(GrowFromCenter(cruncher))

        function = MathTex(r"f(x)", r"\rightarrow")
        function.next_to(cruncher, LEFT)

        number = MathTex(r"\rightarrow", r"x\in\mathbb{R}")
        number.next_to(cruncher, RIGHT)

        self.play(Write(function[0]))
        self.wait()
        self.play(Write(function[1]))
        self.wait()
        self.play(Write(number[0]))
        self.wait()
        self.play(Write(number[1]))
        self.wait(2)

        action = MathTex(r"\int_0^1", r"\tfrac{1}{2} f'(x)^2-10 f(x)", r"\,\rm{d}x")
        action.set_color(WHITE)
        action.next_to(cruncher, DOWN)

        self.play(Write(action[0]), Write(action[2]))
        self.wait()
        self.play(Write(action[1]))
        self.wait(2)

        action2 = MathTex(r"\int_0^1", r"\tfrac{1}{2} m v(t)^2-m g h(t)", r"\,\rm{d}t")
        action2.set_color(YELLOW)
        action2.next_to(action, DOWN)

        self.play(Write(action2))
        self.wait(2)

        action3 = MathTex("S = ", r"\int_{t_0}^{t_1}", r"E_\text{kin}-E_\text{pot}", r"\,\rm{d}t", "=",
                          r"\int_{t_0}^{t_1}", r"L(\dot{\vec{x}}(t),\vec{x}(t))", r"\,\rm{d}t")
        action3.set_color(YELLOW)
        action3.next_to(action2, DOWN)

        rect = SurroundingRectangle(action3)
        rect.set_color(RED)

        self.play(Write(action3[0:4]))
        self.wait(2)
        self.play(Write(action3[4:8]))
        self.wait(2)
        self.play(GrowFromEdge(rect, LEFT))
        self.wait(2)
        self.wait(20)


class LeastAction2(Scene):
    def construct(self):
        title = Tex("Least Action Principle")
        title.to_edge(UP)
        title.shift(0.1 * RIGHT)
        title.set_color(YELLOW)

        self.add(title)
        self.wait(2)

        box = ImageMobject("foldedBox.png")
        box.scale(0.6)
        box.next_to(title, DOWN)
        box.to_edge(LEFT, buff=LARGE_BUFF)

        self.play(GrowFromCenter(box))
        self.wait(2)

        lines = []
        lines.append(MathTex(r"\frac{\rm{d}}{\rm{d}x} V(x)", "=", "V'(x)", "=", "0"))
        lines.append(MathTex(r"\Longrightarrow  x", " =", " 5.5"))
        lines.append(MathTex(r"\Longrightarrow V( x)", "=", "2.7\,l"))

        lines[0].next_to(box, DOWN)
        self.play(Write(lines[0]))
        self.wait(2)

        for i in range(1, len(lines)):
            lines[i].next_to(lines[i - 1], DOWN, buff=MED_LARGE_BUFF)
            lines[i][1].align_to(lines[i - 1][1], LEFT)
            lines[i][0].next_to(lines[i][1], LEFT)
            lines[i][2].next_to(lines[i][1], RIGHT)
            self.play(Write(lines[i]))
            self.wait(2)

        ax = Axes(
            x_range=[0, 1., 0.2],
            y_range=[0, 5, 1],
            x_length=2,
            y_length=2,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": [0.5, 1.0],
                "numbers_with_eleongated_tics": np.arange(0, 1.1, 0.5),
                "label": 't',
                'decimal_number_config': {
                    'num_decimal_places': 1,
                }
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 5, 5),
                "numbers_with_eleongated_tics": np.arange(0, 5, 5),
                "label": 'h(t)',
            },
            include_tip=True,
        )
        labels = ax.get_axis_labels(x_label="t", y_label="h(t)")
        labels[1].shift(0.5 * DOWN - 1.2 * RIGHT)
        labels[0].shift(0.3 * LEFT)
        ax.add(labels)
        ax.shift(3.5 * RIGHT + 0.8 * UP)

        parabel = ax.get_graph(lambda x: 5 - 5 * x * x, color=YELLOW, x_range=[0, 1])

        lines2 = []
        lines2.append(MathTex(r"\frac{\delta}{\delta h(t)} S[h(t),\dot h(t)]", "=", "0"))
        lines2.append(MathTex(r"\Longrightarrow  \ddot h(t)", " =", " -g"))
        lines2.append(MathTex(r"\Longrightarrow h(t)", "=", r"5-\tfrac{g}{2} t^2"))

        lines2[0].next_to(lines[0], RIGHT)
        lines2[0].to_edge(RIGHT, buff=2 * LARGE_BUFF)
        self.play(Write(lines2[0]))
        self.wait(2)

        for i in range(1, len(lines2)):
            lines2[i].next_to(lines2[i - 1], DOWN)
            lines2[i][1].align_to(lines2[i - 1][1], LEFT)
            lines2[i][0].next_to(lines2[i][1], LEFT)
            lines2[i][2].next_to(lines2[i][1], RIGHT)
            self.play(Write(lines2[i]))
            self.wait(2)

        self.add(ax, parabel)
        self.wait(2)

        self.wait(20)


class Application(Scene):
    def construct(self):
        title = Tex("Pendulum")
        title.to_edge(UP)
        title.shift(0.1 * RIGHT)
        title.set_color(BLUE)

        self.add(title)
        self.wait(2)

        fades = []

        lines = [MathTex(r"E_\text{kin}", "=", r"\tfrac{1}{2}mv^2", r"=\tfrac{1}{2}m l^2", r"\dot\varphi^2"),
                 MathTex(r"E_\text{pot}", "=", r"mg", "h", "=mg(", "l", "-", r"l\cdot \cos \varphi", ")"),
                 MathTex(r"S[\varphi,\dot\varphi]", "=",
                         r"\int \tfrac{1}{2} m l^2 \dot \varphi^2-mgl(1-\cos\varphi)\,\rm{d}t"),
                 MathTex(r"\frac{\delta}{\delta \varphi(t)}S[\varphi,\dot\varphi]","=","0",r"\,\,\Longrightarrow"),
                 MathTex(r"\ddot \varphi", "=", r"-\frac{g}{l} \sin \varphi")]

        fades.extend(lines[0:4])
        # for i in range(0,3):
        #     fades.append(lines[i])

        lines[0].next_to(title, DOWN, buff=0.5*LARGE_BUFF)
        lines[0][4].set_color(YELLOW)
        lines[1][3].set_color(GREEN)
        lines[1][5].set_color(RED)
        lines[1][7].set_color(PURPLE)
        lines[0].to_edge(LEFT, buff=2*LARGE_BUFF)
        lines[4].set_color(YELLOW)
        self.play(Write(lines[0][0:3]))
        self.wait(2)

        # create pendulum with length l
        l = 3
        pendulum = Pendulum(l)
        pendulum.shift(4 * RIGHT)

        pendulum.play(self)
        fades.append(pendulum)

        # rotate by angle alpha
        alpha = PI / 5
        arc = Arc(1, -PI / 2, alpha)
        arc.set_color(YELLOW)
        arc.shift(4 * RIGHT + 3 * UP)
        angle = MathTex(r"\varphi")
        angle.set_color(YELLOW)
        angle.shift(4.25 * RIGHT + 2.25 * UP)

        pendulum2 = pendulum.copy()
        pendulum2.rotate(alpha)
        self.play(TransformFromCopy(pendulum, pendulum2), GrowFromPoint(arc, arc.get_left()), Write(lines[0][3:5]))
        self.play(Write(angle))
        self.wait(2)

        fades.extend([arc, angle])

        for i in range(1, len(lines)):
            # layout
            lines[i].next_to(lines[i - 1], DOWN)
            if i == 2:
                lines[i].shift(LARGE_BUFF * DOWN)
            align_formulas_with_equal(lines[i], lines[i - 1], 1, 1)
            if i == 1:
                # explain potential energy
                self.play(Write(lines[1][0:3]))
                center = pendulum.get_body().get_center()
                center2 = pendulum2.get_body().get_center()
                h = l * (1 - np.cos(alpha))
                aux_line = Line(center2, center + h * UP)
                aux_line2 = Line(center, center2 + h * DOWN)
                self.play(GrowFromPoint(aux_line, center2), GrowFromPoint(aux_line2, center))
                h_line = Line(aux_line.get_center(), aux_line2.get_center())
                h_line.set_color(GREEN)
                h_label = MathTex("h")
                h_label.set_color(GREEN)
                h_label.next_to(h_line)
                self.play(Create(h_line), Write(h_label))
                self.wait()
                h_copy = h_label.copy()
                self.play(Transform(h_copy, lines[1][3]))
                self.wait()
                self.play(Write(lines[1][3:5]))
                l_label = MathTex("l")
                l_label.set_color(RED)
                l_label.next_to(pendulum.get_rode(), LEFT)
                self.play(Write(l_label))
                l_copy = pendulum.get_rode().copy()
                self.play(Create(l_copy))
                self.wait(2)
                self.play(Transform(l_label, lines[1][5]))
                self.wait()
                aux_line3 = Line(pendulum.get_rode().get_top(), center + h * UP)
                aux_line3.set_color(PURPLE)
                self.play(Create(aux_line3))
                self.wait()
                self.play(Write(lines[1][6]))
                self.play(Transform(aux_line3, lines[1][7]))
                self.play(Write(lines[1][8]))
                self.wait(2)
                fades.extend([l_copy, h_line, aux_line, aux_line2, aux_line3, h_label, h_label, h_copy, l_label])
            elif i==3:
                rect = SurroundingRectangle(lines[3][0:3])
                rect.set_color(YELLOW)
                fades.append(rect)
                self.play(Write(lines[i]))
                self.play(GrowFromCenter(rect))
            elif i==4:
                lines[i].shift(3*RIGHT)
                lines[i].scale(1.5)
                self.play(Write(lines[i]))
            else:
                self.play(Write(lines[i]))
            self.wait(10)

        self.play(*[FadeOut(fades[i]) for i in range(0, len(fades))])
        self.play(ApplyMethod(lines[4].to_corner, UL))


class Application2(Scene):
    def construct(self):
        title = Tex("Pendulum")
        title.to_edge(UP)
        title.shift(0.1 * RIGHT)
        title.set_color(BLUE)

        l = 2
        alpha = PI / 5
        pendulum = Pendulum(l)
        pendulum.shift(4 * RIGHT + 0.5 * UP)
        pendulum.rotate(alpha)

        eom = MathTex(r"\ddot \varphi", "=", r"-\frac{g}{l} \sin \varphi")
        eom.scale(1.5)
        eom.to_corner(UL)
        eom.set_color(YELLOW)

        self.add(title, eom)

        self.wait(2)
        pendulum.play(self)
        self.wait(2)
        pendulum.remove(self)

        (pendulum1, remove1) = self.swing(angle=PI / 5, pendulum_shift=0.5 * UP, duration=10, height=2)
        self.wait(2)
        (pendulum2, remove2) = self.swing(angle=99 * PI / 100, ax_shift=3 * DOWN, pendulum_shift=3.5 * DOWN,duration=10, height=3,color=RED)
        self.wait(10)

    def swing(self, ax_shift=0, pendulum_shift=0, angle=0, duration=2, height=2,color = BLUE):
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-180, 180, 90],
            x_length=7,
            y_length=height,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": np.arange(0, 10, 1),
                "numbers_with_eleongated_tics": np.arange(0, 10, 1),
            },
            y_axis_config={
                "numbers_to_include": np.arange(-180, 181, 90),
                "numbers_with_eleongated_tics": np.arange(-180, 181, 90),
            },
            include_tip=True,
        )
        labels = ax.get_axis_labels(x_label="t", y_label=r"\varphi(t)")
        labels.scale(0.5)
        labels[1].shift(-0.3 * UP + 1.5 * LEFT)
        labels[0].shift(1.3 * RIGHT + 0.5 * DOWN)
        ax.add(labels)
        ax.shift(3 * LEFT + 0.8 * UP)
        self.add(ax)
        ax.shift(ax_shift)

        t = ValueTracker(0)
        t.add_updater(lambda mobject, dt: mobject.increment_value(dt))

        l = 1
        init_angle = angle
        phi = ValueTracker(init_angle)
        omega = ValueTracker(0)
        omega.add_updater(lambda mobject, dt: mobject.increment_value(-10 / l * np.sin(phi.get_value()) * dt))
        phi.add_updater(lambda mobject, dt: mobject.increment_value(omega.get_value() * dt))

        draw_pendulum = (lambda: Pendulum(2 * l, central_color = color).shift(4 * RIGHT + pendulum_shift).rotate(phi.get_value()))
        pendulum_anim = always_redraw(draw_pendulum)

        draw_graph = (lambda: ax.add(Dot().set_style(fill_color=color, stroke_color=color, stroke_width=4).move_to(
            ax.coords_to_point(t.get_value(), phi.get_value() * 180 / PI))))
        graph = always_redraw(draw_graph)

        self.add(t, omega, phi)
        self.add(pendulum_anim, graph)
        self.wait(duration)
        t.clear_updaters()
        phi.clear_updaters()
        omega.clear_updaters()
        pendulum_anim.clear_updaters()

        return pendulum_anim, ax


def align_formulas_with_equal(f1, f2, i1, i2):
    c1 = f1[i1].get_center()
    c2 = f2[i2].get_center()
    distance = c2 - c1
    f1.shift(RIGHT * distance[0])


class Pendulum(VGroup, ABC):
    def __init__(self, length=3,central_color=BLUE, **kwargs):
        VGroup.__init__(self, **kwargs)

        self.circle = Circle()
        self.circle.set_color(central_color)
        self.circle.scale(0.25)
        self.circle.set_style(fill_color=central_color, fill_opacity=1, stroke_color=YELLOW, stroke_width=5)
        self.line = Line(length * UP, self.circle.get_center())
        self.line.set_style(stroke_width=5, stroke_color=YELLOW)

        self.pivot = self.line.get_all_points()[0]

        self.add(self.line)
        self.add(self.circle)

    def shift(self,s):
        super().shift(s)
        self.pivot=self.pivot+s
        return self

    def get_top(self):
        return self.line.get_all_points()[0]

    def get_center(self):
        return self.circle.get_center()

    def get_rode(self):
        return self.line

    def get_body(self):
        return self.circle

    def remove(self, scene):
        scene.remove(self.line,self.circle)

    def fadeout(self, scene):
        scene.play(FadeOut(self.line),FadeOut(self.circle))

    def rotate(self, angle=0):
        self.circle.rotate(angle=angle, about_point=self.pivot)
        self.line.rotate(angle=angle, about_point=self.pivot)
        return self

    def play(self, scene):
        scene.play(Create(self.line))
        scene.play(GrowFromCenter(self.circle))


class Application3(Scene):
    def construct(self):
        title = Tex("Double Pendulum")
        title.to_edge(UP)
        title.shift(0.1 * RIGHT)
        title.set_color(BLUE)

        self.add(title)
        self.wait(2)

        lines = [MathTex(r"E_\text{pot}", "=",r"mgl(1-\cos\varphi_1)","+",r"mgl(1-\cos\varphi_1)+mgl(1-\cos\varphi_2)"),
                 MathTex(r"E_\text{kin}", "=", r"\tfrac{1}{2} m l^2 \dot\varphi_1^2","+", r"\tfrac{1}{2} m l^2 \dot\varphi_1^2+\tfrac{1}{2} m l^2\dot\varphi_2^2","+",r"m l^2 \cos(\varphi_1-\varphi_2)\dot \varphi_1\dot\varphi_2"),
                 MathTex("S","=",r"\int  m l^2 (\dot\varphi_1^2+\tfrac{1}{2}\dot\varphi_2^2+\cos(\varphi_1-\varphi_2)\dot\varphi_1\dot\varphi_2)-2mgl(1-\cos\varphi_1)-mgl(1-\cos\varphi_2)\rm{d}t")]

        lines[0].next_to(title,DOWN)
        lines[0].to_edge(LEFT)
        lines[0][2].set_color(BLUE)
        lines[0][4:7].set_color(RED)
        lines[1][2].set_color(BLUE)
        lines[1][4].set_color(RED)
        lines[1][6].set_color(PURPLE)
        lines[2].set_color(YELLOW)
        lines[2][2].scale(0.7)
        lines[2][2].next_to(lines[2][1],RIGHT)

        alpha1 = 0.2 *PI
        l = 2
        alpha2 = 0.1 *PI
        p=Pendulum(l,BLUE).shift(DOWN).rotate(alpha1)
        p2=Pendulum(l,RED).shift(DOWN+l*np.cos(alpha1)*DOWN+l*np.sin(alpha1)*RIGHT).rotate(alpha2)
        p.play(self)
        p2.play(self)
        self.wait(2)

        for i in range(0,len(lines)):
            if i>0:
                lines[i].next_to(lines[i - 1], DOWN)
                align_formulas_with_equal(lines[i], lines[i-1], 1, 1)
            for j in range(0,len(lines[i])):
                self.play(Write(lines[i][j]))
                self.wait()

        self.play(FadeOut(lines[0]),FadeOut(lines[1]))
        self.play(ApplyMethod(lines[2].next_to,title,DOWN),FadeOut(p), FadeOut(p2))
        self.wait(2)
        self.swing2(angle1=2*PI/3,angle2=3*PI/4,duration=10)
        self.swing3(angle1=2*PI/3,angle2=2*PI/3,duration=10)
        self.wait(5)

    def swing2(self, angle1=PI/6, angle2=-PI/6, duration=2, height=2,color1=BLUE,color2=RED):
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-180, 180, 90],
            x_length=7,
            y_length=height,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": np.arange(0, 10, 1),
                "numbers_with_eleongated_tics": np.arange(0, 10, 1),
            },
            y_axis_config={
                "numbers_to_include": np.arange(-180, 181, 90),
                "numbers_with_eleongated_tics": np.arange(-180, 181, 90),
            },
            include_tip=True,
        )
        labels = ax.get_axis_labels(x_label="t", y_label=r"\varphi(t)")
        labels.scale(0.5)
        labels[1].shift(-0.3 * UP + 1.5 * LEFT)
        labels[0].shift(1.3 * RIGHT + 0.5 * DOWN)
        ax.add(labels)
        ax.shift(3 * LEFT + 1*UP)
        self.add(ax)

        ax2 = Axes(
            x_range=[0, 10, 1],
            y_range=[-180, 180, 90],
            x_length=7,
            y_length=height,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": np.arange(0, 10, 1),
                "numbers_with_eleongated_tics": np.arange(0, 10, 1),
            },
            y_axis_config={
                "numbers_to_include": np.arange(-180, 181, 90),
                "numbers_with_eleongated_tics": np.arange(-180, 181, 90),
            },
            include_tip=True,
        )
        labels = ax2.get_axis_labels(x_label="t", y_label=r"\varphi(t)")
        labels.scale(0.5)
        labels[1].shift(-0.3 * UP + 1.5 * LEFT)
        labels[0].shift(1.3 * RIGHT + 0.5 * DOWN)
        ax2.add(labels)
        ax2.shift(3 * LEFT + 1*UP)
        ax2.shift(3*DOWN)
        self.add(ax2)

        t = ValueTracker(0)
        t.add_updater(lambda mobject, dt: mobject.increment_value(dt))

        l = 1
        g = 10
        f = 0.1
        phi = ValueTracker(angle1)
        phi2 = ValueTracker(angle2)
        omega = ValueTracker(0)
        omega2 = ValueTracker(0)

        rhs_phi = lambda phi,phi2,omega,omega2: (-f*omega-2*g/l*np.sin(phi)-np.sin(phi-phi2)*np.cos(phi-phi2)*omega*omega+g/l*np.cos(phi-phi2)*np.sin(phi2)-np.sin(phi-phi2)*omega2*omega2)/(2-np.cos(phi-phi2)**2)
        rhs_phi2= lambda phi,phi2,omega,omega2: (-f*omega2-2*g/l*np.sin(phi2)+np.sin(phi-phi2)*np.cos(phi-phi2)*omega2*omega2+2*g/l*np.cos(phi-phi2)*np.sin(phi)+2*np.sin(phi-phi2)*omega*omega)/(2-np.cos(phi-phi2)**2)

        omega.add_updater(lambda mobject, dt: mobject.increment_value(rhs_phi(phi.get_value(),phi2.get_value(),omega.get_value(),omega2.get_value()) * dt))
        omega2.add_updater(lambda mobject, dt: mobject.increment_value(rhs_phi2(phi.get_value(),phi2.get_value(),omega.get_value(),omega2.get_value()) * dt))
        phi.add_updater(lambda mobject, dt: mobject.increment_value(omega.get_value() * dt))
        phi2.add_updater(lambda mobject, dt: mobject.increment_value(omega2.get_value() * dt))

        yoff = 2*DOWN
        draw_pendulum = (lambda: Pendulum(2 * l,color = color1).shift(3*RIGHT+yoff).rotate(phi.get_value()))
        draw_pendulum2 = (lambda: Pendulum(2*l, color = color2).shift((2*l*np.sin(phi.get_value())+3)*RIGHT+2*l*np.cos(phi.get_value())*DOWN+yoff).rotate(phi2.get_value()))
        pendulum_anim = always_redraw(draw_pendulum)
        pendulum_anim2 = always_redraw(draw_pendulum2)

        def mod_phi(x):
            while x>PI:
                x=x-2*PI
            while x<-PI:
                x=x+2*PI
            return x

        draw_graph = (lambda: ax.add(Dot().set_style(fill_color=color1, stroke_color=color1, stroke_width=4).scale(0.25).move_to(
            ax.coords_to_point(t.get_value(), mod_phi(phi.get_value()) * 180 / PI))))
        draw_graph2 = (lambda: ax2.add(Dot().set_style(fill_color=color2, stroke_color=color2, stroke_width=4).scale(0.25).move_to(
            ax2.coords_to_point(t.get_value(), mod_phi(phi2.get_value()) * 180 / PI))))
        graph = always_redraw(draw_graph)
        graph2 = always_redraw(draw_graph2)

        self.add(t, omega, phi,omega2,phi2)
        self.add(pendulum_anim, graph,pendulum_anim2,graph2)
        self.wait(duration)
        t.clear_updaters()
        phi.clear_updaters()
        phi2.clear_updaters()
        omega.clear_updaters()
        omega2.clear_updaters()
        pendulum_anim.clear_updaters()
        pendulum_anim2.clear_updaters()
        self.play(FadeOut(pendulum_anim),FadeOut(pendulum_anim2))

    def swing3(self,angle1=PI/6, angle2=-PI/6, duration=2, height=2,color1=PURPLE,color2=YELLOW):
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-180, 180, 90],
            x_length=7,
            y_length=height,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": np.arange(0, 10, 1),
                "numbers_with_eleongated_tics": np.arange(0, 10, 1),
            },
            y_axis_config={
                "numbers_to_include": np.arange(-180, 181, 90),
                "numbers_with_eleongated_tics": np.arange(-180, 181, 90),
            },
            include_tip=True,
        )
        labels = ax.get_axis_labels(x_label="t", y_label=r"\varphi(t)")
        labels.scale(0.5)
        labels[1].shift(-0.3 * UP + 1.5 * LEFT)
        labels[0].shift(1.3 * RIGHT + 0.5 * DOWN)
        ax.add(labels)
        ax.shift(3 * LEFT + 1 * UP)
        self.add(ax)

        ax2 = Axes(
            x_range=[0, 10, 1],
            y_range=[-180, 180, 90],
            x_length=7,
            y_length=height,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": np.arange(0, 10, 1),
                "numbers_with_eleongated_tics": np.arange(0, 10, 1),
            },
            y_axis_config={
                "numbers_to_include": np.arange(-180, 181, 90),
                "numbers_with_eleongated_tics": np.arange(-180, 181, 90),
            },
            include_tip=True,
        )
        labels = ax2.get_axis_labels(x_label="t", y_label=r"\varphi(t)")
        labels.scale(0.5)
        labels[1].shift(-0.3 * UP + 1.5 * LEFT)
        labels[0].shift(1.3 * RIGHT + 0.5 * DOWN)
        ax2.add(labels)
        ax2.shift(3 * LEFT + 1 * UP)
        ax2.shift(3 * DOWN)
        self.add(ax2)

        t = ValueTracker(0)
        t.add_updater(lambda mobject, dt: mobject.increment_value(dt))

        l = 1
        g = 10
        f = 0.1
        phi = ValueTracker(angle1)
        phi2 = ValueTracker(angle2)
        omega = ValueTracker(0)
        omega2 = ValueTracker(0)

        rhs_phi = lambda phi,phi2,omega,omega2: (-f*omega-2*g/l*np.sin(phi)-np.sin(phi-phi2)*np.cos(phi-phi2)*omega*omega+g/l*np.cos(phi-phi2)*np.sin(phi2)-np.sin(phi-phi2)*omega2*omega2)/(2-np.cos(phi-phi2)**2)
        rhs_phi2= lambda phi,phi2,omega,omega2: (-f*omega2-2*g/l*np.sin(phi2)+np.sin(phi-phi2)*np.cos(phi-phi2)*omega2*omega2+2*g/l*np.cos(phi-phi2)*np.sin(phi)+2*np.sin(phi-phi2)*omega*omega)/(2-np.cos(phi-phi2)**2)

        omega.add_updater(lambda mobject, dt: mobject.increment_value(rhs_phi(phi.get_value(),phi2.get_value(),omega.get_value(),omega2.get_value()) * dt))
        omega2.add_updater(lambda mobject, dt: mobject.increment_value(rhs_phi2(phi.get_value(),phi2.get_value(),omega.get_value(),omega2.get_value()) * dt))
        phi.add_updater(lambda mobject, dt: mobject.increment_value(omega.get_value() * dt))
        phi2.add_updater(lambda mobject, dt: mobject.increment_value(omega2.get_value() * dt))

        yoff = 2 * DOWN
        draw_pendulum = (lambda: Pendulum(2 * l,color = color1).shift(3*RIGHT+yoff).rotate(phi.get_value()))
        draw_pendulum2 = (lambda: Pendulum(2*l, color = color2).shift((2*l*np.sin(phi.get_value())+3)*RIGHT+2*l*np.cos(phi.get_value())*DOWN+yoff).rotate(phi2.get_value()))
        pendulum_anim = always_redraw(draw_pendulum)
        pendulum_anim2 = always_redraw(draw_pendulum2)

        def mod_phi(x):
            while x > PI:
                x = x - 2 * PI
            while x < -PI:
                x = x + 2 * PI
            return x

        draw_graph = (lambda: ax.add(Dot().set_style(fill_color=color1, stroke_color=color1, stroke_width=4).scale(0.25).move_to(
        ax.coords_to_point(t.get_value(), mod_phi(phi.get_value()) * 180 / PI))))
        draw_graph2 = (lambda: ax2.add(Dot().set_style(fill_color=color2, stroke_color=color2, stroke_width=4).scale(0.25).move_to(
            ax2.coords_to_point(t.get_value(), mod_phi(phi2.get_value()) * 180 / PI))))
        graph = always_redraw(draw_graph)
        graph2 = always_redraw(draw_graph2)

        self.add(t, omega, phi,omega2,phi2)
        self.add(pendulum_anim, graph,pendulum_anim2,graph2)
        self.wait(duration)
        t.clear_updaters()
        phi.clear_updaters()
        phi2.clear_updaters()
        omega.clear_updaters()
        omega2.clear_updaters()
        pendulum_anim.clear_updaters()
        pendulum_anim2.clear_updaters()
        self.play(FadeOut(pendulum_anim), FadeOut(pendulum_anim2))


class Final(Scene):
    def construct(self):
        title = Tex("The Least Action Principle")
        title.to_edge(UP)
        title.set_color(YELLOW)
        self.play(Write(title))
        self.wait()

        tops = BulletedList("General Relativity", "The Standard Model of Particle Physics",
                            "Model Building beyond", "However: Quantum Physics")
        tops[0].set_color(RED)
        tops[1].set_color(GREEN)
        tops[2].set_color(YELLOW)
        tops[3].set_color(BLUE)

        self.play(Write(tops[0]))
        self.wait(1)
        self.play(Write(tops[1]))
        self.wait(1)
        self.play(Write(tops[2]))
        self.wait(1)
        self.play(Write(tops[3]))
        self.wait(10)


class EulerLagrange(Scene):
    def construct(self):
        title = Tex("What is the meaning of:")
        title2 = MathTex(r"\frac{\delta}{\delta x} S[\dot{x},x]=0")
        title.to_edge(UP)
        title2.next_to(title,DOWN)
        title.set_color(WHITE)
        title2.set_color(YELLOW)
        self.play(Write(title))
        self.play(Write(title2))
        self.wait()

        ax = Axes(
            x_range=[0, 1., 0.2],
            y_range=[0, 5, 1],
            x_length=4,
            y_length=4,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": [0.2, 0.4, 0.6, 0.8, 1.0],
                "numbers_with_eleongated_tics": np.arange(0, 1.1, 1),
                "label": 't',
                'decimal_number_config': {
                    'num_decimal_places': 1,
                }
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 5, 1),
                "numbers_with_eleongated_tics": np.arange(0, 5, 1),
            },
            include_tip=True,
        )
        labels = ax.get_axis_labels(x_label="t", y_label="")
        labels[0].shift(0.3 * LEFT)
        ax.add(labels)
        ax.shift(4 * RIGHT+DOWN)

        self.play(Create(ax))
        self.wait(2)

        a = Dot()
        a.set_color(YELLOW)
        a.move_to(ax.coords_to_point(0, 5))
        b = Dot()
        b.set_color(YELLOW)
        b.move_to(ax.coords_to_point(1, 0))

        self.play(Create(a), Create(b))
        self.wait(2)

        parabel = ax.get_graph(lambda x: 5 - 5 * x * x, color=RED, x_range=[0, 1])
        label = MathTex("S","=","-16.7")
        label.set_color(RED)
        label.scale(0.7)
        label.move_to(ax.coords_to_point(0.8, 3.5))
        self.play(Create(parabel))
        self.play(Write(label))
        self.wait(2)

        parabel2 = ax.get_graph(lambda x: 5 - 5 * x, color=GREEN, x_range=[0, 1])
        label2 = MathTex("S","=","-12.5")
        label2.set_color(GREEN)
        label2.scale(0.7)
        label2.move_to(ax.coords_to_point(0.4, 1.5))
        self.play(Create(parabel2))
        self.play(Write(label2))
        self.wait(2)

        label3 = MathTex(r"\delta x(t)","=",r"\varepsilon \cdot \sin(5\pi t)")
        label3.set_color(BLUE)
        label3.next_to(title2,DOWN)
        label3.to_edge(LEFT)

        label3b = MathTex(r"\varepsilon","=","0.00")
        label3b.set_color(BLUE)
        label3b.next_to(label3b,DOWN)
        align_formulas_with_equal(label3b,label3,1,1)

        l_value = DecimalNumber(0, num_decimal_places=2)
        l_value.set_color(BLUE)
        l_value.move_to(label3b[2].get_center())

        self.play(Write(label3))
        self.play(Write(label3b))
        self.play(Transform(label3b[2],l_value))
        self.wait(2)

        l = ValueTracker(0)
        self.first = True

        def reverse(dt):
            if l.get_value()<0.5 and self.first==True:
                return dt
            else:
                self.first = False
                return -dt

        l.add_updater(lambda mob,dt: mob.increment_value(reverse(0.5*dt)))
        perturbation = always_redraw(lambda: ax.get_graph(lambda x: l.get_value() * np.sin(5 * 3.141592654 * x), color=BLUE, x_range=[0, 1]))
        l_value_dyn=always_redraw(lambda: l_value.set_value(l.get_value()))

        self.add(l)
        self.add(perturbation)
        self.remove(label3b[2])
        self.add(l_value_dyn)
        self.wait(2)
        l.clear_updaters()
        self.play(FadeOut(perturbation))
        self.wait(2)

        S_value = DecimalNumber(-50/3, num_decimal_places=1)
        S_value.set_color(RED)
        S_value.set_scale(0.7)
        S_value.move_to(label[2].get_center())
        S2_value = DecimalNumber(-50/4, num_decimal_places=1)
        S2_value.set_color(GREEN)
        S2_value.set_scale(0.7)
        S2_value.move_to(label2[2].get_center())

        pi = 3.141592654

        l.add_updater(lambda mob, dt: mob.increment_value(reverse(0.125*dt)))
        pert_parabel = always_redraw(lambda: ax.get_graph(lambda x: 5-5*x*x+l.get_value() * np.sin(5 * 3.141592654 * x), color = RED, x_range=[0, 1]))
        pert_parabel2 = always_redraw(lambda: ax.get_graph(lambda x:5-5*x+ l.get_value() * np.sin(5 * 3.141592654 * x), color = GREEN, x_range=[0, 1]))
        S_value_dyn = always_redraw(lambda: S_value.set_value(-50/3+25/4*pi*pi*l.get_value()*l.get_value()))
        S2_value_dyn = always_redraw(lambda: S2_value.set_value(-50/4+25/4*pi*pi*l.get_value()*l.get_value()-16*l.get_value()))

        self.first = True
        l.set_value(0)
        self.remove(parabel2,parabel)
        self.add(pert_parabel,pert_parabel2,l,S_value,S2_value)
        self.remove(label2[2],label[2])
        self.wait(8)
        l.clear_updaters()
        self.play(FadeOut(l_value),FadeOut(l_value_dyn),FadeOut(label3b))
        self.wait(2)

        label4 = MathTex(r"\delta S","=",r"S[x(t)+\delta x(t)]-S[x(t)]")
        label4.set_color(WHITE)
        label4.set_scale(0.5)
        label4.next_to(label3, DOWN)
        align_formulas_with_equal(label4, label3, 1, 1)

        label5 = MathTex(r"\delta S","=",r"\frac{\delta S}{\delta x} \delta x+\mathcal{O}\left(\delta x^2\right)")
        label5.set_color(WHITE)
        label5.set_scale(0.5)
        label5.next_to(label4, DOWN)
        align_formulas_with_equal(label5, label4, 1, 1)

        self.play(Write(label4))
        self.play(Write(label5))

        ax2 = Axes(
            x_range=[0, 0.01, 0.005],
            y_range=[-0.006, 0.006, 0.002],
            x_length=4,
            y_length=2,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": [ 0.005, 0.01],
                "label": 't',
                'decimal_number_config': {
                    'num_decimal_places': 3,
                }
            },
            y_axis_config={
                "numbers_to_include":[],
            },
            include_tip=True,
        )
        labels = ax2.get_axis_labels(x_label=r"\varepsilon", y_label="")
        labels[0].shift(0.3 * LEFT+0.35*DOWN)
        ax2.add(labels)
        ax2.shift(4 * LEFT + 2.5*DOWN)

        self.play(Create(ax2))
        self.wait(2)

        dS = ax2.get_graph((lambda x:25/4*pi*pi*x*x),color=RED,x_range=[0,0.01])
        dS2 = ax2.get_graph((lambda x:25/4*pi*pi*x*x-4/pi*x),color=GREEN,x_range=[0,0.01])
        dS_label = MathTex(r"\delta S")
        dS_label.set_color(RED)
        dS_label.move_to(ax2.coords_to_point(0.01,0.004))
        dS2_label = MathTex(r"\delta S")
        dS2_label.set_color(GREEN)
        dS2_label.move_to(ax2.coords_to_point(0.01, -0.005))
        self.play(Create(dS),Write(dS_label))
        self.wait(2)
        self.play(Create(dS2),Write(dS2_label))

        self.wait(10)


class EulerLagrange2(Scene):
    def construct(self):
        title = Tex("What is the meaning of:")
        title2 = MathTex(r"\frac{\delta}{\delta \vec{x}} S[\dot{\vec{x}},\vec{x}]=0")
        title.to_edge(UP)
        title2.next_to(title,DOWN)
        title.set_color(WHITE)
        title2.set_color(YELLOW)
        self.play(Write(title))
        self.play(Write(title2))
        self.wait()



        lines = [
            MathTex(r"S[\dot{\vec{x}},\vec{x}]","=",r"\int_{t_1}^{t_2} L(\dot{\vec{x}},\vec{x}) {\rm d}t"),
            MathTex(r"\delta S[\dot{\vec{x}},\vec{x}]","=",r"\int_{t_1}^{t_2} \left(\frac{\partial L}{\partial \dot{\vec{x}}} \cdot \delta \dot{\vec{x}}+\frac{\partial L}{\partial \vec{x}} \cdot \delta \vec{x}\right) {\rm d}t"),
        ]

        lines[0].scale(0.7)
        lines[0].next_to(title2,DOWN)
        lines[0].to_edge(LEFT)

        for i in range(0,len(lines)):
            if i>0:
                lines[i].scale(0.7)
                lines[i].next_to(lines[i - 1], DOWN)
                align_formulas_with_equal(lines[i], lines[i-1], 1, 1)
            if i==1:
                graph(self)
            for j in range(0,len(lines[i])):
                self.play(Write(lines[i][j]))
                self.wait()

        self.wait(2)
