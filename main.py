import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # don't know
from simulation.simulator import *


display = simulations(1)

print(display)