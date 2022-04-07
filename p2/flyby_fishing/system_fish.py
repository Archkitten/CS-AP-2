from ui_elements import Text, Picture
from config import *
import pygame
import random


class SystemFish:
    def __init__(self):
        self.timer = 0
        self.exists = False

        self.delay = None
        self.opportunity = None
        self.fish_counter = None
        self.randomize()

        self.fish_alert = Picture('img/Zap.png', 800, 450, 4)

    def __call__(self, screen, left_click):
        # Fish counter
        self.fish_counter(screen)

        # Increase timer if user is fishing.
        if left_click:
            self.timer += 1
        else:
            self.timer = 0

        # If the timer passes the delay (Fish appears!)
        if self.timer > self.delay:
            if left_click:
                self.fish_alert(screen, 255)
                self.exists = True
        # If the user misses the fish
        if self.timer > self.delay + self.opportunity:
            self.randomize()

        # Catch!
        if self.exists and left_click == False:
            Config.data['FISH_COUNT'] += 1
            self.randomize()

    def randomize(self):
        self.timer = 0
        self.exists = False
        # 5 20
        self.delay = random.uniform(1.5, 6) * 60
        self.opportunity = random.uniform(0.5, 1) * 60
        # Update fish counter
        self.fish_counter = Text(f"Fish: {str(Config.data['FISH_COUNT'])}", 200, 100, 'Blue', 'pristina', 120)
