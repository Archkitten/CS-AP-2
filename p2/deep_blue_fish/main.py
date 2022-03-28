from ui_menu import UIMenu
from ui_elements import Text, Button
from static_fish import StaticFish


class Main(UIMenu):
    def __init__(self):
        super().__init__()
        self.title = Text("Deep Blue Fish", 800, 200, 'Blue', 'pristina', 100)
        self.button_play = Button('img/button.png', 800, 400, 0.15, "Play", 'Blue', 'pristina', 70)
        self.button_options = Button('img/button.png', 800, 550, 0.15, "Options", 'Blue', 'pristina', 70)
        self.button_quit = Button('img/button.png', 800, 700, 0.15, "Quit", 'Blue', 'pristina', 70)
        self.static_fish = StaticFish()

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
        # Static Fish
        self.static_fish(self.SCREEN, self.timer)
