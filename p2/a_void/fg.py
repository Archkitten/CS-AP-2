import pygame
from util import *


class Foreground:
    def __init__(self, x, y):
        self.bx = x
        self.by = y
        self.speed = 5
        self.win_width = 1600 * Config.data['WIN_SCALE']
        self.win_height = 900 * Config.data['WIN_SCALE']
        self.tile_map = ['...........................................',
                         '...........................................',
                         '........................TTTTTTTT...........',
                         '...............TTTTT.......................',
                         '.......................................F...',
                         '.......TTTTT........................GGGGGGG',
                         '....................................DDDDDDD',
                         '................TTTTT...............DDDDDDD',
                         '....................................DDDDDDD',
                         'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGDDDDDDD',
                         'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD',
                         'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD',
                         'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD',
                         'DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD']
        self.grass_surf = pygame.image.load('img/Grass.png').convert_alpha()
        self.grass_surf = pygame.transform.scale(self.grass_surf, (self.grass_surf.get_width() * Config.data['WIN_SCALE'] * 0.1,
                                                         self.grass_surf.get_height() * Config.data['WIN_SCALE'] * 0.1))
        self.dirt_surf = pygame.image.load('img/Dirt.png').convert_alpha()
        self.dirt_surf = pygame.transform.scale(self.dirt_surf,
                                                 (self.dirt_surf.get_width() * Config.data['WIN_SCALE'] * 0.1,
                                                  self.dirt_surf.get_height() * Config.data['WIN_SCALE'] * 0.1))

    def __call__(self, screen):
        self.move()
        self.change_gravity()
        self.print_screen(screen)

    def print_screen(self, screen):
        for i, row in enumerate(self.tile_map):
            for j, column in enumerate(row):
                if column == 'G':
                    screen.blit(self.grass_surf, (j * Config.data['WIN_SCALE'] * 90 - self.bx, i * Config.data['WIN_SCALE'] * 90 - self.by + 450))
                if column == 'D':
                    screen.blit(self.dirt_surf, (j * Config.data['WIN_SCALE'] * 90 - self.bx, i * Config.data['WIN_SCALE'] * 90 - self.by + 450))
                if column == 'T':
                    screen.blit(self.grass_surf, (j * Config.data['WIN_SCALE'] * 90 - self.bx, i * Config.data['WIN_SCALE'] * 90 - self.by + 450))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.bx -= self.speed
        if keys[pygame.K_d]:
            self.bx += self.speed
        if keys[pygame.K_SPACE]:
            self.gravity = -8

    def change_gravity(self):
        self.gravity += 0.4
        self.by += self.gravity
