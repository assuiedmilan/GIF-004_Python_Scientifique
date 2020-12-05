from sympy import symbols, Function, Eq, dsolve

t, w0 = symbols('t w0')
x = Function('x')

eqdiff = Eq(x(t).diff(t, 2)+w0**2 * x(t), 0)
print(dsolve(eqdiff, x(t)))