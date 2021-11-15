
from IStrategy import *
from Strategies import *
from Choices import *
import uuid




class Stats:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.total_points = 0
        self.games = []


class Player():
    def __init__(self, strategy: IStrategy, name, elo=800, constant=None) -> None:
        self.id = 1
        self.constant = constant
        self._strategy = strategy
        self.choices = CHOICES
        self.name = name
        self.elo = elo
        self.stats = Stats()

    @property
    def strategy(self) -> IStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: IStrategy) -> None:
        self._strategy = strategy

    def pickOut(self) -> None:
        length = len(self.stats.games)
        last_game = self.stats.games[length-1] if length > 0 else {}
        result = self._strategy.do_algorithm(self.choices, last_game, self.constant)
        return result


if __name__ == "__main__":
    context = Player(RandomStrategy(), "Random")
    print("Client: Strategy is set to normal sorting.")
    context.pickOut()
    print(context.pickOut())

    context.strategy = ConstantStrategy(ROCK)
    print(context.pickOut())

    # print("Client: Strategy is set to reverse sorting.")
    # context.strategy = ConcreteStrategyB()
    # context.do_some_business_logic()
