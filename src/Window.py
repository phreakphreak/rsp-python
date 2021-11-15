
from turtle import width
import pygame
import random

lizard = pygame.image.load(r'assets/lizard.png')
spock = pygame.image.load(r'assets/spock.png')
scissors = pygame.image.load(r'assets/scissors.png')
rock = pygame.image.load(r'assets/rock.png')
paper = pygame.image.load(r'assets/paper.png')

choices = [lizard, spock, scissors, rock, paper]

def random_choice():
    return choices[random.randint(0, choices.__len__() - 1)]

class RandomStrategy:    
    @staticmethod
    def get_choice(self):
        return random_choice()
    


class Window():
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.title = pygame.display.set_caption("RSPLP")
        self.backcolor = (0, 0, 0)
        self.__init__properties()

    def __init__properties(self):
        self.screen.fill(self.backcolor)
        pygame.display.update()

    def play(self):
        while True:
            self.screen.fill(self.backcolor)
            self.screen.blit(lizard, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                pygame.display.update()



wn = Window(500, 500)

wn.play()