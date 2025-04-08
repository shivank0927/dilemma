import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # don't know
from simulation.simulator import *

while True:
    try:
        counts = int(input("Enter simulation counts"))
        break

    except Exception as e:
        print(e, "\n")

display = simulations(counts)
print(display)