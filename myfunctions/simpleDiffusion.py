from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


###################
# this is for a constant current application:


def diffusion_spherical_FV(c, t, r, D, j):
    """
    This function finds the right hand side of dcdt. It takes as inputs the parameters a time and parameters
    :param u:
    :param t:
    :param grid:
    :param D:
    :param j:
    :return:
    """
    dr = r[1]-r[0]

    q = - D*r[1:-1] ** 2. * (c[1:] - c[0:-1]) / dr
    q_surf = -j
    q = np.append(0, q)
    q = np.append(q, q_surf)

    dcdt_out = - (2. / (r[1:] + r[0:-1])) ** 2. \
             * (q[1:] - q[0:-1]) / dr
    return dcdt_out

# Set up grid
r = np.linspace(0., 1., 100)  # neg, sep, pos, particle, grid

# Initial conditions
c0 = np.ones(np.size(r)-1)  # neg, pos, electrolyte, grid

# Solve ODEs
tmax = 100
tsteps = 100
D = 0.1
current = 1.0
t = np.linspace(0, tmax, tsteps)
c = odeint(diffusion_spherical_FV, c0, t, args=(r, D, current))

print(c)

for i in range(1, np.size(t)):
    plt.clf()
    plt.plot(r[:-1], c[i, :])
    plt.pause(0.1)
################

