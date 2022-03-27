from p2.deep_blue_fish.util.ui_menu import UIMenu
from p2.deep_blue_fish.util.ui_elements import Text, Button
from p2.deep_blue_fish.util.sprites import Fish_Left, Fish_Right
from p2.deep_blue_fish.util.config import *
import random


class Main(UIMenu):
    def __init__(self):
        super().__init__()
        self.title = Text("Deep Blue Fish", 800, 200, 'Blue', 'pristina', 100)
        self.button_play = Button('img/button.png', 800, 400, 0.15, "Play", 'Blue', 'pristina', 70)
        self.button_options = Button('img/button.png', 800, 550, 0.15, "Options", 'Blue', 'pristina', 70)
        self.button_quit = Button('img/button.png', 800, 700, 0.15, "Quit", 'Blue', 'pristina', 70)
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

        # Fish
        if self.timer % 40 == 0:
            direction = random.randint(0, 4)
            if direction == 0:
                self.fish_list.append(Fish_Left(-100, random.randint(150, 900), 0.25))
            elif direction == 1:
                self.fish_list.append(Fish_Right(1700, random.randint(150, 900), 0.25))
            else:
                pass
        for fish in self.fish_list:
            fish(self.SCREEN, 255)
            if fish.image_rect.x > 1800 * WIN_SCALE or fish.image_rect.x < -200 * WIN_SCALE:
                self.fish_list.remove(fish)

        # Timer
        self.timer += 1
