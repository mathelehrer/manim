import cmath
import math
from abc import ABC

import numpy as np
from manim import *
from typing import Iterable
import csv
from cmath import *


def align_formulas_with_equal(f1, f2, i1, i2):
    c1 = f1[i1].get_center()
    c2 = f2[i2].get_center()
    distance = c2 - c1
    f1.shift(RIGHT * distance[0])


class Fourier(Scene):
    def construct(self):
        title = MathTex(r"\text{The step function: }", r"(-1)^{\left \lfloor{\tfrac{x}{\pi}}\right \rfloor }")
        title.to_edge(UP)
        title.set_color(YELLOW)
        self.play(Write(title))

        ax = Axes(
            x_range=[-0, 4 * np.pi + 1],
            y_range=[-1.5, 1.5],
            x_length=10,
            y_length=5,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(0, 4 * np.pi, 1),
                "color": GRAY
            },
            y_axis_config={
                "numbers_to_include": np.arange(-1, 1.1, 1),
                "color": GRAY
            },
            tips=True,
        )
        labels = ax.get_axis_labels(x_label="x", y_label="y")
        labels[0].shift(0.4 * DOWN)
        labels[1].shift(0.4 * LEFT)
        labels.set_color(WHITE)
        ax.add(labels)
        ax.set_color(WHITE)

        def rectilinear(x):
            if int(x / np.pi) % 2 == 0:
                return 1
            else:
                return -1

        rect1 = ax.get_graph(lambda x: rectilinear(x), color=YELLOW, x_range=[0, 0.99 * np.pi])
        rect2 = ax.get_graph(lambda x: rectilinear(x), color=YELLOW, x_range=[1.01 * np.pi, 1.99 * np.pi])
        rect3 = ax.get_graph(lambda x: rectilinear(x), color=YELLOW, x_range=[2.01 * np.pi, 2.99 * np.pi])
        rect4 = ax.get_graph(lambda x: rectilinear(x), color=YELLOW, x_range=[3.01 * np.pi, 3.99 * np.pi])

        pi_labels = MathTex(r"\pi",r"2\pi",r"3\pi",r"4\pi")
        pi_labels.set_color(YELLOW)
        for i,l in enumerate(pi_labels):
            l.move_to(ax.coords_to_point((i+1)*np.pi,0.11))

        origin = ax.coords_to_point(0, 0)
        self.play(Create(ax))
        self.wait(1)
        self.play(Create(rect1))
        self.play(Write(pi_labels[0]))
        self.play(Create(rect2))
        self.play(Write(pi_labels[1]))
        self.play(Create(rect3))
        self.play(Write(pi_labels[2]))
        self.play(Create(rect4))
        self.play(Write(pi_labels[3]))
        self.wait(1)

        def harmonic(x, n):
            return np.sin(x * n) * 4 / n / np.pi

        def approx(x, n):
            result = 0
            for i in range(1, 2 * n, 2):
                result = result + np.sin(x * i) * 4 / i / np.pi
            return result

        t = ValueTracker(0)
        t.add_updater(lambda mobject, dt: mobject.increment_value(dt / 10))

        colors = color_gradient([GREEN, BLUE],100)

        draw_harmonic = (lambda: ax.get_graph(lambda x: max(0,(1-t.get_value()))*harmonic(x,3),color=BLUE,x_range=[0,4*np.pi]))
        draw_result = (lambda: ax.get_graph(lambda x: approx(x,1)+min(t.get_value(),1)*harmonic(x,3),
                                            color=colors[min(len(colors)-1,int(t.get_value()*len(colors)))],x_range=[0,4*np.pi]))

        approx1 = ax.get_graph(lambda x: approx(x, 1), color=GREEN, x_range=[0, 4 * np.pi])
        approx2 = ax.get_graph(lambda x: approx(x, 2), color=BLUE, x_range=[0, 4 * np.pi])
        approx3 = ax.get_graph(lambda x: approx(x, 3), color=RED, x_range=[0, 4 * np.pi])
        approx4 = ax.get_graph(lambda x: approx(x, 50), color=WHITE, x_range=[0, 4 * np.pi, 0.001])

        functions = []
        function = MathTex(r"\tfrac{4}{\pi}\sin(x)")
        function.set_color(GREEN)
        functions.append(function)
        function2 = MathTex(r"\tfrac{4}{\pi}\sin(x)+\tfrac{4}{3\pi}\sin(3x)")
        function2.set_color(BLUE)
        functions.append(function2)
        function3 = MathTex(r"\tfrac{4}{\pi}\sin(x)+\tfrac{4}{3\pi}\sin(3x)+\tfrac{4}{5\pi}\sin(5x)")
        function3.set_color(RED)
        functions.append(function3)
        function4 = MathTex(
            r"\tfrac{4}{\pi}\sin(x)+\tfrac{4}{3\pi}\sin(3x)+\tfrac{4}{5\pi}\sin(5x)+\dots+\tfrac{4}{49\pi}\sin(49x)")
        function4.set_color(WHITE)
        functions.append(function4)
        for function in functions:
            function.next_to(ax, DOWN)

        self.play(Create(approx1), Write(functions[0]))
        self.wait(2)

        self.add(t)
        removable = always_redraw(draw_harmonic)
        self.play(Create(removable),Create(always_redraw(draw_result)),rate_func=smooth)
        self.wait(10)
        t.clear_updaters()
        self.play(FadeOut(removable), Transform(functions[0], functions[1]))
        self.wait(3)

        t2 = ValueTracker(0)
        t2.add_updater(lambda mobject, dt: mobject.increment_value(dt / 10))

        colors2 = color_gradient([BLUE, RED], 100)

        draw_harmonic2 = (lambda: ax.get_graph(lambda x: max(0, (1 - t2.get_value())) * harmonic(x, 5), color=RED,
                                              x_range=[0, 4 * np.pi]))
        draw_result2 = (lambda: ax.get_graph(lambda x: approx(x, 2) + min(t2.get_value(), 1) * harmonic(x, 5),
                                            color=colors2[min(len(colors2) - 1, int(t2.get_value() * len(colors2)))] ,
                                            x_range=[0, 4 * np.pi]))

        self.add(t2)
        removable2 = always_redraw(draw_harmonic2)
        self.play(Create(removable2), Create(always_redraw(draw_result2)), rate_func=smooth)
        self.wait(10)
        t2.clear_updaters()
        self.play(FadeOut(removable2), Transform(functions[0], functions[2]))
        self.wait(3)


        self.play(Create(approx4), Transform(functions[0], functions[3]))
        self.wait(3)

        self.wait(10)


class Fourier_Trailer(Scene):
    def construct(self):
        title = MathTex(r"\text{The step function: }", r"(-1)^{\left \lfloor{\tfrac{x}{\pi}}\right \rfloor }")
        title.to_edge(UP)
        title.set_color(YELLOW)
        # self.play(Write(title))

        ax = Axes(
            x_range=[-0, 4 * np.pi + 1],
            y_range=[-1.5, 1.5],
            x_length=10,
            y_length=5,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(0, 4 * np.pi, 1),
                "color": GRAY
            },
            y_axis_config={
                "numbers_to_include": np.arange(-1, 1.1, 1),
                "color": GRAY
            },
            tips=True,
        )
        labels = ax.get_axis_labels(x_label="x", y_label="y")
        labels[0].shift(0.4 * DOWN)
        labels[1].shift(0.4 * LEFT)
        labels.set_color(WHITE)
        ax.add(labels)
        ax.set_color(WHITE)

        def rectilinear(x):
            if int(x / np.pi) % 2 == 0:
                return 1
            else:
                return -1

        rect1 = ax.get_graph(lambda x: rectilinear(x), color=YELLOW, x_range=[0, 0.99 * np.pi])
        rect2 = ax.get_graph(lambda x: rectilinear(x), color=YELLOW, x_range=[1.01 * np.pi, 1.99 * np.pi])
        rect3 = ax.get_graph(lambda x: rectilinear(x), color=YELLOW, x_range=[2.01 * np.pi, 2.99 * np.pi])
        rect4 = ax.get_graph(lambda x: rectilinear(x), color=YELLOW, x_range=[3.01 * np.pi, 3.99 * np.pi])

        origin = ax.coords_to_point(0, 0)
        self.play(Create(ax))
        self.wait(1)
        self.play(Create(rect1))
        self.play(Create(rect2))
        self.play(Create(rect3))
        self.play(Create(rect4))
        self.wait(1)

        def approx(x, n):
            result = 0
            for i in range(1, 2 * n, 2):
                result = result + np.sin(x * i) * 4 / i / np.pi
            return result

        approx1 = ax.get_graph(lambda x: approx(x, 1), color=GREEN, x_range=[0, 4 * np.pi])
        approx2 = ax.get_graph(lambda x: approx(x, 2), color=BLUE, x_range=[0, 4 * np.pi])
        approx3 = ax.get_graph(lambda x: approx(x, 3), color=RED, x_range=[0, 4 * np.pi])
        approx4 = ax.get_graph(lambda x: approx(x, 100), color=WHITE, x_range=[0, 4 * np.pi, 0.001])

        functions = []
        function = MathTex(r"\tfrac{4}{\pi}\sin(x)")
        function.set_color(GREEN)
        functions.append(function)
        function2 = MathTex(r"\tfrac{4}{\pi}\sin(x)+\tfrac{4}{3\pi}\sin(3x)")
        function2.set_color(BLUE)
        functions.append(function2)
        function3 = MathTex(r"\tfrac{4}{\pi}\sin(x)+\tfrac{4}{3\pi}\sin(3x)+\tfrac{4}{5\pi}\sin(5x)")
        function3.set_color(RED)
        functions.append(function3)
        function4 = MathTex(
            r"\tfrac{4}{\pi}\sin(x)+\tfrac{4}{3\pi}\sin(3x)+\tfrac{4}{5\pi}\sin(5x)+\dots+\tfrac{4}{99\pi}\sin(99x)")
        function4.set_color(WHITE)
        functions.append(function4)
        for function in functions:
            function.next_to(ax, DOWN)
        self.play(Create(approx1))
        self.wait(3)
        self.play(Create(approx2))
        self.wait(3)
        self.play(Create(approx3))
        self.wait(3)
        self.play(Create(approx4))
        self.wait(3)

        self.wait(10)


class Fourier2(Scene):
    def construct(self):
        title = Tex("Fourier's theorem")
        title.to_edge(UP)
        title.set_color(YELLOW)
        self.play(Write(title))

        conclusion = MathTex(r"(-1)^{\left \lfloor{\tfrac{x}{\pi}}\right \rfloor }", "=",
                             r"\tfrac{4}{\pi}\sin(x)+\tfrac{4}{3\pi}\sin(3x)+\tfrac{4}{5\pi}\sin(5x)+\dots")
        conclusion.set_color(YELLOW)
        conclusion.next_to(title, DOWN)

        theorem = MathTex(r"(-1)^{\left \lfloor{\tfrac{x}{\pi}}\right \rfloor} ", "=", r"\sum_{n=0}^\infty", r"a_n",
                          r"\sin(n\cdot x)+", "b_n", r"\cos(n\cdot x)")
        theorem.set_color(WHITE)
        theorem.scale(0.7)
        theorem.next_to(conclusion, DOWN)
        theorem.to_edge(LEFT)

        theorem2 = MathTex(r"a_n", r"=",
                           r"\tfrac{1}{\pi}\int\limits_{0}^{2\pi}(-1)^{\left \lfloor{\tfrac{x}{\pi}}\right \rfloor} \sin(n\cdot x) {\rm d} x")

        theorem3 = MathTex(r"b_n", r"=",
                           r"\tfrac{1}{\pi}\int\limits_{0}^{2\pi}(-1)^{\left \lfloor{\tfrac{x}{\pi}}\right \rfloor} \cos(n\cdot x) {\rm d} x")
        theorem2.set_color(GREEN)
        theorem3.set_color(RED)
        theorem2.scale(0.7)
        theorem3.scale(0.7)
        theorem2.next_to(theorem, DOWN)
        solution1 = MathTex(r" a_n", "=",
                            r"\left\{0,\tfrac{4}{\pi},0,\tfrac{4}{3\pi},0,\tfrac{4}{5\pi},\dots\right\}")
        solution1.set_color(GREEN)
        solution1.scale(0.7)
        solution1.next_to(theorem2, DOWN)
        align_formulas_with_equal(solution1, theorem2, 1, 1)

        theorem3.next_to(solution1, DOWN)
        align_formulas_with_equal(theorem2, theorem, 1, 1)
        align_formulas_with_equal(theorem3, theorem2, 1, 1)
        self.play(Write(conclusion))
        self.wait(3)
        self.play(Write(theorem))
        self.wait(3)
        self.play(ApplyMethod(theorem[3].set_color, GREEN), Transform(theorem[3].copy(), theorem2[0]))
        self.play(Write(theorem2[1:]))
        self.wait(3)
        self.play(ApplyMethod(theorem[5].set_color, RED), Transform(theorem[5].copy(), theorem3[0]))
        self.play(Write(theorem3[1:]))
        self.wait(3)

        solution2 = MathTex(r"b_n", "=", r"\left\{0,0,0,0,0,0,\dots\right\}")
        solution2.set_color(RED)
        solution2.scale(0.7)
        solution2.next_to(theorem3, DOWN)
        align_formulas_with_equal(solution2, solution1, 1, 1)

        self.play(Write(solution1))
        self.wait(3)
        self.play(Write(solution2))
        self.wait(10)


class Primes(Scene):
    def construct(self):
        title = MathTex(r"\text{The prime counting function: }", "\pi(x)")
        title.to_edge(UP)
        title.set_color(YELLOW)
        self.play(Write(title))

        prime_dist = [0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 11,
                      11, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 16, 16, 16,
                      16, 16, 16, 17, 17, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 20, 20, 21, 21, 21, 21, 21, 21, 22,
                      22, 22, 22, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25]
        primes = [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                  101]

        def pdf(x):
            return prime_dist[int(x)]

        ax = Axes(
            x_range=[0, 110],
            y_range=[0, 30],
            x_length=13,
            y_length=6,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(0, 101, 10),
                "tick_size": 0.03,
                "longer_tick_multiple": 3,
                "numbers_with_elongated_ticks": np.arange(0, 101, 5),
                "color": GRAY,
                "font_size": 18,
                "line_to_number_buff": 1.3 * MED_SMALL_BUFF
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 30, 5),
                "color": GRAY
            },
            tips=True,
        )
        labels = ax.get_axis_labels(x_label="x", y_label="\\pi(x)")
        labels[0].shift(0.4 * DOWN)
        labels[1].shift(0.4 * LEFT)
        labels.set_color(WHITE)
        labels[1].set_color(YELLOW)
        ax.add(labels)
        ax.set_color(WHITE)

        prime_graphs = []
        for i in range(0, len(primes) - 1):
            prime_graphs.append(
                ax.get_graph(lambda x: pdf(x), color=YELLOW, x_range=[primes[i] + 0.01, primes[i + 1] - 0.01, 0.1]))
        self.play(Create(ax))
        self.wait(3)
        for i in range(0, len(prime_graphs)):
            if i > 0:
                lab = MathTex(primes[i])
                lab.scale(0.7)
                lab.set_color(YELLOW)
                lab.move_to(ax.coords_to_point(primes[i], -2 + (-1) ** (i + 1)))
                self.play(Create(prime_graphs[i]), Write(lab))
            else:
                self.play(Create(prime_graphs[i]))
        self.wait(3)

        self.wait(10)


