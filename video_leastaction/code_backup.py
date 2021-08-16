l = 1
g = 10
f = 0.1
t = ValueTracker(0)
t.add_updater(lambda mobject, dt: mobject.increment_value(dt))



rhs_phi = lambda phi, phi2, omega, omega2: ( - 2 * g / l * np.sin(phi) - np.sin(phi - phi2) * np.cos(phi - phi2) * omega * omega + g / l * np.cos(phi - phi2) * np.sin(phi2) - np.sin(phi - phi2) * omega2 * omega2) / (2 - np.cos(phi - phi2) ** 2)
rhs_phi2 = lambda phi, phi2, omega, omega2: ( - 2 * g / l * np.sin(phi2) + np.sin(phi - phi2) * np.cos( phi - phi2) * omega2 * omega2 + 2 * g / l * np.cos(phi - phi2) * np.sin(phi) + 2 * np.sin( phi - phi2) * omega * omega) / (2 - np.cos(phi - phi2) ** 2)

omega.add_updater(lambda mobject, dt: mobject.increment_value( rhs_phi(phi.get_value(), phi2.get_value(), omega.get_value(), omega2.get_value()) * dt))
omega2.add_updater(lambda mobject, dt: mobject.increment_value(rhs_phi2(phi.get_value(), phi2.get_value(), omega.get_value(), omega2.get_value()) * dt))
phi.add_updater(lambda mobject, dt: mobject.increment_value(omega.get_value() * dt))
phi2.add_updater(lambda mobject, dt: mobject.increment_value(omega2.get_value() * dt))

draw_pendulum = (lambda: Pendulum(2 * l, central_color=color1).shift(3 * RIGHT).rotate(phi.get_value()))
draw_pendulum2 = (lambda: Pendulum(2 * l, central_color=color2).shift((2 * l * np.sin(phi.get_value()) + 3) * RIGHT + 2 * l * np.cos(phi.get_value()) * DOWN ).rotate(phi2.get_value()))
pendulum_anim = always_redraw(draw_pendulum)
pendulum_anim2 = always_redraw(draw_pendulum2)

self.add(t, omega, phi, omega2, phi2)
self.add(pendulum_anim2,  pendulum_anim)
self.wait(duration)
t.clear_updaters()
phi.clear_updaters()
phi2.clear_updaters()
omega.clear_updaters()
omega2.clear_updaters()
pendulum_anim.clear_updaters()
pendulum_anim2.clear_updaters()
