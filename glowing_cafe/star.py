import pygame
import math
from config import *

class Star:
    # Constructor
    def __init__(self, x, y, mx, my):
        self.x = x
        self.y = y
        self.RADIUS = 5
        self.SPEED = 10
        self.circle = (self.x, self.y)

        # Big Math Stuff
        angle = math.atan2(my - y, mx - x)
        self.dx = math.cos(angle) * self.SPEED
        self.dy = math.sin(angle) * self.SPEED

    # Main - Run all other functions.
    def main(self, screen):
        self.move()
        self.circle = (self.x, self.y)
        pygame.draw.circle(screen, 'Yellow', self.circle, self.RADIUS)

    # Move
    def move(self):
        self.x += self.dx
        self.y += self.dy
        # self.x = int(self.x)
        # self.y = int(self.y)
