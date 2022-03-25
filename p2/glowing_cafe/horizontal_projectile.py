import pygame
import random
from config import *

class HorizontalProjectile:
    # Constructor
    def __init__(self, x):
        self.x = x
        self.y = random.randint(0, WIN_HEIGHT)
        self.RADIUS = 5
        self.SPEED = 9
        self.COLOR = 'White'
        self.circle = (self.x, self.y)

    # Main - Run all other functions.
    def main(self, screen):
        self.move()
        self.circle = (self.x, self.y)
        pygame.draw.circle(screen, self.COLOR, self.circle, self.RADIUS)
        self.animate(screen)

    # Move
    def move(self):
        self.x += self.SPEED

    # Animate
    def animate(self, screen):
        pass