class Primes2(Scene):
    def construct(self):
        title = MathTex(r"\text{The prime counting function: }", "\pi(x)")
        title.to_edge(UP)
        title.set_color(YELLOW)

        prime_dist = [0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 11,
                      11, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 16, 16, 16,
                      16, 16, 16, 17, 17, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 20, 20, 21, 21, 21, 21, 21, 21, 22,
                      22, 22, 22, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25]
        prime_dist2 = [0., 0., 1., 2., 2.5, 3.5, 3.5, 4.5, 4.83333, 5.33333, 5.33333, 6.33333, 6.33333, 7.33333,
                       7.33333, 7.33333, 7.58333, 8.58333, 8.58333, 9.58333, 9.58333, 9.58333, 9.58333, 10.5833,
                       10.5833, 11.0833, 11.0833, 11.4167, 11.4167, 12.4167, 12.4167, 13.4167, 13.6167, 13.6167,
                       13.6167, 13.6167, 13.6167]
        primes = [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                  101]
        primes2 = [0, 2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29, 31, 32, 37]
        primes2_labels = ["0", " 2", " 3", "2^2", " 5", " 7", " 2^3", " 3^2", " 11", " 13", "2^4", " 17", " 19", " 23",
                          " 5^2", " 3^3", " 29", " 31", " 2^5", " 37"]

        prime_color = [YELLOW, YELLOW, YELLOW, RED, YELLOW, YELLOW, GREEN, RED, YELLOW, YELLOW, BLUE, YELLOW, YELLOW,
                       YELLOW, RED, GREEN, YELLOW, YELLOW, ORANGE, YELLOW]

        def pdf(x):
            return prime_dist[int(x)]

        def pdf2(x):
            return prime_dist2[int(x)]

        ax = Axes(
            x_range=[0, 110],
            y_range=[0, 30],
            x_length=13,
            y_length=6,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(0, 101, 10),
                "tick_size": 0.03,
                "longer_tick_multiple": 3,
                "numbers_with_elongated_ticks": np.arange(0, 101, 5),
                "color": GRAY,
                "font_size": 18,
                "line_to_number_buff": 1.3 * MED_SMALL_BUFF
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 30, 5),
                "color": GRAY
            },
            tips=True,
        )
        labels = ax.get_axis_labels(x_label="x", y_label="\\pi(x)")
        labels[0].shift(0.4 * DOWN)
        labels[1].shift(0.4 * LEFT)
        labels.set_color(WHITE)
        labels[1].set_color(YELLOW)
        ax.add(labels)
        ax.set_color(WHITE)

        prime_graphs = []
        prime_labels = []
        for i in range(0, len(primes) - 1):
            prime_graphs.append(
                ax.get_graph(lambda x: pdf(x), color=YELLOW, x_range=[primes[i] + 0.01, primes[i + 1] - 0.01, 0.1]))

        for i in range(1, len(prime_graphs)):
            lab = MathTex(primes[i])
            lab.scale(0.7)
            lab.set_color(YELLOW)
            lab.move_to(ax.coords_to_point(primes[i], -2 + (-1) ** (i + 1)))
            prime_labels.append(lab);

        graph_group = VGroup(ax, *prime_graphs, *prime_labels)
        graph_group_transform = VGroup(ax, *prime_graphs)

        self.add(title, graph_group)
        self.wait(3)

        ax2 = Axes(
            x_range=[0, 39],
            y_range=[0, 15],
            x_length=13,
            y_length=6,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(0, 36, 5),
                "color": GRAY,
                "font_size": 18,
                "line_to_number_buff": 1.6 * MED_SMALL_BUFF
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 16, 5),
                "color": GRAY
            },
            tips=True,
        )
        labels2 = ax2.get_axis_labels(x_label="x", y_label="\\pi(x)")
        labels2[0].shift(0.4 * DOWN)
        labels2[1].shift(0.4 * LEFT)
        labels2.set_color(WHITE)
        labels2[1].set_color(YELLOW)
        ax2.add(labels2)
        ax2.set_color(WHITE)

        prime_graphs2 = []
        prime_labels2 = []
        for i in range(0, 12):
            prime_graphs2.append(
                ax2.get_graph(lambda x: pdf(x), color=YELLOW, x_range=[primes[i] + 0.01, primes[i + 1] - 0.01, 0.1]))

        for i in range(1, len(prime_graphs)):
            lab = MathTex(primes[i])
            lab.scale(0.7)
            if i < 13:
                lab.set_color(YELLOW)
            else:
                lab.set_color(BLACK)  # make larger primes invisible
            lab.move_to(ax2.coords_to_point(primes[i], -0.6))
            prime_labels2.append(lab);
        graph_group2 = VGroup(ax2, *prime_graphs2)

        self.play(Transform(graph_group_transform, graph_group2),
                  *[Transform(prime_labels[j], prime_labels2[j]) for j in range(0, len(prime_labels2))])
        self.play(*[ApplyMethod(prime_graphs[i].set_color, WHITE) for i in range(0, len(prime_graphs))],
                  *[ApplyMethod(prime_labels[i].set_color, WHITE) for i in range(0, 12)])
        self.wait(3)

        prime_graphs3 = []
        prime_labels3 = []
        for i in range(0, len(primes2) - 1):
            prime_graphs3.append(
                ax2.get_graph(lambda x: pdf2(x), color=prime_color[i],
                              x_range=[primes2[i] + 0.01, primes2[i + 1] - 0.01, 0.1]))

        new_labels = []
        for i in range(1, len(primes2_labels)):
            lab = MathTex(primes2_labels[i])
            lab.scale(0.7)
            lab.set_color(prime_color[i])
            if primes2[i] in primes:
                lab.move_to(ax2.coords_to_point(primes2[i], -0.6))
            else:
                lab.move_to(ax2.coords_to_point(primes2[i], -1.8))
            new_labels.append(lab)

        for i in range(0, len(prime_graphs3)):
            if i > 0:
                self.play(Create(prime_graphs3[i]), Write(new_labels[i - 1]))
            else:
                self.play(Create(prime_graphs3[i]))
            if not primes2[i] in primes:
                self.wait(3)
        self.play(Write(new_labels[i]))
        self.wait(3)

        self.remove(*prime_graphs)
        title2 = MathTex(r"\text{Riemann's prime counting function: }", r"\Pi(x)")
        title2.to_edge(UP)
        title2.set_color(YELLOW)
        new_label = MathTex(r"\Pi(x)")
        new_label.move_to(labels[1].get_center())
        new_label.set_color(YELLOW)

        self.play(Transform(title, title2), Transform(labels[1], new_label))
        self.wait(10)


class Primes3(Scene):
    def construct(self):
        title = MathTex(r"\text{Riemann's prime counting function: }", r"\Pi(x)")
        title.to_edge(UP)
        title.set_color(YELLOW)

        ax = Axes(
            x_range=[0, 39],
            y_range=[0, 15],
            x_length=13,
            y_length=6,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(0, 36, 5),
                "color": GRAY,
                "font_size": 18,
                "line_to_number_buff": 1.6 * MED_SMALL_BUFF
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 16, 5),
                "color": GRAY
            },
            tips=True,
        )
        labels = ax.get_axis_labels(x_label="x", y_label="\\Pi(x)")
        labels[0].shift(0.4 * DOWN)
        labels[1].shift(0.4 * LEFT)
        labels.set_color(WHITE)
        labels[1].set_color(YELLOW)
        ax.add(labels)

        prime_dist2 = [0., 0., 1., 2., 2.5, 3.5, 3.5, 4.5, 4.83333, 5.33333, 5.33333, 6.33333, 6.33333, 7.33333,
                       7.33333, 7.33333, 7.58333, 8.58333, 8.58333, 9.58333, 9.58333, 9.58333, 9.58333, 10.5833,
                       10.5833, 11.0833, 11.0833, 11.4167, 11.4167, 12.4167, 12.4167, 13.4167, 13.6167, 13.6167,
                       13.6167, 13.6167, 13.6167]
        primes = [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                  101]
        primes2 = [0, 2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29, 31, 32, 37]
        primes2_labels = ["0", " 2", " 3", "2^2", " 5", " 7", " 2^3", " 3^2", " 11", " 13", "2^4", " 17", " 19", " 23",
                          " 5^2", " 3^3", " 29", " 31", " 2^5", " 37"]

        prime_color = [YELLOW, YELLOW, YELLOW, RED, YELLOW, YELLOW, GREEN, RED, YELLOW, YELLOW, BLUE, YELLOW, YELLOW,
                       YELLOW, RED, GREEN, YELLOW, YELLOW, ORANGE, YELLOW]

        def pdf2(x):
            return prime_dist2[int(x)]

        prime_graphs = []
        for i in range(0, len(primes2) - 1):
            prime_graphs.append(
                ax.get_graph(lambda x: pdf2(x), color=prime_color[i],
                             x_range=[primes2[i] + 0.01, primes2[i + 1] - 0.01, 0.1]))

        new_labels = []
        later_movers = []
        for i in range(1, len(primes2_labels)):
            lab = MathTex(primes2_labels[i])
            lab.scale(0.7)
            lab.set_color(prime_color[i])
            if primes2[i] in primes:
                lab.move_to(ax.coords_to_point(primes2[i], -0.6))
            else:
                lab.move_to(ax.coords_to_point(primes2[i], -1.8))
                later_movers.append(lab)
            new_labels.append(lab)

        self.add(title, ax, *prime_graphs, *new_labels)
        dist = ax.coords_to_point(0, 1.3) - ax.coords_to_point(0, 0)
        self.play(*[ApplyMethod(later_movers[i].shift, dist[1] * UP) for i in range(0, len(later_movers))])
        self.play(*[ApplyMethod(new_labels[i].scale, 0.7) for i in range(0, len(new_labels))])
        self.wait(6)

        ranges = [r"\infty",str(14),str(50),str(77),str(101),str(123),str(143),str(163),str(182),str(201),str(219),str(236),r"\infty"]
        results=[]
        for r in ranges:
            result = MathTex(r"\Pi(x)", "=",
                             r"\frac{1}{2\pi}\int\limits_{-"+str(r)+"}^{+"+str(r)+r"}\log\left(\zeta(a+i b)\right )\frac{x^{a+i b}}{a+ i b}{\rm d}b")
            result[0].set_color(YELLOW)
            result.to_edge(RIGHT)
            result.shift(1.5 * DOWN)
            results.append(result)

        data = load_data()
        x_vals = []
        for i in range(1, len(data[0]) + 1):
            x_vals.append(37 / 1000 * i)
        dots = []
        for i in range(0, len(data)):
            dots.append(VGroup(*[Line(ax.coords_to_point(x_vals[j], data[i][j]),
                                      ax.coords_to_point(x_vals[j + 1], data[i][j + 1])).set_color(WHITE) for j in
                                 range(0, len(data[i]) - 1)]))

        self.play(Write(results[0]))
        self.wait(3)

        print(len(dots))
        for i in range(0, len(dots)):
            if i > 0:
                self.remove(dots[i - 1])
            if i==0:
                self.play(Create(dots[i]),Transform(results[0],results[1]))
            else:
                self.play(Create(dots[i]), Transform(results[0],results[i+1]))
            self.wait(2)

        rect = SurroundingRectangle(results[len(results)-1])
        self.play(Write(result))
        self.wait()
        self.play(GrowFromPoint(rect, DL))
        self.wait()
        self.wait(10)


def load_data():
    values = []
    with open(f'prime_dist_approx_37_first_hundred_step_ten.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            row_data = []
            for data in row:
                row_data.append(float(data))
            values.append(row_data)
    csvFile.close()
    return values


class Primes4(Scene):
    def construct(self):
        title = MathTex(r"\text{Riemann's prime counting function: }", r"\Pi(x)")
        title.to_edge(UP)
        title.set_color(YELLOW)

        ax = Axes(
            x_range=[0, 39],
            y_range=[0, 15],
            x_length=13,
            y_length=6,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(0, 36, 5),
                "color": GRAY,
                "font_size": 18,
                "line_to_number_buff": 1.6 * MED_SMALL_BUFF
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 16, 5),
                "color": GRAY
            },
            tips=True,
        )
        labels = ax.get_axis_labels(x_label="x", y_label="\\Pi(x)")
        labels[0].shift(0.4 * DOWN)
        labels[1].shift(0.4 * LEFT)
        labels.set_color(WHITE)
        labels[1].set_color(YELLOW)
        ax.add(labels)

        prime_dist2 = [0., 0., 1., 2., 2.5, 3.5, 3.5, 4.5, 4.83333, 5.33333, 5.33333, 6.33333, 6.33333, 7.33333,
                       7.33333, 7.33333, 7.58333, 8.58333, 8.58333, 9.58333, 9.58333, 9.58333, 9.58333, 10.5833,
                       10.5833, 11.0833, 11.0833, 11.4167, 11.4167, 12.4167, 12.4167, 13.4167, 13.6167, 13.6167,
                       13.6167, 13.6167, 13.6167]
        primes = [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                  101]
        primes2 = [0, 2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29, 31, 32, 37]
        primes2_labels = ["0", " 2", " 3", "2^2", " 5", " 7", " 2^3", " 3^2", " 11", " 13", "2^4", " 17", " 19", " 23",
                          " 5^2", " 3^3", " 29", " 31", " 2^5", " 37"]

        prime_color = [YELLOW, YELLOW, YELLOW, RED, YELLOW, YELLOW, GREEN, RED, YELLOW, YELLOW, BLUE, YELLOW, YELLOW,
                       YELLOW, RED, GREEN, YELLOW, YELLOW, ORANGE, YELLOW]

        def pdf2(x):
            return prime_dist2[int(x)]

        prime_graphs = []
        for i in range(0, len(primes2) - 1):
            prime_graphs.append(
                ax.get_graph(lambda x: pdf2(x), color=prime_color[i],
                             x_range=[primes2[i] + 0.01, primes2[i + 1] - 0.01, 0.1]))

        labels = []
        for i in range(1, len(primes2_labels)):
            lab = MathTex(primes2_labels[i])
            lab.scale(0.7)
            lab.set_color(prime_color[i])
            lab.move_to(ax.coords_to_point(primes2[i], -0.6))
            labels.append(lab)

        self.add(title, ax, *prime_graphs, *labels)

        # zoom in further
        graph_group = VGroup(ax, *prime_graphs, *labels)
        graph_group_transform = VGroup(ax, *prime_graphs)

        ax2 = Axes(
            x_range=[0, 11],
            y_range=[0, 7],
            x_length=6,
            y_length=3.5,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(0, 10, 1),
                "color": GRAY,
                "font_size": 18,
                "line_to_number_buff": 10 * LARGE_BUFF  # move out of sight
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 7, 1),
                "color": GRAY
            },
            tips=True,
        )
        labels2 = ax2.get_axis_labels(x_label="x", y_label="\\Pi(x)")
        labels2[0].shift(1 * DOWN + 0.5 * LEFT)
        labels2[1].shift(0.4 * LEFT)
        labels2.set_color(WHITE)
        labels2[1].set_color(YELLOW)
        ax2.add(labels2)
        ax2.to_edge(RIGHT)
        ax2.shift(1.5 * DOWN)

        prime_graphs2 = []
        prime_labels2 = []
        for i in range(0, 8):
            prime_graphs2.append(
                ax2.get_graph(lambda x: pdf2(x), color=prime_color[i],
                              x_range=[primes2[i] + 0.01, primes2[i + 1] - 0.01, 0.1]))

        for i in range(1, len(prime_graphs) + 1):
            lab = MathTex(primes2_labels[i])
            lab.scale(0.7)
            lab.set_color(prime_color[i])
            if i < len(prime_graphs2):
                lab.move_to(ax2.coords_to_point(primes2[i], -0.6))
            else:
                lab.move_to(ax2.coords_to_point(primes2[i] + 3, -0.6))  # move out of sight
            prime_labels2.append(lab)

        graph_group2 = VGroup(ax2, *prime_graphs2)

        title2 = MathTex(r"\text{Riemann's prime counting function}")
        title2.to_edge(UP)
        title2.set_color(YELLOW)

        self.play(Transform(title, title2), Transform(graph_group_transform, graph_group2),
                  *[Transform(labels[j], prime_labels2[j]) for j in range(0, len(prime_labels2))])
        self.wait(3)

        data = load_data2()
        x_vals = []
        for i in range(1, len(data[0]) + 1):
            x_vals.append(37 / 1000 * i)
        dots = []
        for i in range(0, len(data)):
            lines = []
            for j in range(0, len(data[i]) - 1):
                if x_vals[j] < 11:
                    lines.append(Line(ax2.coords_to_point(x_vals[j], data[i][j]),
                                      ax2.coords_to_point(x_vals[j + 1], data[i][j + 1])).set_color(WHITE))
            dots.append(VGroup(*lines))
        for i in range(0, len(dots)):
            if i > 0:
                self.remove(dots[i - 1])
            self.play(Create(dots[i]))
            self.wait(2)

        self.wait(10)


