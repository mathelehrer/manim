def first_line(phi):
    return Line(UP, DOWN).shift(DOWN).rotate(phi, about_point=0 * UP).set_color(BLUE)

def second_line(phi1, phi2):
    pos1 = 2 * (DOWN * numpy.cos(phi1) + RIGHT * numpy.sin(phi1))
    return Line(UP, DOWN).move_to(pos1).shift(DOWN).rotate(phi2, about_point=pos1).set_color(RED)

pendulum1 = always_redraw(lambda: first_line(phi1.get_value()))
pendulum2 = always_redraw(lambda: second_line(phi1.get_value(), phi2.get_value()))

self.add(t, d_phi1, phi1, d_phi2, phi2)
self.add(pendulum1, pendulum2)
self.wait(10)

t.clear_updaters()
... # clear remaining updaters