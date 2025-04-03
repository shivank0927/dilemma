import itertools
from strategies import strategy
import pandas as pd

HISTORY = []

def combinations():

    return list(itertools.combinations(strategy, 2))

def calculate():
    
    pairs = combinations()
    matches = []
    dictionary = {}
    p1points = 0
    p2points = 0
    
    
    for _ in range(50): # later add the number of simulations for now 50 only.
        for playerOne, playerTwo in pairs:
            
            p1 = playerOne() 
            p2 = playerTwo()

            p1name = p1.name
            p2name = p2.name
            
            p1pts = 0
            p2pts = 0
            
            matches.append((p1.move(HISTORY), p2.move(HISTORY)))

            for points in matches:
                
                if points[0] == 0 and points[1] == 0:
                    pass # both defect
                
                elif points[0] == 1 and points[1] == 1: # both co-operate
                    
                    p1pts += 3
                    p2pts += 3
                
                elif points[1] == 0 and points[0] == 1:
                    
                    p1pts += 5 # reward the cheater
                    p2pts += 1 
                
                elif points[1] == 1 and points[0] == 0:
                    
                    p1pts += 1
                    p2pts += 5
                    
                else:
                    raise ValueError("error occured")
            
            

print(calculate())
