import numpy as np


def solve_linear_equations(a,b):
    a=np.array(a)
    b=np.array(b)
    #x = np.linalg.solve(a, b)
    x = np.linalg.lstsq(a, b)
    return x.tolist()
