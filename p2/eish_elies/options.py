from config import *
from ui_menu import UIMenu
from ui_elements import Text, Button
import pygame


class Options(UIMenu):
    def __init__(self):
        super().__init__()
        self.title = Text("Options", 800, 200, 'Blue', 'pristina', 100)
        self.button_upscale = Button('img/Button.png', 800, 400, 0.2, "Upscale", 'Blue', 'pristina', 70)
        self.button_downscale = Button('img/Button.png', 800, 550, 0.2, "Downscale", 'Blue', 'pristina', 70)
        self.button_back = Button('img/Button.png', 200, 800, 0.2, "Back", 'Blue', 'pristina', 70)

    def while_loop(self):
        self.SCREEN.fill('Black')
        self.title(self.SCREEN)
        if self.button_upscale(self.SCREEN, 255, self.mx, self.my, self.left_click):
            data['WIN_SCALE'] += 0.1
            self.resize()
        if self.button_downscale(self.SCREEN, 255, self.mx, self.my, self.left_click):
            data['WIN_SCALE'] -= 0.1
            self.resize()
        if self.button_back(self.SCREEN, 255, self.mx, self.my, self.left_click):
            self.running = False

    def resize(self):
        self.SCREEN = pygame.display.set_mode((1600 * data['WIN_SCALE'], 900 * data['WIN_SCALE']))
        self.title = Text("Options", 800, 200, 'Blue', 'pristina', 100)
        self.button_upscale = Button('img/Button.png', 800, 400, 0.2, "Upscale", 'Blue', 'pristina', 70)
        self.button_downscale = Button('img/Button.png', 800, 550, 0.2, "Downscale", 'Blue', 'pristina', 70)
        self.button_back = Button('img/Button.png', 200, 800, 0.2, "Back", 'Blue', 'pristina', 70)
