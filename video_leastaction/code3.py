phi1.add_updater(lambda mob, dt: mob.increment_value(d_phi1.get_value() * dt))
phi2.add_updater(lambda mob, dt: mob.increment_value(d_phi2.get_value() * dt))

d_phi1.add_updater(lambda mob, dt: mob.increment_value(
    ddf1(phi1.get_value(), phi2.get_value(), d_phi1.get_value(), d_phi2.get_value()) * dt))
d_phi2.add_updater(lambda mob, dt: mob.increment_value(
    ddf2(phi1.get_value(), phi2.get_value(), d_phi1.get_value(), d_phi2.get_value()) * dt))

