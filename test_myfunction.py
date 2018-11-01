from myfunctions import *


# Root finder tests
def f(r):
    return r


def test_mybisection():
    assert abs(mybisection(f, -0.5, 0.55, 0.001)) <= 0.001


# Integration tests

def test_integration():
    N = 100
    x = np.linspace(0.0, 1.0, N)
    h = x[1] - x[0]
    y = f(x)
    assert abs(mytrapz(x, y)-0.5) <= h


# Heat equation tests
def test_heatequation():
    x0, t0, temp = heat1D_solver(0.01, 1, 0.5, [0, 3600], 10, [50, 50], 1.172 * 10 ** (-5))
    assert temp.max() > 10 and temp.min() < 50