class Primes4_Trailer(Scene):
    def construct(self):
        title = MathTex(r"\text{Riemann's prime counting function: }", r"\Pi(x)")
        title.to_edge(UP)
        title.set_color(YELLOW)

        ax = Axes(
            x_range=[0, 39],
            y_range=[0, 15],
            x_length=13,
            y_length=6,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(0, 36, 5),
                "color": GRAY,
                "font_size": 18,
                "line_to_number_buff": 1.6 * MED_SMALL_BUFF
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 16, 5),
                "color": GRAY
            },
            tips=True,
        )
        labels = ax.get_axis_labels(x_label="x", y_label="\\Pi(x)")
        labels[0].shift(0.4 * DOWN)
        labels[1].shift(0.4 * LEFT)
        labels.set_color(WHITE)
        labels[1].set_color(YELLOW)
        ax.add(labels)

        prime_dist2 = [0., 0., 1., 2., 2.5, 3.5, 3.5, 4.5, 4.83333, 5.33333, 5.33333, 6.33333, 6.33333, 7.33333,
                       7.33333, 7.33333, 7.58333, 8.58333, 8.58333, 9.58333, 9.58333, 9.58333, 9.58333, 10.5833,
                       10.5833, 11.0833, 11.0833, 11.4167, 11.4167, 12.4167, 12.4167, 13.4167, 13.6167, 13.6167,
                       13.6167, 13.6167, 13.6167]
        primes = [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                  101]
        primes2 = [0, 2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29, 31, 32, 37]
        primes2_labels = ["0", " 2", " 3", "2^2", " 5", " 7", " 2^3", " 3^2", " 11", " 13", "2^4", " 17", " 19", " 23",
                          " 5^2", " 3^3", " 29", " 31", " 2^5", " 37"]

        prime_color = [YELLOW, YELLOW, YELLOW, RED, YELLOW, YELLOW, GREEN, RED, YELLOW, YELLOW, BLUE, YELLOW, YELLOW,
                       YELLOW, RED, GREEN, YELLOW, YELLOW, ORANGE, YELLOW]

        def pdf2(x):
            return prime_dist2[int(x)]

        prime_graphs = []
        for i in range(0, len(primes2) - 1):
            prime_graphs.append(
                ax.get_graph(lambda x: pdf2(x), color=prime_color[i],
                             x_range=[primes2[i] + 0.01, primes2[i + 1] - 0.01, 0.1]))

        labels = []
        for i in range(1, len(primes2_labels)):
            lab = MathTex(primes2_labels[i])
            lab.scale(0.7)
            lab.set_color(prime_color[i])
            lab.move_to(ax.coords_to_point(primes2[i], -0.6))
            labels.append(lab)

        self.add(ax, *prime_graphs, *labels)

        # zoom in further
        graph_group = VGroup(ax, *prime_graphs, *labels)
        graph_group_transform = VGroup(ax, *prime_graphs)

        ax2 = Axes(
            x_range=[0, 11],
            y_range=[0, 7],
            x_length=6,
            y_length=3.5,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(0, 10, 1),
                "color": GRAY,
                "font_size": 18,
                "line_to_number_buff": 10 * LARGE_BUFF  # move out of sight
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 7, 1),
                "color": GRAY
            },
            tips=True,
        )
        labels2 = ax2.get_axis_labels(x_label="x", y_label="\\Pi(x)")
        labels2[0].shift(1 * DOWN + 0.5 * LEFT)
        labels2[1].shift(0.4 * LEFT)
        labels2.set_color(WHITE)
        labels2[1].set_color(YELLOW)
        ax2.add(labels2)
        ax2.to_edge(RIGHT)
        ax2.shift(1.5 * DOWN)

        prime_graphs2 = []
        prime_labels2 = []
        for i in range(0, 8):
            prime_graphs2.append(
                ax2.get_graph(lambda x: pdf2(x), color=prime_color[i],
                              x_range=[primes2[i] + 0.01, primes2[i + 1] - 0.01, 0.1]))

        for i in range(1, len(prime_graphs) + 1):
            lab = MathTex(primes2_labels[i])
            lab.scale(0.7)
            lab.set_color(prime_color[i])
            if i < len(prime_graphs2):
                lab.move_to(ax2.coords_to_point(primes2[i], -0.6))
            else:
                lab.move_to(ax2.coords_to_point(primes2[i] + 3, -0.6))  # move out of sight
            prime_labels2.append(lab)

        graph_group2 = VGroup(ax2, *prime_graphs2)

        title2 = MathTex(r"\text{Riemann's prime counting function}")
        title2.to_edge(UP)
        title2.set_color(YELLOW)

        self.play(Transform(graph_group_transform, graph_group2),
                  *[Transform(labels[j], prime_labels2[j]) for j in range(0, len(prime_labels2))])
        self.wait(3)

        data = load_data2()
        x_vals = []
        for i in range(1, len(data[0]) + 1):
            x_vals.append(37 / 1000 * i)
        dots = []
        for i in range(0, len(data)):
            lines = []
            for j in range(0, len(data[i]) - 1):
                if x_vals[j] < 11:
                    lines.append(Line(ax2.coords_to_point(x_vals[j], data[i][j]),
                                      ax2.coords_to_point(x_vals[j + 1], data[i][j + 1])).set_color(WHITE))
            dots.append(VGroup(*lines))
        for i in range(0, len(dots)):
            if i > 0:
                self.remove(dots[i - 1])
            self.play(Create(dots[i]))
            self.wait(2)

        self.wait(10)


