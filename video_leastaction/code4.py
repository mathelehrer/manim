def first_line(phi):# a line for the first pendulum
    return Line(UP, DOWN).shift(DOWN).rotate(phi, about_point=0 * UP)

def second_line(phi1, phi2): # a line for the second pendulum
    pos1 = 2 * (DOWN * cos(phi1) + RIGHT * sin(phi1))
    return Line(UP, DOWN).move_to(pos1).shift(DOWN).rotate(phi2, about_point=pos1)

pendulum1 = always_redraw(lambda: first_line(phi1.get_value())) # update lines
pendulum2 = always_redraw(lambda: second_line(phi1.get_value(), phi2.get_value()))

self.add(t, d_phi1, phi1, d_phi2, phi2)
self.add(pendulum1, pendulum2)
self.wait(20) # run the simulation for 20 seconds

t.clear_updaters() # ... clear remaining updaters