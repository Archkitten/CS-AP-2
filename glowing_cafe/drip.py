import pygame
from config import *
from player import Player
from projectile import Star
from spritesheet import SpriteSheet


class Drip(Player):
    # Constructor
    def __init__(self, x, y):
        super().__init__(x, y)
        self.SPEED = 7
        self.SLOW_PERCENT = 0.5
        self.COLOR = 'Yellow'

        self.PROJECTILE_COOLDOWN = 30

        self.KEY_SHOOT = pygame.K_c
        self.KEY_LEFT = pygame.K_a
        self.KEY_RIGHT = pygame.K_d
        self.KEY_UP = pygame.K_w
        self.KEY_DOWN = pygame.K_s

        self.health = 4
        self.MAX_HEALTH = 4
        self.HEALTH_BAR_POSITION = 3

        self.SPRITE_SHEET = SpriteSheet('img/CharacterAkhil.png')
        self.sprite_sheet_x = 0
        self.sprite_sheet_y = 0
        self.image = self.SPRITE_SHEET.get_sprite(self.sprite_sheet_x * 200, self.sprite_sheet_y * 250, 200, 250)

    # Shoot
    def shoot(self, tx, ty):
        keys = pygame.key.get_pressed()
        if keys[self.KEY_SHOOT] and self.projectile_counter == self.PROJECTILE_COOLDOWN:
            self.projectiles.append(Star(self.x, self.y - 35, tx, ty))

        if self.projectile_counter >= self.PROJECTILE_COOLDOWN:
            self.projectile_counter = 0
        self.projectile_counter += 1

    # Animate
    def animate(self, screen):
        keys = pygame.key.get_pressed()
        # Conditionals
        if keys[self.KEY_SHOOT]:
            self.sprite_sheet_x += 1
            self.sprite_sheet_y = 1
            if self.sprite_sheet_x >= 6:
                self.sprite_sheet_x = 0
        else:
            self.sprite_sheet_x = 0
            self.sprite_sheet_y = 0

        self.image = self.SPRITE_SHEET.get_sprite(self.sprite_sheet_x * 200, self.sprite_sheet_y * 250, 200, 250)
        self.image = pygame.transform.scale(self.image, (200 * 0.4, 250 * 0.4))
        screen.blit(self.image, (self.x - 40, self.y - 65))

