from p2.deep_blue_fish.util.config import *
import pygame


class Text:
    def __init__(self, text, x, y, color, font):
        self.text = font.render(text, True, color)
        self.text_rect = self.text.get_rect(center=(x * WIN_SCALE, y * WIN_SCALE))

    def __call__(self, screen):
        screen.blit(self.text, self.text_rect)


class Picture:
    def __init__(self, image, x, y, scale):
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * WIN_SCALE * scale, self.image.get_height() * WIN_SCALE * scale))
        self.image_rect = self.image.get_rect(center=(x * WIN_SCALE, y * WIN_SCALE))

    def __call__(self, screen, opacity):
        self.image.set_alpha(opacity)
        screen.blit(self.image, self.image_rect)
