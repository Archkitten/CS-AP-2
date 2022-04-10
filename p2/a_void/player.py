import pygame
from util import *


class Player:
    def __init__(self, x, y, scale):
        self.x = x
        self.y = y
        self.scale = scale
        self.speed = 5
        self.health = 4

        self.gravity = 0

        self.bobbing = 0
        self.bobbing_timer = 0

        self.animate_timer = 0

        self.image_surf = None
        self.image_rect = None
        self.animate()
        self.update()

    def __call__(self, screen, tile_map):
        # self.move()
        # if colliding:
        self.animate_bobbing()
        # self.jump_count = 2
        # else:
        # self.change_gravity()
        # self.collide(tile_map)
        self.animate()
        self.update()
        screen.blit(self.image_surf, self.image_rect)

    def animate_bobbing(self):
        self.bobbing_timer += 1
        if self.bobbing_timer > 20:
            self.bobbing -= 0.5
        else:
            self.bobbing += 0.5
        if self.bobbing_timer > 40:
            self.bobbing_timer = 0

    def animate(self):
        self.animate_timer += 1
        if self.animate_timer > 59:
            self.animate_timer = 0
        if self.animate_timer < 20:
            self.image_surf = pygame.image.load('img/Void1.png').convert_alpha()
        elif self.animate_timer < 40:
            self.image_surf = pygame.image.load('img/Void2.png').convert_alpha()
        elif self.animate_timer < 60:
            self.image_surf = pygame.image.load('img/Void3.png').convert_alpha()

    def update(self):
        self.image_surf = pygame.transform.scale(self.image_surf,
                                                 (self.image_surf.get_width() * Config.data['WIN_SCALE'] * self.scale,
                                                  self.image_surf.get_height() * Config.data['WIN_SCALE'] * self.scale))
        self.image_rect = self.image_surf.get_rect(
            center=(self.x * Config.data['WIN_SCALE'], self.y * Config.data['WIN_SCALE'] + self.bobbing))

    # def collide(self, tile_map):
    #     for i, row in enumerate(tile_map):
    #         for j, column in enumerate(row):
    #             if column == 'G' or 'D' or 'T':
    #                 if self.y > i * Config.data['WIN_SCALE'] * 90 - self.by + 450:
    #                     self.by -= self.gravity
