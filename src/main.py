
from Utils import *
from Player import *
from Strategies import *


def getPlayers():
    data = readFile("src/players.json")
    players = []
    for item in data["players"]:
        strategy = STRATEGIES[item["strategy"]]
        player = Player(strategy(), item["name"])
        players.append(player)
    return players


res =  getPlayers();

for i in res:
    print(i.name, i.id,i.pickOut())
    