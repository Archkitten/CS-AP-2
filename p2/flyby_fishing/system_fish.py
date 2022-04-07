from ui_elements import Text, Picture
from config import *
import pygame
import random


class SystemFish:
    def __init__(self):
        self.timer = 0

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
            # If the user catches it
            if not left_click:
                print("Does this even work?")
                data['FISH_COUNT'] += 1
                self.randomize()
        # If the user misses the fish
        if self.timer > self.delay + self.opportunity:
            self.randomize()

    def randomize(self):
        self.timer = 0
        # 5 20
        self.delay = random.randint(2, 4) * 60
        self.opportunity = random.randint(1, 3) * 60
        # Update fish counter
        self.fish_counter = Text(f"Fish: {str(data['FISH_COUNT'])}", 200, 100, 'Blue', 'pristina', 120)
