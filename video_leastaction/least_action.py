from abc import ABC

import numpy as np
from manim import *
import sympy as sp


class Intro(Scene):
    def construct(self):
        title = Tex("Overview")
        title.to_edge(UP)
        title.set_color(YELLOW)
        self.play(Write(title))
        self.wait()

        tops = BulletedList("Optimal points", "Optimal functions",
                            "Least action principle", "Applications")
        tops[0].set_color(RED)
        tops[1].set_color(GREEN)
        tops[2].set_color(BLUE)
        tops[3].set_color(WHITE)

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
        title.shift(0.1*RIGHT)
        title.set_color(RED)
        self.play(Write(title))
        self.wait()

        paper=ImageMobject("paper.png")
        paper.scale(0.7)
        self.add(paper)
        self.wait(3)

        label = Tex("33\,cm")
        label.set_color(RED)
        label.shift(3.5*DOWN)
        line = DoubleArrow(2.7*LEFT,2.7*RIGHT)
        line.shift(3*DOWN)
        line.set_color(RED)

        self.play(Write(label),Create(line))
        self.wait(2)

        self.play(FadeOut(paper),FadeOut(label),FadeOut(line))

        volume1 = MathTex("21\,cm\cdot 21\,cm\cdot 6\,cm = 2646\,cm^3=2.6\,l")
        volume1.scale(0.7)
        volume1.to_corner(DL,buff=LARGE_BUFF)

        self.play(Write(volume1))
        self.wait(2)

        ax = Axes(
            x_range=[0,20],
            y_range=[0,4],
            x_length=6,
            y_length=4,
            axis_config={"color":GRAY},
            x_axis_config={
                "numbers_to_include":np.arange(0,20,5),
                "numbers_with_eleongated_tics":np.arange(0,15,5),
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 4, 1),
                "numbers_with_eleongated_tics": np.arange(0, 4, 1),
            },
            include_tip=True,
        )

        ax.shift(3.5*RIGHT)

        self.play(Create(ax))

        dot_A = Dot().move_to(ax.coords_to_point(6, 2.646))
        label_A=MathTex(r"(6,2.6)")
        label_A.scale(0.7)
        label_A.next_to(dot_A,UP)
        self.play(Create(dot_A),Write(label_A))

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

        self.play(GrowFromCenter(line2), Write(label2),GrowFromCenter(line3), Write(label3))
        self.wait(2)

        label = MathTex("33-2\cdot x")
        label.set_color(RED)
        label.scale(0.7)
        line = DoubleArrow(0.9*LEFT, 0.9*RIGHT)
        line.set_color(RED)
        line.next_to(box, DOWN)
        label.next_to(line,DOWN)

        self.play(GrowFromCenter(line),Write(label))
        self.wait(2)

        volume4 = MathTex("V(x)=(33-2\cdot x)^2\cdot x=4x^3-132x^2+1089x")
        volume4.to_corner(DL, buff=LARGE_BUFF)
        volume4.shift(0.5*DOWN)
        volume4.set_color(RED)

        func = ax.get_graph(lambda x:(4*x**3-132*x**2+1089*x)/1000,color=RED,x_range=[0,16.5])
        self.play(Write(volume4),Create(func))
        self.wait(2)

        self.play(FadeOut(box),FadeOut(dot_A),FadeOut(dot_B),FadeOut(dot_C),FadeOut(label_A),FadeOut(label_B),FadeOut(label_C),FadeOut(line),FadeOut(line3),FadeOut(line2),FadeOut(label),FadeOut(label2),FadeOut(label3))

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

        rows = [vol_prime,necessary,eq,sol1,sol2]

        rows[0].to_corner(UL,buff=LARGE_BUFF)
        rows[0].shift(DOWN)

        for i in range(1,len(rows)):
            rows[i].next_to(rows[i-1],DOWN)
            rows[i].align_to(rows[i-1],LEFT)

        colors = [WHITE,WHITE,WHITE,RED,BLUE]
        for i in range(0,2):
            self.play(Write(rows[i]))
            rows[i].set_color(colors[i])


        rect = SurroundingRectangle(necessary)
        rect.set_color(YELLOW)
        self.play(GrowFromCenter(rect))
        self.wait(2)

        #moving tangent

        alpha = ValueTracker(0)  # this is the value we're changing when animating

        # function for drawing the tangent line
        draw_tangent = (lambda:
                        TangentLine(func, alpha.get_value(), length=2, color=YELLOW))

        # always redraw the tangent line, i.e. update when alpha changes
        tangent = always_redraw(draw_tangent)

        self.play(Create(tangent))

        # move the value of alpha around
        for alpha_ in (0,0.9,0.43): # animate range as a fraction of the entire x-range of the graph
            self.play(alpha.animate.set_value(alpha_),run_time=3)

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
        title.shift(0.1*RIGHT)
        title.set_color(GREEN)
        self.play(Write(title))
        self.wait()

        demo=ImageMobject("freeFall.png")
        demo.to_edge(LEFT)
        self.add(demo)

        line = NumberLine(x_range=[0,5],length=5,include_numbers=True,include_tip=True)
        line.shift(4.25*LEFT+1.2*UP)
        line.rotate(PI/2)
        line.set_color(GRAY)

        self.play(Create(line))

        self.wait(2)

        ax = Axes(
            x_range=[0, 1.,0.2],
            y_range=[0, 5,1],
            x_length=5,
            y_length=5,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": [0.2,0.4,0.6,0.8,1.0],
                "numbers_with_eleongated_tics": np.arange(0, 1.1, 1),
                "label": 't',
                'decimal_number_config': {
                    'num_decimal_places': 1,
                }
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 5, 1),
                "numbers_with_eleongated_tics": np.arange(0, 5, 1),
                "label":'h(t)',
            },
        include_tip=True,
        )
        labels = ax.get_axis_labels(x_label="t",y_label = "h(t)")
        labels[1].shift(0.5*DOWN-1.2*RIGHT)
        labels[0].shift(0.3*LEFT)
        ax.add(labels)
        ax.shift(3.5 * RIGHT+0.8*UP)

        self.play(Create(ax))
        self.wait(2)

        h = lambda t:5-5*t*t

        alpha = ValueTracker(0)  # this is the value we're changing when animating
        # function for drawing the tangent line

        arrow = always_redraw(lambda: Arrow(start = (h(alpha.get_value())-1.5)*UP+1.5*LEFT,end = (h(alpha.get_value())-1.5)*UP+4*LEFT,stroke_color=RED,fill_color=RED,stroke_width=2))
        self.add(arrow)
        label = always_redraw(lambda: MathTex(r"(",round(alpha.get_value(),1),",",round(h(alpha.get_value()),1),")").scale(0.7).next_to(arrow,RIGHT).set_color(RED))

        parabel = always_redraw(lambda: ax.get_graph(lambda x:5-5*x*x,color=RED,x_range=[0,alpha.get_value()]))

        self.add(label)
        self.add(parabel)

        dot = always_redraw(lambda: Dot(stroke_color=RED,stroke_width=2,fill_color=RED_D).move_to(ax.coords_to_point(alpha.get_value(),h(alpha.get_value()))))
        self.add(dot)

        self.play(alpha.animate.set_value(0),run_time = 2)
        self.play(alpha.animate.set_value(1),run_time = 5,rate_func = linear)
        self.wait(2)

        self.wait(20)


