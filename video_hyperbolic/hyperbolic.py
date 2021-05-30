from abc import ABC

from manim import *
import numpy as np


class Intro(ThreeDScene):

    def construct(self):
        title = Tex("Constant curvature surfaces")
        title.set_color(YELLOW)
        self.add_fixed_in_frame_mobjects(title)
        title.to_edge(UP)

        self.play(GrowFromCenter(title))

        resolution_fa = 11

        plane_section = Tex("The flat plane:")
        plane_section.set_color(BLUE)
        plane_section.next_to(title, DOWN, buff=MED_LARGE_BUFF)
        plane_section.to_edge(LEFT)

        plane_curvature = Tex("R=0")
        plane_curvature.set_color(BLUE)
        plane_curvature.scale(0.7)
        plane_curvature.align_to(plane_section, LEFT)
        plane_curvature.to_edge(DOWN, buff=LARGE_BUFF)
        self.play(Write(plane_section))
        self.add_fixed_in_frame_mobjects(plane_section)

        plane = ParametricSurface(lambda u, v: np.array([u, v, 0]),
                                  resolution=(resolution_fa, resolution_fa),
                                  v_min=-2,
                                  v_max=2,
                                  u_min=-2,
                                  u_max=2)

        plane.rotate(55 * DEGREES, LEFT)
        plane.shift(4.3 * LEFT)

        plane.scale_about_point(1, ORIGIN)
        plane.set_style(fill_opacity=1)
        plane.set_style(stroke_color=BLUE)
        plane.set_fill_by_checkerboard(YELLOW, BLUE, opacity=0.9)

        self.play(Create(plane))
        self.play(Write(plane_curvature))
        self.add_fixed_in_frame_mobjects(plane_curvature)

        self.wait(3)

        sphere_section = Tex("The sphere:")
        sphere_section.set_color(GREEN)
        sphere_section.next_to(title, DOWN, buff=MED_LARGE_BUFF)

        sphere_curvature = MathTex(r"R=\tfrac{2}{r^2}")
        sphere_curvature.set_color(GREEN)
        sphere_curvature.scale(0.7)
        sphere_curvature.to_edge(DOWN, buff=LARGE_BUFF)

        self.play(Write(sphere_section))
        self.add_fixed_in_frame_mobjects(sphere_section)

        sphere = Sphere(radius=1.5)
        sphere.rotate(55 * DEGREES, LEFT)
        sphere.set_style(fill_opacity=1)
        sphere.set_style(stroke_color=GREEN)
        sphere.set_fill_by_checkerboard(YELLOW, GREEN, opacity=0.9)

        self.play(GrowFromCenter(sphere))

        self.play(Write(sphere_curvature))
        self.add_fixed_in_frame_mobjects(sphere_curvature)

        self.wait(3)

        hyperbolic_section = Tex("The hyperbolic plane:")
        hyperbolic_section.set_color(RED)
        hyperbolic_section.next_to(title, DOWN, buff=MED_LARGE_BUFF)
        hyperbolic_section.to_edge(RIGHT, buff=MED_LARGE_BUFF)

        hyperbolic_curvature = MathTex(r"R=-\tfrac{2}{r^2}")
        hyperbolic_curvature.set_color(RED)
        hyperbolic_curvature.scale(0.7)
        hyperbolic_curvature.align_to(hyperbolic_section, RIGHT)
        hyperbolic_curvature.to_edge(DOWN, buff=LARGE_BUFF)

        self.play(Write(hyperbolic_section))
        self.add_fixed_in_frame_mobjects(hyperbolic_section)

        hyperbolic = ParametricSurface(
            lambda u, v: np.array([3 * (-0.5 + u), 3 * (-0.5 + v), 5 * ((-0.5 + u) ** 2 - (-0.5 + v) ** 2)]),
            resolution=(resolution_fa, resolution_fa)
        )
        hyperbolic.set_color(RED, 0.3)
        hyperbolic.rotate(90 * DEGREES, LEFT)
        hyperbolic.rotate(25 * DEGREES, UP)
        hyperbolic.shift(4.5 * RIGHT)
        hyperbolic.set_style(fill_opacity=1)
        hyperbolic.set_style(stroke_color=RED)
        hyperbolic.set_fill_by_checkerboard(YELLOW, RED, opacity=0.9)

        self.play(Create(hyperbolic))

        self.play(Write(hyperbolic_curvature))
        self.add_fixed_in_frame_mobjects(hyperbolic_curvature)

        question = Tex("?")
        question.set_color(RED)
        question.set_style(fill_color=RED, fill_opacity=0.5, stroke_color=YELLOW, stroke_opacity=1, stroke_width=2)
        question.scale(10)
        question.move_to(hyperbolic)

        self.play(Write(question), run_time=5)
        self.add_fixed_in_frame_mobjects(question)

        self.wait(5)


