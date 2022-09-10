#!/usr/bin/env python

from manim_imports_ext import *
import operator as op


class Complex(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(self, x_min=-1.5,
                            x_max=1.5,
                            y_min=-1.5,
                            y_max=1.5,
                            y_axis_height=6,
                            x_axis_width=6,
                            y_axis_label="",
                            x_axis_label="",
                            graph_origin=RIGHT * 3.5,
                            **kwargs)

    def construct(self):
        title = Title("Complex numbers")
        title.set_color(YELLOW)
        title.move_to(LEFT * 3.5)
        title.to_edge(UP)
        self.play(Write(title))

        root = TexMobject(r"q\phantom{^2}=\phantom{-}\tfrac{1}{2}+\tfrac{\sqrt{3}}{2} i",
                          tex_to_color_map={r"\tfrac{1}{2}+\tfrac{\sqrt{3}}{2} i": GREEN})
        root.to_edge(LEFT)
        root.shift(UP * 2)
        self.play(Write(root))
        self.wait()

        r2 = TexMobject(r"q^2")
        r2z = TexMobject(r"=(\tfrac{1}{2}+\tfrac{\sqrt{3}}{2} i)\cdot (\tfrac{1}{2}+\tfrac{\sqrt{3}}{2} i)")
        r2.next_to(root, DOWN)
        r2.align_to(root, LEFT)
        r2z.next_to(r2, RIGHT, buff=SMALL_BUFF * 1.8)
        self.play(Write(r2), Write(r2z))
        self.wait()

        r2a = TexMobject(r"q^2=\phantom{(}\tfrac{1}{4}+\tfrac{3}{4}i^2+\tfrac{\sqrt{3}}{2} i",
                         tex_to_color_map={"q^2": BLACK})
        r2a.next_to(r2, DOWN)
        r2a.align_to(r2, LEFT)
        self.play(Write(r2a))
        self.wait()

        r2b = TexMobject(r"q^2")
        r2b.set_color(BLACK)
        r2w = TexMobject(r"=-\tfrac{1}{2}+\tfrac{\sqrt{3}}{2} i",
                         tex_to_color_map={"q^2": BLACK, r"-\tfrac{1}{2}+\tfrac{\sqrt{3}}{2} i": GREEN})
        r2b.next_to(r2a, DOWN)
        r2b.align_to(r2a, LEFT)
        r2w.next_to(r2b, RIGHT, buff=SMALL_BUFF * 1.8)
        self.play(Write(r2b), Write(r2w))
        self.wait()

        self.play(Uncreate(r2a), Uncreate(r2z), Uncreate(r2b))
        self.play(r2w.next_to, r2, RIGHT, buff=SMALL_BUFF * 2)
        self.wait()

        r3 = TexMobject(r"q^3=-1",
                        tex_to_color_map={r"-1": GREEN})
        r3.next_to(r2, DOWN)
        r3.align_to(r2, LEFT)
        self.play(Write(r3))
        self.wait()

        r4 = TexMobject(r"q^4=-\tfrac{1}{2}-\tfrac{\sqrt{3}}{2} i",
                        tex_to_color_map={r"-\tfrac{1}{2}-\tfrac{\sqrt{3}}{2} i": GREEN})
        r4.next_to(r3, DOWN)
        r4.align_to(r3, LEFT)
        self.play(Write(r4))
        self.wait()

        r5 = TexMobject(r"q^5=\phantom{-}\tfrac{1}{2}-\tfrac{\sqrt{3}}{2} i",
                        tex_to_color_map={r"\tfrac{1}{2}-\tfrac{\sqrt{3}}{2} i": GREEN})
        r5.next_to(r4, DOWN)
        r5.align_to(r4, LEFT)
        self.play(Write(r5))
        self.wait()

        r6 = TexMobject(r"q^0=\phantom{-}1",
                        tex_to_color_map={r"1": GREEN})
        r6.next_to(r5, DOWN)
        r6.align_to(r5, LEFT)
        self.play(Write(r6))
        self.wait()

        self.wait(6)

        self.setup_axes()

        origin = (RIGHT * 3.5)

        for i in range(1, 7):
            d = Dot()
            q = TexMobject(f"q^{i % 6}")
            q.set_color(GREEN)
            d.move_to(self.coords_to_point(np.cos(2 * np.pi * i / 6), np.sin(2 * np.pi * i / 6)))
            q.move_to((self.coords_to_point(np.cos(2 * np.pi * i / 6 + 0.15),
                                            np.sin(2 * np.pi * i / 6 + 0.15)) - origin) * 1.2 + origin)
            self.play(ShowCreation(d))
            self.play(Write(q))
            self.wait()

        for i in range(1, 7):
            l = Line(self.coords_to_point(np.cos(2 * np.pi * i / 6), np.sin(2 * np.pi * i / 6)),
                     self.coords_to_point(np.cos(2 * np.pi * (i + 1) / 6), np.sin(2 * np.pi * (i + 1) / 6)))
            l.set_color(YELLOW)
            self.play(ShowCreation(l))

        self.wait(6)


class Quaternions(Scene):

    def construct(self):
        title = Title("Quaternions")
        title.set_color(YELLOW)
        title.move_to(LEFT * 3.5)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(3)

        root = TexMobject(r"\omega \phantom{^2}=\tfrac{1}{2} (-1+i + j + k)")
        root.scale(0.75)
        root.to_edge(LEFT, buff=SMALL_BUFF)
        root.shift(UP * 2)
        self.play(Write(root))
        self.wait()

        r2 = TexMobject(r"\omega^2=\tfrac{1}{4}(-1+i+j+k)",
                        tex_to_color_map={"-1": BLUE, "i": RED, "j": GREEN, "k": ORANGE})
        r2a = TexMobject(r"\cdot(-1+i+j+k)")
        r2.scale(0.75)
        r2a.scale(0.75)
        r2.next_to(root, DOWN)
        r2.align_to(root, LEFT)
        r2a.next_to(r2, RIGHT, buff=SMALL_BUFF)
        self.play(Write(r2), Write(r2a))
        self.wait()

        r2b = TexMobject(r"\omega^2")
        r2b.set_color(BLACK)
        r2b.scale(0.75)
        r2b.next_to(r2, DOWN)
        r2b.align_to(r2, LEFT)

        r2c = TexMobject(r"=\tfrac{1}{4}(")
        r2c.scale(0.75)
        r2c.next_to(r2b, RIGHT, buff=SMALL_BUFF)

        a0 = TexMobject("1")
        a0.scale(0.75)
        a0.set_color(BLUE)
        a0.next_to(r2c, RIGHT)

        a1 = TexMobject("-i")
        a1.scale(0.75)
        a1.set_color(BLUE)
        a1.next_to(a0, RIGHT)

        a2 = TexMobject("-j")
        a2.scale(0.75)
        a2.set_color(BLUE)
        a2.next_to(a1, RIGHT)

        a3 = TexMobject("-k")
        a3.scale(0.75)
        a3.set_color(BLUE)
        a3.next_to(a2, RIGHT)

        b0 = TexMobject("-i")
        b0.scale(0.75)
        b0.set_color(RED)
        b0.next_to(a3, RIGHT)

        b1 = TexMobject("+i^2")
        b1.scale(0.75)
        b1.set_color(RED)
        b1.next_to(b0, RIGHT, buff=SMALL_BUFF)

        b2 = TexMobject("+ij")
        b2.scale(0.75)
        b2.set_color(RED)
        b2.next_to(b1, RIGHT, buff=SMALL_BUFF)

        b3 = TexMobject("+ik")
        b3.scale(0.75)
        b3.set_color(RED)
        b3.next_to(b2, RIGHT, buff=SMALL_BUFF)

        c0 = TexMobject("-j")
        c0.scale(0.75)
        c0.set_color(GREEN)
        c0.next_to(a0, DOWN)

        c1 = TexMobject("+ji")
        c1.scale(0.75)
        c1.set_color(GREEN)
        c1.next_to(c0, RIGHT, buff=SMALL_BUFF)

        c2 = TexMobject("+j^2")
        c2.scale(0.75)
        c2.set_color(GREEN)
        c2.next_to(c1, RIGHT, buff=SMALL_BUFF)

        c3 = TexMobject("+jk")
        c3.scale(0.75)
        c3.set_color(GREEN)
        c3.next_to(c2, RIGHT, buff=SMALL_BUFF)

        d0 = TexMobject("-k")
        d0.scale(0.75)
        d0.set_color(ORANGE)
        d0.next_to(c3, RIGHT, buff=SMALL_BUFF)

        d1 = TexMobject("+ki")
        d1.scale(0.75)
        d1.set_color(ORANGE)
        d1.next_to(d0, RIGHT, buff=SMALL_BUFF)

        d2 = TexMobject("+kj")
        d2.scale(0.75)
        d2.set_color(ORANGE)
        d2.next_to(d1, RIGHT, buff=SMALL_BUFF)

        d3 = TexMobject("+k^2")
        d3.scale(0.75)
        d3.set_color(ORANGE)
        d3.next_to(d2, RIGHT, buff=SMALL_BUFF)

        d4 = TexMobject(")")
        d4.scale(0.75)
        d4.set_color(WHITE)
        d4.next_to(d3, RIGHT, buff=SMALL_BUFF)

        self.play(Write(r2b), Write(r2c), Write(a1), Write(a0), Write(a2), Write(a3))
        self.play(Write(b1), Write(b0), Write(b2), Write(b3))
        self.play(Write(c1), Write(c0), Write(c2), Write(c3))
        self.play(Write(d1), Write(d0), Write(d2), Write(d3), Write(d4))
        self.wait(3)

        rules = TextMobject("Rules: ")
        rules.set_color(YELLOW)
        rules.to_edge(LEFT, buff=SMALL_BUFF)
        rules.shift(DOWN * 0.5)

        self.play(Write(rules))
        self.wait()

        rule1 = TexMobject("i^2=j^2=k^2=-1")
        rule1.next_to(rules, DOWN)
        rule1.align_to(rules, LEFT)

        self.play(Write(rule1))
        self.wait()

        r1 = TextMobject("-1")
        r1.scale(0.75)
        r1.set_color(RED)
        r1.move_to(b1.get_center())

        r2 = TextMobject("-1")
        r2.scale(0.75)
        r2.set_color(BLUE)
        r2.move_to(c2.get_center())

        r3 = TextMobject("-1")
        r3.scale(0.75)
        r3.set_color(ORANGE)
        r3.move_to(d3.get_center())

        self.play(Transform(b1, r1), Transform(c2, r2), Transform(d3, r3))
        self.wait(3)

        rule2 = TexMobject("ij=-ji=k")
        rule2.next_to(rule1, DOWN)
        rule2.align_to(rule1, LEFT)
        rule3 = TexMobject("ik=-ki=-j")
        rule3.next_to(rule2, DOWN)
        rule3.align_to(rule2, LEFT)
        rule4 = TexMobject("jk=-kj=i")
        rule4.next_to(rule3, DOWN)
        rule4.align_to(rule3, LEFT)

        self.play(Write(rule2), Write(rule3), Write(rule4))
        self.wait()

        self.play(b2.set_color, WHITE, c1.set_color, WHITE)
        self.play(Uncreate(b2), Uncreate(c1))
        self.wait()
        self.play(b3.set_color, WHITE, d1.set_color, WHITE)
        self.play(Uncreate(b3), Uncreate(d1))
        self.wait()
        self.play(c3.set_color, WHITE, d2.set_color, WHITE)
        self.play(Uncreate(c3), Uncreate(d2))
        self.wait(3)

        self.play(a0.set_color, WHITE, r1.set_color, WHITE, r2.set_color, WHITE, r3.set_color, WHITE)
        r4 = TexMobject("-2")
        r4.scale(0.65)
        r4.move_to(a0.get_center())

        self.play(Transform(a0, r4),
                  b1.move_to, a0.get_center(), FadeOut(r1), Uncreate(b1),
                  c2.move_to, a0.get_center(), FadeOut(r2), Uncreate(c2),
                  d3.move_to, a0.get_center(), FadeOut(r3), Uncreate(d3)
                  )
        self.wait(3)

        r5 = TexMobject("-2i")
        r5.scale(0.65)
        r5.next_to(r4, RIGHT, buff=SMALL_BUFF)

        self.play(b0.set_color, WHITE, a1.set_color, WHITE)
        self.play(Transform(a1, r5),
                  b0.move_to, a1.get_center(),
                  FadeOut(b0)
                  )

        self.wait()

        r6 = TexMobject("-2j")
        r6.scale(0.65)
        r6.next_to(r5, RIGHT, buff=SMALL_BUFF)

        self.play(c0.set_color, WHITE, a2.set_color, WHITE)
        self.play(Transform(a2, r6),
                  c0.move_to, a2.get_center(),
                  FadeOut(c0)
                  )

        self.wait()

        r7 = TexMobject("-2k")
        r7.scale(0.65)
        r7.next_to(r6, RIGHT, buff=SMALL_BUFF)

        self.play(d0.set_color, WHITE, a3.set_color, WHITE)
        self.play(Transform(a3, r7),
                  d0.move_to, a3.get_center(),
                  FadeOut(d0),
                  d4.next_to, a3, RIGHT, buff=SMALL_BUFF
                  )

        self.wait(6)


class Group(Scene):
    def construct(self):
        title = Title("Fun with two quaternions")
        title.set_color(YELLOW)
        title.move_to(LEFT * 3.5)
        title.to_edge(UP)
        self.play(Write(title))

        linesep = 1.8
        colsep = 0.6

        gen1parts = [TexMobject(r"\omega"), TexMobject("="), TexMobject(r"\tfrac{1}{2} (-1+i + j + k)")]
        for i in range(1, 3):
            gen1parts[i].next_to(gen1parts[i - 1], RIGHT)
        gen1 = VGroup(*gen1parts)
        gen1.scale(0.7)
        gen1.to_edge(LEFT, buff=SMALL_BUFF)
        gen1.shift(UP * 2.5)
        self.play(Write(gen1))

        gen2parts = [TexMobject("q"), TexMobject("="),
                     TexMobject(r"\tfrac{1}{4} \left(2i+(\sqrt{5}+1)j+(\sqrt{5}-1)k\right)")]
        gen2 = VGroup(*gen2parts)
        gen2.scale(0.7)
        gen2parts[2].scale(0.8)
        for i in range(1, 3):
            gen2parts[i].next_to(gen2parts[i - 1], RIGHT)
        gen2.next_to(gen1, DOWN)
        gen2.align_to(gen1, LEFT)
        self.play(Write(gen2))
        self.wait(3)

        gen1trafo = TexMobject(r"[-\tfrac{1}{2},\tfrac{1}{2},\tfrac{1}{2},\tfrac{1}{2}]")
        gen2trafo = TexMobject(r"[0,\tfrac{1}{2},r_5^+,r_5^-]")
        gen1trafo.scale(0.7)
        gen2trafo.scale(0.7)
        gen1trafo.next_to(gen1parts[1], RIGHT)
        gen2trafo.next_to(gen2parts[1], RIGHT)
        abbreviation = TexMobject(r"r_5^+=\frac{\sqrt{5}+1}{4} \,\,\, r_5^-=\frac{\sqrt{5}-1}{4}")
        abbreviation.scale(0.5)
        abbreviation.to_edge(DOWN, buff=0)
        abbreviation.align_to(gen1, LEFT)

        self.play(Transform(gen1parts[2], gen1trafo), Transform(gen2parts[2], gen2trafo), Write(abbreviation))

        self.wait(3)

        new_elems = TextMobject("new elems")
        new_elems.scale(0.7)
        new_elems.next_to(gen1, RIGHT, buff=LARGE_BUFF)
        new_elems.set_color(GREEN)

        all_elems = TextMobject("all elements")
        all_elems.scale(0.7)
        all_elems.next_to(new_elems, RIGHT, buff=LARGE_BUFF * 0.5)
        all_elems.set_color(YELLOW)

        gen1[0].generate_target()
        gen1[0].target.next_to(new_elems, DOWN, buff=SMALL_BUFF)
        gen1[0].target.align_to(new_elems, LEFT)
        gen1[0].target.set_color(GREEN)

        gen1[2].generate_target()
        gen1[2].target.scale(0.7)
        gen1[2].target.next_to(all_elems, DOWN, buff=SMALL_BUFF)
        gen1[2].target.align_to(all_elems, LEFT)
        gen1[2].target.set_color(YELLOW)

        gen2[0].generate_target()
        gen2[0].target.next_to(gen1[0].target, DOWN, buff=SMALL_BUFF)
        gen2[0].target.align_to(gen1[0].target, LEFT)
        gen2[0].target.set_color(GREEN)

        gen2[2].generate_target()
        gen2[2].target.scale(0.7)
        gen2[2].target.next_to(gen1[2].target, DOWN, buff=SMALL_BUFF)
        gen2[2].target.align_to(gen1[2].target, LEFT)
        gen2[2].target.set_color(YELLOW)

        gen1copy = gen1[2].copy()
        gen2copy = gen2[2].copy()

        new_group = VGroup(new_elems, gen1[0].target, gen2[0].target)
        rect_green = SurroundingRectangle(new_group)
        rect_green.set_color(GREEN)

        news = [gen1[0].copy(), gen2[0].copy()]
        full_group = VGroup(all_elems, gen1[2].target, gen2[2].target)
        rect_orange = SurroundingRectangle(full_group)
        rect_orange.set_color(YELLOW)
        self.play(Write(new_elems), Write(all_elems), GrowFromCenter(rect_green), GrowFromCenter(rect_orange))
        self.play(MoveToTarget(news[0]), MoveToTarget(gen1copy), MoveToTarget(news[1]),
                  MoveToTarget(gen2copy))
        self.wait(3)

        # make double copies of the new elements

        news[0].generate_target()
        news[0].target.next_to(gen2, DOWN, buff=LARGE_BUFF)
        news[0].target.align_to(gen2, LEFT)
        news[1].generate_target()
        news[1].target.next_to(news[0].target, DOWN, buff=SMALL_BUFF * linesep)
        for i in range(1, 2):
            news[i].target.align_to(news[i - 1].target)

        next_parts = [news[0].copy(), news[1].copy()]
        self.play(MoveToTarget(next_parts[0]), MoveToTarget(next_parts[1]))

        news[0].generate_target()
        news[0].target.next_to(next_parts[1], DOWN, buff=SMALL_BUFF * linesep)
        news[0].target.align_to(gen2, LEFT)
        news[1].generate_target()
        news[1].target.next_to(news[0].target, DOWN, buff=SMALL_BUFF * linesep)
        for i in range(1, 2):
            news[i].target.align_to(news[i - 1].target)

        next_parts.append(news[0].copy())
        next_parts.append(news[1].copy())
        self.play(MoveToTarget(next_parts[2]), MoveToTarget(next_parts[3]))

        self.wait(3)

        mul = []
        equal = []
        next_parts2 = []
        for i in range(0, 4):
            mul.append(TexMobject(r"\cdot"))
            mul[i].next_to(next_parts[i], RIGHT)
            if i < 2:
                gen1parts[0].generate_target()
                gen1parts[0].target.next_to(mul[i], RIGHT)
                equal.append(TexMobject("="))
                equal[i].next_to(gen1parts[0].target, RIGHT)
                next_parts2.append(gen1parts[0].copy())
            else:
                gen2parts[0].generate_target()
                gen2parts[0].target.next_to(mul[i], RIGHT)
                equal.append(TexMobject("="))
                equal[i].next_to(gen2parts[0].target, RIGHT)
                next_parts2.append(gen2parts[0].copy())
            if i > 0:
                equal[i].align_to(equal[i - 1], LEFT)
            self.play(Write(mul[i]), MoveToTarget(next_parts2[i]), Write(equal[i]))

        self.wait(3)

        results = [TexMobject(r"-[\tfrac{1}{2},\tfrac{1}{2},\tfrac{1}{2},\tfrac{1}{2}]"),
                   TexMobject(r"-[r_5^+,0,\tfrac{1}{2},r_5^-]"),
                   TexMobject(r"-[r_5^+,\tfrac{1}{2},r_5^-,0]"),
                   TexMobject(r"-[1,0,0,0]")]

        for i in range(0, 4):
            results[i].scale(0.5)
            results[i].next_to(equal[i], RIGHT)

        self.play(*[Write(results[i]) for i in range(0, 4)])
        self.wait(3)

        self.remove(*news)
        for i in range(0, 4):
            next_parts[i].generate_target()
            next_parts2[i].generate_target()
            results[i].generate_target()

            if i == 0:
                next_parts[i].target.next_to(new_elems, DOWN)
                results[i].target.next_to(gen2[2], DOWN)
            else:
                next_parts[i].target.next_to(next_parts[i - 1].target, DOWN)
                results[i].target.next_to(results[i - 1].target, DOWN)

            next_parts[i].target.align_to(new_elems, LEFT)
            next_parts2[i].target.next_to(next_parts[i].target, RIGHT, buff=SMALL_BUFF * 0.5)
            results[i].target.align_to(all_elems, LEFT)
            next_parts[i].target.set_color(GREEN)
            next_parts2[i].target.set_color(GREEN)
            results[i].target.set_color(YELLOW)

        new_group2 = VGroup(new_elems, *[next_parts[i].target for i in range(0, 4)])
        rect_green2 = SurroundingRectangle(new_group2)
        rect_green2.set_color(GREEN)

        full_group2 = VGroup(full_group, *[results[i].target for i in range(0, 4)])
        rect_orange2 = SurroundingRectangle(full_group2)
        rect_orange2.set_color(YELLOW)
        self.play(Transform(rect_green, rect_green2), Transform(rect_orange, rect_orange2))

        self.play(*[MoveToTarget(results[i]) for i in range(0, 4)],
                  *[MoveToTarget(next_parts[i]) for i in range(0, 4)],
                  *[MoveToTarget(next_parts2[i]) for i in range(0, 4)],
                  *[Uncreate(mul[i]) for i in range(0, 4)],
                  *[Uncreate(equal[i]) for i in range(0, 4)],
                  )

        self.wait(3)

        news = []
        new_factors = []
        for i in range(0, 4):
            news.append(VGroup(next_parts[i], next_parts2[i]))
            news[i].generate_target()
            if i == 0:
                news[i].target.next_to(gen2, DOWN, buff=LARGE_BUFF * colsep)
            else:
                news[i].target.next_to(news[i - 1].target, DOWN, buff=SMALL_BUFF * linesep)
            news[i].target.align_to(gen2, LEFT)
            new_factors.append(news[i].copy())

        self.play(*[MoveToTarget(new_factors[i]) for i in range(0, 4)])

        for i in range(4, 8):
            news.append(VGroup(next_parts[i - 4], next_parts2[i - 4]))
            news[i].generate_target()
            news[i].target.next_to(news[i - 1].target, DOWN, buff=SMALL_BUFF * linesep)
            news[i].target.align_to(gen2, LEFT)
            new_factors.append(news[i].copy())

        self.play(*[MoveToTarget(new_factors[i]) for i in range(4, 8)])
        self.wait(3)

        mul = []
        equal = []
        next_parts3 = []
        for i in range(0, 8):
            mul.append(TexMobject(r"\cdot"))
            mul[i].next_to(news[i].target, RIGHT)
            if i > 0:
                mul[i].align_to(mul[i - 1], LEFT)
            if i < 4:
                gen1parts[0].generate_target()
                gen1parts[0].target.next_to(mul[i], RIGHT)
                equal.append(TexMobject("="))
                equal[i].next_to(gen1parts[0].target, RIGHT)
                next_parts3.append(gen1parts[0].copy())
            else:
                gen2parts[0].generate_target()
                gen2parts[0].target.next_to(mul[i], RIGHT)
                equal.append(TexMobject("="))
                equal[i].next_to(gen2parts[0].target, RIGHT)
                next_parts3.append(gen2parts[0].copy())
            if i > 0:
                equal[i].align_to(equal[i - 1], LEFT)
            self.play(Write(mul[i]), MoveToTarget(next_parts3[i]), Write(equal[i]))

        self.wait(3)

        results2 = [TexMobject(r"[1,0,0,0]"),
                    TexMobject(r"[r_5^+,-\tfrac{1}{2},r_5^-,0]"),
                    TexMobject(r"[r_5^+,r_5^-,0,-\tfrac{1}{2}]"),
                    TexMobject(r"[\tfrac{1}{2},-\tfrac{1}{2},-\tfrac{1}{2},-\tfrac{1}{2}]"),
                    TexMobject(r"[r_5^+,0,-\tfrac{1}{2},r_5^-]"),
                    TexMobject(r"[\tfrac{1}{2},r_5^-,-r_5^+,0]"),
                    TexMobject(r"[\tfrac{1}{2},-\tfrac{1}{2},-\tfrac{1}{2},-\tfrac{1}{2}]"),
                    TexMobject(r"-[0,\tfrac{1}{2},r_5^+,r_5^-]")]

        for i in range(0, 8):
            results2[i].scale(0.4)
            results2[i].next_to(equal[i], RIGHT)

        self.play(*[Write(results2[i]) for i in range(0, 8)])
        self.wait(3)

        for i in range(0, 8):
            new_factors[i].generate_target()
            next_parts3[i].generate_target()
            results2[i].generate_target()
            results2[i].target.scale(1.2)

            if i == 0:
                new_factors[i].target.next_to(new_elems, DOWN)
                results2[i].target.next_to(results[3], DOWN, buff=SMALL_BUFF * linesep * 0.9)
            elif i < 7:
                new_factors[i].target.next_to(new_factors[i - 1].target, DOWN)
                results2[i].target.next_to(results2[i - 1].target, DOWN)
            else:
                new_factors[i].target.next_to(new_factors[5].target, DOWN, buff=SMALL_BUFF * linesep)
                results2[i].target.next_to(gen1[2].target, RIGHT, buff=LARGE_BUFF * colsep)

            new_factors[i].target.align_to(new_elems, LEFT)
            next_parts3[i].target.next_to(new_factors[i].target, RIGHT, buff=SMALL_BUFF * linesep)
            if i < 7:
                results2[i].target.align_to(all_elems, LEFT)
            new_factors[i].target.set_color(GREEN)
            next_parts3[i].target.set_color(GREEN)
            results2[i].target.set_color(YELLOW)

        self.remove(*next_parts, *next_parts2)
        self.remove(*news)

        new_group3 = VGroup(new_elems, *[next_parts3[i].target for i in range(0, 6)])
        rect_green3 = SurroundingRectangle(new_group3)
        rect_green3.set_color(GREEN)

        full_group3 = VGroup(full_group2, *[results2[i].target for i in range(0, 6)])
        rect_orange3 = SurroundingRectangle(full_group3)
        rect_orange3.set_color(YELLOW)
        self.play(Transform(rect_green, rect_green3), Transform(rect_orange, rect_orange3))

        self.play(*[MoveToTarget(results2[i]) for i in range(0, 6)],
                  *[MoveToTarget(new_factors[i]) for i in range(0, 6)],
                  *[MoveToTarget(next_parts3[i]) for i in range(0, 6)],
                  *[Uncreate(mul[i]) for i in range(0, 6)],
                  *[Uncreate(equal[i]) for i in range(0, 6)]
                  )

        self.wait(3)

        rect1 = SurroundingRectangle(results2[6])
        rect1.set_color(RED)

        rect2 = SurroundingRectangle(results2[3])
        rect2.set_color(RED)

        self.play(GrowFromCenter(rect1), GrowFromCenter(rect2))
        self.wait(3)

        self.play(ShrinkToCenter(rect1), ShrinkToCenter(rect2))
        self.play(Uncreate(mul[6]), Uncreate(equal[6]), Uncreate(results2[6]), Uncreate(new_factors[6]),
                  Uncreate(next_parts3[6]))
        self.wait(3)

        new_group4 = VGroup(new_elems, *[next_parts3[i].target for i in range(0, 8)])
        rect_green4 = SurroundingRectangle(new_group4)
        rect_green4.set_color(GREEN)

        full_group4 = VGroup(full_group3, results2[7].target)
        rect_orange4 = SurroundingRectangle(full_group4)
        rect_orange4.set_color(YELLOW)
        self.play(Transform(rect_green, rect_green4), Transform(rect_orange, rect_orange4))

        self.play(Uncreate(mul[7]), Uncreate(equal[7]), MoveToTarget(results2[7]), MoveToTarget(new_factors[7]),
                  MoveToTarget(next_parts3[7]))

        self.wait(3)

        self.remove(rect_green, *new_factors, *next_parts3, new_elems, rect_orange4)
        self.wait(3)

        fuller_group = VGroup(all_elems, gen1copy, gen2copy, *results, *results2, rect_orange)
        self.play(Uncreate(gen1), Uncreate(gen2), Uncreate(abbreviation),
                  fuller_group.shift, LEFT * 5.5,
                  fuller_group.set_color, WHITE)

        self.wait(3)

        results3 = [TexMobject(r"-[0,\tfrac{1}{2},r_5^+,r_5^-]"),
                    TexMobject(r"[\tfrac{1}{2},\tfrac{1}{2},\tfrac{1}{2},\tfrac{1}{2}]"),
                    TexMobject(r"[0,r_5^+,r_5^-,\tfrac{1}{2}]"), TexMobject(r"[r_5^-,0,r_5^+,\tfrac{1}{2}]"),
                    TexMobject(r"[0,r_5^-,\tfrac{1}{2},r_5^+]"), TexMobject(r"[r_5^+,0,\tfrac{1}{2},r_5^-]"),
                    TexMobject(r"[\tfrac{1}{2},r_5^-,r_5^+,0]"), TexMobject(r"[r_5^+,\tfrac{1}{2},r_5^-,0]"),
                    TexMobject(r"[r_5^-,r_5^+,\tfrac{1}{2},0]"), TexMobject(r"[-r_5^+,r_5^-,0,-\tfrac{1}{2}]"),
                    TexMobject(r"-[r_5^+,r_5^-,0,\tfrac{1}{2}]"), TexMobject(r"[-r_5^+,\tfrac{1}{2},r_5^-,0]"),
                    TexMobject(r"[-r_5^+,\tfrac{1}{2},-r_5^-,0]"), TexMobject(r"[-r_5^+,r_5^-,0,\tfrac{1}{2}]"),
                    TexMobject(r"[-r_5^+,0,-\tfrac{1}{2},r_5^-]"), TexMobject(r"[-r_5^+,0,\tfrac{1}{2},r_5^-]"),
                    TexMobject(r"[-r_5^+,-r_5^-,0,\tfrac{1}{2}]"), TexMobject(r"[-r_5^+,0,\tfrac{1}{2},-r_5^-]"),
                    TexMobject(r"[-r_5^+,-\tfrac{1}{2},r_5^-,0]"), TexMobject(r"[-\tfrac{1}{2},r_5^-,r_5^+,0]"),
                    TexMobject(r"[r_5^-,-r_5^+,-\tfrac{1}{2},0]"), TexMobject(r"[0,-r_5^+,-r_5^-,-\tfrac{1}{2}]"),
                    TexMobject(r"[\tfrac{1}{2},-r_5^+,0,-r_5^-]"), TexMobject(r"[0,-r_5^-,-\tfrac{1}{2},-r_5^+]"),
                    TexMobject(r"[r_5^-,-\tfrac{1}{2},0,-r_5^+]"), TexMobject(r"[r_5^-,0,-r_5^+,-\tfrac{1}{2}]"),
                    TexMobject(r"[\tfrac{1}{2},0,-r_5^-,-r_5^+]"), TexMobject(r"[-r_5^-,0,-r_5^+,-\tfrac{1}{2}]"),
                    TexMobject(r"[0,0,-1,0]"), TexMobject(r"[-\tfrac{1}{2},-r_5^-,-r_5^+,0]"),
                    TexMobject(r"[0,-\tfrac{1}{2},-r_5^+,r_5^-]"), TexMobject(r"[-r_5^-,-r_5^+,-\tfrac{1}{2},0]"),
                    TexMobject(r"[r_5^+,r_5^-,0,\tfrac{1}{2}]"), TexMobject(r"[\tfrac{1}{2},r_5^+,0,r_5^-]"),
                    TexMobject(r"[\tfrac{1}{2},0,r_5^-,r_5^+]"), TexMobject(r"[r_5^-,\tfrac{1}{2},0,r_5^+]"),
                    TexMobject(r"[r_5^+,-r_5^-,0,\tfrac{1}{2}]"),
                    TexMobject(r"[\tfrac{1}{2},-\tfrac{1}{2},\tfrac{1}{2},\tfrac{1}{2}]"),
                    TexMobject(r"[r_5^+,-\tfrac{1}{2},r_5^-,0]"), TexMobject(r"[\tfrac{1}{2},-r_5^-,r_5^+,0]"),
                    TexMobject(r"[r_5^+,0,\tfrac{1}{2},-r_5^-]"), TexMobject(r"[r_5^+,r_5^-,0,-\tfrac{1}{2}]"),
                    TexMobject(r"[\tfrac{1}{2},\tfrac{1}{2},\tfrac{1}{2},-\tfrac{1}{2}]"),
                    TexMobject(r"[r_5^+,\tfrac{1}{2},-r_5^-,0]"), TexMobject(r"[\tfrac{1}{2},r_5^+,0,-r_5^-]"),
                    TexMobject(r"[r_5^+,0,-\tfrac{1}{2},r_5^-]"),
                    TexMobject(r"[-\tfrac{1}{2},\tfrac{1}{2},\tfrac{1}{2},-\tfrac{1}{2}]"),
                    TexMobject(r"[-r_5^-,r_5^+,\tfrac{1}{2},0]"), TexMobject(r"[-\tfrac{1}{2},r_5^+,0,-r_5^-]"),
                    TexMobject(r"[-\tfrac{1}{2},r_5^+,0,r_5^-]"), TexMobject(r"[-r_5^-,\tfrac{1}{2},0,r_5^+]"),
                    TexMobject(r"[-\tfrac{1}{2},\tfrac{1}{2},-\tfrac{1}{2},\tfrac{1}{2}]"),
                    TexMobject(r"[-\tfrac{1}{2},0,r_5^-,r_5^+]"), TexMobject(r"[-\tfrac{1}{2},0,-r_5^-,r_5^+]"),
                    TexMobject(r"[-r_5^-,0,r_5^+,\tfrac{1}{2}]"), TexMobject(r"[-\tfrac{1}{2},-r_5^-,r_5^+,0]"),
                    TexMobject(r"[-\tfrac{1}{2},-\tfrac{1}{2},\tfrac{1}{2},\tfrac{1}{2}]"), TexMobject(r"[0,0,1,0]"),
                    TexMobject(r"[-r_5^-,0,r_5^+,-\tfrac{1}{2}]"), TexMobject(r"[-0,\tfrac{1}{2},r_5^+,-r_5^-]"),
                    TexMobject(r"[-\tfrac{1}{2},-r_5^+,0,-r_5^-]"), TexMobject(r"[0,-1,0,0]"),
                    TexMobject(r"[-r_5^-,-\tfrac{1}{2},0,-r_5^+]"), TexMobject(r"[0,-r_5^+,r_5^-,-\tfrac{1}{2}]"),
                    TexMobject(r"[-\tfrac{1}{2},0,-r_5^-,-r_5^+]"), TexMobject(r"[0,r_5^-,-\tfrac{1}{2},-r_5^+]"),
                    TexMobject(r"[0,0,0,-1]"), TexMobject(r"[-\tfrac{1}{2},\tfrac{1}{2},-\tfrac{1}{2},-\tfrac{1}{2}]"),
                    TexMobject(r"[0,\tfrac{1}{2},-r_5^+,-r_5^-]"), TexMobject(r"[-\tfrac{1}{2},r_5^-,-r_5^+,0]"),
                    TexMobject(r"[-r_5^-,0,-r_5^+,\tfrac{1}{2}]"),
                    TexMobject(r"[-\tfrac{1}{2},-\tfrac{1}{2},-\tfrac{1}{2},\tfrac{1}{2}]"),
                    TexMobject(r"[-\tfrac{1}{2},-r_5^+,0,r_5^-]"), TexMobject(r"[0,-r_5^+,-r_5^-,\tfrac{1}{2}]"),
                    TexMobject(r"[\tfrac{1}{2},0,-r_5^-,r_5^+]"),
                    TexMobject(r"[\tfrac{1}{2},\tfrac{1}{2},-\tfrac{1}{2},\tfrac{1}{2}]"),
                    TexMobject(r"[\tfrac{1}{2},-\tfrac{1}{2},-\tfrac{1}{2},\tfrac{1}{2}]"),
                    TexMobject(r"[r_5^-,-\tfrac{1}{2},0,r_5^+]"), TexMobject(r"[\tfrac{1}{2},-r_5^+,0,r_5^-]"),
                    TexMobject(r"[r_5^-,-r_5^+,\tfrac{1}{2},0]"),
                    TexMobject(r"[\tfrac{1}{2},-\tfrac{1}{2},\tfrac{1}{2},-\tfrac{1}{2}]"),
                    TexMobject(r"[\tfrac{1}{2},0,r_5^-,-r_5^+]"), TexMobject(r"[r_5^-,0,r_5^+,-\tfrac{1}{2}]"),
                    TexMobject(r"[\tfrac{1}{2},\tfrac{1}{2},-\tfrac{1}{2},-\tfrac{1}{2}]"),
                    TexMobject(r"[r_5^-,\tfrac{1}{2},0,-r_5^+]"), TexMobject(r"[\tfrac{1}{2},r_5^-,-r_5^+,0]"),
                    TexMobject(r"[r_5^-,r_5^+,-\tfrac{1}{2},0]"), TexMobject(r"[r_5^-,0,-r_5^+,\tfrac{1}{2}]"),
                    TexMobject(r"[0,r_5^+,r_5^-,-\tfrac{1}{2}]"), TexMobject(r"[0,1,0,0]"),
                    TexMobject(r"[0,r_5^+,-r_5^-,\tfrac{1}{2}]"), TexMobject(r"[-r_5^-,r_5^+,-\tfrac{1}{2},0]"),
                    TexMobject(r"[0,0,0,1]"), TexMobject(r"[0,r_5^-,-\tfrac{1}{2},r_5^+]"),
                    TexMobject(r"[-0,-r_5^-,\tfrac{1}{2},r_5^+]"), TexMobject(r"[-r_5^-,-\tfrac{1}{2},0,r_5^+]"),
                    TexMobject(r"[0,-\tfrac{1}{2},r_5^+,r_5^-]"), TexMobject(r"[-0,-\tfrac{1}{2},r_5^+,-r_5^-]"),
                    TexMobject(r"[0,r_5^-,\tfrac{1}{2},-r_5^+]"),
                    TexMobject(r"[-\tfrac{1}{2},-\tfrac{1}{2},\tfrac{1}{2},-\tfrac{1}{2}]"),
                    TexMobject(r"[-r_5^-,-r_5^+,\tfrac{1}{2},0]"), TexMobject(r"[-\tfrac{1}{2},0,r_5^-,-r_5^+]"),
                    TexMobject(r"[0,-r_5^-,\tfrac{1}{2},-r_5^+]"), TexMobject(r"[-r_5^-,\tfrac{1}{2},0,-r_5^+]"),
                    TexMobject(r"[0,r_5^+,-r_5^-,-\tfrac{1}{2}]"), TexMobject(r"[-0,\tfrac{1}{2},-r_5^+,r_5^-]"),
                    TexMobject(r"[0,-r_5^-,-\tfrac{1}{2},r_5^+]"), TexMobject(r"[-0,-r_5^+,r_5^-,\tfrac{1}{2}]")]

        for i in range(0, len(results3)):
            results3[i].scale(0.47)
            if i == 0:
                results3[i].next_to(gen1copy, RIGHT, buff=LARGE_BUFF * colsep)
            elif i % 12 == 0:
                results3[i].next_to(results3[i - 12], RIGHT, buff=LARGE_BUFF * colsep)
            else:
                results3[i].next_to(results3[i - 1], DOWN, buff=SMALL_BUFF * 2.2)
                results3[i].align_to(results3[i - 1], LEFT)

        self.play(Uncreate(results2[7]), *[Write(results3[i]) for i in range(0, 12)])

        for j in range(0, 5):
            if j == 4:
                fuller_group = VGroup(all_elems, gen1copy, gen2copy, *results, *results2,
                                      *[results3[i] for i in range(0, 108)])
                self.play(fuller_group.stretch_in_place, 0.55, 0, fuller_group.stretch_in_place, 0.7, 1,
                          fuller_group.shift, 4.5 * LEFT)
                fuller_group = VGroup(all_elems, *[results3[i] for i in range(0, 108)])
                rect_orange_new = SurroundingRectangle(fuller_group)
                rect_orange_new.set_color(WHITE)
                self.play(Transform(rect_orange, rect_orange_new))
            else:
                fuller_group = VGroup(all_elems, *[results3[i] for i in range(0, 24 + 12 * j)])
                rect_orange_new = SurroundingRectangle(fuller_group)
                rect_orange_new.set_color(WHITE)
                self.play(Transform(rect_orange, rect_orange_new))
                self.play(*[Write(results3[i]) for i in range(12 + 12 * j, 24 + 12 * j)])

        self.wait(10)


class Quat2Vect(Scene):
    def construct(self):
        title = Title("Quaternions to Vectors")
        title.set_color(YELLOW)
        title.move_to(LEFT * 3.5)
        title.to_edge(UP)
        self.play(Write(title))

        retreat = TextMobject("Treat quaternions as vectors")
        retreat.to_edge(LEFT, buff=SMALL_BUFF)
        retreat.shift(UP * 2)
        retreat_example = TexMobject(r"\omega =[-\tfrac{1}{2},\tfrac{1}{2},\tfrac{1}{2},\tfrac{1}{2}]\\")
        retreat_example2 = TexMobject(
            r"\rightarrow \vec \omega =\left(-\tfrac{1}{2}|\tfrac{1}{2}|\tfrac{1}{2}|\tfrac{1}{2}\right)")
        retreat_example.next_to(retreat, DOWN)
        retreat_example.align_to(retreat, LEFT)
        retreat_example2.next_to(retreat_example, DOWN)
        retreat_example2.shift(2 * RIGHT)

        self.play(Write(retreat))
        self.play(Write(retreat_example))
        self.play(Write(retreat_example2))
        self.wait(3)
        result = TextMobject(r"\text{Set of 120 vectors: }")
        result2 = TexMobject(r"\left\{\vec v_1, \vec v_2,\cdots \vec v_{119}, \vec v_{120}\right\}")
        result2.set_color(YELLOW)

        result.next_to(retreat_example, DOWN, buff=LARGE_BUFF * 2)
        result2.next_to(result, DOWN)
        result2.align_to(result, LEFT)

        self.play(Write(result))
        self.play(Write(result2))
        self.wait(10)


class Properties(Scene):
    def construct(self):
        title = Title("The Properties")
        title.set_color(YELLOW)
        title.move_to(LEFT * 3.5)
        title.to_edge(UP)
        self.play(Write(title))

        result = TexMobject(r"\left\{\vec v_1, \vec v_2,\cdots \vec v_{119}, \vec v_{120}\right\}")
        result.set_color(YELLOW)
        result.to_edge(LEFT)
        result.shift(UP * 2.2)
        rect = SurroundingRectangle(result)

        self.play(Write(result))
        self.play(Write(rect))
        self.wait(3)

        obs = TextMobject("Scalar product:")
        obs.next_to(result, DOWN, buff=SMALL_BUFF * 2)
        obs.align_to(result)

        sp = TexMobject(r"\vec v_i\cdot \vec v_i = 1")
        sp.next_to(obs, DOWN)
        sp.align_to(obs, LEFT)

        res = TexMobject(r"\vec v_i \in S^3")
        res.set_color(YELLOW)
        res.next_to(sp, DOWN)
        res.align_to(sp, LEFT)

        self.play(Write(obs))
        self.play(Write(sp))
        self.play(Write(res))
        self.wait(3)

        smallD = TextMobject("min. Distance")
        largeD = TextMobject("max. Distance")

        smallD.next_to(res, DOWN)
        smallD.shift(LEFT * 0.5)
        largeD.next_to(smallD, RIGHT, buff=SMALL_BUFF * 4)

        v6 = TexMobject(r"\vec v_6=(-1|0|0|0)}")
        v7 = TexMobject(r"\vec v_7=(1|0|0|0)}")
        v6.scale(0.8)
        v7.scale(0.8)
        v6.next_to(largeD, DOWN)
        v6.align_to(largeD, LEFT)

        v7.next_to(v6, DOWN)
        v7.align_to(v6, LEFT)

        d67 = TexMobject(r"\vec d_{67}=\vec v_7-\vec v_6")
        d67.scale(0.8)
        below(v7, d67)

        d_max = TexMobject(r"d^2_\text{max}=\vec d_{67}\cdot \vec d_{67}=4")
        d_max.scale(0.8)
        below(d67, d_max)

        blueG = VGroup(largeD, v6, v7, d67, d_max)
        blueG.set_color(BLUE)

        v1 = TexMobject(r"\vec v_1=(-\tfrac{1}{2}|\tfrac{1}{2}|\tfrac{1}{2}|\tfrac{1}{2})}")
        v2 = TexMobject(r"\vec v_2=(0|\tfrac{1}{2}|r_5^+|r_5^-)}")
        v1.scale(0.6)
        v2.scale(0.6)
        below(smallD, v1)
        below(v1, v2)
        d12 = TexMobject(r"\vec d_{12}=\vec v_2-\vec v_1")
        d12.scale(0.8)
        below(v2, d12)

        d_min = TexMobject(r"d^2_\text{min}", r"=", r"\vec d_{12}\cdot \vec d_{12}")
        d_min.scale(0.6)
        below(d12, d_min)
        d_min2 = TexMobject(r"=", r"\tfrac{1}{2}(3-\sqrt{5})")
        d_min2.scale(0.6)
        below(d_min[1], d_min2)

        rect = SurroundingRectangle(d_min2[1])
        rect.set_color(RED)

        orangeG = VGroup(smallD, v1, v2, d12, d_min, d_min2)
        orangeG.set_color(ORANGE)

        self.play(Write(largeD))
        self.wait(3)
        self.play(Write(v6), Write(v7))
        self.play(Write(d67))
        self.play(Write(d_max))
        self.wait(3)
        self.play(Write(smallD))
        self.play(Write(v1), Write(v2))
        self.play(Write(d12))
        self.play(Write(d_min), Write(d_min2))
        self.play(GrowFromCenter(rect))
        self.wait(3)


class Lines(Scene):
    def construct(self):
        title = Title("Find all edges")
        title.set_color(YELLOW)
        title.move_to(LEFT * 3.5)
        title.to_edge(UP)
        self.play(Write(title))

        definition = TextMobject("All points with minimal distance")
        definition2 = TextMobject("are connected by edges.")
        task = TextMobject("Find all pairs of points ", "$(i,j)$", " with:")
        task2 = TexMobject(r"d_{ij}^2=\tfrac{1}{2}(3-\sqrt{5})")
        task2.set_color(ORANGE)
        task[1].set_color(ORANGE)

        definition.to_edge(LEFT)
        definition.shift(2 * UP)
        below(definition, definition2)
        below(definition2, task)
        below(task, task2)

        self.play(Write(definition))
        self.play(Write(definition2))
        self.play(Write(task))
        self.play(Write(task2))
        self.wait(3)

        result = TextMobject("Result: ")
        result2 = TextMobject(r"{\bf There are 720 edges}")
        result2.set_color(ORANGE)
        result3 = TextMobject("Every point is connected to")
        result4 = TextMobject(r"12 other points $[120\cdot 12/2=720]$")

        below(task2, result, LARGE_BUFF)
        below(result, result2)
        below(result2, result3)
        below(result3, result4)

        self.play(Write(result))
        self.play(Write(result2))
        self.play(Write(result3))
        self.play(Write(result4))
        self.wait(3)


class Triangles(Scene):
    def construct(self):
        title = Title("Find all triangles")
        title.set_color(YELLOW)
        title.move_to(LEFT * 3.5)
        title.to_edge(UP)
        self.play(Write(title))

        question = TextMobject("When do 3 edges form a triangle?")
        question.to_edge(LEFT)
        question.shift(2 * UP)

        l1 = TextMobject(r"edge 1: (", "1", r",2)")
        l2 = TextMobject(r"edge 2: (", "1", r",14)")
        l3 = TextMobject(r"edge 3: (", "1", r",16)")

        l4 = TextMobject(r"edge 1: (", "1", ",", "2", r")")
        l5 = TextMobject(r"edge 2: (", "1", ",", "14", r")")
        l6 = TextMobject(r"edge 13: (", "2", ",", "14", r")")

        examples = TextMobject("Example 1", r"\hspace{3em}", "Example 2")

        group_orange = VGroup(l1, l2, l3, examples[0])
        group_blue = VGroup(l4, l5, l6, examples[2])

        group_orange.set_color(ORANGE)
        group_blue.set_color(BLUE)

        below(question, examples)
        below(examples[0], l1)
        below(l1, l2)
        below(l2, l3)

        below(examples[2], l4)
        below(l4, l5)
        below(l5, l6)

        self.play(Write(question))
        self.wait()

        self.play(Write(examples[0]))
        self.play(Write(l1))
        self.play(Write(l2))
        self.play(Write(l3))
        self.wait(3)
        self.play(l1[1].set_color, YELLOW, l2[1].set_color, YELLOW, l3[1].set_color, YELLOW)
        self.wait(3)

        self.play(Write(examples[2]))
        self.play(Write(l4))
        self.play(Write(l5))
        self.play(Write(l6))
        self.wait(3)
        self.play(l4[1].set_color, YELLOW, l5[1].set_color, YELLOW)
        self.wait(3)
        self.play(l4[3].set_color, RED, l6[1].set_color, RED)
        self.wait(3)
        self.play(l5[3].set_color, GREEN, l6[3].set_color, GREEN)
        self.wait(3)

        result = TextMobject("Result: ")
        result2 = TextMobject(r"{\bf There are 1200 triangles}")
        result2.set_color(ORANGE)
        result3 = TextMobject("Every edge is part of")
        result4 = TextMobject(r"5 triangles $[720\cdot 5/3=1200]$.")

        below(l3, result, LARGE_BUFF)
        below(result, result2)
        below(result2, result3)
        below(result3, result4)

        self.play(Write(result))
        self.play(Write(result2))
        self.play(Write(result3))
        self.play(Write(result4))
        self.wait(3)


class Tetrahedra(Scene):
    def construct(self):
        title = Title("Find all tetrahedra")
        title.set_color(YELLOW)
        title.move_to(LEFT * 3.5)
        title.to_edge(UP)
        self.play(Write(title))

        question = TextMobject("Find all pairs of triangles with a common edge")
        question.scale(0.5)
        question.to_edge(LEFT)
        question.shift(2 * UP)

        result = TextMobject("7200 pairs of triangles")
        result.set_color(ORANGE)
        result.scale(0.7)
        below(question, result)

        question2 = TextMobject("Combine any two pairs with four different triangles")
        question3 = TextMobject("Find all combinations with only six different edges")
        question2.scale(0.5)
        question3.scale(0.5)

        below(result, question2,LARGE_BUFF)
        below(question2, question3)

        result2 = TextMobject("There are 600 tetrahedra")
        result2.set_color(ORANGE)
        below(question2, result2,LARGE_BUFF)
        result3 = TextMobject("Each triangle is part of 2 tetrahedra $[1200/2=600]$")
        result3.scale(0.5)
        below(result2, result3)
        euler = TextMobject("Euler number in 4D: ")
        euler2 = TexMobject("600-1200+720-120 = 0")
        euler.scale(0.7)
        euler2.scale(0.7)

        below(result3, euler,LARGE_BUFF)
        below(euler, euler2)

        self.play(Write(question))
        self.wait(3)
        self.play(Write(result))
        self.wait(3)
        self.play(Write(question2))
        self.play(Write(question3))
        self.wait(3)
        self.play(Write(result2))
        self.play(Write(result3))
        self.wait(3)

        self.play(Write(euler),Write(euler2))

        self.wait(10)


def below(a, b, buff=SMALL_BUFF):
    b.next_to(a, DOWN, buff)
    b.align_to(a, LEFT)
