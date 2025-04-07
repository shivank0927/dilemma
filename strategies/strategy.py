import random

class Strategy: # base class

    def __init__(self, name: str):
        self.name = name

    def move(self, history: list):
        raise NotImplementedError("error occured")


class TitForTat(Strategy):

    def __init__(self):
        super().__init__("tit for tat")
    
    def move(self, history: list): 
        if not history: # very first move
            return 1
        return 0 if 0 in history[-1] else 1


class GrimTrigger(Strategy):

    def __init__(self):
        super().__init__("grim trigger")
    
    def move(self, history: list):
        if not history:
            return 1
        opponent_moves = [i[1] for i in history]
        if 0 in opponent_moves:
            return 0
        else:
            return 1

class Random(Strategy):

    def __init__(self):
        super().__init__("random")
    
    def move(self, history: list):
        return random.randint(0, 1)


class AlwaysCooperate(Strategy):

    def __init__(self):
        super().__init__("always cooperate")
    
    def move(self, history: list):
        return 1


class AlwaysDefect(Strategy):

    def __init__(self):
        super().__init__("always defect")
    
    def move(self, history: list):
        return 0


class TitForTwoTats(Strategy):

    def __init__(self):
        super().__init__("tit for two tats")
    
    def move(self, history: list):
        if len(history) < 2:
            return 1

        if history[-1][1] == 0 and history[-2][1] == 0:

            return 0
        return 1


class SuspiciousTitForTat(Strategy):

    def __init__(self):
        super().__init__("suspicious tit for tat")
    
    def move(self, history: list):

        if not history:
            return 0
        return 0 if 0 in history[-1] else 1


class Joss(Strategy):

    def __init__(self):
        super().__init__("joss")
    
    def move(self, history: list):
        if not history:
            return 1
        if 0 in history[-1]:
            return 0
        return 0 if random.randint(1, 6) == 4 else 1 # 1/6 chance to defect despite other player being cooperative


strategy_list = [TitForTat, AlwaysCooperate, AlwaysDefect, Random, GrimTrigger, TitForTwoTats, SuspiciousTitForTat, Joss]
