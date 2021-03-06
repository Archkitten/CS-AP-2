import pygame
from config import *
from player import Player
from projectile import Feather


class Ro(Player):
    # Constructor
    def __init__(self, x, y):
        super().__init__(x, y)
        self.SPEED = 7
        self.SLOW_PERCENT = 0.5
        self.COLOR = 'Gray'

        self.PROJECTILE_COOLDOWN = 22

        self.KEY_SHOOT = pygame.K_m
        self.KEY_LEFT = pygame.K_g
        self.KEY_RIGHT = pygame.K_j
        self.KEY_UP = pygame.K_y
        self.KEY_DOWN = pygame.K_h

        self.health = 2
        self.MAX_HEALTH = 2
        self.HEALTH_BAR_POSITION = 4

    # Shoot
    def shoot(self, tx, ty, keys):
        if keys[self.KEY_SHOOT] and self.projectile_counter == self.PROJECTILE_COOLDOWN:
            self.projectiles.append(Feather(self.x, self.y, tx, ty))
            self.projectiles.append(Feather(self.x, self.y, tx, ty + 100))
            self.projectiles.append(Feather(self.x, self.y, tx, ty - 100))

        if self.projectile_counter >= self.PROJECTILE_COOLDOWN:
            self.projectile_counter = 0
        self.projectile_counter += 1

    # Ghost Animate
    def ghost_animate(self, screen):
        pygame.draw.rect(screen, self.COLOR, (self.x - self.RADIUS / 1.5, self.y - self.RADIUS / 1.5,
                                              self.RADIUS * 1.5, self.RADIUS * 1.5))
