import matplotlib.pyplot as plt
import numpy as np


def myfunc(x):
    return np.sin(x**2) - x + 5


def mybisection(myfunc, a, b, epsilon):

    if abs(myfunc(a)) < epsilon:
        print('a is a root!')
        return a

    if abs(myfunc(b)) < epsilon:
        print('b is a root!')
        return b

    while abs(b-a) > epsilon:

        m = a + (b - a)/2
        #print(m)

        if myfunc(a)*myfunc(m) < 0:
            b = m
        else:
            a = m

    return m

"""
m = mybisection(myfunc, 3.8, 6, 0.001)
x = np.linspace(m - 1, m + 1, 100)
plt.plot(x, myfunc(x))
plt.plot(m, 0, 'bo')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('root finding plot')
plt.show()


def f(x):
    return x


print(mybisection(f, -0.5, 0.5, 0.001))

"""
