import pygame
import random
from config import *
from player import Player
from projectile import Goop


class Blob(Player):
    # Constructor
    def __init__(self, x, y):
        super().__init__(x, y)
        self.SPEED = 7
        self.SLOW_PERCENT = 0.5
        self.COLOR = 'Purple'

        self.PROJECTILE_COOLDOWN = 10

        self.KEY_SHOOT = pygame.K_SPACE
        self.KEY_LEFT = pygame.K_LEFT
        self.KEY_RIGHT = pygame.K_RIGHT
        self.KEY_UP = pygame.K_UP
        self.KEY_DOWN = pygame.K_DOWN

        self.health = 4
        self.MAX_HEALTH = 4
        self.HEALTH_BAR_POSITION = 2

    # Shoot
    def shoot(self, tx, ty, keys):
        if keys[self.KEY_SHOOT] and self.projectile_counter == self.PROJECTILE_COOLDOWN:
            self.projectiles.append(Goop(self.x, self.y, tx + random.randint(-100, 100), ty + random.randint(-100, 100)))

        if self.projectile_counter >= self.PROJECTILE_COOLDOWN:
            self.projectile_counter = 0
        self.projectile_counter += 1

    # Ghost Animate
    def ghost_animate(self, screen):
        pygame.draw.rect(screen, self.COLOR, (self.x - self.RADIUS / 1.5, self.y - self.RADIUS / 1.5,
                                              self.RADIUS * 1.5, self.RADIUS * 1.5))
