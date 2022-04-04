from ui_menu import UIMenu
from static_water import StaticWater


class Play(UIMenu):
    def __init__(self):
        super().__init__()
        self.static_water = StaticWater()

    def while_loop(self):
        self.SCREEN.fill('Black')
        self.static_water(self.SCREEN, self.timer)
