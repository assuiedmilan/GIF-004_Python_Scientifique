"""Exercices sur module_4.sympy"""
from numpy.ma import sqrt
from sympy import Eq
from sympy import Function
from sympy import cos
from sympy import diff
from sympy import dsolve
from sympy import integrate
from sympy import limit
from sympy import oo
from sympy import sin
from sympy import symbols


# pylint: disable=not-callable

def derive_sin_over_x():
    """En utilisant le module sympy, trouvez la dérivée de 𝑓(𝑥)=sin(𝑥)𝑥 et affectez-la à la variable"""

    x = symbols('x')
    f = sin(x) / x

    return diff(f, x)


def integration_of_inverse_cosine():
    """En utilisant le module sympy, trouvez l'intégrale  𝑓(𝑥)=∫1cos2(𝑎𝑥)𝑑𝑥"""

    x, a = symbols('x a')

    fprime = 1 / cos(a * x) ** 2

    return integrate(fprime, x)


def limit_of_simple_function():
    """
    Soit 𝑓 la fonction définie sur ℝ par 𝑓(𝑥)=49𝑥2−2𝑥+3⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯√ − 7𝑥

    Dans un premier temps, définissez l'expression Sympy de 𝑓
    (nommez-là expr) sans oublier de définir le symbole 𝑥, puis affichez avec print la limite de 𝑓 lorsque 𝑥 tend vers +∞. Utilisez la fonction sympy.limit.
    """

    x = symbols('x')
    expr = sqrt(49 * x ** 2 - 2 * x + 3) - 7 * x
    return limit(expr, x, oo)


def harmonic_oscillator():
    """
    Un oscillateur harmonique est représenté par l'équation différentielle 𝑥¨+𝜔20𝑥=0, avec 𝜔0 représentant la pulsation propre de l'oscillateur.
    Dans cette équation, 𝑥 correspond à la position de l'extrémité du ressort, 𝑥˙ sa vitesse, et 𝑥¨son accélération.

    Dans cet exercice, nous vous demandons d'écrire dans un premier temps l'équation différentielle de l'oscillateur harmonique, puis de la résoudre en utilisant sympy.dsolve.
    Nommez vos variables t et w0, votre fonction x et votre équation différentielle eqdiff. Affichez la solution de l'équation différentielle avec print.
    """

    t, w0 = symbols('t w0')
    x = Function('x')

    eqdiff = Eq(x(t).diff(t, 2) + w0 ** 2 * x(t), 0)
    return dsolve(eqdiff, x(t))
