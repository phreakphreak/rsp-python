
from Player import *
from Rules import *
from Utils import *

data = readFile()


class Game:
    def __init__(self, number, player1: Player, player2: Player):
        self.number = number
        self.player1 = player1
        self.player2 = player2
        self.winner = None
        self.loser = None

    def Start(self):

        self.choice_player1 = self.player1.pickOut()
        self.choice_player2 = self.player2.pickOut()
        print(self.choice_player1, "player 1")
        print(self.choice_player2, "player 2")
        if(self.choice_player1 == self.choice_player2):
            print("Draw Empate")
            self.winner = None
            self.loser = None
            return
        if(self.choice_player1 in RULES[self.choice_player2]["win"]):
            (self.winner, self.loser) = (self.player2, self.player1)
        else:
            (self.winner, self.loser) = (self.player1, self.player2)

        print("The winner is: " + self.winner.name)
        return

    def getWinner(self):
        if (self.winner):
            return self.winner.name
        else:
            return "Draw"

    def getLoser(self):
        if (self.loser):
            return self.loser.name
        else:
            return "Draw"

    def Play(self):
        self.Start()

        global data

        self.result = {
            "id": self.number,
            "player1": {
                "name": self.player1.name,
                "id": self.player1.id,
                },
            "player2": self.player2.name,
            "winner": self.getWinner(),
            "loser": self.getLoser(),
            "score": self.getScore()
        }
        data["games"].append(self.result)
        writeFile(data)
        return self.getWinner()

    def getScore(self):
        if(self.getWinner() == "Draw"):
            return {"player1": 0.5, "player2": 0.5}
        if(self.getWinner() == self.player1.name):
            return {"player1": 1, "player2": 0}
        else:
            return {"player1": 0, "player2": 1}


game1 = Game(1, Player(RandomStrategy(), "Player 1"),
             Player(RandomStrategy(), "Player 2"))

game1.Play()
