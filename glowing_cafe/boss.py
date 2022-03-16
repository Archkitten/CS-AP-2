import pygame
from config import *
from player import Player
from star import Star


class Boss(Player):
    # Constructor
    def __init__(self, x, y):
        super().__init__(x, y)
        self.RADIUS = 100
        self.PROJECTILE_COOLDOWN = 60

    # Move
    def move(self):
        pass

    # Shoot
    def shoot(self, tx, ty):
        if self.projectile_counter == self.PROJECTILE_COOLDOWN:
            self.projectiles.append(Star(self.x, self.y, tx, ty))
            self.projectiles.append(Star(self.x, self.y, tx, ty + 50))
            self.projectiles.append(Star(self.x, self.y, tx, ty - 50))
            self.projectiles.append(Star(self.x, self.y, tx, ty + 100))
            self.projectiles.append(Star(self.x, self.y, tx, ty - 100))

        if self.projectile_counter >= self.PROJECTILE_COOLDOWN:
            self.projectile_counter = 0
        self.projectile_counter += 1
