import cmath
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
        self.play(Create(approx1), Write(functions[0]))
        self.wait(3)
        self.play(Create(approx2), Transform(functions[0], functions[1]))
        self.wait(3)
        self.play(Create(approx3), Transform(functions[0], functions[2]))
        self.wait(3)
        self.play(Create(approx4), Transform(functions[0], functions[3]))
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

        theorem = MathTex(r"f(x)", "=", r"\sum_{n=0}^\infty", r"a_n", r"\sin(n\cdot x)+", "b_n", r"\cos(n\cdot x)")
        theorem.set_color(WHITE)
        theorem.scale(0.7)
        theorem.next_to(conclusion, DOWN)
        theorem.to_edge(LEFT)

        theorem2 = MathTex(r"a_n", r"=", r"\tfrac{1}{\pi}\int\limits_{0}^{2\pi}f(x)\sin(n\cdot x) {\rm d} x")
        theorem3 = MathTex(r"b_n", r"=", r"\tfrac{1}{\pi}\int\limits_{0}^{2\pi}f(x)\cos(n\cdot x) {\rm d} x")
        theorem2.set_color(GREEN)
        theorem3.set_color(RED)
        theorem2.scale(0.7)
        theorem3.scale(0.7)
        theorem2.next_to(theorem, DOWN)
        theorem3.next_to(theorem2, DOWN)
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
        self.wait(10)


class Primes(Scene):
    def construct(self):
        title = MathTex(r"\text{The prime distribution function: }", "\pi(x)")
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
        self.wait(3)
        data = load_data()
        x_vals = []
        for i in range(1, len(data[0]) + 1):
            x_vals.append(37 / 1000 * i)
        dots = []
        for i in range(0, len(data)):
            dots.append(VGroup(*[Line(ax.coords_to_point(x_vals[j], data[i][j]),
                                      ax.coords_to_point(x_vals[j + 1], data[i][j + 1])).set_color(WHITE) for j in
                                 range(0, len(data[i]) - 1)]))
        for i in range(0, len(dots)):
            if i > 0:
                self.remove(dots[i - 1])
            self.play(Create(dots[i]))
            self.wait(2)

        result = MathTex(r"\Pi", "(", "x", ")", "=",
                         r"\frac{1}{2\pi}\int\limits_{-\infty}^{+\infty}\log\left(\zeta(a+i b)\right )\frac{x^{a+i b}}{a+ i b}{\rm d}b")
        result[0].set_color(YELLOW)
        result[1].set_color(RED)
        result[2].set_color(GREEN)
        result[3].set_color(BLUE)
        result.to_edge(RIGHT)
        result.shift(1.5 * DOWN)
        rect = SurroundingRectangle(result)
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
        title = Tex("Riemann 1856")
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
        title = Tex("Riemann 1856")
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
        title = Tex("Riemann 1856")
        title.to_edge(UP)
        title.set_color(YELLOW)

        self.add(title)

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
                               r"\int\limits_" + str(p[i]) + "^" + str(p[i + 1]) + r"x^{-s-1}{\rm d}x")
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
        title = Tex("Riemann 1856")
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


