from p2.deep_blue_fish.util.ui_elements import Picture
from p2.deep_blue_fish.util.config import *
import pygame


class Feesh(Picture):
    def __init__(self, x, y, scale, direction):
        super().__init__('img/feesh.png', x, y, scale)
        # Directional
        self.direction = direction
        if self.direction == "Right":
            self.image = pygame.transform.flip(self.image, True, True)

    def __call__(self, screen, opacity):
        super().__call__(screen, opacity)
        self.move()

    def move(self):
        if self.direction == "Left":
            self.image_rect.x -= int(3 * WIN_SCALE)
        elif self.direction == "Right":
            self.image_rect.x += int(3 * WIN_SCALE)