class Start(ThreeDScene):
    def construct(self):
        title = Tex("The standard embeddings of the hyperbolic plane")
        title.set_color(YELLOW)
        title.to_edge(UP)

        self.play(GrowFromCenter(title))
        self.add_fixed_in_frame_mobjects(title)

        hyperboloid = Hyperboloid()
        hyperboloid.shift(2 * DOWN)

        hyperboloid.set_style(fill_opacity=0.3, stroke_color=BLUE, stroke_opacity=1, stroke_width=2, fill_color=GREY)

        self.play(Create(hyperboloid))
        self.play(ApplyMethod(hyperboloid.rotate, 30 * DEGREES, LEFT), run_time=5)
        # self.play(ApplyMethod(hyperboloid.rotate, -30*DEGREES, LEFT), run_time=1)

        self.wait(3)

        pd = PoincareDisc()
        pd.set_style(fill_opacity=0.3, stroke_color=BLUE, stroke_opacity=1, stroke_width=2, fill_color=GREY)
        pd.scale(3)
        pd.rotate(-60 * DEGREES, LEFT)

        self.play(Transform(hyperboloid, pd), run_time=5)

        self.wait(3)

        hyperboloid.generate_target()
        hyperboloid.target.scale(0.3333)
        hyperboloid.target.rotate(60 * DEGREES, LEFT)
        self.play(MoveToTarget(hyperboloid))

        mirror = Circle(radius=np.sqrt(2), arc_center=DOWN)
        mirror.set_color(YELLOW)
        self.play(
            GrowFromCenter(mirror), run_time=5
        )

        uhp = UpperHalfPlane(maximum=2, res=10)
        uhp.set_style(fill_opacity=0.3, stroke_color=BLUE, stroke_opacity=1, stroke_width=2, fill_color=GREY)
        self.play(Create(uhp), run_time=5)
        self.wait(3)

        uhp2 = UpperHalfPlane(maximum=4, res=20)
        uhp2.set_style(fill_opacity=0.0, stroke_color=BLUE, stroke_opacity=1, stroke_width=2)
        uhp2.set_fill_by_checkerboard(YELLOW, BLUE, opacity=0.9)
        self.play(Create(uhp2), run_time=5)
        self.wait(10)


