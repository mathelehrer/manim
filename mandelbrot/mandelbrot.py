from manim import *
from typing import Iterable
from colour import Color


class Mandelbrot(PGroup):
    def __init__(
            self,
            length: float = 7,
            max_steps: int = 25,
            threshold: float = 4,
            color_scheme: Iterable[Color] = [BLACK, GREEN, BLACK],
            stroke_width: float = 2,
            **kwargs
    ):

        complex_plane = ComplexPlane(
            x_range=[-2, 0.47],
            y_range=[-1.12, 1.12],
            x_length=length,
            y_length=length,
        )
        self.complex_plane = complex_plane

        self.real_length = complex_plane.x_range[1] - complex_plane.x_range[0] + 0.02
        self.ima_length = complex_plane.y_range[1] - complex_plane.y_range[0] + 0.02

        self.x_axis_length = complex_plane.x_length
        self.y_axis_length = complex_plane.y_length

        if len(color_scheme) == max_steps:
            colors = color_scheme
        else:
            colors = color_gradient(
                color_scheme,
                max_steps
            )

        all_points = self.get_list_of_points_for_each_iteration(
            threshlod=threshold,
            max_steps=max_steps
        )

        PGroup.__init__(self, **kwargs)

        for k in range(max_steps):
            ring = PMobject()
            ring.add_points(
                all_points[k]
            )
            ring.set_color(colors[k])
            ring.set_stroke_width(stroke_width)
            self.add(ring)

    def get_x_pixel_number(self):
        return int((config.pixel_width / config.frame_width) * self.x_axis_length)

    def get_y_pixel_number(self):
        return int((config.pixel_height / config.frame_height) * self.y_axis_length)

    def get_iterations_for_complex_number(self, c, threshlod, max_steps):
        z = c
        i = 0
        while i < max_steps and (z * z.conjugate()).real < threshlod:
            z = z ** 2 + c
            i += 1
        return i

    def get_list_of_points_for_each_iteration(self, threshlod, max_steps):
        mx = self.real_length / (self.get_x_pixel_number() - 1)
        my = self.ima_length / (self.get_y_pixel_number() - 1)
        mapper = lambda x, y: (mx * x + self.complex_plane.x_range[0], my * y + self.complex_plane.y_range[0])
        points_list = [[] for _ in range(max_steps)]
        for x in range(self.get_x_pixel_number()):
            for y in range(self.get_y_pixel_number()):
                it = self.get_iterations_for_complex_number(
                    complex(*mapper(x, y)),
                    threshlod=threshlod,
                    max_steps=max_steps
                )
                new_point = self.complex_plane.number_to_point(complex(*mapper(x, y)))
                points_list[it - 1].append(new_point)
        return points_list


class Show(Scene):
    def construct(self):
        m = Mandelbrot()
        self.add(m)