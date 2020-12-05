from sympy import diff, sin, symbols

x = symbols('x')
f = sin(x)/x

fprime = diff(f, x)