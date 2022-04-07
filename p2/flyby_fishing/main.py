from config import *
from ui_menu import UIMenu
from ui_elements import Text, Button
from static_fish import StaticFish
from play import Play
from options import Options


class Main(UIMenu):
    def __init__(self):
        super().__init__()
        self.title = Text(f"{Config.data['GAME_TITLE']}", 800, 200, 'Blue', 'pristina', 100)
        self.button_play = Button('img/Button.png', 800, 400, 0.2, "Play", 'Blue', 'pristina', 70)
        self.button_options = Button('img/Button.png', 800, 550, 0.2, "Options", 'Blue', 'pristina', 70)
        self.button_quit = Button('img/Button.png', 800, 700, 0.2, "Quit", 'Blue', 'pristina', 70)
        self.static_fish = StaticFish()

    def while_loop(self):
        self.SCREEN.fill('Black')
        # Static Fish
        self.static_fish(self.SCREEN, self.timer)
        # Menu and Buttons
        self.title(self.SCREEN)
        if self.button_play(self.SCREEN, 255, self.mx, self.my, self.left_click):
            play = Play()
            play()
        if self.timer >= 30:
            if self.button_options(self.SCREEN, 255, self.mx, self.my, self.left_click):
                options = Options()
                options()
                self.resize()
                # Set left click to false to prevent immediate quit
                self.left_click = False
        if self.timer >= 60:
            if self.button_quit(self.SCREEN, 255, self.mx, self.my, self.left_click):
                self.running = False

    def resize(self):
        self.title = Text(f"{Config.data['GAME_TITLE']}", 800, 200, 'Blue', 'pristina', 100)
        self.button_play = Button('img/Button.png', 800, 400, 0.2, "Play", 'Blue', 'pristina', 70)
        self.button_options = Button('img/Button.png', 800, 550, 0.2, "Options", 'Blue', 'pristina', 70)
        self.button_quit = Button('img/Button.png', 800, 700, 0.2, "Quit", 'Blue', 'pristina', 70)
        self.static_fish = StaticFish()