class OptimalFunction2(Scene):
    def construct(self):
        title = Tex("Optimal Functions")
        title.to_edge(DOWN)
        title.shift(0.1*RIGHT)
        title.set_color(GREEN)

        ax = Axes(
            x_range=[0, 1.,0.2],
            y_range=[0, 5,1],
            x_length=5,
            y_length=5,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": [0.2,0.4,0.6,0.8,1.0],
                "numbers_with_eleongated_tics": np.arange(0, 1.1, 1),
                "label": 't',
                'decimal_number_config': {
                    'num_decimal_places': 1,
                }
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 5, 1),
                "numbers_with_eleongated_tics": np.arange(0, 5, 1),
                "label":'h(t)',
            },
        include_tip=True,
        )
        labels = ax.get_axis_labels(x_label="t",y_label = "h(t)")
        labels[1].shift(0.5*DOWN-1.2*RIGHT)
        labels[0].shift(0.3*LEFT)
        ax.add(labels)
        ax.shift(3.5 * RIGHT+0.8*UP)

        parabel =  ax.get_graph(lambda x: 5 - 5 * x * x, color=RED, x_range=[0,1])

        self.add(title,ax,parabel)
        self.wait(2)

        self.play(ApplyMethod(title.to_edge,UP),ApplyMethod(ax.shift,1.5*DOWN+0.5*RIGHT),ApplyMethod(parabel.shift,1.5*DOWN+0.5*RIGHT))
        self.wait(2)

        dotA = Dot(ax.coords_to_point(0,5)).set_color(GREEN).scale(2)
        dotB = Dot(ax.coords_to_point(1,0)).set_color(GREEN).scale(2)

        self.play(GrowFromCenter(dotA))
        self.play(GrowFromCenter(dotB))

        fcns = [lambda x:5-5*x**32,lambda x:5-5*x**16,lambda x:5-5*x**8,lambda x:5-5*x**4, lambda x:5-5*x**2,lambda x:5-5*x]

        # calculating the mirror images of the above functions, for some reason the functions are not evaluated correctly for too small exponents
        fcns2 = []
        for fcn in fcns:
            fcns2.append(ParametricFunction(lambda u: ax.coords_to_point(1 - 1 / 5*fcn(u), 5-5*u),color=GREEN,t_min=0,t_max=1))

        functions = []

        for fcn in fcns2:
            self.play(Create(fcn),run_time=0.2)
            functions.append(fcn)

        for fcn in reversed(fcns):
            p = ax.get_graph(fcn, color=GREEN, x_range=[0, 1])
            self.play(Create(p), run_time=0.2)
            functions.append(p)

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
                "numbers_to_include": np.arange(-30,130,60),
                "numbers_with_eleongated_tics": np.arange(0, 5, 1)
            },
            include_tip=True,
        )
        ax2.shift(3.5 * LEFT -0.2*UP)
        self.add(ax2)

        count = 0
        for parabel,action_value in zip(functions,action_values):
            copy = parabel.copy()
            copy.shift(4.1*LEFT+0.45*UP)
            copy.scale(0.25)
            self.play(TransformFromCopy(parabel,copy))
            value = MathTex(action_value)
            value.set_color(RED)
            value.scale(0.7)
            self.play(FadeOut(copy),FadeIn(value),run_time=5)
            dot = Dot()
            dot.set_color(RED)
            self.play(Transform(value,dot))
            self.play(ApplyMethod(value.shift,ax2.coords_to_point(count,num_action_values[count])))
            count=count+1

        self.wait(2)

        pTwo = lambda n:2**(n-5)
        solFunc = lambda x:  25*pTwo(x)*(4+(pTwo(x)-7)*pTwo(x))/2/(2*pTwo(x)**2+pTwo(x)-1)
        solution = ax2.get_graph(solFunc, color=RED, x_range=[0, 3.9])
        solution2 = ax2.get_graph(solFunc, color=RED, x_range=[4.06, 10])

        self.play(GrowFromPoint(solution,ax2.coords_to_point(0, 0)))
        self.play(GrowFromPoint(solution2,ax2.coords_to_point(4.01, solFunc(4.01))))
        self.wait(2)

        alpha = ValueTracker(1)  # this is the value we're changing when animating

        # function for drawing the tangent line
        draw_tangent = (lambda: TangentLine(solution2, alpha.get_value(), length=2, color=YELLOW))

        # always redraw the tangent line, i.e. update when alpha changes
        tangent = always_redraw(draw_tangent)

        self.play(Create(tangent))

        # move the value of alpha around
        for alpha_ in (0.1,0.325): # animate range as a fraction of the entire x-range of the graph
            self.play(alpha.animate.set_value(alpha_),run_time=3)

        self.wait(2)

        dot = Dot(ax2.coords_to_point(6,-16.7))
        dot.set_color(YELLOW)
        dot.scale(1.5)

        emphasize = functions[7]
        self.play(GrowFromCenter(dot),ApplyMethod(emphasize.set_color,YELLOW))
        self.wait(2)



        self.wait(20)

