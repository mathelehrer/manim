g=10 # define model parameters
l=1
pi = 3.141592654

t = ValueTracker(0)
t.add_updater(lambda mob, dt: mob.increment_value(dt))

# set initial conditions
phi1 = ValueTracker(pi/2) # 90 degrees
phi2 = ValueTracker(-2*pi/3) #-120 degrees
d_phi1 = ValueTracker(0)
d_phi2 = ValueTracker(0)
