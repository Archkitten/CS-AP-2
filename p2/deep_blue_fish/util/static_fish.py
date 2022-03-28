from p2.deep_blue_fish.util.ui_elements import Picture
from p2.deep_blue_fish.util.config import *
import pygame
import random


class StaticFish:
    def __init__(self):
        self.fish_list = []

    def __call__(self, screen, timer):
        # Fish
        if timer % 40 == 0:
            direction = random.randint(0, 4)
            if direction == 0:
                self.fish_list.append(FishLeft(-100, random.randint(150, 900), 0.25))
            elif direction == 1:
                self.fish_list.append(FishRight(1700, random.randint(150, 900), 0.25))
            else:
                pass
        for fish in self.fish_list:
            fish(screen, 255)
            if fish.image_rect.x > 1800 * WIN_SCALE or fish.image_rect.x < -200 * WIN_SCALE:
                self.fish_list.remove(fish)


class FishLeft(Picture):
    def __init__(self, x, y, scale):
        super().__init__('img/feesh.png', x, y, scale)
        self.image = pygame.transform.flip(self.image, True, True)
        self.SPEED = random.randint(2, 4)

    def __call__(self, screen, opacity):
        self.x += self.SPEED
        self.image_rect = self.image.get_rect(center=(self.x * WIN_SCALE, self.y * WIN_SCALE))
        super().__call__(screen, opacity)


class FishRight(Picture):
    def __init__(self, x, y, scale):
        super().__init__('img/feesh.png', x, y, scale)
        self.SPEED = random.randint(2, 4)

    def __call__(self, screen, opacity):
        self.x -= self.SPEED
        self.image_rect = self.image.get_rect(center=(self.x * WIN_SCALE, self.y * WIN_SCALE))
        super().__call__(screen, opacity)
