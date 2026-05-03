import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
    # these are both 'unique' import variables for python lib imports
import sympy as sym
import scipy as sci

from scipy import stats 
#from scipy import [submodule]
#. . . 


# personal imports from local files
from Structural import *



print("   entering: EngineeringCalculatorMain.py")



'''


    --> steel, concrete, wood, masonry, and aluminum
        Young's Modulus / Poissons Ratio
Structural
-moment of intertia
-bending stress
-shear stress
-deflection


    --> https://mccord.cm.utexas.edu/courses/fall2014/ch301/thermoequations.php
        https://atmos.uw.edu/~robwood/teaching/535/ThermoEquations_2014.pdf
        https://web.mit.edu/16.unified/www/FALL/thermodynamics/EquationCompendium.pdf
Thermal
-Fourier's Law of Conduction
-Newton's Law of Cooling


    --> https://cfdland.com/the-essential-fluid-dynamics-equations/
Fluid Dynamics
-The Continuity Equation
-Navier-Stokes Equations
-The Energy Equation
-Fluid Dynamics Bernoulli Equation
-Euler's Equations


'''

if __name__ == "__main__":
    test = RectangularMomentOfInertia(6, 6)
    print(test)