g=10
l=1

t = ValueTracker(0)
t.add_updater(lambda mobject, dt: mobject.increment_value(dt))

phi1 = ValueTracker(np.PI/6) # initial conditions
phi2 = ValueTracker(np.PI/3)
d_phi1 = ValueTracker(0)
d_phi2 = ValueTracker(0)

ddf1 = lambda f1,f2,df1,df2: (-np.sin(f1-f2)*(np.cos(f1-f2)*df1**2+df2**2)
                              -g/l*(2*np.sin(f1)+np.cos(f1-f2)*np.sin(f2))
                              )/(2-np.cos(f1-f2)**2)

ddf1 = lambda f1,f2,df1,df2: (np.sin(f1-f2)*(np.cos(f1-f2)*df2**2+2*df1**2)
                              -g/l*(2*np.sin(f2)+np.cos(f1-f2)*np.sin(f1))
                              )/(2-np.cos(f1-f2)**2)