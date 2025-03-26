import sympy.polys.polytools
from sympy import *
init_printing()

import numpy as np

x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

expin = '((1+2*x + x**2) - (1-x**3))*((x**2-4)-(x**3+7))/(5*x+6)-(7*x-8)*(14*x**2+6+x+7*x**8)'
e = Poly(expin)

c_res = Poly(49.0*x**9+56.0*x**8-0.2*x**5+0.2*x**4-98.5*x**3+103.8*x**2-34.7*x+44.5)

e1 = ((1+2*x + x**2) - (1-x**3))*((x**2-4)-(x**3+7))
e1d = (5*x+6)
e2 = -(7*x-8)*(14*x**2+6+x+7*x**8)

es1 = expand(simplify(expand(e1)))

es1_np = es1.as_poly()
es1_dp = e1d.as_poly()

q, r = sympy.polys.polytools.pdiv(es1_np, es1_dp)
e1 = q + r

e2 = e2.as_poly()

ev = e1 + e2


#=============================
# define the polynomials
# p(x) = -245x^10 - 14x^9 + 336x^8 - x^6 - 491x^4 - 72x^3 + 449x^2 + 14x + 288
# px = (288, 14, 449, -72, -491, 0, -1, 0, 336, -14, -245)

# g(x) = 5x + 6
# gx = (6, 5)

# divide the polynomials
# qx, rx = np.polynomial.polynomial.polydiv(px, gx)
