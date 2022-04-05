from config import *
from ui_menu import UIMenu
from static_water import StaticWater
import pygame


class Play(UIMenu):
    def __init__(self):
        super().__init__()
        self.static_water = StaticWater()
        # Music
        self.music = pygame.mixer.Sound('audio/Eish_Elies.ogg')
        self.music.set_volume(data['MUSIC_VOLUME'])
        self.music.play(loops=-1)

    def while_loop(self):
        self.SCREEN.fill('Black')
        self.static_water(self.SCREEN, self.timer)
