import pygame
from config import *
from player import Player


class Drip(Player):
    # Constructor
    def __init__(self, x, y):
        super().__init__(x, y)
        self.COLOR = 'Yellow'
        self.PROJECTILE_COOLDOWN = 30
