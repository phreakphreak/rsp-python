

from Player import *
from Rules import *
from Utils import *
data = readFile()
playersData =readFile("src/players.json")

class Game:
    def __init__(self, number, player1: Player, player2: Player):
        self.number = number
        self.player1 = player1
        self.player2 = player2
        self.winner: Player = None
        self.loser: Player = None
        self.result = None

    def calculate_new_rating(self, player_rating, opponent_rating, result):
        K = 32
        expected_score_a = self.calculate_expected_score(
            player_rating, opponent_rating)
        new_rating_a = player_rating + K * (result - expected_score_a)
        return new_rating_a

    def calculate_expected_score(self, player_rating, opponent_rating):
        expected_score_a = 1 / \
            (1 + 10 ** ((opponent_rating - player_rating) / 400))
        return expected_score_a

    def getRating(self, player: Player, opponent: Player, result):
        elo = self.calculate_new_rating(player.elo, opponent.elo, result)
        expected_score = self.calculate_expected_score(
            player.elo, opponent.elo)
        return {
            "elo": round(elo),
            "expected_score": round(expected_score, 3),
        }

    def Draw(self):
        result = 0.5
        self.player1.elo = self.getRating(
            self.player1, self.player2, result)["elo"]
        self.player2.elo = self.getRating(
            self.player2, self.player1, result)["elo"]
        self.player1.stats.draws += 1
        self.player2.stats.draws += 1
        self.player1.stats.total_points += result
        self.player2.stats.total_points += result

    def calcStats(self):
        self.winner.elo = self.getRating(self.winner, self.loser, 1)["elo"]
        self.loser.elo = self.getRating(self.loser, self.winner, 0)["elo"]
        self.winner.stats.wins += 1
        self.loser.stats.losses += 1
        self.winner.stats.total_points += 1
        self.loser.stats.total_points += 0
        return

    def Start(self):
        self.choice_player1 = self.player1.pickOut()
        self.choice_player2 = self.player2.pickOut()
        print(self.choice_player1, "player 1: ", self.player1.name)
        print(self.choice_player2, "player 2: ", self.player2.name)
        if(self.choice_player1 == self.choice_player2):
            self.winner = None
            self.loser = None
            self.Draw()
        elif(self.choice_player1 in RULES[self.choice_player2]["win"]):
            self.winner = self.player2
            self.loser = self.player1
            self.calcStats()
        else:
            self.winner = self.player1
            self.loser = self.player2
            self.calcStats()

        print(self.player1.elo, "P1")
        print(self.player2.elo, "P2")
        if(self.winner):
            print("Winner: ", self.winner.name)
        else:
            print("Draw")

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
        global playersData

        self.result = self.getResult()

        self.player1.stats.games.append(self.result["player1"])
        self.player2.stats.games.append(self.result["player2"])
        P1 = find(lambda x: x["id"] == self.player1.id, playersData["players"])
        P2 = find(lambda x: x["id"] == self.player2.id, playersData["players"])
        index1 = playersData["players"].index(P1)
        index2 = playersData["players"].index(P2)

        playersData["players"][index2] = self.player2.toJSON()
        playersData["players"][index1] = self.player1.toJSON()

        data["games"].append(self.result)
        writeFile(data)
        writeFile( playersData,"src/players.json")
        return self.getWinner()

    def getStatus(self, player):
        if(self.winner is not None):
            if(self.winner.id == player.id):
                return "victory"
            else:
                return "loss"
        else:
            return "draw"

    def getScore(self):
        if(self.getWinner() == "Draw"):
            self.score = {"player1": 0.5, "player2": 0.5}
        elif(self.getWinner() == self.player1.name):
            self.score = {"player1": 1, "player2": 0}
        else:
            self.score = {"player1": 0, "player2": 1}
        return self.score

    def getResult(self):
        return {
            "id": self.number,
            "player1": {
                "game_id": self.number,
                "status": self.getStatus(self.player1),
                "id": self.player1.id,
                "name": self.player1.name,
                "choice_player": self.choice_player1,
                "choice_opponent": self.choice_player2,
                "elo": self.player1.old_elo,
                "expected_score": self.calculate_expected_score(self.player1.elo, self.player2.elo),
                "score": self.getScore()["player1"]
            },
            "player2": {
                "game_id": self.number,
                "status": self.getStatus(self.player2),
                "id": self.player2.id,
                "name": self.player2.name,
                "choice_player": self.choice_player2,
                "choice_opponent": self.choice_player1,
                "elo":self.player2.old_elo,
                "expected_score": self.calculate_expected_score(self.player2.elo, self.player1.elo),
                "score": self.getScore()["player2"]
            },
            "winner": self.getWinner(),
            "loser": self.getLoser(),
            "score": self.getScore()
        }

