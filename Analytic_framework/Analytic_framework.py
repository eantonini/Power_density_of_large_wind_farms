import numpy as np

performance_curve = np.array([[ 0.0,     0.0,  0.00],
                              [ 1.0,     0.0,  0.00],
                              [ 2.0,     0.0,  0.00],
                              [ 3.0,     0.0,  0.00],
                              [ 4.0,   147.3,  0.88],
                              [ 5.0,   699.5,  0.87],
                              [ 6.0,  1307.0,  0.84],
                              [ 7.0,  2153.9,  0.82],
                              [ 8.0,  3240.0,  0.79],
                              [ 9.0,  4620.7,  0.76],
                              [10.0,  6295.9,  0.73],
                              [11.0,  7952.7,  0.67],
                              [12.0,  8818.0,  0.52],
                              [13.0,  8983.6,  0.39],
                              [14.0,  9000.0,  0.30],
                              [15.0,  9000.0,  0.24],
                              [16.0,  9000.0,  0.19],
                              [17.0,  9000.0,  0.16],
                              [18.0,  9000.0,  0.14],
                              [19.0,  9000.0,  0.12],
                              [20.0,  9000.0,  0.10],
                              [21.0,  9000.0,  0.09],
                              [22.0,  9000.0,  0.08],
                              [23.0,  9000.0,  0.07],
                              [24.0,  9000.0,  0.06],
                              [25.0,  9000.0,  0.05],
                              [26.0,     0.0,  0.00],
                              [27.0,     0.0,  0.00],
                              [28.0,     0.0,  0.00],
                              [29.0,     0.0,  0.00],
                              [30.0,     0.0,  0.00]])

geostrophic_wind_speeds = np.array([8,12,16,20,24])
coriolis_parameters = np.array([0.05,0.55,1.05,1.35,1.45])*10**(-4)
turbine_densities = np.array([1,0.5])

diameter = 165
hubheight = 130

kappa = 0.4
z_0lo = 0.0001
C_thrust = np.zeros((len(geostrophic_wind_speeds),len(coriolis_parameters),len(turbine_densities)))
u_0 = 0.1*np.ones((len(geostrophic_wind_speeds),len(coriolis_parameters),len(turbine_densities))) # assumption
u_H = 2*np.ones((len(geostrophic_wind_speeds),len(coriolis_parameters),len(turbine_densities))) # assumption

spacing = np.zeros((len(geostrophic_wind_speeds),len(coriolis_parameters),len(turbine_densities)))
for rrr in range(len(turbine_densities)):
    spacing[:,:,rrr] = 1000/(diameter*np.sqrt(turbine_densities[rrr]))

iterations = 20
for ii in range(iterations):
    for r in range(len(geostrophic_wind_speeds)):
        for rr in range(len(coriolis_parameters)):
            for rrr in range(len(turbine_densities)):
                C_thrust[r,rr,rrr] = np.interp(u_H[r,rr,rrr],performance_curve[:,0], performance_curve[:,2])
    c_ft = np.pi*C_thrust/(4*spacing*spacing)
    nu_w = (0.5*c_ft)**0.5*u_H*diameter/(kappa*u_0*hubheight)
    z_0hi = hubheight*(1+0.5*diameter/hubheight)**(nu_w/(1+nu_w))*np.exp(-(0.5*c_ft/kappa**2+(np.log(hubheight/z_0lo*(1-0.5*diameter/hubheight)**(nu_w/(1+nu_w))))**(-2))**(-0.5))
    for iii in range(iterations):
        for r in range(len(geostrophic_wind_speeds)):
            for rr in range(len(coriolis_parameters)):
                for rrr in range(len(turbine_densities)):
                    u_0[r,rr,rrr] = geostrophic_wind_speeds[r]/((np.log(u_0[r,rr,rrr]/(coriolis_parameters[rr]*z_0hi[r,rr,rrr]))/kappa-4)**2+12**2)**0.5
    u_H = u_0/kappa*np.log(hubheight/z_0hi*(1+0.5*diameter/hubheight)**(nu_w/(1+nu_w)))

Rossby_numbers = np.zeros((len(geostrophic_wind_speeds),len(coriolis_parameters),len(turbine_densities)))
for r in range(len(geostrophic_wind_speeds)):
    for rr in range(len(coriolis_parameters)):
        for rrr in range(len(turbine_densities)):
            Rossby_numbers[r,rr,rrr] = geostrophic_wind_speeds[r]/(coriolis_parameters[rr]*z_0hi[r,rr,rrr])

mean_power_densities = np.zeros((len(geostrophic_wind_speeds),len(coriolis_parameters),len(turbine_densities)))
for r in range(len(geostrophic_wind_speeds)):
        for rr in range(len(coriolis_parameters)):
            for rrr in range(len(turbine_densities)):
                mean_power_densities[r,rr,rrr] = np.interp(u_H[r,rr,rrr],performance_curve[:,0], performance_curve[:,1])*turbine_densities[rrr]
