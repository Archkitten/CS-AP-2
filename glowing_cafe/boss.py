import pygame
from config import *
from player import Player
from projectile import Bullet


class Boss(Player):
    # Constructor
    def __init__(self, x, y):
        super().__init__(x, y)
        self.RADIUS = 100
        self.PROJECTILE_COOLDOWN = 60

    # Move
    def move(self):
        pass

    # Shoot - Call all other "shoot" functions
    def shoot(self, tx, ty):
        self.shoot_spread(tx, ty)
        self.shoot_missiles(tx, ty)

        if self.projectile_counter >= self.PROJECTILE_COOLDOWN:
            self.projectile_counter = 0
        self.projectile_counter += 1

    def shoot_spread(self, tx, ty):
        if self.projectile_counter == self.PROJECTILE_COOLDOWN:
            self.projectiles.append(Bullet(self.x, self.y, tx, ty))
            self.projectiles.append(Bullet(self.x, self.y, tx, ty + 50))
            self.projectiles.append(Bullet(self.x, self.y, tx, ty - 50))
            self.projectiles.append(Bullet(self.x, self.y, tx, ty + 100))
            self.projectiles.append(Bullet(self.x, self.y, tx, ty - 100))

    def shoot_missiles(self, tx, ty):
        if self.projectile_counter == self.PROJECTILE_COOLDOWN / 2:
            self.projectiles.append(Bullet(self.x, self.y + 200, tx, ty))
            self.projectiles.append(Bullet(self.x, self.y - 200, tx, ty))
