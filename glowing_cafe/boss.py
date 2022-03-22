import pygame
from config import *
from player import Player
from projectile import Bullet, LingeringBullet


class Boss(Player):
    # Constructor
    def __init__(self, x, y):
        super().__init__(x, y)
        self.RADIUS = 120
        self.PROJECTILE_COOLDOWN = 60

        self.health = 120
        self.MAX_HEALTH = 120
        self.uses_health_bar = True
        self.HEALTH_BAR_POSITION = 1

        self.outer_wall_exists = False

    # Move
    def move(self):
        pass

    # Shoot - Call all other "shoot" functions
    def shoot(self, tx, ty):
        if self.health < 90:
            self.shoot_spread(tx, ty)
        if self.health < 60 or self.health > 90:
            self.shoot_missiles(tx, ty)
        if self.health < 30 and self.outer_wall_exists == False:
            self.outer_wall()
            self.outer_wall_exists = True

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

    def outer_wall(self):
        horizontal = WIN_WIDTH
        vertical = WIN_HEIGHT
        while horizontal >= 0:
            self.projectiles.append(LingeringBullet(horizontal, 10))
            self.projectiles.append(LingeringBullet(horizontal, WIN_HEIGHT - 10))
            horizontal -= 40
        while vertical >= 0:
            self.projectiles.append(LingeringBullet(10, vertical))
            self.projectiles.append(LingeringBullet(WIN_WIDTH - 10, vertical))
            vertical -= 40
