from IStrategy import IStrategy
from Utils import *
from Rules import *


import random

#TODO Son 11 tipos de jugadores , y son 10 rounds, cada uno de los 11 jugadores juega contra los otros 10 y esto lo repites 100 veces

# * Jugar siempre lo mismo
class ConstantStrategy(IStrategy):
    def do_algorithm(self, data, last_game=None, constant=None) -> str:
        self.choice = self.constant
        return self.choice

# * Jugar al azar
class RandomStrategy(IStrategy):
    def do_algorithm(self, data, last_game=None, constant=None) -> str:
        self.choice = random.choice(data)
        return self.choice
    def __str__(self):
        return "random"

# * Jugar siempre lo que tiró el contrario en el juego anterior
class OppositeStrategy(IStrategy):
    def do_algorithm(self, data: list, last_game=None, constant=None) -> str:
        self.choice = last_game["choice_opponent"]
        return self.choice


# * Jugar lo mismo si ganó, jugar lo que tiró el contrario si perdió
class SameIfWinStrategy(IStrategy):
    def do_algorithm(self, data: list, last_game=None, constant=None) -> str:
        if(last_game["status"] == 'victory'):
            self.choice = last_game['choice_player']
            return self.choice
        else:
            self.choice = last_game["choice_opponent"]
            return self.choice

# * Jugar lo mismo si perdió, jugar lo que tiró el contrario si ganó


class SameIfLoseStrategy(IStrategy):
    def do_algorithm(self, data: list, last_game=None, constant=None) -> str:
        if(last_game["status"] == 'loss'):
            self.choice = last_game['choice_player']
            return self.choice
        else:
            self.choice = last_game['choice_opponent']
            return self.choice

# * Jugar lo que derrotaría a la elección anterior del adversario


class WinOpponentPreviousChoiceStrategy(IStrategy):
    def do_algorithm(self, data: list, last_game=None, constant=None) -> str:
        arr = RULES[last_game["choice_opponent"]]["lose"]
        self.choice = random.choice(arr)
        return self.choice

# * Jugar lo sería derrotado dada la elección anterior del adversario


class LoseOpponentPreviousChoiceStrategy(IStrategy):
    def do_algorithm(self, data: list, last_game=None, constant=None) -> str:
        arr = RULES[last_game["choice_opponent"]]["win"]
        self.choice = random.choice(arr)
        return self.choice


# * Jugar suponiendo que el adversario sigue un ciclo (i.e. R, S, P, R, S, P,... )


class PatternOpponentStrategy(IStrategy):
    def gen(pattern_opponent):
        def init():
            return 0
        i = init()

        while True:
            val = (yield pattern_opponent[i])
            if val == "restart":
                i = init()
            else:
                i += 1

    def do_algorithm(self, data: list, last_game=None, constant=None) -> str:
        self.last = "";
        self.pattern_opponent = ["RK", "SC", "PA", "LZ", "SP"]
        g = self.gen(self.pattern_opponent)
        value = ""
        if(self.last == self.pattern_opponent[len(self.pattern_opponent)-1]):
            value = g.send("restart")
        else:
            value = g.__next__()
        x = find(lambda x: RULES[x]["symbol"] == value, RULES)
        choice = random.choice(RULES[x]["lose"])
        self.last = value
        return choice


STRATEGIES = {
    "constant": ConstantStrategy,
    "random":RandomStrategy,
    "oppsite":OppositeStrategy,
    "sameIfWin":SameIfWinStrategy,
    "sameIfLose":SameIfLoseStrategy,
    "winOpponentPreviousChoice":WinOpponentPreviousChoiceStrategy,
    "loseOpponentPreviousChoice":LoseOpponentPreviousChoiceStrategy,
    "patternOpponent":PatternOpponentStrategy
}


# def gen(pattern_opponent):

#     def init():
#         return 0
#     i = init()

#     while True:

#         val = (yield pattern_opponent[i])
#         if val == "restart":
#             i = init()
#         else:
#             i += 1


# pattern_opponent = ["RK", "SC", "PA", "LZ", "SP"]
# g = gen(pattern_opponent)

# last = ""


# def test():
#     global last
#     value = ""
#     if(last == pattern_opponent[len(pattern_opponent)-1]):
#         value = g.send("restart")
#     else:
#         value = g.__next__()
#     x = find(lambda x: RULES[x]["symbol"] == value, RULES)
#     choice = random.choice(RULES[x]["lose"])
#     last = value
#     print(choice)
#     return choice
