import pygame
from config import *
from player import Player
from projectile import Star


class Drip(Player):
    # Constructor
    def __init__(self, x, y):
        super().__init__(x, y)
        self.COLOR = 'Yellow'
        self.PROJECTILE_COOLDOWN = 30

    # Shoot
    def shoot(self, tx, ty):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.projectile_counter == self.PROJECTILE_COOLDOWN:
            self.projectiles.append(Star(self.x, self.y, tx, ty))

        if self.projectile_counter >= self.PROJECTILE_COOLDOWN:
            self.projectile_counter = 0
        self.projectile_counter += 1
