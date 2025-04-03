import random

class TitForTat:
    def __init__(self):
        self.name = "tit for tat"
    
    def move(self, history: list):
        if not history:  # The very first move
            return 1
        return 0 if 0 in history[-1] else 1


class GrimTrigger:
    def __init__(self):
        self.name = "grim trigger"
    
    def move(self, history: list):
        if not history:
            return 1
        
        opponent_moves = [i[0] for i in history]
        return 0 if 0 in opponent_moves else 1


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

# if __name__ == "__main__":
#     pass
