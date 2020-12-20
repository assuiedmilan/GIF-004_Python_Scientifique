from sympy import symbols
from sympy import sqrt
from sympy import limit
from sympy import oo

x = symbols('x')
expr = sqrt(49*x**2 - 2*x + 3) - 7*x
print(limit(expr, x, oo))
