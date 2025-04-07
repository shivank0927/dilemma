import itertools
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # root path or smth
from strategies.strategy import strategy_list

    
def combinations():

    return list(itertools.combinations(strategy_list, 2))

def calcpoints(p1, p2):
    lookup = {
        (0, 0): (0, 0),
        (0, 1): (5, 1),
        (1, 0): (1, 5),
        (1, 1): (3, 3)
    }
    
    return lookup[(p1, p2)] 


def calculate(counter_sim, rounds=20):
    results = []
    pairs = combinations()

    try:
        for i, j in pairs:
            result = {}
            HISTORY = []
            p1, p2 = i(), j() # single instances 

            p1name, p2name = p1.name, p2.name
            p1pts, p2pts = 0, 0

            for _ in range(rounds): # multiple rounds per simulation
                p1move = p1.move(HISTORY)
                p2move = p2.move(HISTORY)
                HISTORY.append([p1move, p2move])

                points = calcpoints(p1move, p2move)
                p1pts += points[0]
                p2pts += points[1]

            result["player A"] = p1name
            result["player B"] = p2name

            result["A's point"] = p1pts
            result["B's point"] = p2pts

            result["result"] = p1pts + p2pts
            result["simulation"] = counter_sim # adding simulation counter to filter and add pts. later

            results.append(result)

        return results

    except Exception as e:
        print(e)


def simulations(simulation: int):
    final_result = []

    for sim_num in range(1, simulation + 1):
        
        result = calculate(sim_num)
        final_result.extend(result) # flattening list for dataframe

    return final_result

