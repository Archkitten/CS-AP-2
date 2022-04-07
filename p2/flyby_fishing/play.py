from config import *
from ui_menu import UIMenu
from ui_elements import Picture, Button, Background
from static_water import StaticWater
from pause import Pause
import pygame


class Play(UIMenu):
    def __init__(self):
        super().__init__()
        self.static_water = StaticWater()
        self.button_quit = Button('img/ButtonCircle.png', 1500, 100, 0.2, "", 'Blue', 'pristina', 0)
        # Music
        self.temporary_volume = 0.0
        self.music = pygame.mixer.Sound('audio/Flyby_Fishing.ogg')
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
        self.bg_loading = Background('img/Loading.png')
        self.opacity_loading = 255
        # Fishing Rod
        self.fishing_rod = Picture('img/FishingRod.png', 800, 450, 1)
        self.fishing_rod_line = Picture('img/FishingRodLine.png', 800, 450, 1)

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

        # Button
        if self.button_quit(self.SCREEN, 255, self.mx, self.my, self.left_click):
            self.running = False

        # Fishing Rod Line
        if self.left_click:
            self.fishing_rod_line(self.SCREEN, 255)

        # Water
        self.static_water(self.SCREEN, self.timer)

        # Fishing Rod
        self.fishing_rod(self.SCREEN, 255)

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

    def event_loop(self, event):
        # X PROGRAM
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # KEYBOARD PRESSES
        if event.type == pygame.KEYDOWN:
            # Escape Key
            if event.key == pygame.K_ESCAPE:
                self.music.stop()
                self.running = False
        # MOUSE
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.left_click = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.left_click = False
