from util import *


class MainMenu(Menu):
    def __init__(self):
        super().__init__()
        self.title = Text(f"{Config.data['GAME_TITLE']}", 800, 100, 'Black', 'mvboli', 100)

    def while_loop(self):
        self.screen.fill('White')

        self.title(self.screen)