class Tesselation(ThreeDScene, MovingCameraScene):
    def construct(self):
        self.set_camera_orientation(phi=135*DEGREES)
        title = Tex("The hyperbolic plane with a tesselation")
        title.set_color(YELLOW)
        title.to_corner(DL)
        self.add(title)
        self.add_fixed_in_frame_mobjects(title)

        dia = DynkinDiagram([3, 7], [0, 1, 0], [YELLOW, YELLOW, YELLOW], ["", "", ""])
        dia.scale(1)
        dia.to_corner(DR)
        self.play(Create(dia))
        self.add_fixed_in_frame_mobjects(dia)

        hyperboloid = Hyperboloid2()
        hyperboloid.set_style(fill_color=GREY)
        #hyperboloid.set_fill_by_checkerboard(YELLOW, RED, opacity=0.3)

        self.play(FadeIn(hyperboloid))
        #self.play(ApplyMethod(hyperboloid.rotate, 30 * DEGREES, LEFT), run_time=5)
        #self.play(ApplyMethod(hyperboloid.rotate, -30 * DEGREES, LEFT), run_time=5)
        #self.play(ApplyMethod(hyperboloid.shift,2*IN),run_time = 5)

        f = open("assets/points7.csv", "r")
        line = f.readline()
        points = []
        while not line == "":
            point = np.array([float(i) for i in line.split(",")])
            points.append(point)
            line = f.readline()

        f.close()

        f = open("assets/lines7.csv", "r")
        line = f.readline()
        edges = []
        while not line == "":
            edge = np.array([int(i) - 1 for i in line.split(",")])  # mathematica index conversion
            edges.append(edge)
            line = f.readline()

        f.close()

        dots = []
        for point in points:
            sphere = Sphere(radius=0.15, resolution=(11, 5))
            sphere.shift(point)
            sphere.set_color(RED)
            if point[2] <= np.cosh(1.5):
                dots.append(sphere)

        curves = []
        for edge in edges:
            curve = HyperArc(points[edge[0]], points[edge[1]])
            curve.set_color(GREEN)
            if points[edge[0]][2] <= np.cosh(1.5) and points[edge[1]][2] <= np.cosh(1.5):
                curves.append(curve)

        self.play(
            *[Create(dot) for dot in dots],
            *[FadeIn(curve) for curve in curves]
        )

        # dots2 = []
        # for point in points:
        #     sphere = Circle(radius=0.015)
        #     sphere.shift(poincare_transform(point))
        #     sphere.set_style(fill_color=RED, fill_opacity=1)
        #     if point[2] <= np.cosh(3):
        #         dots2.append(sphere)
        #
        # curves2 = []
        # for edge in edges:
        #     curve = HyperPoincareArc(points[edge[0]],
        #                              points[edge[1]])
        #     curve.set_color(GREEN)
        #     if points[edge[0]][2] <= np.sinh(3) and points[edge[1]][2] <= np.sinh(3):
        #         curves2.append(curve)
        #
        # self.move_camera(phi=0, distance=UP)
        #
        # poincare_disc = PoincareDisk()
        # self.play(
        #     Transform(hyperboloid, poincare_disc),
        #     *[Transform(src, img) for src, img in zip(curves, curves2)],
        #     # *[Transform(src, img) for src, img in zip(dots, dots2)],
        #     *[FadeOut(d) for d in dots],
        #     *[FadeIn(d) for d in dots2],
        #     FadeOut(hyperboloid),
        #     frame.animate.increment_phi(-45 * DEGREES),
        #     run_time=3
        # )
        #
        # group = Group(*curves, *dots2)
        # self.play(ApplyMethod(group.shift, OUT * 20), frame.animate.increment_theta(90 * DEGREES), run_time=5)
        # self.play(ApplyMethod(group.shift, IN * 20), frame.animate.increment_theta(90 * DEGREES), run_time=5)
        #
        # mirror = Circle(radius=np.sqrt(2), arc_center=DOWN)
        # mirror.set_color(YELLOW)
        #
        # self.play(
        #     GrowFromCenter(mirror), run_time=5
        # )
        #
        # self.wait(5)
        #
        # dots3a = []
        # dots3b = []
        # for point in points:
        #     sphere = Circle(radius=0.03)
        #     sphere.shift(inversion(poincare_transform(point)))
        #     sphere.set_style(fill_color=RED, fill_opacity=1)
        #     if point[2] <= np.cosh(3):
        #         dots3a.append(sphere)
        #     else:
        #         dots3b.append(sphere)
        #
        # curves3a = []
        # curves3b = []
        # for edge in edges:
        #     curve = HyperUHPArc(points[edge[0]],
        #                         points[edge[1]])
        #     curve.set_color(GREEN)
        #     if points[edge[0]][2] <= np.sinh(3) and points[edge[1]][2] <= np.sinh(3):
        #         curves3a.append(curve)
        #     else:
        #         curves3b.append(curve)
        #
        # self.play(
        #     *[Transform(src, img) for src, img in zip(curves, curves3a)],
        #     *[Transform(src, img) for src, img in zip(dots2, dots3a)],
        #     run_time=10
        # )
        #
        # self.play(
        #     *[FadeIn(d) for d in curves3b],
        #     *[FadeIn(d) for d in dots3b],
        #     FadeOut(mirror),
        #     run_time=5
        # )

        self.wait(10)


