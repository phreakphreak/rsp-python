
from IStrategy import *
from Strategies import *
from Choices import *


class Stats:
    def __init__(self):
        self.draws = 0
        self.wins = 0
        self.losses = 0
        self.total_points = 0
        self.games = []
        self.rating = []


class Player():
    def __init__(self, strategy: IStrategy, id, name, elo=800, constant=None) -> None:
        self.id = str(id)
        self.constant = constant
        self._strategy = strategy
        self.choices = CHOICES
        self.name = name
        self.elo = elo
        self.old_elo = elo
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
        result = self._strategy.do_algorithm(
            self.choices, last_game, self.constant)
        return result

    def toJSON(self) -> dict:
        return{
            "id": self.id,
            "name": self.name,
            "elo": self.elo,
            "strategy": self._strategy.__str__(),
            "next_strategy": "constant",
            "constant": self.constant,
            "stats": {
                "wins":self.stats.wins,
                "losses":self.stats.losses,
                "draws":self.stats.draws,
                "total_points":self.stats.total_points,
                "games":self.stats.games,
                "rating":self.stats.rating
            }
        }
