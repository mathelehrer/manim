g=10
l=1

t = ValueTracker(0)
t.add_updater(lambda mob, dt: mob.increment_value(dt))

phi1 = ValueTracker(np.pi/6)
phi2 = ValueTracker(np.pi/3)
d_phi1 = ValueTracker(0)
d_phi2 = ValueTracker(0)
