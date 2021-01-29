"""Exercices sur module_2.matplotlib"""
import datetime
import pickle
from math import pi
from math import sin

import matplotlib.pyplot as mpl
import numpy as np

from scientific_python.definitions import temperatures_pickle


def draw_sinus():
    """
    Draw a simple sinusoïde

    Returns:
        None
    """

    x = np.linspace(-pi, pi, 20)
    y = [sin(value) for value in x]

    mpl.plot(x, y, 'ro')
    mpl.plot(x, y, 'b-')

    mpl.xlabel('angle en radians')
    mpl.ylabel('valeur du sinus')
    mpl.title('Graphique du sinus')
    mpl.grid(True, axis='y')

    mpl.show()


def tracer_températures(date1: datetime.date, date2: datetime.date):
    """
    Draw a temperature reports of measured temperatures at Lesage Québec Airport, between two dates.

    Args:
        date1 (datetime.date): First date
        date2 (datetime.date): Second date

    Returns:
        None
    """

    temperatures = pickle.loads(temperatures_pickle.PICKLE)

    set_of_temperatures = list(filter(lambda x: date1 <= x[0] <= date2, temperatures))

    dates = [x[0] for x in set_of_temperatures]
    min_temp = [x[1] for x in set_of_temperatures]
    max_temp = [x[2] for x in set_of_temperatures]
    moy_temp = [x[3] for x in set_of_temperatures]

    mpl.plot(dates, min_temp, 'b', )
    mpl.plot(dates, max_temp, 'r')
    mpl.plot(dates, moy_temp, 'y')

    mpl.legend(['min', 'max', 'moy'])
    mpl.ylabel('température en degrés Celsius')
    mpl.title('Graphique des températures à l\'Aéroport de Québec')
    mpl.grid(True)

    mpl.xticks(rotation=45)

    mpl.show()

    return sum(moy_temp) / len(moy_temp)
