import pygame
from collections import namedtuple
pygame.init()
font = pygame.font.Font('arial.ttf', 25)

Ball = namedtuple('Ball', 'x, y')
# colours
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Pong():
    def __init__(self, width=1000, height=600, radius=15):
        self.width = width
        self.height = height
        # init display
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pong Game")
        self.clock = pygame.time.clock()

        # set pong ball
        self.radius = radius
        
        # init game
        