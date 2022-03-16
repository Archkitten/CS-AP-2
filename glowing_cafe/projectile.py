import pygame
import math
from config import *
from linear_projectile import LinearProjectile


class Bullet(LinearProjectile):
    # Constructor
    def __init__(self, x, y, mx, my):
        super().__init__(x, y, mx, my)


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
