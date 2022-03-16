import pygame
from config import *
from player import Player
from projectile import Feather


class Ro(Player):
    # Constructor
    def __init__(self, x, y):
        super().__init__(x, y)
        self.COLOR = 'Gray'
        self.PROJECTILE_COOLDOWN = 22

    # Shoot
    def shoot(self, tx, ty):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.projectile_counter == self.PROJECTILE_COOLDOWN:
            self.projectiles.append(Feather(self.x, self.y, tx, ty))
            self.projectiles.append(Feather(self.x, self.y, tx, ty + 100))
            self.projectiles.append(Feather(self.x, self.y, tx, ty - 100))

        if self.projectile_counter >= self.PROJECTILE_COOLDOWN:
            self.projectile_counter = 0
        self.projectile_counter += 1
