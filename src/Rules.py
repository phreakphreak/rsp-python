from Choices import *


RULES = {
    ROCK: {
        "win":  [SCISSORS, LIZARD],
        "lose": [PAPER, SPOCK],
        "symbol":"RK"
    },

    PAPER: {
        "win":  [ROCK, SPOCK],
        "lose": [SCISSORS, LIZARD],
        "symbol":"PA"
    },

    LIZARD: {
        "win": [PAPER, SPOCK],
        "lose": [SCISSORS, ROCK],
        "symbol":"LZ"
    },
    SPOCK:{
        "win":  [ROCK, SCISSORS],
        "lose": [PAPER, LIZARD],
        "symbol":"SP"
    },
    SCISSORS: {
        "win":[PAPER, LIZARD],
        "lose": [ROCK, SPOCK],
        "symbol":"SC"
    }
}
