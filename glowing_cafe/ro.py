import pygame
from config import *
from player import Player


class Ro(Player):
    # Constructor
    def __init__(self, x, y):
        super().__init__(x, y)
        self.COLOR = 'Orange'
