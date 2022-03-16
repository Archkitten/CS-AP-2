import pygame
from config import *
from player import Player
from projectile import Goop


class Blob(Player):
    # Constructor
    def __init__(self, x, y):
        super().__init__(x, y)
        self.SPEED = 5
        self.SLOW_PERCENT = 0.8
        self.COLOR = 'Purple'

        self.PROJECTILE_COOLDOWN = 10

        self.KEY_SHOOT = pygame.K_SPACE
        self.KEY_LEFT = pygame.K_LEFT
        self.KEY_RIGHT = pygame.K_RIGHT
        self.KEY_UP = pygame.K_UP
        self.KEY_DOWN = pygame.K_DOWN

    # Shoot
    def shoot(self, tx, ty):
        keys = pygame.key.get_pressed()
        if keys[self.KEY_SHOOT] and self.projectile_counter == self.PROJECTILE_COOLDOWN:
            self.projectiles.append(Goop(self.x, self.y, tx, ty))

        if self.projectile_counter >= self.PROJECTILE_COOLDOWN:
            self.projectile_counter = 0
        self.projectile_counter += 1