class Logo(Scene):
    def construct(self):
        title = Tex("Primes and $\zeta(s)$")
        title.set_color(YELLOW)
        title.to_edge(UP)

        self.play(Write(title))

        n= 19

        def path(t):
            step = np.floor(np.abs(n*t)/np.pi)
            sign = (-1)**step
            val = 0.25*sign*np.cos(sign*np.abs(n*t))-0.5*step+(n-1)/4+1j*(0.25*np.sin(n*t)+0.75)
            inv = 1/val.conjugate() #circluar inversion
            return np.array((inv.real, inv.imag, 0))

        function = ParametricFunction(path, t_range=np.array([-np.pi, np.pi]), fill_opacity=0).set_color(RED)

        circles1 = []
        for i in range(-int(np.floor(n/2)),int(np.floor(n/2))):
            den = 2+i*i
            r = 1/den
            x = 2*i/den
            y = 3/den
            c = Circle().scale(r).move_to(x*LEFT+y*UP)
            c.set_style(fill_color=RED,fill_opacity=0.8);
            circles1.append(c)

        circles2 = []
        for i in range(-int(np.floor(n / 2)), int(np.floor(n / 2))):
            den = 6+4*i*(i-1)
            r = 1 / den
            x = (8 * i-4) / den
            y = 9 / den
            c = Circle().scale(r).move_to(x * LEFT + y * UP)
            c.set_style(fill_color=GREEN, fill_opacity=0.8,stroke_color=GREEN);
            circles2.append(c)

        circles3 = []
        for i in range(-int(np.floor(n / 2)), int(np.floor(n / 2))):
            den = 15+4*i*(i-1)
            r = 1 / den
            x = (8*i-4) / den
            y = 15 / den
            c = Circle().scale(r).move_to(x * LEFT + y * UP)
            c.set_style(fill_color=BLUE, fill_opacity=0.8,stroke_color=BLUE);
            circles3.append(c)

        group = VGroup(function,*circles1,*circles2,*circles3)

        group.scale(2)
        group.shift(-5*RIGHT+0.9*UP)
        anims = []
        anims.append(Create(function,run_time=6,rate_func=rate_functions.double_smooth))
        anims.append(AnimationGroup(*[AnimationGroup(GrowFromCenter(circles1[i],run_time=1.5),GrowFromCenter(circles2[i],run_time=1),GrowFromCenter(circles3[i],run_time=1.5)) for i in range(0,len(circles1))],lag_ratio=0.1))
        self.play(AnimationGroup(*anims,lag_ratio=0.5))

        #squares

        squares = [1,4,9,16,25]

        anims = []
        for s in squares:
            anims.append(get_squares(s))

        square_groups = VGroup(*anims)
        square_groups.arrange()
        #primes

        # ax = Axes(
        #     x_range=[0, 33],
        #     y_range=[0, 15],
        #     x_length=12,
        #     y_length=6.5,
        #     axis_config={"color": GREEN},
        #     x_axis_config={
        #         "numbers_to_include": np.arange(0, 32, 5),
        #         "color": GRAY,
        #     },
        #     y_axis_config={
        #         "numbers_to_include": np.arange(0, 16, 5),
        #         "color": GRAY
        #     },
        #     tips=True,
        # )
        # labels = ax.get_axis_labels(x_label="", y_label="")
        # labels[0].shift(0.4 * DOWN)
        # labels[1].shift(0.4 * LEFT)
        # labels.set_color(WHITE)
        # labels[1].set_color(YELLOW)
        # ax.add(labels)
        #
        #
        # primes2 = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29, 31, 32, 37]
        # primes2_labels = [" 2", " 3", "2^2", " 5", " 7", " 2^3", " 3^2", " 11", " 13", "2^4", " 17", " 19", " 23",
        #                   " 5^2", " 3^3", " 29", " 31", " 2^5", " 37"]
        #
        # prime_color = [YELLOW, YELLOW, RED, YELLOW, YELLOW, GREEN, RED, YELLOW, YELLOW, BLUE, YELLOW, YELLOW,
        #                YELLOW, RED, GREEN, YELLOW, YELLOW, ORANGE, YELLOW]
        #
        # ax.next_to(title,DOWN)
        # ax.shift(0.5*UP+ 0.75*RIGHT)
        #
        # self.play( Create(ax))
        # self.wait()
        #
        # data = load_data()
        # x_vals = []
        # for k in range(1, len(data[0]) + 1):
        #     x_vals.append(37 / 1000 * k)
        #
        # lines = []
        # last = len(data) - 2
        #
        # for j in range(0, len(data[last]) - 1):
        #     line = Line(ax.coords_to_point(x_vals[j], data[last][j]),
        #                 ax.coords_to_point(x_vals[j + 1], data[last][j + 1])).set_color(WHITE)
        #     line.set_color(YELLOW)
        #     line.set_style(stroke_width=3)
        #     lines.append(line)
        #
        # current_label_index = 0
        # current_label = primes2_labels[current_label_index]
        # collect_lines = []
        # count = 0
        # old_label = None
        # for i in range(0, len(lines)):
        #     collect_lines.append(Create(lines[i],rate_func=linear))
        #     if x_vals[i] > primes2[current_label_index]:
        #         self.play(AnimationGroup(*collect_lines,lag_ratio=1,run_time=1))
        #         collect_lines = []
        #         lab = MathTex(current_label)
        #         p_color = prime_color[current_label_index]
        #         lab.set_color(p_color)
        #         circle = Circle(radius = 0.3)
        #         circle.set_style(fill_color=p_color,fill_opacity=0.1,stroke_opacity=1,stroke_color=p_color)
        #         if count%2==0:
        #             pos = lines[i].get_last_point()+0.5*UP
        #         else:
        #             pos = lines[i].get_last_point()-0.8*UP
        #         label = VGroup(circle,lab)
        #         label.move_to(pos)
        #         if old_label is None:
        #             self.play(Write(lab),GrowFromCenter(circle))
        #         else:
        #             self.play(Write(lab),GrowFromCenter(circle))
        #             #self.play(FadeOut(old_label),Write(lab),GrowFromCenter(circle))
        #         current_label_index = current_label_index + 1
        #         current_label = primes2_labels[current_label_index]
        #         count=count+1
        #         old_label = label
        #
        # self.wait(2)
