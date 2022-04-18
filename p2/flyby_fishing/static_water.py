from config import *
import pygame


class StaticWater:
    def __init__(self):
        self.y = 700
        self.WIDTH = 15
        self.y_wave_center = 750
        self.wave_speed = 0.06

        self.water_list = []
        self.DISTANCE = 1
        self.CREATE_SPEED = 10
        self.LENGTH = 1600

    def __call__(self, screen, timer):
        # Water
        if timer % self.DISTANCE == 0 and timer < self.LENGTH / self.CREATE_SPEED:
            self.water_list.append(Water(timer * self.CREATE_SPEED, self.y, self.WIDTH, self.y_wave_center, self.wave_speed))
        for water in self.water_list:
            water(screen)


class Water:
    def __init__(self, x, y, radius, center, speed):
        self.x = x
        self.y = y
        self.circle = (self.x, self.y)
        self.RADIUS = radius

        self.gravity = 0
        self.center = center
        self.speed = speed

        self.droplet_y = self.y

    def __call__(self, screen):
        self.move()
        self.circle = (self.x * Config.data['WIN_SCALE'], self.y * Config.data['WIN_SCALE'])
        pygame.draw.circle(screen, 'Blue', self.circle, self.RADIUS * Config.data['WIN_SCALE'])

        # This is only for if you want the area under the wave to be filled.
        while self.droplet_y < 900:
            self.droplet_y += 20
            pygame.draw.circle(screen, 'Blue', (self.x * Config.data['WIN_SCALE'], self.droplet_y * Config.data['WIN_SCALE']), self.RADIUS * Config.data['WIN_SCALE'])
        self.droplet_y = self.y

    def move(self):
        if self.y < self.center:
            self.gravity += self.speed
        else:
            self.gravity -= self.speed
        self.y += self.gravity