def load_data2():
    values = []
    with open(f'prime_dist_approx_37_first_ten.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            row_data = []
            for data in row:
                row_data.append(float(data))
            values.append(row_data)
    csvFile.close()
    return values


class HiddenPrimes(Scene):
    def construct(self):
        title = MathTex(r"\text{Can primes be found by integration?}")
        title.to_edge(UP)
        title.set_color(YELLOW)

        zeta = MathTex(r"\zeta(s)", "=", r"\sum\limits_{n=1}^{\infty} \frac{1}{n^s}", r"\rule{3em}{0ex}\Longrightarrow",
                       r"\Pi(x)=\frac{1}{2\pi i}\int\limits_{a- i\infty}^{a+i\infty} \log\zeta(s) x^s\frac{{\rm d}s}{s}")
        zeta.set_color(WHITE)
        zeta[4].scale(0.7)
        zeta.next_to(title, DOWN, buff=1 * LARGE_BUFF)

        self.play(Write(title))
        self.wait(2)
        self.play(Write(zeta[0:3]))
        self.wait(3)
        self.play(Write(zeta[3:]))
        self.wait(3)

        step = MathTex(r"\Pi(N+)-\Pi(N-)", "=", r"\frac{1}{m}", r"\rule{3em}{0ex}\Longrightarrow\rule{3em}{0ex}",
                       r" N=p^m")
        step[0].scale(0.7)
        step.set_color(WHITE)
        step.next_to(zeta, DOWN)
        step[0].shift(0.5 * RIGHT)
        align_formulas_with_equal(step, zeta, 3, 3)

        self.play(Write(step[0:3]))
        self.wait(2)
        self.play(Write(step[3:]))
        self.wait(2)

        prime = MathTex(r"m", "=", r"1", r"\rule{3em}{0ex}\Longrightarrow\rule{3em}{0ex}", r"N\text{ prime}")
        prime[4].set_color(YELLOW)
        prime.next_to(step, DOWN, buff=6 * MED_SMALL_BUFF)
        align_formulas_with_equal(prime, step, 3, 3)

        self.play(Write(prime[0:3]))
        self.wait(2)
        self.play(Write(prime[3:]))
        self.wait(2)

        box = SurroundingRectangle(prime[4])
        self.play(GrowFromCenter(box))

        self.wait(10)


class Riemann(Scene):
    def construct(self):
        title = Tex("Riemann 1859")
        title.to_edge(UP)
        title.set_color(YELLOW)

        self.play(Write(title))

        page1 = ImageMobject("riemann1")
        page1.to_edge(LEFT)
        self.play(FadeIn(page1))
        self.wait(3)

        sub = highlight_part(self, page1, 174, 484, 316, 532)
        csub = sub.copy()
        csub.scale(2)
        csub.to_corner(UL, buff=LARGE_BUFF)

        self.play(Transform(sub, csub))
        self.wait(3)

        sum = MathTex(r"\sum_{n=1}^{\infty}\frac{1}{n^s} ", r"=",
                      r" \frac{1}{1^s}+\frac{1}{2^s}+\frac{1}{3^s}+\frac{1}{4^s}+\dots")
        sum.scale(0.7)
        sum.next_to(sub, DOWN)
        sum[0].set_color(YELLOW)
        sum.to_edge(LEFT, buff=LARGE_BUFF)

        self.play(Write(sum))
        self.wait(3)

        prod = MathTex(r"\prod_{p}^{\infty}\frac{1}{1-\tfrac{1}{p^s}} ", r"=",
                       r" \left(\frac{1}{1-\tfrac{1}{2^s}}\right)", r"\cdot",
                       r"\left(\frac{1}{1-\tfrac{1}{3^s}}\right)", r"\cdot", r"\left(\frac{1}{1-\tfrac{1}{5^s}}\right)",
                       r"\cdot", r"\left(\frac{1}{1-\tfrac{1}{7^s}}\right)", r"\cdot\dots")
        prod.scale(0.7)
        prod.next_to(sum, DOWN)
        prod[0].set_color(YELLOW)
        align_formulas_with_equal(prod, sum, 1, 1)

        self.play(Write(prod))
        self.wait(3)

        geo_series = MathTex(r"\tfrac{1}{1-q}=1+q^2+q^3+\dots\,\,\,\,\text{for } (|q|<1)")
        geo_series.scale(0.7)
        geo_series.next_to(prod, DOWN)
        geo_series.set_color(GREEN)
        geo_series.to_corner(RIGHT)
        self.play(Write(geo_series))
        self.wait(3)

        expansion = MathTex("(", "1", "+", r"\tfrac{1}{2^s}", "+", r"\tfrac{1}{2^{2s}}", "+", r"\tfrac{1}{2^{3s}}", "+",
                            r"\dots)", r"\cdot", r"(", "1", "+", r"\tfrac{1}{3^s}", "+", r"\tfrac{1}{3^{2s}}", "+",
                            r"\tfrac{1}{3^{3s}}", "+", r"\dots)", r"\cdot", r"(", "1", "+", r"\tfrac{1}{5^s}", "+",
                            r"\tfrac{1}{5^{2s}}", "+", r"\tfrac{1}{5^{3s}}", "+", r"\dots)", r"\cdot", r"(", "1", "+",
                            r"\tfrac{1}{7^s}", "+", r"\tfrac{1}{7^{2s}}", "+", r"\tfrac{1}{7^{3s}}", "+", r"\dots)",
                            r"\cdot\dots")
        expansion.scale(0.55)
        expansion.next_to(geo_series, DOWN)
        expansion.to_edge(LEFT)

        self.play(TransformFromCopy(prod[2], expansion[0:10]))
        self.wait()
        self.play(TransformFromCopy(prod[3], expansion[10]))
        self.wait()
        self.play(TransformFromCopy(prod[4], expansion[11:21]))
        self.wait()
        self.play(TransformFromCopy(prod[5], expansion[21]))
        self.wait()
        self.play(TransformFromCopy(prod[6], expansion[22:32]))
        self.wait()
        self.play(TransformFromCopy(prod[7], expansion[32]))
        self.wait()
        self.play(TransformFromCopy(prod[8], expansion[33:43]))
        self.wait()
        self.play(TransformFromCopy(prod[9], expansion[43]))
        self.wait(3)

        scaled = []  # keeps track which parts are scaled up
        for i in range(0, len(expansion)):
            scaled.append(False)

        def get_group(a, b, c, d):
            indices = [2 * (a - 1) + 1, 2 * (b - 1) + 12, 2 * (c - 1) + 23, 2 * (d - 1) + 34]
            colors = []
            scales = []
            n = len(expansion)
            for index in range(0, n):
                if index in indices:
                    colors.append(YELLOW)
                    if not scaled[index]:
                        scales.append(1.5)
                        scaled[index] = True
                    else:
                        scales.append(1)
                else:
                    colors.append(WHITE)
                    if scaled[index]:
                        scales.append(0.666667)
                        scaled[index] = False
                    else:
                        scales.append(1)

            for j in range(0, n):
                expansion[j].generate_target()
                expansion[j].target.move_to(expansion[j])
                expansion[j].target.scale(scales[j])
                expansion[j].target.set_color(colors[j])

            self.play(*[MoveToTarget(expansion[j]) for j in range(0, n)])

            return VGroup(*[expansion[ind] for ind in indices])

        expansion2 = MathTex(r"1", "+", r"\tfrac{1}{2^s}", "+", r"\tfrac{1}{3^s}", "+", r"\tfrac{1}{5^s}", "+",
                             r"\tfrac{1}{7^s}", "+", r"\tfrac{1}{(2\cdot 3)^s}", "+", r"\tfrac{1}{(2\cdot 5)^s}", "+",
                             r"\tfrac{1}{(2\cdot 7)^s}", "+", r"\tfrac{1}{(2^2)^s}", "+",
                             r"\tfrac{1}{(2^2\cdot 3)^s}", "+", r"\tfrac{1}{(2^2\cdot 5)^s}", "+",
                             r"\tfrac{1}{(2^2\cdot 7)^s}", "+\dots")
        expansion2.scale(0.7)
        expansion2.next_to(expansion, DOWN)
        expansion2.to_edge(LEFT)

        expansion2[0].set_color(YELLOW)
        self.play(TransformFromCopy(get_group(1, 1, 1, 1), expansion2[0]), runtime=2)
        self.wait()
        self.play(expansion2[0].animate().set_color(WHITE), Write(expansion2[1]))
        self.wait()
        expansion2[2].set_color(YELLOW)
        self.play(TransformFromCopy(get_group(2, 1, 1, 1), expansion2[2]), runtime=2)
        self.wait()
        self.play(expansion2[2].animate().set_color(WHITE), Write(expansion2[3]))
        self.wait()
        expansion2[4].set_color(YELLOW)
        self.play(TransformFromCopy(get_group(1, 2, 1, 1), expansion2[4]), runtime=2)
        self.wait()
        self.play(expansion2[4].animate().set_color(WHITE), Write(expansion2[5]))
        self.wait()
        expansion2[6].set_color(YELLOW)
        self.play(TransformFromCopy(get_group(1, 1, 2, 1), expansion2[6]), runtime=2)
        self.wait()
        self.play(expansion2[6].animate().set_color(WHITE), Write(expansion2[7]))
        self.wait()
        expansion2[8].set_color(YELLOW)
        self.play(TransformFromCopy(get_group(1, 1, 1, 2), expansion2[8]), runtime=2)
        self.wait()
        self.play(expansion2[8].animate().set_color(WHITE), Write(expansion2[9]))
        self.wait()
        expansion2[10].set_color(YELLOW)
        self.play(TransformFromCopy(get_group(2, 2, 1, 1), expansion2[10]), runtime=2)
        self.wait()
        self.play(expansion2[10].animate().set_color(WHITE), Write(expansion2[11]))
        self.wait()
        expansion2[12].set_color(YELLOW)
        self.play(TransformFromCopy(get_group(2, 1, 2, 1), expansion2[12]), runtime=2)
        self.wait()
        self.play(expansion2[12].animate().set_color(WHITE), Write(expansion2[13]))
        self.wait()
        expansion2[14].set_color(YELLOW)
        self.play(TransformFromCopy(get_group(2, 1, 1, 2), expansion2[14]), runtime=2)
        self.wait()
        self.play(expansion2[14].animate().set_color(WHITE), Write(expansion2[15]))
        self.wait()
        expansion2[16].set_color(YELLOW)
        self.play(TransformFromCopy(get_group(3, 1, 1, 1), expansion2[16]), runtime=2)
        self.wait()
        self.play(expansion2[16].animate().set_color(WHITE), Write(expansion2[17]))
        self.wait()
        expansion2[18].set_color(YELLOW)
        self.play(TransformFromCopy(get_group(3, 2, 1, 1), expansion2[18]), runtime=2)
        self.wait()
        self.play(expansion2[18].animate().set_color(WHITE), Write(expansion2[19]))
        self.wait()
        expansion2[20].set_color(YELLOW)
        self.play(TransformFromCopy(get_group(3, 1, 2, 1), expansion2[20]), runtime=2)
        self.wait()
        self.play(expansion2[20].animate().set_color(WHITE), Write(expansion2[21]))
        self.wait()
        expansion2[22].set_color(YELLOW)
        self.play(TransformFromCopy(get_group(3, 1, 1, 2), expansion2[22]), runtime=2)
        self.wait()
        self.play(expansion2[22].animate().set_color(WHITE), Write(expansion2[23]))

        self.wait(3)


def highlight_part(scene, img, x1, y1, x2, y2):
    '''
    A part of the image gets cut out and positioned at the original position
    The rest of the image is faded away
    only use even coordinates to avoid errors during rounding
    Parameters
    ----------
    scene
    img
    x1
    y1
    x2
    y2

    Returns
    -------

    '''
    img_array = img.get_pixel_array()
    new_img_array = []

    def pix_to_coord(image, x, y):
        ul = image.get_corner(UL)
        dr = image.get_corner(DR)
        rows = len(image.get_pixel_array())
        cols = len(image.get_pixel_array()[0])
        return ul + x / cols * (dr - ul)[0] * RIGHT + y / rows * (dr - ul)[1] * UP

    for row in range(y1, y2):
        new_row = []
        for col in range(x1, x2):
            new_row.append(img_array[row][col])
        new_img_array.append(new_row)

    sub_img = ImageMobject(np.uint8(new_img_array))
    sub_img.move_to(pix_to_coord(img, 0.5 * (x1 + x2), 0.5 * (y1 + y2)))

    scene.add(sub_img)
    scene.play(FadeOut(img))
    scene.wait(3)
    return sub_img


class Riemann2(Scene):
    def construct(self):
        title = Tex("Riemann 1859")
        title.to_edge(UP)
        title.set_color(YELLOW)

        self.add(title)

        page4 = ImageMobject("riemann4")
        page4.to_edge(LEFT)
        self.play(FadeIn(page4))
        self.wait(3)

        sub = highlight_part(self, page4, 30, 680, 466, 710)
        csub = sub.copy()
        csub.scale(2)
        csub.to_corner(UL, buff=LARGE_BUFF)

        self.play(Transform(sub, csub))
        self.wait(3)

        log_zeta = MathTex(r"\log\zeta(s)", "=", r"\log \prod_{p}^{\infty} \frac{1}{1-\tfrac{1}{p^s}}", r"=",
                           r"\log\prod_{p}^{\infty}\left(1-p^{-s}\right)^{-1}")
        log_zeta[0].set_color(YELLOW)
        log_zeta.next_to(csub, DOWN)
        log_zeta.to_edge(LEFT)

        self.play(Write(log_zeta))
        self.wait(3)

        log_law = MathTex(r"\log(a\cdot b)", "=", r"\log a+\log b")
        log_law2 = MathTex("\log(a^b)", "=", r"b\cdot \log a")
        log_law.set_color(GREEN)
        log_law2.set_color(GREEN)
        log_law.scale(0.7)
        log_law2.scale(0.7)
        log_law.next_to(log_zeta, DOWN)
        log_law.to_edge(RIGHT)
        log_law2.next_to(log_law, DOWN)
        align_formulas_with_equal(log_law2, log_law, 1, 1)

        self.play(Write(log_law))
        self.play(Write(log_law2))
        self.wait(3)

        log_zeta2 = MathTex(r"\log\zeta(s)", "=", r"-\sum_{p}^{\infty}\log\left(1-p^{-s}\right)")
        log_zeta2.set_color(YELLOW)
        log_zeta2.next_to(log_law2, DOWN)
        log_zeta2.shift(0.5 * UP)
        align_formulas_with_equal(log_zeta2, log_zeta, 1, 1)

        self.play(Write(log_zeta2))
        self.wait(3)

        tayler = MathTex(r"\log(1-x)", "=", r"-x-\tfrac{1}{2}x^2-\tfrac{1}{3}x^3-\dots \,\,\,\text{for }(|x|<1)")
        tayler.set_color(GREEN)
        tayler.scale(0.7)
        tayler.next_to(log_zeta2, DOWN)
        tayler.to_edge(RIGHT)

        self.play(Write(tayler))
        self.wait(3)

        log_zeta3 = MathTex(r"\log\zeta(s)", "=",
                            r"\sum_{p}^{\infty}p^{-s}+\tfrac{1}{2}\sum_{p}^{\infty}p^{-2s}+\tfrac{1}{3}\sum_{p}^{"
                            r"\infty}p^{-3s}+\dots")
        log_zeta3.set_color(YELLOW)
        log_zeta3.next_to(tayler, DOWN)
        align_formulas_with_equal(log_zeta3, log_zeta2, 1, 1)

        self.play(Write(log_zeta3))
        self.wait(3)


class Riemann3(Scene):
    def construct(self):
        title = Tex("Riemann 1859")
        title.to_edge(UP)
        title.set_color(YELLOW)

        self.add(title)

        page4 = ImageMobject("riemann4")
        page4.to_edge(LEFT)
        self.play(FadeIn(page4))


        sub = highlight_part(self, page4, 30, 680, 466, 770)
        csub = sub.copy()
        csub.scale(2)
        csub.to_corner(UL, buff=LARGE_BUFF)

        self.play(Transform(sub, csub))


        log_zeta3 = MathTex(r"\log\zeta(s)", "=",
                            r"\sum_{p}^{\infty}", "p^{-s}", "+", r"\tfrac{1}{2}\sum_{p}^{\infty}", "p^{-2s}", "+",
                            r"\tfrac{1}{3}\sum_{p}^{"
                            r"\infty}", "p^{-3s}", r"+\dots")
        log_zeta3.set_color(YELLOW)
        log_zeta3.scale(0.7)
        log_zeta3.next_to(csub, DOWN)
        log_zeta3.to_edge(LEFT)

        self.play(Write(log_zeta3))


        integral = MathTex(r"s\int\limits_a^\infty x^{-s-1}{\rm d}x=\left.-\frac{s}{s} x^{-s}\right|^\infty_a=a^{-s}")
        integral.scale(0.7)
        integral.set_color(GREEN)
        integral.next_to(log_zeta3, DOWN)
        integral.to_edge(RIGHT)

        self.play(Write(integral))


        log_zeta4 = MathTex(r"\log\zeta(s)", "=",
                            r"\sum_{p}^{\infty}",
                            r"s\int\limits^\infty_{p} x^{-s-1}{\rm d}x", "+", r"\tfrac{1}{2}\sum_{p}^{\infty}",
                            r"s\int\limits^\infty_{p^2} x^{-s-1}{\rm d}x", "+", r"\tfrac{1}{3}\sum_{p}^{\infty}",
                            r"s\int\limits^\infty_{p^3} x^{-s-1}{\rm d}x"
                            , r"+\dots")

        log_zeta4.scale(0.7)
        log_zeta4[0].set_color(YELLOW)
        log_zeta4.next_to(integral, DOWN)
        align_formulas_with_equal(log_zeta4, log_zeta3, 1, 1)

        self.play(Write(log_zeta4[0:2]))
        for i in range(2, len(log_zeta3)):
            self.play(TransformFromCopy(log_zeta3[i], log_zeta4[i]))
            if i % 2 == 0:
                self.wait(2)



        # make factor s dynamic
        log_zeta5 = MathTex(r"\log\zeta(s)", "=",
                            r"\sum_{p}^{\infty}",
                            "s", r"\int\limits^\infty_{p} x^{-s-1}{\rm d}x", "+", r"\tfrac{1}{2}\sum_{p}^{\infty}",
                            "s", r"\int\limits^\infty_{p^2} x^{-s-1}{\rm d}x", "+", r"\tfrac{1}{3}\sum_{p}^{\infty}",
                            "s", r"\int\limits^\infty_{p^3} x^{-s-1}{\rm d}x"
                            , r"+\dots")

        log_zeta5.scale(0.7)
        log_zeta5[0].set_color(YELLOW)
        log_zeta5.move_to(log_zeta4)

        self.add(log_zeta5)
        self.remove(log_zeta4)

        log_zeta6 = MathTex(r"\frac{\log\zeta(s)}{s}", "=",
                            r"\sum_{p}^{\infty}",
                            r"\int\limits^\infty_{p} x^{-s-1}{\rm d}x", "+", r"\tfrac{1}{2}\sum_{p}^{\infty}",
                            r"\int\limits^\infty_{p^2} x^{-s-1}{\rm d}x", "+", r"\tfrac{1}{3}\sum_{p}^{\infty}",
                            r"\int\limits^\infty_{p^3} x^{-s-1}{\rm d}x"
                            , r"+\dots")
        log_zeta6.scale(0.7)
        log_zeta6.next_to(log_zeta5, DOWN)
        align_formulas_with_equal(log_zeta6, log_zeta5, 1, 1)

        group = VGroup(log_zeta5[0], log_zeta5[3], log_zeta5[7], log_zeta5[11])
        group2 = VGroup(log_zeta5[1], log_zeta5[2], log_zeta5[4], log_zeta5[5], log_zeta5[6], log_zeta5[8],
                        log_zeta5[9], log_zeta5[10], log_zeta5[12:len(log_zeta5)])
        self.play(TransformFromCopy(group, log_zeta6[0]))
        self.wait()
        self.play(TransformFromCopy(group2, log_zeta6[1:len(log_zeta6)]))


        rect = Rectangle(color=BLACK, width=14.0, height=5.5)
        rect.set_style(fill_color=BLACK, fill_opacity=1, stroke_color=BLACK)
        rect.shift(0.25 * UP)
        self.play(GrowFromEdge(rect, UP))
        self.wait()

        self.add(log_zeta6)

        self.play(log_zeta6.animate().next_to(title, DOWN))
        self.play(log_zeta6[2:4].animate().set_color(GREEN))


        part = MathTex(r"\sum_{p}^{\infty}\int\limits^\infty_{p} x^{-s-1}{\rm d}x", "=",
                       r"\int\limits_2^\infty x^{-s-1}{\rm d}x", "+",
                       r"\int\limits_3^\infty x^{-s-1}{\rm d}x", "+",
                       r"\int\limits_5^\infty x^{-s-1}{\rm d}x", "+",
                       r"\int\limits_7^\infty x^{-s-1}{\rm d}x", r"+\dots")
        part.scale(0.5)
        part[0].set_color(GREEN)
        part.next_to(log_zeta6, DOWN)
        align_formulas_with_equal(part, log_zeta6, 1, 1)

        subpart = VGroup(log_zeta6[2:4])
        csubpart = subpart.copy()
        csubpart.move_to(subpart)
        self.play(Transform(csubpart, part[0]))
        self.play(Write(part[1:len(part)]))


        lines = [
            MathTex(r"\int\limits^\infty_{2} x^{-s-1}{\rm d}x", "=",
                    r"\int\limits_2^3 x^{-s-1}{\rm d}x", "+",
                    r"\int\limits_3^5 x^{-s-1}{\rm d}x", "+",
                    r"\int\limits_5^7x^{-s-1}{\rm d}x", "+",
                    r"\int\limits_7^{11} x^{-s-1}{\rm d}x", r"+\dots"),
            MathTex(r"\int\limits^\infty_{3} x^{-s-1}{\rm d}x", "=",
                    r"\int\limits_3^5 x^{-s-1}{\rm d}x", "+",
                    r"\int\limits_5^7x^{-s-1}{\rm d}x", "+",
                    r"\int\limits_7^{11} x^{-s-1}{\rm d}x", r"+\dots"),
            MathTex(r"\int\limits^\infty_{5} x^{-s-1}{\rm d}x", "=",
                    r"\int\limits_5^7x^{-s-1}{\rm d}x", "+",
                    r"\int\limits_7^{11} x^{-s-1}{\rm d}x", r"+\dots"),
            MathTex(r"\int\limits^\infty_{7} x^{-s-1}{\rm d}x", "=",
                    r"\int\limits_7^{11} x^{-s-1}{\rm d}x", r"+\dots"),
        ]

        old_line = part
        for i, line in enumerate(lines):
            line.scale(0.5)
            line.next_to(old_line, DOWN)
            for j in range(0, len(line)):
                if i == 0 or j < 2:
                    if j == 0:
                        line[j].align_to(old_line[j], RIGHT)
                    else:
                        line[j].align_to(old_line[j], LEFT)
                else:
                    line[j].align_to(old_line[j + 2], LEFT)
            old_line = line

        for i in range(0, len(lines)):
            self.play(TransformFromCopy(part[2 * i + 2], lines[i][0]))
            self.wait(2)
            self.play(Write(lines[i][1:]))
            self.wait(2)

        self.play(Unwrite(part[2:]), *[Unwrite(lines[i][0:2]) for i in range(0, len(lines))])
        self.wait(2)

        p = [2, 3, 5, 7, 11]

        old_part = part[0:2]
        removeables = []
        for i in range(0, 4):
            new_part = MathTex(str(i + 1) + "\cdot",
                               r"\int\limits_" + str(p[i]) + "^{" + str(p[i + 1]) + r"}x^{-s-1}{\rm d}x")
            new_part.scale(0.5)
            new_part[0].set_color(YELLOW)
            new_part.next_to(old_part, RIGHT)
            col_group = []
            plus_group = []
            for col in range(0, i + 1):
                self.play(lines[col][2 * i + 2 - 2 * col].animate(run_time=0.1).set_color(YELLOW))
                col_group.append(lines[col][2 * i + 2 - 2 * col])
                plus_group.append(lines[col][2 * i + 3 - 2 * col])
            self.wait(2)
            group = VGroup(*col_group)
            self.play(Transform(group, new_part))
            removeables.append(group)

            if i < 3:
                new_plus = MathTex("+")
            else:
                new_plus = MathTex(r"+\dots")
            new_plus.scale(0.5)
            new_plus.next_to(new_part)
            group = VGroup(*plus_group)
            removeables.append(group)
            self.play(Transform(group, new_plus))
            old_part = VGroup(old_part, new_part, new_plus)



        pcf = MathTex("=", r"\int\limits_0^\infty", r"\pi(x)\cdot", r"x^{-s-1}\rm{d} x")
        pcf.scale(0.5)
        pcf.next_to(part, DOWN)
        pcf[2].set_color(YELLOW)
        align_formulas_with_equal(pcf, part, 0, 1)

        self.play(Write(pcf))
        removeables.append(pcf)
        self.wait(2)

        pcf2 = MathTex("=", r"\int\limits_0^2", r"0\cdot", r"x^{-s-1}\rm{d} x",
                       "+", r"\int\limits_2^3", r"1\cdot", r"x^{-s-1}\rm{d} x",
                       "+", r"\int\limits_3^5", r"2\cdot", r"x^{-s-1}\rm{d} x",
                       "+", r"\int\limits_5^7", r"3\cdot", r"x^{-s-1}\rm{d} x",
                       "+", r"\int\limits_7^{11}", r"4\cdot", r"x^{-s-1}\rm{d} x",
                       r"+\dots")
        pcf2.scale(0.5)
        pcf2.next_to(pcf, DOWN)
        for i in range(2, len(pcf2), 4):
            pcf2[i].set_color(YELLOW)
        align_formulas_with_equal(pcf2, pcf, 0, 0)

        prime_dist = [0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 11,
                      11, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 16, 16, 16,
                      16, 16, 16, 17, 17, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 20, 20, 21, 21, 21, 21, 21, 21, 22,
                      22, 22, 22, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25]
        primes = [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                  101]

        def pdf(x):
            return prime_dist[int(x)]

        ax = Axes(
            x_range=[0, 12],
            y_range=[0, 6],
            x_length=6,
            y_length=3,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(0, 12, 100),
                "color": GRAY,
                "font_size": 18,
                "line_to_number_buff": 3 * MED_SMALL_BUFF  # make them disappear
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 5, 1),
                "font_size": 24,
                "color": GRAY
            },
            tips=True,
        )
        labels = ax.get_axis_labels(x_label="x", y_label="\\pi(x)")
        labels[0].shift(0.4 * DOWN)
        labels[1].shift(0.4 * LEFT)
        labels.set_color(WHITE)
        labels[1].set_color(YELLOW)
        ax.add(labels)
        ax.scale(0.7)
        ax.to_corner(LEFT + DOWN)

        prime_graphs = []
        for i in range(0, len(primes) - 1):
            prime_graphs.append(
                ax.get_graph(lambda x: pdf(x), color=YELLOW, x_range=[primes[i] + 0.01, primes[i + 1] - 0.01, 0.1]))
        self.play(Create(ax))

        labels = []
        for i in range(0, 5):
            text = pcf2[4 * i:4 * (i + 1)]
            if i > 0:
                lab = MathTex(primes[i])
                lab.scale(0.7)
                lab.set_color(YELLOW)
                lab.move_to(ax.coords_to_point(primes[i], -1))
                labels.append(lab)
                self.play(Create(prime_graphs[i]), Write(lab), Write(text))
            else:
                self.play(Create(prime_graphs[i]), Write(text))
            removeables.append(text)
            self.wait(2)
        text = Write(pcf2[20])
        self.play(text)
        removeables.append(text)


        self.remove(part[1], pcf2[20])
        self.remove(*removeables)
        self.remove(ax)
        self.remove(*prime_graphs, *labels)
        self.remove(csubpart)


        log_zeta7 = MathTex(r"\frac{\log\zeta(s)}{s}",
                            "=", r"\int\limits_0^\infty", r"\pi(x)\cdot", r"x^{-s-1}\rm{d} x", "+",
                            r"\int\limits_0^\infty", r"\tfrac{1}{2}\pi\left(\sqrt{x}\right)\cdot",
                            r"x^{-s-1}\rm{d} x", "+",
                            r"\int\limits_0^\infty",
                            r"\tfrac{1}{3}\pi\left( \sqrt[\leftroot{-1}\uproot{2}\scriptstyle 3]{x}\right)\cdot",
                            r"x^{-s-1}\rm{d} x", r"+\dots"
                            )
        log_zeta7.scale(0.7)
        log_zeta7[3].set_color(YELLOW)
        log_zeta7[7].set_color(YELLOW)
        log_zeta7[11].set_color(YELLOW)
        log_zeta7.next_to(log_zeta6, DOWN)
        align_formulas_with_equal(log_zeta7, log_zeta6, 1, 1)

        self.play(Write(log_zeta7[0:2]))
        self.wait(2)
        self.play(TransformFromCopy(log_zeta6[2:4], log_zeta7[2:5]))
        self.wait(2)
        self.play(TransformFromCopy(log_zeta6[4], log_zeta7[5]))
        self.wait(2)
        self.play(TransformFromCopy(log_zeta6[5:7], log_zeta7[6:9]))
        self.wait(2)
        self.play(TransformFromCopy(log_zeta6[7], log_zeta7[9]))
        self.wait(2)
        self.play(TransformFromCopy(log_zeta6[8:10], log_zeta7[10:13]))
        self.wait(2)
        self.play(TransformFromCopy(log_zeta6[10], log_zeta7[13]))



        page5 = ImageMobject("riemann5")
        page5.scale(1)
        page5.next_to(log_zeta7, DOWN)
        page5.to_edge(LEFT)
        self.play(FadeIn(page5))


        sub = highlight_part(self, page5, 36, 56, 366, 160)
        csub = sub.copy()
        csub.scale(2)
        csub.to_corner(DOWN + LEFT, buff=LARGE_BUFF)

        self.play(Transform(sub, csub))


        result = MathTex(r"\frac{\log\zeta(s)}{s}",
                         "=", r"\int\limits_0^\infty", r"\Pi(x)\cdot", r"x^{-s-1}\rm{d} x")
        result.set_color(YELLOW)
        result.next_to(csub)

        self.play(Write(result))


        self.play(FadeOut(log_zeta7), FadeOut(log_zeta6), FadeOut(sub),
                  result.animate().set_color(WHITE).scale(0.7).to_corner(UP + LEFT, buff=LARGE_BUFF))
        self.wait(10)



