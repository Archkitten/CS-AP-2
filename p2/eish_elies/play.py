from config import *
from ui_menu import UIMenu
from ui_elements import Background
from static_water import StaticWater
import pygame


class Play(UIMenu):
    def __init__(self):
        super().__init__()
        self.static_water = StaticWater()
        # Music
        self.temporary_volume = 0.0
        self.music = pygame.mixer.Sound('audio/Eish_Elies.ogg')
        self.music.set_volume(data['MUSIC_VOLUME'] * self.temporary_volume)
        self.music.play(loops=-1)
        # Background
        self.background_timer = 0
        self.bg_day = Background('img/Day.png')
        self.opacity_day = 0
        self.bg_evening = Background('img/Evening.png')
        self.opacity_evening = 0
        self.bg_night = Background('img/Night.png')
        self.opacity_night = 0
        self.bg_loading = Background('img/Black.png')
        self.opacity_loading = 255

    def while_loop(self):
        # Background
        self.background_timer += 1
        # Day
        if self.background_timer <= 1860:
            # Remove blur
            self.bg_night(self.SCREEN, 255)
            # Fade in Day
            self.opacity_day += 1
            self.bg_day(self.SCREEN, self.opacity_day)
        # Evening
        elif self.background_timer <= 2520:
            # Remove blur
            self.bg_day(self.SCREEN, 255)
            # Fade in Evening
            self.opacity_evening += 1
            self.bg_evening(self.SCREEN, self.opacity_evening)
        # Night - Ends at 3909
        elif self.background_timer <= 3910:
            # Remove blur
            self.bg_evening(self.SCREEN, 255)
            # Fade in Night
            self.opacity_night += 1
            self.bg_night(self.SCREEN, self.opacity_night)
        # Reset
        else:
            self.opacity_day = 0
            self.opacity_evening = 0
            self.opacity_night = 0
            self.background_timer = 0

        # Water
        self.static_water(self.SCREEN, self.timer)

        # Loading... Background
        if self.timer < 160:
            self.bg_loading(self.SCREEN, 255)
            # For fading in music - Volume fades up to 1.007999 so a cap is required.
            self.temporary_volume += 0.0063
            if self.temporary_volume > 1:
                self.temporary_volume = 1
            self.music.set_volume(data['MUSIC_VOLUME'] * self.temporary_volume)
        elif self.timer < 211:
            self.opacity_loading -= 15
            self.bg_loading(self.SCREEN, self.opacity_loading)
