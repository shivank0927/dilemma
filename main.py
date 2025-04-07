import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # to start module search from root path
from simulation.simulator import *


result_simulation = simulations(1)

frame = pd.DataFrame(data=result_simulation)
print(frame)
