from myfunctions import *


# Test
def test_sphericalSolver():
    x0, t0, temp = sphericalSolver(0.01, 1, 0.5, [0, 3600], 10, [50, 50], 1.172 * 10 ** (-5))
    assert temp.max() > 10 and temp.min() < 50
