import itertools
from strategies import strategy
import pandas as pd

HISTORY = []

def combinations():

    return list(itertools.combinations(strategy, 2))

def calculate():
    
    pairs = combinations()
    matches = []
    dictionary ={}
    
    # for _ in range(100): # later add the number of simulations for now one only.
    for playerOne, playerTwo in pairs:
        p1 = playerOne() 
        p2 = playerTwo()

        p1name = p1.name
        p2name = p2.name
        
        matches.append((p1.move(HISTORY), p2.move(HISTORY)))
        
        for result in matches:
            pass

        
print(calculate())
