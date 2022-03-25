import pygame
import math
from config import *
from spritesheet import SpriteSheet
from horizontal_projectile import HorizontalProjectile
from linear_projectile import LinearProjectile
from lingering_projectile import LingeringProjectile


class HorizontalBullet(HorizontalProjectile):
    # Constructor
    def __init__(self, x):
        super().__init__(x)
        self.SPEED = -3
        self.RADIUS = 7


class Bullet(LinearProjectile):
    # Constructor
    def __init__(self, x, y, mx, my):
        super().__init__(x, y, mx, my)


class LingeringBullet(LingeringProjectile):
    # Constructor
    def __init__(self, x, y):
        super().__init__(x, y)
        self.RADIUS = 20
        self.duration = 61


class Goop(LinearProjectile):
    # Constructor
    def __init__(self, x, y, mx, my):
        super().__init__(x, y, mx, my)
        self.SPEED = 9
        self.COLOR = 'Purple'
        # Big Math Stuff
        angle = math.atan2(my - y, mx - x)
        self.dx = math.cos(angle) * self.SPEED
        self.dy = math.sin(angle) * self.SPEED


class Star(LinearProjectile):
    # Constructor
    def __init__(self, x, y, mx, my):
        super().__init__(x, y, mx, my)
        self.SPEED = 12
        self.COLOR = 'Yellow'
        # Big Math Stuff
        angle = math.atan2(my - y, mx - x)
        self.dx = math.cos(angle) * self.SPEED
        self.dy = math.sin(angle) * self.SPEED

        self.SPRITE_SHEET = SpriteSheet('img/CharacterAkhil.png')
        self.sprite_sheet_x = 0
        self.sprite_sheet_y = 2050
        self.image = self.SPRITE_SHEET.get_sprite(self.sprite_sheet_x, self.sprite_sheet_y, 100, 100)
        self.animation_frame = 0
        self.ANIMATION_COOLDOWN = 2

    # Animate
    def animate(self, screen):
        if self.animation_frame == self.ANIMATION_COOLDOWN:
            if self.sprite_sheet_x == 0:
                self.sprite_sheet_x = 185
            elif self.sprite_sheet_x == 185:
                self.sprite_sheet_x = 390
            elif self.sprite_sheet_x == 390:
                self.sprite_sheet_x = 570
            else:
                self.sprite_sheet_x = 0
            self.animation_frame = 0
        else:
            self.animation_frame += 1
        # If animation is complete, loop it.
        if self.sprite_sheet_x > 3 * 180:
            self.sprite_sheet_x = 0

        self.image = self.SPRITE_SHEET.get_sprite(self.sprite_sheet_x, self.sprite_sheet_y, 100, 100)
        self.image = pygame.transform.scale(self.image, (100 * 0.4, 100 * 0.4))
        screen.blit(self.image, (self.x - 25, self.y - 25))


class Feather(LinearProjectile):
    # Constructor
    def __init__(self, x, y, mx, my):
        super().__init__(x, y, mx, my)
        self.SPEED = 6
        self.COLOR = 'Gray'
        # Big Math Stuff
        angle = math.atan2(my - y, mx - x)
        self.dx = math.cos(angle) * self.SPEED
        self.dy = math.sin(angle) * self.SPEED
