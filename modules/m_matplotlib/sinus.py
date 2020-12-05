import numpy as np
import matplotlib.pyplot as mpl
from math import pi, sin

x = np.linspace(-pi, pi, 20)
y = [sin(value) for value in x]

mpl.plot(x, y, 'ro')
mpl.plot(x, y, 'b-')

mpl.xlabel('angle en radians')
mpl.ylabel('valeur du sinus')
mpl.title('Graphique du sinus')
mpl.grid(True, axis='y')

mpl.show()
