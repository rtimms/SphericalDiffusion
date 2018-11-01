from scipy.integrate import ode
from numpy import *
import matplotlib.pyplot as plt


def diffusion_equation(t, c, d, g):

    n = c.size
    dx = 1/(n-1)

    # Create finite difference matrix
    a = diag(ones(n - 1), 1) - diag(2 * ones(n)) + diag(ones(n - 1), -1)
    a[0, 0] = -1
    a[n - 1, n - 1] = -1

    # create b
    b = zeros(n)
    b[n - 1] = g * c[n-1]

    return (d/pow(dx, 2)) * a.dot(c) + b/dx


# Parameters
pts = 50
flux = -10
diff = 10

# Grid and initial conditions
x = linspace(0, 1, pts)
c0 = 0.9 * ones(pts)

# Interactive plotting on
plt.ion()

# Initialise ODE solver
t0 = 0
r = ode(diffusion_equation)
r.set_initial_value(c0, t0).set_f_params(diff, flux)
t1 = 10
dt = 0.001
while r.successful() and r.t < t1:
    r.integrate(r.t+dt)
    plt.clf()
    plt.ylim([0, 2])
    plt.plot(x, r.y, color='red')
    plt.xlabel('Distance')
    plt.ylabel('Concentration')
    plt.title('Profile at t=%g' % r.t)
    plt.pause(0.01)

