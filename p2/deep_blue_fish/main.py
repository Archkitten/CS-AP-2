from p2.deep_blue_fish.util.ui_menu import UIMenu
from p2.deep_blue_fish.util.ui_elements import Text, Button
from p2.deep_blue_fish.util.config import *
import pygame


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
        # Timer
        self.timer = 0

    def while_loop(self):
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
