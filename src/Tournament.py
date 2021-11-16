

from Utils import *
from Player import *
from Strategies import *
from Game import *




class Tournament:
    def __init__(self, name="RSPLP", rounds=10, matches=[]):
        self.name = name
        self.players = self.initializePlayers()
        self.counter = 0
        self.rounds = rounds
        self.matches = matches

    def initializePlayers(self):
        playersData = readFile("src/players.json")
        players = []
        for item in playersData["players"]:
            initial_strategy = item["strategy"]
            next_strategy = item["next_strategy"]
            player = Player(
                STRATEGIES[item["strategy"]](), initial_strategy, next_strategy, item["id"], item["name"], item["elo"], item["constant"])
            players.append(player)
        return players

    def LoadPlayers(self):
        playersData = readFile("src/players.json")
        players = []
        for item in playersData["players"]:
            initial_strategy = item["strategy"]
            next_strategy = item["next_strategy"]
            player = Player(
                STRATEGIES[item["next_strategy"]](), initial_strategy, next_strategy, item["id"], item["name"], item["elo"], item["constant"])

            player.stats.wins = item["stats"]["wins"]
            player.stats.losses = item["stats"]["losses"]
            player.stats.draws = item["stats"]["draws"]
            player.stats.total_points = item["stats"]["total_points"]
            player.stats.games = item["stats"]["games"]
            player.stats.rating = item["stats"]["rating"]

            players.append(player)
        return players

    def createVersus(self):
        count = 1
        for i in self.players:
            for j in self.players:
                if i != j:
                    if(self.ifExists(i, j)):
                        self.matches.append(Game(count, i, j))
                    count += 1

    def ifExists(self, player1, player2):
        for i in self.matches:
            arr = [i.player1.id, i.player2.id]
            if player1.id in arr and player2.id in arr:
                return False
        return True

    def Start(self):
        for i in self.matches:
            i.Play()

    def getRating(self):
        dataPlayers = readFile("src/players.json")
        rating = []
        for i in dataPlayers["players"]:
            wins = i["stats"]["wins"]
            losses = i["stats"]["losses"]
            draws = i["stats"]["draws"]
            elo = i["elo"]
            name = i["name"]
            rating.append({"name": name, "elo": elo, "wins": wins, "losses": losses, "draws": draws})
        rating.sort(key=lambda item:item['elo'], reverse=True)
        
        ratingData = readFile("src/rating.json")
        ratingData["rating"] = rating
        writeFile(ratingData, "src/rating.json")

tornament = Tournament()
tornament.createVersus()
tornament.Start()

tornament.getRating()