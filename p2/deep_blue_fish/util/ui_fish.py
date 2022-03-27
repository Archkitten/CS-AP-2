from p2.deep_blue_fish.util.ui_elements import Picture
from p2.deep_blue_fish.util.config import *
import pygame


class Fish_Left(Picture):
    def __init__(self, x, y, scale):
        super().__init__('img/feesh.png', x, y, scale)
        self.image = pygame.transform.flip(self.image, True, True)
        self.SPEED = 3

    def __call__(self, screen, opacity):
        self.x += self.SPEED
        self.image_rect = self.image.get_rect(center=(self.x * WIN_SCALE, self.y * WIN_SCALE))
        super().__call__(screen, opacity)


class Fish_Right(Picture):
    def __init__(self, x, y, scale):
        super().__init__('img/feesh.png', x, y, scale)
        self.SPEED = 3

    def __call__(self, screen, opacity):
        self.x -= self.SPEED
        self.image_rect = self.image.get_rect(center=(self.x * WIN_SCALE, self.y * WIN_SCALE))
        super().__call__(screen, opacity)
