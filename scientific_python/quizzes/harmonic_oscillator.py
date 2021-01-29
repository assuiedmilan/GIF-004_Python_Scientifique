from sympy import I
from sympy import diff
from sympy import exp
from sympy import simplify
from sympy import solve
from sympy import symbols

"""
t, w0, C1, C2, v0 = symbols('t w0 C1 C2 v0')
x = Function('x')
solution = Eq(x(t), C1*exp(I*t*w0) + C2*exp(-I*t*w0))

solution_at_0 = solution.subs(t, 0).subs(x(0), 0)
C2_value = solve(solution_at_0, C2)[0]

solution = solution.subs(C2, C2_value)
vitesse = diff(solution, t)
vitesse_at_0 = vitesse.subs(t, 0)


# définir l'expression de x(t)
x = C1 * exp(I*w0*t) + C2 * exp(-I*w0*t)

# trouver l'expression de C2
C2_expr = solve(x.subs(t, 0), C2)[0]

# substituer C2 dans x(t)
x = x.subs(C2, C2_expr)

# dériver x(t) pour obtenir v(t)
v = diff(x, t)
print(solution)
print(vitesse)
"""


def compute_variable_value_at_initial_condition(equation, integration_variable, initial_condition, variable_to_solve):
    equation_with_initial_condition = equation.subs(integration_variable, 0) - initial_condition
    return solve(equation_with_initial_condition, variable_to_solve)[0]


def replace_variable_by_value_and_derive(equation, integration_variable, variable_to_replace, variable_value):
    equation_to_derive = equation.subs(variable_to_replace, variable_value)
    return diff(equation_to_derive, integration_variable)


def compute_harmonic_oscillator():
    t, w0, C1, C2, v0, x = symbols('t w0 C1 C2 v0, x')

    movement_equation = C1 * exp(I * t * w0) + C2 * exp(-I * t * w0)

    C2_value = compute_variable_value_at_initial_condition(movement_equation, t, 0, C2)

    movement_equation = movement_equation.subs(C2, C2_value)
    speed_equation = diff(movement_equation, t)

    C1_value = compute_variable_value_at_initial_condition(speed_equation, t, v0, C1)
    movement_equation = movement_equation.subs(C1, C1_value)
    return simplify(movement_equation)


print(compute_harmonic_oscillator())
