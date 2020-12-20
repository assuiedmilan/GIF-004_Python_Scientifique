from sympy import Function, Eq, symbols, I, exp, simplify, diff
from sympy import solve

t, w0, C1, C2, v0 = symbols('t w0 C1 C2 v0')
x = Function('x')
solution = Eq(x(t), C1*exp(I*t*w0) + C2*exp(-I*t*w0))

solution_at_0 = solution.subs(t, 0).subs(x(0), 0)
C2_value = solve(solution_at_0, C2)[0]

solution = solution.subs(C2, C2_value)
vitesse = diff(solution, t)



print(solution)
print(vitesse)