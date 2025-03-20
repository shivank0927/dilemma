import numpy as np
from strategy.strategies import strategy
import itertools


class Simulate:
    
    def __init__(self, rounds):
        self.rounds = rounds
    
# from mode import PvP, Simulation # two modes either simuPlayerlation or Player vs .
history = [1]
simulations = 10

i = 0
for simulation in range(simulations):
    
    instance = [s(history) for s in strategy]
    combination = itertools.combinations(strategy, 2) # combinations of each class in pairs
    for combo in combination:
        print(combo, "\n")
        
        for strat in instance:
            print(strat.get_move())

