from config import *
import pygame


class StaticWater:
    def __init__(self):
        self.y = 450
        self.WIDTH = 40
        self.y_wave_center = 500
        self.wave_speed = 0.1

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

    def __call__(self, screen):
        self.move()
        self.circle = (self.x, self.y)
        pygame.draw.circle(screen, 'Blue', self.circle, self.RADIUS)

    def move(self):
        if self.y < self.center:
            self.gravity += self.speed
        else:
            self.gravity -= self.speed
        self.y += self.gravity
