import pygame
from config import *
from player import Player
from projectile import Bullet, LingeringBullet, HorizontalBullet


class Boss(Player):
    # Constructor
    def __init__(self, x, y):
        super().__init__(x, y)
        self.RADIUS = 120
        self.PROJECTILE_COOLDOWN = 60

        self.health = 105
        self.MAX_HEALTH = 105
        self.uses_health_bar = True
        self.HEALTH_BAR_POSITION = 1

    # Move
    def move(self, keys):
        pass

    # Shoot - Call all other "shoot" functions
    def shoot(self, tx, ty, keys):
        # First Phase - Intro 0:00
        if self.health <= 104 + 1 and self.health > 92 + 1:
            self.starry_night()
        # Second Phase - Speak 0:13
        elif self.health <= 92 + 1 and self.health > 86 + 1:
            pass
        # Third Phase - Sing 0:19
        elif self.health <= 86 + 1 and self.health > 73 + 1:
            self.shoot_missiles(tx, ty)
        # Fourth Phase - Rap 0:32
        elif self.health <= 73 + 1 and self.health > 61 + 1:
            self.shoot_spread(tx, ty)
        # Fifth Phase - Sing 0:44
        elif self.health <= 61 + 1 and self.health > 48 + 1:
            self.shoot_missiles(tx, ty)
        # Sixth Phase - All Together 0:57
        elif self.health <= 48 + 1 and self.health > 35 + 1:
            self.starry_night()
            self.shoot_missiles(tx, ty)
        # Seventh Phase - All Together 1:10
        elif self.health <= 35 + 1 and self.health > 21 + 1:
            self.starry_night()
            self.shoot_missiles(tx, ty)
            self.shoot_spread(tx, ty)
        # Eighth Phase - Concerto 1:23
        elif self.health <= 21 + 1 and self.health > 7 + 1:
            self.outer_wall()
            i = 0
            while i <= 10:
                self.starry_night()
                i += 1
        # Last Phase - Outro 1:38
        elif self.health <= 7 + 1:
            pass

        if self.projectile_counter >= self.PROJECTILE_COOLDOWN:
            self.projectile_counter = 0
        self.projectile_counter += 1

    def starry_night(self):
        if self.projectile_counter == 10 or self.projectile_counter == 40:
            self.projectiles.append(HorizontalBullet(WIN_WIDTH))

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
        if self.projectile_counter == self.PROJECTILE_COOLDOWN:
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
