from config import *
from ui_menu import UIMenu
from ui_elements import Text, Button
import pygame


class Options(UIMenu):
    def __init__(self):
        super().__init__()
        self.title = None
        # Resolution
        self.button_downscale = None
        self.button_resolution = None
        self.button_upscale = None
        # Music
        self.button_decrease = None
        self.button_volume = None
        self.button_increase = None
        # Back
        self.button_back = None
        # Define all the variables listed above
        self.resize()

    def while_loop(self):
        self.SCREEN.fill('Black')
        self.title(self.SCREEN)
        # Resolution
        if self.button_downscale(self.SCREEN, 255, self.mx, self.my, self.left_click):
            if Config.data['WIN_SCALE'] > 0.2:
                Config.data['WIN_SCALE'] -= 0.1
                self.resize()
        if self.button_resolution(self.SCREEN, 255, self.mx, self.my, self.left_click):
            Config.data['WIN_SCALE'] = 0.8
            self.resize()
        if self.button_upscale(self.SCREEN, 255, self.mx, self.my, self.left_click):
            if Config.data['WIN_SCALE'] < 1.4:
                Config.data['WIN_SCALE'] += 0.1
                self.resize()
        # Music
        if self.button_decrease(self.SCREEN, 255, self.mx, self.my, self.left_click):
            if Config.data['MUSIC_VOLUME'] > 0.1:
                Config.data['MUSIC_VOLUME'] -= 0.1
                self.resize()
        if self.button_volume(self.SCREEN, 255, self.mx, self.my, self.left_click):
            Config.data['MUSIC_VOLUME'] = 0.5
            self.resize()
        if self.button_increase(self.SCREEN, 255, self.mx, self.my, self.left_click):
            if Config.data['MUSIC_VOLUME'] < 0.9:
                Config.data['MUSIC_VOLUME'] += 0.1
                self.resize()
        # Back
        if self.button_back(self.SCREEN, 255, self.mx, self.my, self.left_click):
            self.running = False

    def resize(self):
        self.SCREEN = pygame.display.set_mode((1600 * Config.data['WIN_SCALE'], 900 * Config.data['WIN_SCALE']))
        self.title = Text("Options", 800, 200, 'Blue', 'pristina', 100)
        # Resolution
        self.button_downscale = Button('img/ButtonMinus.png', 200, 450, 0.2, "", 'Blue', 'pristina', 0)
        self.button_resolution = Button('img/Button.png', 450, 450, 0.2, f"Resolution: {int(round(Config.data['WIN_SCALE'] * 1600))} x {int(round(Config.data['WIN_SCALE'] * 900))}", "Blue", "pristina", 40)
        self.button_upscale = Button('img/ButtonPlus.png', 700, 450, 0.2, "", 'Blue', 'pristina', 0)
        # Music
        self.button_decrease = Button('img/ButtonMinus.png', 900, 650, 0.2, "", 'Blue', 'pristina', 0)
        self.button_volume = Button('img/Button.png', 1150, 650, 0.2, f"Volume: {int(round(Config.data['MUSIC_VOLUME'] * 10))}", "Blue", "pristina", 70)
        self.button_increase = Button('img/ButtonPlus.png', 1400, 650, 0.2, "", 'Blue', 'pristina', 0)
        # Back
        self.button_back = Button('img/Button.png', 200, 800, 0.2, "Back", 'Blue', 'pristina', 70)
