import random

class TitForTat:
    def __init__(self):
        self.name = "tit for tat"
    
    def move(self, history: list):
        
        if not history: # the very first move
            return 1
        
        if history[-1] == 0: # checks for the last move
            return 0
        else:
            return 1
class GrimTrigger:
    def __init__(self):
        self.name = "grim trigger"
    
    def move(self, history: list):
        
        if not history:
            return 1
        
        if 0 in history:
            return 0
        
        return 1
class Random:
    def __init__(self):
        self.name = "random"
    
    def move(self, history: list):
        
        return random.randint(0, 1)
class AlwaysCooperate:
    def __init__(self):
        self.name = "always cooperate"
    
    def move(self, history: list):
        return 1

class AlwaysDefect:
    def __init__(self):
        self.name = "always defect"
    
    def move(self, history: list):
        return 0
    
    
strategy = [TitForTat, AlwaysCooperate, AlwaysDefect, Random, GrimTrigger]
