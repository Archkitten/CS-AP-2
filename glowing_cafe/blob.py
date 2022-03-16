import pygame
from config import *
from player import Player
from projectile import Goop


class Blob(Player):
    # Constructor
    def __init__(self, x, y):
        super().__init__(x, y)
        self.COLOR = 'Purple'
        self.PROJECTILE_COOLDOWN = 10

    # Shoot
    def shoot(self, tx, ty):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.projectile_counter == self.PROJECTILE_COOLDOWN:
            self.projectiles.append(Goop(self.x, self.y, tx, ty))

        if self.projectile_counter >= self.PROJECTILE_COOLDOWN:
            self.projectile_counter = 0
        self.projectile_counter += 1
