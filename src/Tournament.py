
import pandas as pd
from Utils import *
from Player import *
from Strategies import *
from Game import *

gamesData = readFile();
playersData = readFile("src/players.json");
ratingPlayers = readFile("src/rating.json");
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
        for match in self.matches:
            result = match.Play()
            self.addGame(result)

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

    def addGame(self, game_result):
        data = readFile()
        data["games"].append(game_result)
        writeFile(data, "src/data.json")
        return True
    
    


tornament = Tournament()
tornament.createVersus()
tornament.Start()

tornament.getRating()



def showRating():
    rating = readFile("src/rating.json")
    elo = []
    wins = []
    losses = []
    name = []
    draws = []
    for i in rating["rating"]:
        elo.append(i["elo"])
        wins.append(i["wins"])
        losses.append(i["losses"])
        name.append(i["name"])
        draws.append(i["draws"])
    df = pd.DataFrame.from_dict({"name": name, "elo": elo, "wins": wins, "losses": losses, "draws": draws})
    
    print(df)

showRating()