class tmp(ThreeDScene):
    def construct(self):
        self.wait(10)


def standard_embedding(u, v):
    return np.array([np.sinh(u) * np.cos(v), np.cosh(u), np.sinh(u) * np.sin(v)])


def standard_embedding2(u, v):
    return np.array([np.sinh(u) * np.cos(v), np.sinh(u) * np.sin(v), np.cosh(u)])


def poincare(x):
    return np.array([x[0] / (1 + x[1]), x[2] / (1 + x[1]), 0])


def inversion(x):
    return np.array([2 * x[0] / (x[0] * x[0] + (x[1] + 1) * (x[1] + 1)),
                     2 * (x[1] + 1) / (x[0] * x[0] + (x[1] + 1) * (x[1] + 1)) - 1, 0])


class Hyperboloid(ParametricSurface, ABC):
    def __init__(self):
        super().__init__(lambda u, v: standard_embedding(u, v),
                         u_min=0,
                         u_max=2,
                         v_min=0,
                         v_max=TAU,
                         resolution=(11, 19)
                         )


class Hyperboloid2(ParametricSurface, ABC):
    def __init__(self):
        super().__init__(lambda u, v: standard_embedding2(u, v),
                         u_min=0,
                         u_max=2,
                         v_min=0,
                         v_max=TAU,
                         resolution=(11, 19)
                         )


class PoincareDisc(ParametricSurface, ABC):
    def __init__(self):
        super().__init__(lambda u, v: poincare(standard_embedding(u, v)),
                         u_min=0,
                         u_max=2,
                         v_min=0,
                         v_max=TAU,
                         resolution=(11, 19)
                         )


class UpperHalfPlane(ParametricSurface, ABC):
    def __init__(self, maximum, res):
        self.maximum = maximum
        self.res = res
        super().__init__(lambda u, v: inversion(poincare(standard_embedding(u, v))),
                         u_min=0,
                         u_max=self.maximum,
                         v_min=0,
                         v_max=TAU,
                         resolution=(res, 51)
                         )


class HyperArc(ParametricFunction, ABC):
    def __init__(self, start, end):
        def parametric_function(t):
            sp = start[0] * end[0] + start[1] * end[1] - start[2] * end[2]
            u = t * sp + np.sqrt(1 + t * t * (sp * sp - 1))
            return np.add(np.multiply(start, u), np.multiply(end, t))

        super().__init__(parametric_function)


class DynkinDiagram(VGroup, ABC):
    def __init__(self, weights, activations, colors, labels, **kwargs):
        VGroup.__init__(self, **kwargs)
        dots = []
        for i in range(0, len(activations)):
            dot = Dot()
            if i > 0:
                dot.next_to(dots[i - 1], RIGHT, buff=LARGE_BUFF)
            self.add(dot)
            dots.append(dot)
            dot.scale(2)
            if activations[i] > 0:
                dot.set_style(stroke_color=colors[i], fill_color=colors[i], fill_opacity=0.5)
            else:
                dot.set_style(stroke_color=colors[i], stroke_width=2, fill_opacity=0)
            label = Tex(labels[i])
            label.next_to(dot, DOWN)
            label.set_color(colors[i])
            self.add(label)
            if i > 0 and weights[i - 1] > 2:
                line = Line(dots[i - 1], dot)
                line.set_style(stroke_color=WHITE, stroke_width=4)
                if weights[i - 1] > 3:
                    weight = Tex(str(weights[i - 1]))
                    weight.set_color(WHITE)
                    weight.next_to(line, UP)
                    self.add(weight)
                elif weights[i - 1] == 3:
                    weight = Tex(str(weights[i - 1]))
                    weight.set_color(WHITE)
                    weight.set_style(stroke_color=WHITE, stroke_opacity=0.5, stroke_width=2, fill_opacity=0)
                    weight.next_to(line, UP)
                    self.add(weight)
                self.add(line)
