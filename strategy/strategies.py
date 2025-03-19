import numpy as np

class Strategies:
    
    def __init__(self, last_move):
        
        self.last_move = True
    
class TitForTat(Strategies):
    
    def __init__(self, last_move):
    
        self.name = "Tit for Tat"

class AlwaysCooperate(Strategies):
    
    def __init__(self, last_move):
        
        self.name = "Always Co-operate"

class AlwaysDefect(Strategies):
    
    def __init__(self, last_move):
        
        self.name = "Always Defect"


class TitForTwoTats(Strategies):
    
    def __init__(self, last_move):
        
        self.name = "Tit for Two Tats"

class Random(Strategies):
    
    def __init__(self, last_move):
        
        self.name = "Random"


class Spiteful(Strategies):
    
    def __init__(self, last_move):
        
        self.name = "Spiteful"

        
class PavLov(Strategies):
    
    def __init__(self, last_move):
        
        self.name = "PavLov"


class GrimTrigger(Strategies):
    
    def __init__(self, last_move):
        
        self.name = "Grim Trigger"