class Riemann3_Trailer(Scene):
    def construct(self):
        title = Tex("Riemann 1859")
        title.to_edge(UP)
        title.set_color(YELLOW)

        #self.add(title)

        page4 = ImageMobject("riemann4")
        page4.to_edge(LEFT)
        self.play(FadeIn(page4))
        self.wait(3)

        sub = highlight_part(self, page4, 30, 680, 466, 770)
        csub = sub.copy()
        csub.scale(2)
        csub.to_corner(UL, buff=LARGE_BUFF)

        self.play(Transform(sub, csub))
        self.wait(3)

        log_zeta3 = MathTex(r"\log\zeta(s)", "=",
                            r"\sum_{p}^{\infty}", "p^{-s}", "+", r"\tfrac{1}{2}\sum_{p}^{\infty}", "p^{-2s}", "+",
                            r"\tfrac{1}{3}\sum_{p}^{"
                            r"\infty}", "p^{-3s}", r"+\dots")
        log_zeta3.set_color(YELLOW)
        log_zeta3.scale(0.7)
        log_zeta3.next_to(csub, DOWN)
        log_zeta3.to_edge(LEFT)

        self.play(Write(log_zeta3))
        self.wait(3)

        integral = MathTex(r"s\int\limits_a^\infty x^{-s-1}{\rm d}x=\left.-\frac{s}{s} x^{-s}\right|^\infty_a=a^{-s}")
        integral.scale(0.7)
        integral.set_color(GREEN)
        integral.next_to(log_zeta3, DOWN)
        integral.to_edge(RIGHT)

        self.play(Write(integral))
        self.wait(3)

        log_zeta4 = MathTex(r"\log\zeta(s)", "=",
                            r"\sum_{p}^{\infty}",
                            r"s\int\limits^\infty_{p} x^{-s-1}{\rm d}x", "+", r"\tfrac{1}{2}\sum_{p}^{\infty}",
                            r"s\int\limits^\infty_{p^2} x^{-s-1}{\rm d}x", "+", r"\tfrac{1}{3}\sum_{p}^{\infty}",
                            r"s\int\limits^\infty_{p^3} x^{-s-1}{\rm d}x"
                            , r"+\dots")

        log_zeta4.scale(0.7)
        log_zeta4[0].set_color(YELLOW)
        log_zeta4.next_to(integral, DOWN)
        align_formulas_with_equal(log_zeta4, log_zeta3, 1, 1)

        self.play(Write(log_zeta4[0:2]))
        for i in range(2, len(log_zeta3)):
            self.play(TransformFromCopy(log_zeta3[i], log_zeta4[i]))
            if i % 2 == 0:
                self.wait(2)

        self.wait(3)

        # make factor s dynamic
        log_zeta5 = MathTex(r"\log\zeta(s)", "=",
                            r"\sum_{p}^{\infty}",
                            "s", r"\int\limits^\infty_{p} x^{-s-1}{\rm d}x", "+", r"\tfrac{1}{2}\sum_{p}^{\infty}",
                            "s", r"\int\limits^\infty_{p^2} x^{-s-1}{\rm d}x", "+", r"\tfrac{1}{3}\sum_{p}^{\infty}",
                            "s", r"\int\limits^\infty_{p^3} x^{-s-1}{\rm d}x"
                            , r"+\dots")

        log_zeta5.scale(0.7)
        log_zeta5[0].set_color(YELLOW)
        log_zeta5.move_to(log_zeta4)

        self.add(log_zeta5)
        self.remove(log_zeta4)

        log_zeta6 = MathTex(r"\frac{\log\zeta(s)}{s}", "=",
                            r"\sum_{p}^{\infty}",
                            r"\int\limits^\infty_{p} x^{-s-1}{\rm d}x", "+", r"\tfrac{1}{2}\sum_{p}^{\infty}",
                            r"\int\limits^\infty_{p^2} x^{-s-1}{\rm d}x", "+", r"\tfrac{1}{3}\sum_{p}^{\infty}",
                            r"\int\limits^\infty_{p^3} x^{-s-1}{\rm d}x"
                            , r"+\dots")
        log_zeta6.scale(0.7)
        log_zeta6.next_to(log_zeta5, DOWN)
        align_formulas_with_equal(log_zeta6, log_zeta5, 1, 1)

        group = VGroup(log_zeta5[0], log_zeta5[3], log_zeta5[7], log_zeta5[11])
        group2 = VGroup(log_zeta5[1], log_zeta5[2], log_zeta5[4], log_zeta5[5], log_zeta5[6], log_zeta5[8],
                        log_zeta5[9], log_zeta5[10], log_zeta5[12:len(log_zeta5)])
        self.play(TransformFromCopy(group, log_zeta6[0]))
        self.wait()
        self.play(TransformFromCopy(group2, log_zeta6[1:len(log_zeta6)]))
        self.wait(3)

        rect = Rectangle(color=BLACK, width=14.0, height=5.5)
        rect.set_style(fill_color=BLACK, fill_opacity=1, stroke_color=BLACK)
        rect.shift(0.25 * UP)
        self.play(GrowFromEdge(rect, UP))
        self.wait()

        self.add(log_zeta6)

        self.play(log_zeta6.animate().next_to(title, DOWN))
        self.play(log_zeta6[2:4].animate().set_color(GREEN))
        self.wait(3)

        part = MathTex(r"\sum_{p}^{\infty}\int\limits^\infty_{p} x^{-s-1}{\rm d}x", "=",
                       r"\int\limits_2^\infty x^{-s-1}{\rm d}x", "+",
                       r"\int\limits_3^\infty x^{-s-1}{\rm d}x", "+",
                       r"\int\limits_5^\infty x^{-s-1}{\rm d}x", "+",
                       r"\int\limits_7^\infty x^{-s-1}{\rm d}x", r"+\dots")
        part.scale(0.5)
        part[0].set_color(GREEN)
        part.next_to(log_zeta6, DOWN)
        align_formulas_with_equal(part, log_zeta6, 1, 1)

        subpart = VGroup(log_zeta6[2:4])
        csubpart = subpart.copy()
        csubpart.move_to(subpart)
        self.play(Transform(csubpart, part[0]))
        self.play(Write(part[1:len(part)]))
        self.wait(3)

        lines = [
            MathTex(r"\int\limits^\infty_{2} x^{-s-1}{\rm d}x", "=",
                    r"\int\limits_2^3 x^{-s-1}{\rm d}x", "+",
                    r"\int\limits_3^5 x^{-s-1}{\rm d}x", "+",
                    r"\int\limits_5^7x^{-s-1}{\rm d}x", "+",
                    r"\int\limits_7^{11} x^{-s-1}{\rm d}x", r"+\dots"),
            MathTex(r"\int\limits^\infty_{3} x^{-s-1}{\rm d}x", "=",
                    r"\int\limits_3^5 x^{-s-1}{\rm d}x", "+",
                    r"\int\limits_5^7x^{-s-1}{\rm d}x", "+",
                    r"\int\limits_7^{11} x^{-s-1}{\rm d}x", r"+\dots"),
            MathTex(r"\int\limits^\infty_{5} x^{-s-1}{\rm d}x", "=",
                    r"\int\limits_5^7x^{-s-1}{\rm d}x", "+",
                    r"\int\limits_7^{11} x^{-s-1}{\rm d}x", r"+\dots"),
            MathTex(r"\int\limits^\infty_{7} x^{-s-1}{\rm d}x", "=",
                    r"\int\limits_7^{11} x^{-s-1}{\rm d}x", r"+\dots"),
        ]

        old_line = part
        for i, line in enumerate(lines):
            line.scale(0.5)
            line.next_to(old_line, DOWN)
            for j in range(0, len(line)):
                if i == 0 or j < 2:
                    if j == 0:
                        line[j].align_to(old_line[j], RIGHT)
                    else:
                        line[j].align_to(old_line[j], LEFT)
                else:
                    line[j].align_to(old_line[j + 2], LEFT)
            old_line = line

        for i in range(0, len(lines)):
            self.play(TransformFromCopy(part[2 * i + 2], lines[i][0]))
            self.wait(2)
            self.play(Write(lines[i][1:]))
            self.wait(2)

        self.play(Unwrite(part[2:]), *[Unwrite(lines[i][0:2]) for i in range(0, len(lines))])
        self.wait(2)

        p = [2, 3, 5, 7, 11]

        old_part = part[0:2]
        removeables = []
        for i in range(0, 4):
            new_part = MathTex(str(i + 1) + "\cdot",
                               r"\int\limits_" + str(p[i]) + "^{" + str(p[i + 1]) + r"}x^{-s-1}{\rm d}x")
            new_part.scale(0.5)
            new_part[0].set_color(YELLOW)
            new_part.next_to(old_part, RIGHT)
            col_group = []
            plus_group = []
            for col in range(0, i + 1):
                self.play(lines[col][2 * i + 2 - 2 * col].animate(run_time=0.1).set_color(YELLOW))
                col_group.append(lines[col][2 * i + 2 - 2 * col])
                plus_group.append(lines[col][2 * i + 3 - 2 * col])
            self.wait(2)
            group = VGroup(*col_group)
            self.play(Transform(group, new_part))
            removeables.append(group)

            if i < 3:
                new_plus = MathTex("+")
            else:
                new_plus = MathTex(r"+\dots")
            new_plus.scale(0.5)
            new_plus.next_to(new_part)
            group = VGroup(*plus_group)
            removeables.append(group)
            self.play(Transform(group, new_plus))
            old_part = VGroup(old_part, new_part, new_plus)

            self.wait(3)

        pcf = MathTex("=", r"\int\limits_0^\infty", r"\pi(x)\cdot", r"x^{-s-1}\rm{d} x")
        pcf.scale(0.5)
        pcf.next_to(part, DOWN)
        pcf[2].set_color(YELLOW)
        align_formulas_with_equal(pcf, part, 0, 1)

        self.play(Write(pcf))
        removeables.append(pcf)
        self.wait(2)

        pcf2 = MathTex("=", r"\int\limits_0^2", r"0\cdot", r"x^{-s-1}\rm{d} x",
                       "+", r"\int\limits_2^3", r"1\cdot", r"x^{-s-1}\rm{d} x",
                       "+", r"\int\limits_3^5", r"2\cdot", r"x^{-s-1}\rm{d} x",
                       "+", r"\int\limits_5^7", r"3\cdot", r"x^{-s-1}\rm{d} x",
                       "+", r"\int\limits_7^{11}", r"4\cdot", r"x^{-s-1}\rm{d} x",
                       r"+\dots")
        pcf2.scale(0.5)
        pcf2.next_to(pcf, DOWN)
        for i in range(2, len(pcf2), 4):
            pcf2[i].set_color(YELLOW)
        align_formulas_with_equal(pcf2, pcf, 0, 0)

        prime_dist = [0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 11,
                      11, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 16, 16, 16,
                      16, 16, 16, 17, 17, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 20, 20, 21, 21, 21, 21, 21, 21, 22,
                      22, 22, 22, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25]
        primes = [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                  101]

        def pdf(x):
            return prime_dist[int(x)]

        ax = Axes(
            x_range=[0, 12],
            y_range=[0, 6],
            x_length=6,
            y_length=3,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(0, 12, 100),
                "color": GRAY,
                "font_size": 18,
                "line_to_number_buff": 3 * MED_SMALL_BUFF  # make them disappear
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 5, 1),
                "font_size": 24,
                "color": GRAY
            },
            tips=True,
        )
        labels = ax.get_axis_labels(x_label="x", y_label="\\pi(x)")
        labels[0].shift(0.4 * DOWN)
        labels[1].shift(0.4 * LEFT)
        labels.set_color(WHITE)
        labels[1].set_color(YELLOW)
        ax.add(labels)
        ax.scale(0.7)
        ax.to_corner(LEFT + DOWN)

        prime_graphs = []
        for i in range(0, len(primes) - 1):
            prime_graphs.append(
                ax.get_graph(lambda x: pdf(x), color=YELLOW, x_range=[primes[i] + 0.01, primes[i + 1] - 0.01, 0.1]))
        self.play(Create(ax))

        labels = []
        for i in range(0, 5):
            text = pcf2[4 * i:4 * (i + 1)]
            if i > 0:
                lab = MathTex(primes[i])
                lab.scale(0.7)
                lab.set_color(YELLOW)
                lab.move_to(ax.coords_to_point(primes[i], -1))
                labels.append(lab)
                self.play(Create(prime_graphs[i]), Write(lab), Write(text))
            else:
                self.play(Create(prime_graphs[i]), Write(text))
            removeables.append(text)
            self.wait(2)
        text = Write(pcf2[20])
        self.play(text)
        removeables.append(text)
        self.wait(3)

        self.remove(part[1], pcf2[20])
        self.remove(*removeables)
        self.remove(ax)
        self.remove(*prime_graphs, *labels)
        self.remove(csubpart)
        self.wait(3)

        log_zeta7 = MathTex(r"\frac{\log\zeta(s)}{s}",
                            "=", r"\int\limits_0^\infty", r"\pi(x)\cdot", r"x^{-s-1}\rm{d} x", "+",
                            r"\int\limits_0^\infty", r"\tfrac{1}{2}\pi\left(\sqrt{x}\right)\cdot",
                            r"x^{-s-1}\rm{d} x", "+",
                            r"\int\limits_0^\infty",
                            r"\tfrac{1}{3}\pi\left( \sqrt[\leftroot{-1}\uproot{2}\scriptstyle 3]{x}\right)\cdot",
                            r"x^{-s-1}\rm{d} x", r"+\dots"
                            )
        log_zeta7.scale(0.7)
        log_zeta7[3].set_color(YELLOW)
        log_zeta7[7].set_color(YELLOW)
        log_zeta7[11].set_color(YELLOW)
        log_zeta7.next_to(log_zeta6, DOWN)
        align_formulas_with_equal(log_zeta7, log_zeta6, 1, 1)

        self.play(Write(log_zeta7[0:2]))
        self.wait(2)
        self.play(TransformFromCopy(log_zeta6[2:4], log_zeta7[2:5]))
        self.wait(2)
        self.play(TransformFromCopy(log_zeta6[4], log_zeta7[5]))
        self.wait(2)
        self.play(TransformFromCopy(log_zeta6[5:7], log_zeta7[6:9]))
        self.wait(2)
        self.play(TransformFromCopy(log_zeta6[7], log_zeta7[9]))
        self.wait(2)
        self.play(TransformFromCopy(log_zeta6[8:10], log_zeta7[10:13]))
        self.wait(2)
        self.play(TransformFromCopy(log_zeta6[10], log_zeta7[13]))

        self.wait(3)

        page5 = ImageMobject("riemann5")
        page5.scale(1)
        page5.next_to(log_zeta7, DOWN)
        page5.to_edge(LEFT)
        self.play(FadeIn(page5))
        self.wait(3)

        sub = highlight_part(self, page5, 36, 56, 366, 160)
        csub = sub.copy()
        csub.scale(2)
        csub.to_corner(DOWN + LEFT, buff=LARGE_BUFF)

        self.play(Transform(sub, csub))
        self.wait(3)

        result = MathTex(r"\frac{\log\zeta(s)}{s}",
                         "=", r"\int\limits_0^\infty", r"\Pi(x)\cdot", r"x^{-s-1}\rm{d} x")
        result.set_color(YELLOW)
        result.next_to(csub)

        self.play(Write(result))
        self.wait(3)

        self.play(FadeOut(log_zeta7), FadeOut(log_zeta6), FadeOut(sub),
                  result.animate().set_color(WHITE).scale(0.7).to_corner(UP + LEFT, buff=LARGE_BUFF))
        self.wait(10)

