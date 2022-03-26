from p2.deep_blue_fish.util.ui_menu import UIMenu
from p2.deep_blue_fish.util.ui_elements import Text, Button
from p2.deep_blue_fish.util.sprites import Feesh, Bouncer
from p2.deep_blue_fish.util.config import *
import pygame
import random


class Main(UIMenu):
    def __init__(self):
        super().__init__()
        self.title = Text("Deep Blue Fish", 800, 200, 'Blue', pygame.font.SysFont('pristina', int(100 * WIN_SCALE)))
        self.button_play = Button('img/button.png', 800, 400, 0.15, "Play", 'Blue',
                                  pygame.font.SysFont('pristina', int(70 * WIN_SCALE)))
        self.button_options = Button('img/button.png', 800, 550, 0.15, "Options", 'Blue',
                                     pygame.font.SysFont('pristina', int(70 * WIN_SCALE)))
        self.button_quit = Button('img/button.png', 800, 700, 0.15, "Quit", 'Blue',
                                  pygame.font.SysFont('pristina', int(70 * WIN_SCALE)))
        self.fish_list = []
        # Timer
        self.timer = 0

    def while_loop(self):
        # Menu and Buttons
        self.SCREEN.fill('Black')
        self.title(self.SCREEN)
        if self.button_play(self.SCREEN, 255, self.mx, self.my, self.left_click):
            pass
        if self.timer >= 30:
            if self.button_options(self.SCREEN, 255, self.mx, self.my, self.left_click):
                pass
        if self.timer >= 60:
            if self.button_quit(self.SCREEN, 255, self.mx, self.my, self.left_click):
                self.running = False
        self.timer += 1

        # Fish
        if self.timer % 40 == 0:
            direction = random.randint(0, 4)
            if direction == 0:
                self.fish_list.append(Feesh(-100, random.randint(150, 900), 0.25, "Right"))
            elif direction == 1:
                self.fish_list.append(Feesh(1700, random.randint(150, 900), 0.25, "Left"))
            else:
                pass
        for fish in self.fish_list:
            fish(self.SCREEN, 255)
            if fish.image_rect.x > 1800 * WIN_SCALE:
                self.fish_list.remove(fish)
            if fish.image_rect.x < -200 * WIN_SCALE:
                self.fish_list.remove(fish)

        # Bouncer
        if self.timer % 1 == 0 and self.timer <= 80:
            self.fish_list.append(Bouncer(self.timer * 20, -225, 0.25))
