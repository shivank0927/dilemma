import itertools
from strategies import strategy
import pandas as pd

HISTORY = []

def combinations():

    return list(itertools.combinations(strategy, 2))

def calculate():
    
    pairs = combinations()
    results = {}

    for _ in range(50): # later add the number of simulations for now 50 only. OR CALL THIS IN ANOTHER FUNC.
        matches = []
        p1pts, p2pts = 0, 0
        
        for playerOne, playerTwo in pairs:

            p1 = playerOne() 
            p2 = playerTwo()
            
            p1name = p1.name
            p2name = p2.name
            
            results["strategy A"] = p1name
            results["strategy B"] = p2name
            
            matches.append((p1.move(HISTORY), p2.move(HISTORY)))

            for points in matches:
                
                if points[0] == 0 and points[1] == 0:
                    results["status (A)"] = "defected" # both defect
                    results["status (B)"] = "defected" 
                    
                elif points[0] == 1 and points[1] == 1: # both co-operate
                    
                    p1pts += 3
                    p2pts += 3
                    results["status (A)"] = "co-operated" 
                    results["status (B)"] = "co-operated" 
                
                elif points[0] == 0 and points[1] == 1:
                    
                    results["status (A)"] = "defected" 
                    results["status (B)"] = "co-operated" 
                    
                    p1pts += 5 # reward the cheater
                    p2pts += 1 
                
                elif points[1] == 1 and points[0] == 0:
                    
                    results["status (A)"] = "co-operated" 
                    results["status (B)"] = "defected" 
                    p1pts += 1
                    p2pts += 5
                    
                else:
                    rest=9
                
                HISTORY.append((p1.move(HISTORY), p2.move(HISTORY)))
                
    return results # append results to some other list

dictionary = calculate()

df = pd.DataFrame(data=dictionary)
print(df)