class Riemann4(Scene):
    def construct(self):
        title = Tex("Riemann 1859")
        title.to_edge(UP)
        title.set_color(YELLOW)

        self.add(title)
        result = MathTex(r"\frac{\log\zeta(s)}{s}",
                         "=", r"\int\limits_0^\infty", r"\Pi(x)", r"\cdot", r"x^{-s-1}\rm{d} x")
        result.set_color(WHITE)
        result.scale(0.7)
        result.to_corner((UP + LEFT), buff=LARGE_BUFF)
        self.add(result)
        self.wait(3)

        self.play(result[3].animate().set_color(YELLOW))
        self.wait(2)

        transform = MathTex(r"\Pi(x)", r"\xrightarrow{\text{\tt Mellin}}", r"\frac{\log\zeta(s)}{s}")
        transform.scale(0.7)
        transform.next_to(result, DOWN)

        self.play(Write(transform))
        self.wait(2)

        inv_transform = MathTex(r"\frac{\log\zeta(s)}{s}",
                                r"\xrightarrow{\text{\begin{tiny} \tt Mellin \end{tiny}}^{-1}}", r"\Pi(x)")
        inv_transform.scale(0.7)
        inv_transform.next_to(transform, DOWN)
        align_formulas_with_equal(inv_transform, transform, 1, 1)

        self.play(Write(inv_transform))
        self.wait(2)

        page6 = ImageMobject("riemann6")
        page6.scale(1)
        page6.next_to(title, DOWN)
        page6.to_edge(RIGHT)

        self.play(FadeIn(page6))
        self.wait(3)

        sub = highlight_part(self, page6, 138, 52, 350, 108)
        csub = sub.copy()
        csub.scale(3)
        csub.to_corner(UP + RIGHT, buff=LARGE_BUFF)

        self.play(Transform(sub, csub))
        self.wait(3)

        result = MathTex(r"\Pi(x)", "=",
                         r"\frac{1}{2\pi i}\int\limits_{a-i\infty}^{a+i\infty}\frac{\log\zeta(s)}{s}x^{s}{\rm d}s")
        result.scale(0.7)
        result[0].set_color(YELLOW)
        result.next_to(csub, DOWN)

        self.play(Write(result))
        self.wait()

        rect = SurroundingRectangle(result)
        self.play(GrowFromPoint(rect, DOWN + LEFT))
        self.wait(3)

        ax = Axes(
            x_range=[0, 33],
            y_range=[0, 15],
            x_length=6.5,
            y_length=3,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(0, 0, 5),
                "color": GRAY,
                "font_size": 18,
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 16, 5),
                "color": GRAY
            },
            tips=True,
        )
        labels = ax.get_axis_labels(x_label="", y_label="")
        labels[0].shift(0.4 * DOWN)
        labels[1].shift(0.4 * LEFT)
        labels.set_color(WHITE)
        labels[1].set_color(YELLOW)
        ax.add(labels)
        ax.shift(2 * DOWN)

        primes2 = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29, 31, 32, 37]
        primes2_labels = [" 2", " 3", "2^2", " 5", " 7", " 2^3", " 3^2", " 11", " 13", "2^4", " 17", " 19", " 23",
                          " 5^2", " 3^3", " 29", " 31", " 2^5", " 37"]

        prime_color = [YELLOW, YELLOW, RED, YELLOW, YELLOW, GREEN, RED, YELLOW, YELLOW, BLUE, YELLOW, YELLOW,
                       YELLOW, RED, GREEN, YELLOW, YELLOW, ORANGE, YELLOW]

        img = ImageMobject("log_zeta.png")
        img.scale(0.5)
        img.to_corner(DOWN + LEFT)
        img.shift(0.5 * UP + LEFT)

        ax.next_to(img, RIGHT)
        ax.shift(DOWN)

        self.play(FadeIn(img), Create(ax))
        self.wait()

        data = load_data()
        x_vals = []
        for k in range(1, len(data[0]) + 1):
            x_vals.append(37 / 1000 * k)

        lines = []
        last = len(data) - 2

        for j in range(0, len(data[last]) - 1):
            line = Line(ax.coords_to_point(x_vals[j], data[last][j]),
                        ax.coords_to_point(x_vals[j + 1], data[last][j + 1])).set_color(WHITE)
            line.set_color(YELLOW)
            line.set_style(stroke_width=1)
            lines.append(line)

        current_label_index = 0
        current_label = primes2_labels[current_label_index]
        collect_lines = []
        for i in range(0, len(lines)):
            collect_lines.append(lines[i])
            if x_vals[i] > primes2[current_label_index]:
                self.play(*[Create(collect_lines[j]) for j in range(0, len(collect_lines))])
                collect_lines = []
                lab = MathTex(current_label)
                lab.scale(0.4)
                lab.set_color(prime_color[current_label_index])
                if prime_color[current_label_index] == YELLOW:
                    lab.move_to(ax.coords_to_point(primes2[current_label_index], -1))
                else:
                    lab.move_to(ax.coords_to_point(primes2[current_label_index], +1))
                self.play(Write(lab))
                current_label_index = current_label_index + 1
                current_label = primes2_labels[current_label_index]

        self.wait(2)

        continued = Tex("To be continued ...")
        continued.scale(0.5)
        continued.to_corner(DOWN + LEFT)
        continued.shift(0.4 * DOWN)

        self.play(Write(continued))
        self.wait(10)


class Riemann4_Trailer(Scene):
    def construct(self):
        title = Tex("Riemann 1859")
        title.to_edge(UP)
        title.set_color(YELLOW)

        # self.add(title)
        result = MathTex(r"\frac{\log\zeta(s)}{s}",
                         "=", r"\int\limits_0^\infty", r"\Pi(x)", r"\cdot", r"x^{-s-1}\rm{d} x")
        result.set_color(WHITE)
        result.scale(0.7)
        result.to_corner((UP + LEFT), buff=LARGE_BUFF)
        self.add(result)
        self.wait(3)

        self.play(result[3].animate().set_color(YELLOW))
        self.wait(2)

        transform = MathTex(r"\Pi(x)", r"\xrightarrow{\text{\tt Mellin}}", r"\frac{\log\zeta(s)}{s}")
        transform.scale(0.7)
        transform.next_to(result, DOWN)

        self.play(Write(transform))
        self.wait(2)

        inv_transform = MathTex(r"\frac{\log\zeta(s)}{s}",
                                r"\xrightarrow{\text{\begin{tiny} \tt Mellin \end{tiny}}^{-1}}", r"\Pi(x)")
        inv_transform.scale(0.7)
        inv_transform.next_to(transform, DOWN)
        align_formulas_with_equal(inv_transform, transform, 1, 1)

        self.play(Write(inv_transform))
        self.wait(2)

        page6 = ImageMobject("riemann6")
        page6.scale(1)
        page6.next_to(title, DOWN)
        page6.to_edge(RIGHT)

        self.play(FadeIn(page6))
        self.wait(3)

        sub = highlight_part(self, page6, 138, 52, 350, 108)
        csub = sub.copy()
        csub.scale(3)
        csub.to_corner(UP + RIGHT, buff=LARGE_BUFF)

        self.play(Transform(sub, csub))
        self.wait(3)

        result = MathTex(r"\Pi(x)", "=",
                         r"\frac{1}{2\pi i}\int\limits_{a-i\infty}^{a+i\infty}\frac{\log\zeta(s)}{s}x^{s}{\rm d}s")
        result.scale(0.7)
        result[0].set_color(YELLOW)
        result.next_to(csub, DOWN)

        self.play(Write(result))
        self.wait()

        rect = SurroundingRectangle(result)
        self.play(GrowFromPoint(rect, DOWN + LEFT))
        self.wait(3)

        ax = Axes(
            x_range=[0, 33],
            y_range=[0, 15],
            x_length=6.5,
            y_length=3,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(0, 0, 5),
                "color": GRAY,
                "font_size": 18,
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 16, 5),
                "color": GRAY
            },
            tips=True,
        )
        labels = ax.get_axis_labels(x_label="", y_label="")
        labels[0].shift(0.4 * DOWN)
        labels[1].shift(0.4 * LEFT)
        labels.set_color(WHITE)
        labels[1].set_color(YELLOW)
        ax.add(labels)
        ax.shift(2 * DOWN)

        primes2 = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29, 31, 32, 37]
        primes2_labels = [" 2", " 3", "2^2", " 5", " 7", " 2^3", " 3^2", " 11", " 13", "2^4", " 17", " 19", " 23",
                          " 5^2", " 3^3", " 29", " 31", " 2^5", " 37"]

        prime_color = [YELLOW, YELLOW, RED, YELLOW, YELLOW, GREEN, RED, YELLOW, YELLOW, BLUE, YELLOW, YELLOW,
                       YELLOW, RED, GREEN, YELLOW, YELLOW, ORANGE, YELLOW]

        img = ImageMobject("log_zeta.png")
        img.scale(0.5)
        img.to_corner(DOWN + LEFT)
        img.shift(0.5 * UP + LEFT)

        ax.next_to(img, RIGHT)
        ax.shift(DOWN)

        self.play(FadeIn(img), Create(ax))
        self.wait()

        data = load_data()
        x_vals = []
        for k in range(1, len(data[0]) + 1):
            x_vals.append(37 / 1000 * k)

        lines = []
        last = len(data) - 2

        for j in range(0, len(data[last]) - 1):
            line = Line(ax.coords_to_point(x_vals[j], data[last][j]),
                        ax.coords_to_point(x_vals[j + 1], data[last][j + 1])).set_color(WHITE)
            line.set_color(YELLOW)
            line.set_style(stroke_width=1)
            lines.append(line)

        current_label_index = 0
        current_label = primes2_labels[current_label_index]
        collect_lines = []
        for i in range(0, len(lines)):
            collect_lines.append(lines[i])
            if x_vals[i] > primes2[current_label_index]:
                self.play(*[Create(collect_lines[j]) for j in range(0, len(collect_lines))])
                collect_lines = []
                lab = MathTex(current_label)
                lab.scale(0.4)
                lab.set_color(prime_color[current_label_index])
                if prime_color[current_label_index] == YELLOW:
                    lab.move_to(ax.coords_to_point(primes2[current_label_index], -1))
                else:
                    lab.move_to(ax.coords_to_point(primes2[current_label_index], +1))
                self.play(Write(lab))
                current_label_index = current_label_index + 1
                current_label = primes2_labels[current_label_index]

        self.wait(2)

        continued = Tex("To be continued ...")
        continued.scale(0.5)
        continued.to_corner(DOWN + LEFT)
        continued.shift(0.4 * DOWN)

        self.play(Write(continued))
        self.wait(10)


def plot_function(axes, fnc, x_range, res, col=WHITE):
    delta = (x_range[1] - x_range[0]) / (res - 1)
    points = []
    for it in range(0, res):
        x = x_range[0] + delta * it
        if fnc(x) < 25:
            points.append([x, fnc(x)])
    lines = []
    for it in range(0, len(points) - 1):
        lines.append(Line(axes.coords_to_point(points[it][0], points[it][1]),
                          axes.coords_to_point(points[it + 1][0], points[it + 1][1])).set_color(col))
    return lines


