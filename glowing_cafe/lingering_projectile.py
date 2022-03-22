import pygame
from config import *


class LingeringProjectile:
    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.RADIUS = 5
        self.duration = 60
        self.COLOR = 'White'
        self.circle = (self.x, self.y)

    # Main - Run all other functions.
    def main(self, screen):
        self.countdown()
        self.circle = (self.x, self.y)
        pygame.draw.circle(screen, self.COLOR, self.circle, self.RADIUS)

    def countdown(self):
        self.duration -= 1
        if self.duration == 0:
            self.x = -20
            self.y = -20
