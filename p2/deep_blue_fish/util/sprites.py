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
        self.move()
        super().__call__(screen, opacity)

    def move(self):
        if self.direction == "Left":
            self.image_rect.x -= int(3 * WIN_SCALE)
        elif self.direction == "Right":
            self.image_rect.x += int(3 * WIN_SCALE)


class Bouncer(Picture):
    def __init__(self, x, y, scale):
        super().__init__('img/feesh.png', x, y, scale)
        self.image = pygame.transform.rotozoom(self.image, 135, 0.5)
        # Wave
        self.wave_phase = "Going down, y increasing"
        self.gravity = 0

    def __call__(self, screen, opacity):
        self.move()
        super().__call__(screen, opacity)

    def move(self):
        # Waving
        if self.wave_phase == "Going down, y increasing":
            self.gravity += 0.1 * WIN_SCALE
        else:
            self.gravity -= 0.1 * WIN_SCALE

        if self.image_rect.y <= 40 * WIN_SCALE:
            self.wave_phase = "Going down, y increasing"
        elif self.image_rect.y >= 40 * WIN_SCALE:
            self.wave_phase = "Going up, y decreasing"

        self.image_rect.y += self.gravity