class Logo(Scene):
    def construct(self):
        title = Tex("Primes and Riemann's $\zeta$-function")
        title.set_color(YELLOW)
        title.to_edge(UP)

        self.add(title)

        # logo
        n = 19

        def path(t):
            step = np.floor(np.abs(n * t) / np.pi)
            sign = (-1) ** step
            val = 0.25 * sign * np.cos(sign * np.abs(n * t)) - 0.5 * step + (n - 1) / 4 + 1j * (
                    0.25 * np.sin(n * t) + 0.75)
            inv = 1 / val.conjugate()  # circluar inversion
            return np.array((inv.real, inv.imag, 0))

        function = ParametricFunction(path, t_range=np.array([-np.pi, np.pi]), fill_opacity=0).set_color(RED)

        circles1 = []
        for index in range(-int(np.floor(n / 2)), int(np.floor(n / 2))):
            den = 2 + index * index
            r = 1 / den
            x = 2 * index / den
            y = 3 / den
            c = Circle().scale(r).move_to(x * LEFT + y * UP)
            c.set_style(fill_color=RED, fill_opacity=0.8);
            circles1.append(c)

        circles2 = []
        for index in range(-int(np.floor(n / 2)), int(np.floor(n / 2))):
            den = 6 + 4 * index * (index - 1)
            r = 1 / den
            x = (8 * index - 4) / den
            y = 9 / den
            c = Circle().scale(r).move_to(x * LEFT + y * UP)
            c.set_style(fill_color=GREEN, fill_opacity=0.8, stroke_color=GREEN);
            circles2.append(c)

        circles3 = []
        for index in range(-int(np.floor(n / 2)), int(np.floor(n / 2))):
            den = 15 + 4 * index * (index - 1)
            r = 1 / den
            x = (8 * index - 4) / den
            y = 15 / den
            c = Circle().scale(r).move_to(x * LEFT + y * UP)
            c.set_style(fill_color=BLUE, fill_opacity=0.8, stroke_color=BLUE);
            circles3.append(c)

        logo = VGroup(function, *circles1, *circles2, *circles3)

        logo.scale(1.5)
        logo.to_corner(UP + LEFT)
        logo.shift(0.5 * RIGHT)

        riem = ImageMobject("riemann_profile.png")
        riem.scale(0.5)
        riem.move_to(logo.get_center())

        anims = []
        time = 10  # 6

        # anims.append(Create(function, run_time=time, rate_func=rate_functions.double_smooth))
        # anims.append(AnimationGroup(*[
        #     AnimationGroup(GrowFromCenter(circles1[i], run_time=time / 4), GrowFromCenter(circles2[i], run_time=1),
        #                    GrowFromCenter(circles3[i], run_time=1.5)) for i in range(0, len(circles1))], lag_ratio=0.1))
        # self.play(AnimationGroup(*anims, lag_ratio=0.5))

        # squares

        squares = [1, 4, 9, 16, 25, 36]
        colors = [RED, GREEN, BLUE, ORANGE, PURPLE, PINK]

        square_groups = []
        for index, s in enumerate(squares):
            square_groups.append(get_squares(s, colors[index]))

        square_vgroups = []
        for group in square_groups:
            square_vgroups.append(VGroup(*group))

        full_group = VGroup(*square_vgroups)
        full_group.arrange(buff=0.8 * LARGE_BUFF)
        full_group.shift(2 * UP + 2 * RIGHT)

        removables = []

        for square_group in square_groups:
            anims = []
            for square in square_group:
                anims.append(Create(square))
                removables.append(square)
            self.play(AnimationGroup(*anims, lag_ratio=1), run_time=2)  # create square one by one
        self.wait(2)

        ax = Axes(
            x_range=[0, 7],
            y_range=[0, 40],
            x_length=7,
            y_length=5,
            x_axis_config={
                "numbers_to_include": np.arange(0, 7, 1),
                "color": GRAY,
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 40, 10),
                "tick_size": 0.01,
                "longer_tick_multiple": 10,
                "numbers_with_elongated_ticks": np.arange(0, 40, 5),
                "color": GRAY
            },
            tips=True,
        )
        labels = ax.get_axis_labels(x_label="", y_label="")
        labels[0].shift(0.4 * DOWN)
        labels[1].shift(0.4 * LEFT)
        labels.set_color(WHITE)
        labels[1].set_color(YELLOW)
        ax.add(labels)
        ax.next_to(full_group, DOWN)
        ax.shift(0.5 * UP)

        self.play(Create(ax))
        self.wait(3)

        dots = []
        for index, s in enumerate(squares):
            dot = Dot().set_color(colors[index]).move_to(ax.coords_to_point(index + 1, s))
            dots.append(dot)
            copy = full_group[index].copy()
            removables.append(copy)
            self.play(Transform(copy, dot))

        self.wait(3)

        graph = ax.get_graph(lambda x: x ** 2, [0, 6], color=YELLOW)
        removables.append(graph)
        self.play(GrowFromPoint(graph, ax.coords_to_point(0, 0)))

        headline1 = Tex("d", "i", "s", "c", "r", "e", "t", "e", "$\,\,\leftrightarrow\,\,$",
                        r"{\calligra \Large smooth}")
        headline2 = Tex("s", "e", "r", "i", "e", "s", "$\,\,\leftrightarrow\,\,$",
                        r"{\calligra \Large functions}")
        headline3 = Tex("n", "u", "m", "b", "e", "r", "s", "$\,\,\leftrightarrow\,\,$", r"{\calligra \Large geometry}")
        for index in range(0, 8):
            headline1[index].set_color(colors[index % len(colors)])
            if index < len(headline2) - 2:
                headline2[index].set_color(colors[index % len(colors)])
            if index < len(headline2) - 1:
                headline3[index].set_color(colors[index % len(colors)])
        headline1[9].set_color(YELLOW)
        headline2[7].set_color(YELLOW)
        headline3[8].set_color(YELLOW)

        last = logo

        headlines = [
            headline1,
            headline2,
            headline3
        ]

        for headline in headlines:
            align_formulas_with_equal(headline, last, len(headline) - 2, len(last) - 2)
            if last == logo:
                headline.shift(-0.2 * RIGHT)
                headline.next_to(last, DOWN, buff=SMALL_BUFF)
            else:
                headline.next_to(last, DOWN, buff=LARGE_BUFF)
            last = headline

        anims = []
        for index in range(0, 8):
            anims.append(Write(headlines[0][index]))
        self.play(Write(headlines[0][8]))
        self.play(AnimationGroup(*anims, rate_func=linear, lag_ratio=0.5, run_time=2),
                  Write(headlines[0][9], rate_func=linear, run_time=2))

        self.wait(3)

        self.remove(ax)
        self.remove(full_group)
        self.remove(*removables)

        # factorial

        table = MathTable(
            [["1!", "1", "1"],
             ["2!", r"1\cdot 2", "2"],
             ["3!", r"1\cdot 2\cdot 3", "6"],
             ["4!", r"1\cdot 2\cdot 3\cdot 4", "24"],
             [r"\tfrac{1}{2}!", "?", r"\tfrac{\sqrt{\pi}}{2}"]
             ],
            # col_labels=[Text("factorial"), Text("expression"),Text("result")],
            # row_labels=[Text("one"), Text("two"),Text("three"),Text("four")],
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": RIGHT},
            v_buff=SMALL_BUFF,
        )

        table.next_to(title, DOWN)
        table.to_edge(RIGHT)

        table_content = table[0]
        for row in range(0, 4):
            table_content[3 * row + 2].set_color(colors[row % len(colors)])
            table_content[3 * row].set_color(colors[row % len(colors)])
            if row == 0:
                self.play(Write(table_content[3 * row]))
                self.play(Write(table_content[3 * row + 2]))
            else:
                self.play(Write(table_content[3 * row]))
                self.play(Write(table_content[3 * row + 1]))
                self.play(Write(table_content[3 * row + 2]))
            self.wait(2)

        ax = Axes(
            x_range=[-4, 5],
            y_range=[-5, 25],
            x_length=8,
            y_length=3.5,
            x_axis_config={
                "numbers_to_include": np.arange(-4, 5, 1),
                "color": GRAY,
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 25, 5),
                "tick_size": 0.01,
                "longer_tick_multiple": 10,
                "numbers_with_elongated_ticks": np.arange(0, 25, 5),
                "color": GRAY
            },
            tips=True,
        )
        labels = ax.get_axis_labels(x_label="", y_label="")
        labels[0].shift(0.4 * DOWN)
        labels[1].shift(0.4 * LEFT)
        labels.set_color(WHITE)
        labels[1].set_color(YELLOW)
        ax.add(labels)
        ax.next_to(full_group, DOWN)
        ax.shift(DOWN)

        self.play(Create(ax))
        self.wait(3)

        removables = []
        dots = []
        for index in range(0, 4):
            dot = Dot().set_color(colors[index]).move_to(ax.coords_to_point(index + 1, math.factorial(index + 1)))
            dots.append(dot)
            copy = table_content[3 * index + 2].copy()
            removables.append(copy)
            self.play(Transform(copy, dot))

        self.wait(3)

        function = plot_function(ax, lambda x: math.gamma(x + 1), [-0.99, 4], 500, col=YELLOW)
        anim = AnimationGroup(*[Create(line, run_time=2 / len(function)) for line in reversed(function)],
                              rate_func=linear, lag_ratio=1)
        for f in function:
            removables.append(f)
        self.play(anim)

        gammas = []
        for i in range(-4, -1):
            gammas.append(
                plot_function(axes=ax, fnc=lambda x: math.gamma(x + 1), x_range=[i + 0.01, i + 0.99], res=500,
                              col=YELLOW))
        self.wait(3)

        for lines in reversed(gammas):
            anim = AnimationGroup(*[Create(line, run_time=1 / len(lines)) for line in reversed(lines)],
                                  rate_func=linear, lag_ratio=1)
            for l in lines:
                removables.append(l)
            self.play(anim)
        self.wait(3)

        dot = Dot().set_color(colors[4]).move_to(ax.coords_to_point(0.5, math.gamma(1.5)))
        self.play(Write(table_content[12].set_color(colors[4])), Create(dot))
        self.wait(2)

        self.play(TransformFromCopy(dot, table_content[14].set_color(colors[4])))

        self.wait(3)

        anims = []
        for index in range(0, 6):
            anims.append(Write(headlines[1][index]))
        self.play(Write(headlines[1][6]))
        self.play(AnimationGroup(*anims, rate_func=linear, lag_ratio=0.5, run_time=2),
                  Write(headlines[1][7], rate_func=linear, run_time=2))

        self.wait(3)

        self.remove(*table_content)
        self.remove(ax)
        self.remove(dot)
        self.remove(*removables)

        self.wait(2)

        # primes

        removables = []

        ax = Axes(
            x_range=[0, 33],
            y_range=[0, 15],
            x_length=8,
            y_length=6,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(0, 32, 5),
                "color": GRAY,
            },
            y_axis_config={
                "tick_size": 0.03,
                "longer_tick_multiple": 3,
                "numbers_with_elongated_ticks": np.arange(0, 16, 5),
                "numbers_to_include": np.arange(0, 16, 5),
                "color": GRAY
            },
            tips=True,
        )
        labels = ax.get_axis_labels(x_label="", y_label="")
        labels[0].shift(0.4 * DOWN)
        labels[1].shift(0.4 * LEFT)
        labels.set_color(WHITE)
        labels[1].set_color(YELLOW)
        ax.add(labels)

        primes2 = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29, 31, 32, 37]
        primes2_labels = [" 2", " 3", "2^2", " 5", " 7", " 2^3", " 3^2", " 11", " 13", "2^4", " 17", " 19", " 23",
                          " 5^2", " 3^3", " 29", " 31", " 2^5", " 37"]
        prime_dist2 = [1., 2., 2.5, 3.5, 4.5, 4.83333, 5.33333, 6.33333, 7.33333, 7.58333, 8.58333, 9.58333, 10.5833,
                       11.0833, 11.4167, 12.4167, 13.4167, 13.6167, 14.6167]

        prime_color = [YELLOW, YELLOW, RED, YELLOW, YELLOW, GREEN, RED, YELLOW, YELLOW, BLUE, YELLOW, YELLOW,
                       YELLOW, RED, GREEN, YELLOW, YELLOW, ORANGE, YELLOW]

        ax.next_to(title, DOWN)
        ax.to_edge(RIGHT)

        removables.append(ax)
        self.play(Create(ax))
        self.wait()

        data = load_data()
        x_vals = []
        for k in range(1, len(data[0]) + 1):
            x_vals.append(37 / 1000 * k)

        lines = []
        last = len(data) - 2

        for j in range(0, len(data[last]) - 1):
            line = Line(ax.coords_to_point(x_vals[j], data[last][j]),
                        ax.coords_to_point(x_vals[j + 1], data[last][j + 1])).set_color(WHITE)
            line.set_color(YELLOW)
            line.set_style(stroke_width=3)
            lines.append(line)

        current_label_index = 0
        current_label = primes2_labels[current_label_index]
        collect_lines = []
        count = 0
        old_label = None
        for i in range(0, len(lines)):
            removables.append(lines[i])
            collect_lines.append(Create(lines[i], rate_func=linear))
            if x_vals[i] > primes2[current_label_index]:
                self.play(AnimationGroup(*collect_lines, lag_ratio=1, run_time=1))
                collect_lines = []
                lab = MathTex(current_label)
                p_color = prime_color[current_label_index]
                lab.set_color(p_color)
                circle = Circle(radius=0.35)
                circle.set_style(fill_color=p_color, fill_opacity=0.1, stroke_opacity=1, stroke_color=p_color)
                if count % 2 == 0:
                    pos = ax.coords_to_point(primes2[count], prime_dist2[count] + 1)
                else:
                    pos = ax.coords_to_point(primes2[count], prime_dist2[count - 1] - 1)
                label = VGroup(circle, lab)
                label.scale(0.7)
                label.move_to(pos)
                removables.append(lab)
                removables.append(circle)
                if old_label is None:
                    self.play(Write(lab), GrowFromCenter(circle))
                else:
                    self.play(Write(lab), GrowFromCenter(circle))
                    # self.play(FadeOut(old_label),Write(lab),GrowFromCenter(circle))
                current_label_index = current_label_index + 1
                current_label = primes2_labels[current_label_index]
                count = count + 1
                old_label = label

        self.wait(2)

        anims = []
        for index in range(0, 7):
            anims.append(Write(headlines[2][index]))
        self.play(Write(headlines[2][7]))
        self.play(AnimationGroup(*anims, rate_func=linear, lag_ratio=0.5, run_time=2),
                  Write(headlines[2][8], rate_func=linear, run_time=2))

        self.wait(3)

        self.remove(*removables)
        self.wait(10)


def get_squares(n=9, color=GREEN):
    rows = int(np.sqrt(n))
    group = []
    row_last = None
    for row in range(0, rows):
        col_last = None
        for col in range(0, rows):
            s = Square().scale(0.1)
            s.set_style(fill_color=color, fill_opacity=0.8, stroke_color=color, stroke_opacity=1)

            if row > 0 and col == 0:
                s.next_to(row_last, DOWN, buff=0.5 * SMALL_BUFF)
            if col > 0:
                s.next_to(col_last, RIGHT, buff=0.5 * SMALL_BUFF)
            else:
                row_last = s

            group.append(s)
            col_last = s

    return group


