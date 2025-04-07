import itertools
from strategies import strategy
import pandas as pd

HISTORY = []

def calcpoints(p1, p2):
    lookup = {
        (0, 0): (0, 0),
        (0, 1): (5, 1),
        (1, 0): (1, 5),
        (1, 1): (3, 3)
    }
    
    return lookup[(p1, p2)] # the issue is how to return cooperate or defect msg? for the dataframe in lates!

    
def combinations():

    return list(itertools.combinations(strategy, 2))

def calculate():

    try:
        result = {}
        pairs = combinations() # 10 combinations

        for i, j in pairs:

            p1, p2 = i(), j() # instantiating class!

            p1name, p2name = p1.name, p2.name
            p1pts, p2pts = 0, 0
            p1move, p2move = p1.move(HISTORY), p2.move(HISTORY)
            HISTORY.append([p1move, p2move])

            result["player A"] = p1name
            result["player B"] = p2name
            
            
            points = calcpoints(p1move, p2move)
            
            # result["A's move": "co-opertae"] 
        return result

    except Exception as e:
        print(e)

def simulations(simulation: int):
    final_result = []

    for _ in range(simulation):

        result = calculate()
        final_result.append(result)

    return final_result


result_simulation = simulations(1)
print(result_simulation) # 1 loop for now atelast 

# df = pd.DataFrame(data=result_simulation)
# print(df)
