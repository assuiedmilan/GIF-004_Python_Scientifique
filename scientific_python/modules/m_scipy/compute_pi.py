import numpy as np
import scipy.integrate as integrate

pi = 4*integrate.quad(lambda x: np.sqrt(1 - x**2), 0, 1)[0]