class zeta(Scene):
    def construct(self):
        title = Tex(r"The $\zeta$-function")
        title.set_color(RED)
        title.to_edge(UP)
        self.play(Write(title))

        first = "01_empty_grid"
        img = ImageMobject(first)
        img.to_corner(UP + LEFT)
        # self.play(FadeIn(img))
        self.wait(2)

        movers = [title]

        labels = []
        for i in range(1, 11, 1):
            label = MathTex(str(i))
            label.scale(0.5)
            label2 = label.copy()
            label.move_to((2.65 - 0.35 * i) * LEFT + 0.75 * DOWN)
            label2.move_to(2.75 * LEFT + (-0.5 + 0.34 * i) * UP)
            labels.append(label)
            labels.append(label2)

        neg_labels = []
        for i in range(-10, 0, 2):
            label = MathTex(str(i))
            label.scale(0.5)
            label.move_to((2.65 - 0.35 * i) * LEFT + 0.75 * DOWN)
            neg_labels.append(label)

        nnew_squares = []
        for i in range(1, 6):
            square = MathTex(r"1", "\over", str(i), "^2")
            square.scale(0.7)
            nnew_squares.append(square)
            movers.append(square)
            if i < 5:
                tex = MathTex("+")
                nnew_squares.append(tex.scale(0.7))
                movers.append(tex)
        math_tex = MathTex(r"\dots")
        movers.append(math_tex)
        nnew_squares.append(math_tex.scale(0.7))

        for i, square in enumerate(nnew_squares):
            if i == 0:
                square.next_to(img, RIGHT, buff=0.8 * LARGE_BUFF)
                square.shift(2.25 * UP)
            else:
                square.next_to(nnew_squares[i - 1], RIGHT, buff=0.7 * SMALL_BUFF)
            if i % 2 == 0:
                square[3].set_color(YELLOW)

        new_squares = []
        for i in range(1, 6):
            square = MathTex(r"1", "\over", str(i * i))
            square.scale(0.7)
            new_squares.append(square)
            movers.append(square)
            if i < 5:
                m = MathTex("+")
                new_squares.append(m.scale(0.7))
        tex1 = MathTex(r"\dots")
        new_squares.append(tex1.scale(0.7))

        for i, square in enumerate(new_squares):
            if i == 0:
                square.next_to(nnew_squares[0], UP)
            elif i<len(new_squares)-1:
                square.next_to(new_squares[i - 1], RIGHT, buff=0.85 * SMALL_BUFF)
            else:
                square.next_to(new_squares[i - 1], RIGHT, buff=1.2 * SMALL_BUFF)
            if i % 2 == 0:
                square[2].set_color(YELLOW)

        squares = []
        for i in range(1, 6):
            square = MathTex(str(i * i))
            square.scale(0.7)
            movers.append(square)
            squares.append(square)
            if i < 5:
                tex2 = MathTex("+")
                squares.append(tex2.scale(0.7))
        tex3 = MathTex("1",r"\dots")
        tex3[0].set_color(BLACK)
        movers.append(tex3)
        squares.append(tex3.scale(0.7))

        for i, square in enumerate(squares):
            square.move_to(new_squares[i])
            # if i == 0:
            #     square.next_to(new_squares[0], UP)
            # else:
            #     square.next_to(squares[i - 1], RIGHT, buff=0.9 * SMALL_BUFF)
            if i % 2 == 0:
                square.set_color(YELLOW)
        self.play(*[Write(squares[i]) for i in range(0, len(squares), 2)],Write(squares[len(squares)-1]))
        self.wait(2)

        self.play(*[Transform(squares[i], new_squares[i]) for i in range(0, len(squares), 2)],)
        self.wait(2)

        self.play(*[TransformFromCopy(squares[i], nnew_squares[i]) for i in range(0, len(squares), 2)])
        self.wait(2)

        zeta = MathTex(r"\zeta(", "2", ")", "=")
        movers.append(zeta)
        zeta.scale(0.7)
        zeta[1].set_color(YELLOW)
        zeta.next_to(nnew_squares[0], LEFT)
        sol = MathTex(r"\approx 1.64")
        movers.append(sol)
        sol.scale(0.7).set_color(YELLOW).next_to(nnew_squares[len(nnew_squares) - 1], RIGHT)

        self.play(*[Write(nnew_squares[i]) for i in range(1, len(nnew_squares), 2)])
        self.play(Write(zeta), Write(sol))
        self.play(title.animate().to_corner(UP + RIGHT).shift(0.9 * LEFT))
        self.wait(2)

        self.play(*[Write(labels[i]) for i in range(0, len(labels))])
        self.wait(2)

        val = [1.20, 1.08, 1.04, 1.02, 1.01, 1.00]
        tmp = nnew_squares

        for i in range(3, 8):
            parts = []
            for j in range(1, 6):
                square = MathTex(r"1", "\over", str(j), "^" + str(i))
                movers.append(square)
                square.scale(0.7)
                square[3].set_color(YELLOW)
                parts.append(square)
                if j < 5:
                    tex4 = MathTex("+")
                    movers.append(tex4)
                    parts.append(tex4.scale(0.7))
            tex5 = MathTex(r"\dots")
            movers.append(tex5)
            parts.append(tex5.scale(0.7))

            for j, square in enumerate(parts):
                if j == 0:
                    square.next_to(tmp[0], DOWN)
                else:
                    square.next_to(parts[j - 1], RIGHT, buff=0.7 * SMALL_BUFF)

            zeta = MathTex(r"\zeta(", str(i), ")", "=")
            movers.append(zeta)
            zeta.scale(0.7)
            zeta[1].set_color(YELLOW)
            zeta.next_to(parts[0], LEFT)
            sol = MathTex(r"\approx " + str(val[i - 3]))
            movers.append(sol)
            sol.scale(0.7).set_color(YELLOW).next_to(parts[len(parts) - 1], RIGHT)

            self.play(Write(zeta), *[Write(parts[i]) for i in range(0, len(parts))], Write(sol))
            self.wait(2)
            tmp = parts

        self.wait(5)

        self.play(*[mover.animate().shift(1.8 * UP) for mover in movers])
        self.wait(2)

        dots = MathTex(r"\dots")
        dots.scale(0.7)
        dots.next_to(zeta,DOWN,buff = LARGE_BUFF)
        dots.align_to(zeta[3],LEFT)
        self.play(Write(dots))
        self.wait(2)

        harmonic = MathTex(r"\zeta(",str(1),")","=")
        harmonic.scale(0.7)
        harmonic[1].set_color(YELLOW)
        parts = []
        for j in range(1, 6):
            square = MathTex(r"1", "\over", str(j), "^" + str(1))
            movers.append(square)
            square.scale(0.7)
            square[3].set_color(YELLOW)
            parts.append(square)
            if j < 5:
                tex4 = MathTex("+")
                movers.append(tex4)
                parts.append(tex4.scale(0.7))
        tex5 = MathTex(r"\dots")
        movers.append(tex5)
        parts.append(tex5.scale(0.7))

        harmonic.next_to(dots, DOWN,buff = LARGE_BUFF)
        align_formulas_with_equal(harmonic, zeta, 3, 3)

        for j, square in enumerate(parts):
            if j == 0:
                square.next_to(harmonic, RIGHT)
            else:
                square.next_to(parts[j - 1], RIGHT, buff=0.7 * SMALL_BUFF)


        infty = MathTex(r"=\infty")
        infty.scale(0.7)
        infty.set_color(YELLOW)
        infty.next_to(parts[len(parts)-1],RIGHT)

        self.play(Write(harmonic))
        self.play(*[Write(part) for part in parts])
        self.play(Write(infty))
        self.wait(2)

        self.play(*[Write(neg_labels[i]) for i in range(0, len(neg_labels))])
        self.wait(2)




        self.wait(10)


class Intro2(Scene):
    def construct(self):

        title = Tex("The sound of primes")
        title.set_color(YELLOW)
        title.to_edge(UP)

        self.play(Write(title))

        # logo
        n = 19

        def path(t):
            step = np.floor(np.abs(n * t) / np.pi)
            sign = (-1) ** step
            val = 0.25 * sign * np.cos(sign * np.abs(n * t)) - 0.5 * step + (n - 1) / 4 + 1j * (
                    0.25 * np.sin(n * t) + 0.75)
            inv = 1 / val.conjugate()  # circluar inversion
            return np.array((inv.real, inv.imag, 0))

        function = ParametricFunction(path, t_range=np.array([-np.pi, np.pi]), fill_opacity=0).set_color(RED)

        circles1 = []
        for index in range(-int(np.floor(n / 2)), int(np.floor(n / 2))):
            den = 2 + index * index
            r = 1 / den
            x = 2 * index / den
            y = 3 / den
            c = Circle().scale(r).move_to(x * LEFT + y * UP)
            c.set_style(fill_color=RED, fill_opacity=0.8);
            circles1.append(c)

        circles2 = []
        for index in range(-int(np.floor(n / 2)), int(np.floor(n / 2))):
            den = 6 + 4 * index * (index - 1)
            r = 1 / den
            x = (8 * index - 4) / den
            y = 9 / den
            c = Circle().scale(r).move_to(x * LEFT + y * UP)
            c.set_style(fill_color=GREEN, fill_opacity=0.8, stroke_color=GREEN);
            circles2.append(c)

        circles3 = []
        for index in range(-int(np.floor(n / 2)), int(np.floor(n / 2))):
            den = 15 + 4 * index * (index - 1)
            r = 1 / den
            x = (8 * index - 4) / den
            y = 15 / den
            c = Circle().scale(r).move_to(x * LEFT + y * UP)
            c.set_style(fill_color=BLUE, fill_opacity=0.8, stroke_color=BLUE);
            circles3.append(c)

        logo = VGroup(function, *circles1, *circles2, *circles3)

        logo.scale(1)
        logo.to_corner(UP + LEFT)
        logo.shift(1.5 * RIGHT)

        number_objects = []
        prime_objects = []
        non_prime_objects = []
        primes = [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                  101]
        prime_dist = [0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 11,
                      11, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 16, 16, 16,
                      16, 16, 16, 17, 17, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 20, 20, 21, 21, 21, 21, 21, 21, 22,
                      22, 22, 22, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25]

        def pdf(x):
            return prime_dist[int(x)]

        for row in range(0, 10):
            for col in range(0, 10):
                number = row * 10 + col + 1
                number_obj = MathTex(str(number))
                number_obj.scale(0.7)
                if number in primes:
                    prime_objects.append(number_obj)
                else:
                    non_prime_objects.append(number_obj)
                number_objects.append(number_obj)

        group = VGroup(*number_objects)
        group.arrange_in_grid(10, 10)
        group.next_to(logo, DOWN)
        group.shift(0.5 * RIGHT)

        ax = Axes(
            x_range=[0, 105],
            y_range=[0, 30],
            x_length=6,
            y_length=5.5,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(0, 101, 10),
                "tick_size": 0.01,
                "longer_tick_multiple": 10,
                "numbers_with_elongated_ticks": np.arange(0, 101, 5),
                "color": GRAY,
                "font_size": 18,
                "line_to_number_buff": 1.3 * MED_SMALL_BUFF
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 30, 5),
                "tick_size": 0.03,
                "longer_tick_multiple": 3,
                "numbers_with_elongated_ticks": np.arange(0, 30, 5),
                "font_size": 18,
                "color": GRAY
            },
            tips=True,
        )
        labels = ax.get_axis_labels(x_label="x", y_label="\\pi(x)")
        labels[0].shift(0.4 * DOWN)
        labels[1].shift(0.4 * LEFT)
        labels.set_color(WHITE)
        labels[1].set_color(YELLOW)
        ax.add(labels)
        ax.next_to(logo, DOWN, buff=-1 * LARGE_BUFF)
        ax.to_edge(LEFT, buff=SMALL_BUFF)

        fade_out_anims = []
        count = 0
        for i in range(1, 101):
            if i in primes:
                graph = ax.get_graph(lambda x: pdf(x), color=YELLOW, x_range=[i + 0.001, i + 1 - 0.001, 0.1])
                fade_out_anims.append(TransformFromCopy(number_objects[i - 1], graph,run_time=2))
                fade_out_anims.append(number_objects[i-1].animate().scale(0.7).set_color(YELLOW).move_to(ax.coords_to_point(i,-1+2*(count%2))))
                count = count+1
            else:
                graph = ax.get_graph(lambda x: pdf(x), color=WHITE, x_range=[i + 0.01, i + 1 - 0.01, 0.1])
                fade_out_anims.append(Transform(number_objects[i - 1], graph))
                #fade_out_anims.append(FadeOut(number_objects[i - 1]))

        time = 15  # 6

        circles_and_graph = AnimationGroup(
                AnimationGroup(
                    *[AnimationGroup(GrowFromCenter(circles1[i], run_time=1.5*time / 4), GrowFromCenter(circles2[i], run_time=1.5),
                           GrowFromCenter(circles3[i], run_time=2.25)) for i in range(0, len(circles1))],
                                    lag_ratio=0.1
                ),# draw circles
                AnimationGroup(*fade_out_anims, lag_ratio=0.1, run_time=3*time / 4), # create graph
                lag_ratio=0)

        logo_lines_and_numbers = AnimationGroup(
            AnimationGroup(
                Create(function, run_time=time / 3, rate_func=rate_functions.linear),  # draw logo lines
                AnimationGroup(*[Write(number, run_time=time / 300) for number in number_objects], lag_ratio=1),# write numbers
                lag_ratio=0)
        )

        axes_and_yellow = AnimationGroup(
            Create(ax),
            *[p.animate().scale(1.2).set_color(YELLOW) for p in prime_objects],
            *[n.animate().fade(0.75) for n in non_prime_objects],
            lag_ratio = 0
        )
        #self.play(AnimationGroup(*anims, lag_ratio=0.5))

        self.play(logo_lines_and_numbers)
        self.play(axes_and_yellow)
        self.play(circles_and_graph)

        self.wait(2)

        zeta = MathTex(r"\zeta",r"(",r"s",r")","=","1","+",r"\frac{1}{2^s}","+",r"\frac{1}{3^s}",r"+",r"\frac{1}{4^s}",r"+",r"\frac{1}{5^s}",r"+",r"\frac{1}{6^s}",r"+",r"\frac{1}{7^s}",r"+",r"\dots")
        colors = color_gradient(["#ff0000", "#ffff000","#ffff00", "#00ff00", "#00ffff", "#0000ff", "#ff00ff","ff0000"],len(zeta))
        for i,z in enumerate(zeta):
            z.set_color(colors[i])
        zeta.next_to(logo, RIGHT, buff=1.5 * LARGE_BUFF)
        zeta.shift(0.25 * DOWN)
        zeta.scale(0.7)

        self.play(Write(zeta))
        self.wait(10)


class Overview(Scene):
    def construct(self):

        title = Tex("The sound of primes")
        title.set_color(YELLOW)
        title.to_edge(UP)

        self.add(title)

        parts = [Tex("I"),Tex("II"),Tex("III"),Tex("IV")]
        for p in parts:
            p.scale(0.7)

        rect1  = Rectangle(WHITE,3,4.5)
        rect1.shift(1.25 *UP+4.75*LEFT)
        parts[0].move_to(rect1.get_corner(UP+LEFT)).shift(0.2*UP)
        rect2 = Rectangle(WHITE, 3, 4.5)
        rect2.shift(1.25 * UP )
        parts[1].move_to(rect2.get_corner(UP + LEFT)).shift(0.2*UP)
        rect3 = Rectangle(WHITE, 3, 4.5)
        rect3.shift(1.25 * UP+4.75*RIGHT)
        parts[2].move_to(rect3.get_corner(UP + LEFT)).shift(0.2*UP)

        rect4 = Rectangle(WHITE,3,9)
        rect4.shift(2.25*DOWN)
        parts[3].move_to(rect4.get_corner(UP+LEFT)).shift(0.2*UP)

        self.play(Write(parts[0]),GrowFromPoint(rect1,rect1.get_corner(UP+LEFT)))
        self.wait(10)
        self.play(Write(parts[1]),GrowFromPoint(rect2,0.5*(rect2.get_corner(UP+LEFT)+rect2.get_corner(UP+RIGHT))))
        self.wait(10)
        self.play(Write(parts[2]),GrowFromPoint(rect3,rect3.get_corner(UP+RIGHT)))
        self.wait(10)
        self.play(Write(parts[3]),GrowFromPoint(rect4,0.5*(rect4.get_corner(DOWN+LEFT)+rect4.get_corner(DOWN+RIGHT))))
        self.wait(2)
        img = ImageMobject("riemann1.png")
        img2 = ImageMobject("riemann2.png")
        img.scale(0.45)
        img2.scale(0.45)
        img.move_to(rect4.get_corner(UP+LEFT)+1.5*DOWN+1*RIGHT)
        img2.next_to(img,RIGHT)
        self.play(FadeIn(img))
        self.play(FadeIn(img2))
        self.wait(10)


class PrimesAndZeta(Scene):
    def construct(self):
        title =Tex("Primes ","and ","$\zeta$")
        title[0].set_color(YELLOW)
        title[2].set_color(RED)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        relation = MathTex(r"\Pi(x)","=",r"\frac{1}{2\pi}\int\limits_{-\infty}^{\infty}\frac{\log\zeta(a+i b)}{a+i b} x^{a+i b}\,{\rm d}b")
        relation[0].set_color(YELLOW)
        relation[2].set_color(RED)
        relation.next_to(title,DOWN)
        relation.to_edge(RIGHT)

        self.play(Write(relation))
        self.wait(10)


class WithoutTitle(Scene):
    def construct(self):
        function = MathTex(r"x^s","x=")
        number = DecimalNumber(num_decimal_places=1)
        number.set_value(1)
        function[1].shift(2*RIGHT)
        number.next_to(function,RIGHT)
        s = ValueTracker(1)
        s.add_updater(lambda mobject, dt: mobject.increment_value(9/5*dt))

        draw_number = (lambda: number.set_value(s.get_value()))

        number_writer=  always_redraw(draw_number)
        self.play(Write(function[0]))
        self.wait()
        self.play(Write(function[1]))
        self.play(Write(number))
        self.wait()
        self.add(s,number_writer)
        self.wait(5)
        s.clear_updaters()

        self.wait(10)

        s.add_updater(lambda mobject, dt: mobject.increment_value(-9/4.333*dt))
        self.add(s)
        self.wait(4.3333)
        s.clear_updaters()

        self.wait(10)

        self.play(FadeOut(function),FadeOut(number))

        self.wait(2)
        eq1 = MathTex(r"\Pi(2.9)"r"\approx",r"1")
        eq2 = MathTex(r"\Pi(3.1)"r"\approx",r"2")
        eq2.next_to(eq1,DOWN)
        align_formulas_with_equal(eq2,eq1,1,1)
        self.play(Write(eq1))
        self.play(Write(eq2))

        self.wait(10)