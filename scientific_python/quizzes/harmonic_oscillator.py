"""
Nous avons résolu l'équation différentielle de l'oscillateur harmonique dans l'exercice 5.4, et nous avons vu que les solutions étaient sous la forme suivante:

𝑥(𝑡)=𝐶1exp(𝑖𝑡𝜔0)+𝐶2exp(−𝑖𝑡𝜔0)

Nous cherchons dans ce quiz à déterminer les constantes 𝐶1 et 𝐶2, et d'en déduire les solutions réelles de l'équation de l'oscillateur harmonique.

Pour ce faire, nous allons utiliser les conditions initiales, nous allons supposer que la vitesse 𝑣(𝑡=0) est 𝑣0, et la position 𝑥(𝑡=0) est 0.
Nous rappelons aussi que pour obtenir la vitesse 𝑣, il suffit de dériver 𝑥 en fonction du temps 𝑡.

Associez à x la fonction 𝑥(𝑡) en remplaçant 𝐶1 et 𝐶2, et en prenant soin de simplifier l'expression.

Détails de la démarche physique:

    Définissez l'expression de 𝑥(𝑡) en prenant soin de spécifier les symboles 𝐶1, 𝐶2, 𝜔0, 𝑣0 et 𝑡.
    Évaluez 𝑥(𝑡) en 𝑡=0 grâce à la méthode subs des expressions Sympy, sachant que 𝑥(0)=0 afin d'exprimer 𝐶2 en fonction de 𝐶1.
    À l'aide de subs, remplacez 𝐶2 par sa nouvelle expression dans 𝑥(𝑡), puis dérivez cette expression en fonction du temps pour obtenir 𝑣(𝑡).
    Évaluez 𝑣(𝑡) en 𝑡=0 grâce à la méthode subs des expressions Sympy, sachant que 𝑣(0)=𝑣0 afin d'exprimer 𝐶1 en fonction de 𝑣0 et 𝑤0.
    À l'aide de subs, remplacez 𝐶1 par sa nouvelle expression dans 𝑥(𝑡), puis simplifiez l'expression, et affectez le résultat à la variable solution.
"""

from sympy import I
from sympy import diff
from sympy import exp
from sympy import simplify
from sympy import solve
from sympy import symbols


def compute_variable_value_at_initial_condition(equation, integration_variable, initial_condition, variable_to_solve):
    """Solve the equation at the specified initial condition and return the value of the variable to solve"""

    equation_with_initial_condition = equation.subs(integration_variable, 0) - initial_condition
    return solve(equation_with_initial_condition, variable_to_solve)[0]


def replace_variable_by_value_and_derive(equation, integration_variable, variable_to_replace, variable_value):
    """In the equation, replace a variable by it's value and the derive the expression"""

    equation_to_derive = equation.subs(variable_to_replace, variable_value)
    return diff(equation_to_derive, integration_variable)


def compute_harmonic_oscillator():
    """Resolve the harmonic oscillator equation"""

    t, w0, C1, C2, v0 = symbols('t w0 C1 C2 v0')

    movement_equation = C1 * exp(I * t * w0) + C2 * exp(-I * t * w0)

    C2_value = compute_variable_value_at_initial_condition(movement_equation, t, 0, C2)

    movement_equation = movement_equation.subs(C2, C2_value)
    speed_equation = diff(movement_equation, t)

    C1_value = compute_variable_value_at_initial_condition(speed_equation, t, v0, C1)
    movement_equation = movement_equation.subs(C1, C1_value)
    return simplify(movement_equation)


print(compute_harmonic_oscillator())
