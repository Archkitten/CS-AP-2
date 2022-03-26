from p2.deep_blue_fish.util.ui_menu import UIMenu
from p2.deep_blue_fish.util.ui_elements import Text
from p2.deep_blue_fish.util.config import *
import pygame


class Main(UIMenu):
    def __init__(self):
        super().__init__()
        self.title = Text("Deep Blue Fish", WIN_WIDTH / 2, 200, 'Blue', pygame.font.SysFont('pristina', int(100 * WIN_SCALE)))

    def while_loop(self):
        self.SCREEN.fill('Black')
        self.title(self.SCREEN)
