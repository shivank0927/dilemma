import random

class Strategies:
    def __init__(self, history):
        self.history = history

class TitForTat(Strategies):
    
    def __init__(self, history):
        super().__init__(history)
        
        self.name = "Tit for Tat"
    
    def get_move(self):
        
        if len(self.history) == 0 or self.history[-1] == 1:
            return 1
        return 0

class AlwaysCooperate(Strategies):
    
    def __init__(self, history):
        super().__init__(history)
        
        self.name = "Always Cooperate"
    
    def get_move(self):    
        
        return 1

class AlwaysDefect(Strategies):
    
    def __init__(self, history):
        super().__init__(history)
        
        self.name = "Always Defect"
    
    def get_move(self):
        
        return 0

class TitForTwoTats(Strategies):
    
    def __init__(self, history):
        super().__init__(history)
        
        self.name = "Tit for Two Tats"
    
    def get_move(self):
        
        if len(self.history) < 2:
            return 1 
        
        if self.history[-1] == 0 and self.history[-2] == 0:
            return 0
        
        return 1

class RandomChoice(Strategies): 
    
    def __init__(self, history):
        super().__init__(history)
        
        self.name = "Random"
    
    def get_move(self):
        
        return random.randint(0, 1)


class GrimTrigger(Strategies):
    
    def __init__(self, history):
        super().__init__(history)
        
        self.name = "Grim Trigger"
    
    def get_move(self):
        
        if 0 in self.history:
            return 0 
        return 1


strategy = [TitForTat, AlwaysCooperate, AlwaysDefect, TitForTwoTats, RandomChoice, GrimTrigger]