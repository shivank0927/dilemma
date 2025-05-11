import itertools
import pandas as pd
import random
import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # no idea

from strategies.strategy import strategy_list


def combinations():
    return list(itertools.combinations(strategy_list, 2))


def noise(x):
    return x + random.uniform(-0.5, 0.5)


def calcpoints(p1: int, p2: int):
    lookup = {
        (0, 0): (0, 0),
        (0, 1): (5, 1),
        (1, 0): (1, 5),
        (1, 1): (3, 3)
    }

    base = lookup[(p1, p2)]
    return (noise(base[0]), noise(base[1])) 


def calculate(counter_sim, rounds=random.randint(1, 1000)): # random rounds for noisy env
    results = []
    pairs = combinations()

    try:
        for i, j in pairs:
            result = {}
            HISTORY = []
            p1, p2 = i(), j()

            p1name, p2name = p1.name, p2.name
            p1pts, p2pts = 0, 0

            for _ in range(rounds): 
                p1move = p1.move(HISTORY)
                p2move = p2.move(HISTORY)
                HISTORY.append([p1move, p2move])

                points = calcpoints(p1move, p2move)
                p1pts += points[0]
                p2pts += points[1]

            result["player A"] = p1name
            result["player B"] = p2name

            result["A's point"] = int(p1pts)
            result["B's point"] = int(p2pts)
 
            result["result"] = int(p1pts + p2pts)
            result["simulation"] = counter_sim

            results.append(result)

        return results

    except Exception as e:
        exit(e)


def result_msg(row):
    if row["A's point"] > row["B's point"]: # adding win msg
        return "A wins"
    elif row["A's point"] < row["B's point"]:
        return "B wins"
    else:
        return "Draw"


def simulations(simulation: int):
    final_result = []

    for sim_num in range(1, simulation + 1):
        result = calculate(sim_num)
        final_result.extend(result)

    frame = pd.DataFrame(data=final_result)

    merged = frame.groupby(["simulation", "player A", "player B"], as_index=False).agg({ # grouping rounds. with no index
        "A's Score": "sum",
        "B's Score": "sum"
    }) 

    merged = merged.drop("simulation", axis=1) # ...
    merged["result"] = merged.apply(result_msg, axis=1)

    return merged


