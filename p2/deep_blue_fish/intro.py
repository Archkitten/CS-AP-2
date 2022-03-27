from p2.deep_blue_fish.util.ui_menu import UIMenu
from p2.deep_blue_fish.util.ui_elements import Text, Picture
import random


class Intro(UIMenu):
    def __init__(self):
        super().__init__()
        # Quotes
        self.quotes = ["If I could, I would.",
                       "Conquer All!",
                       "As if.",
                       "the876",
                       "And countless more on memories...",
                       "I think this guy is possessed",
                       "Ma Clique",
                       "Wait, who is michael?",
                       "Cover your bald head",
                       "ciao!",
                       "we shall fight in Lakliin",
                       "My signature move: The Backstabbing Victory",
                       "T H E  W A L L",
                       "We'll burn that bridge when we get to it",
                       "L'Mao",
                       "Taking too long.",
                       "02/11/2018",
                       "Au",
                       "feesh",
                       "Under Pressure",
                       "Nay I say!",
                       "Ohn",
                       "SCP-8704 and Protocol 520-Gan"]
        q = random.randint(-3, len(self.quotes) - 1)
        if q == -1:
            self.quote = Text('"Instead of fading everything out, just make Black.png fade in" - Q', 800, 450, 'Blue', 'cambria', 50)
        elif q == -2:
            self.quote = Text("BOTTOM TEXT", 800, 800, 'Blue', 'impact', 100)
        elif q == -3:
            self.quote = Text("To each it is left unknown, that to each it is granted, this gift brings a curse; that every memory of something as a part of anything can become everything in an instant, as existence in this place and time brings a power unlike any other to create that which can create, and to manifest something in the mind of anyone, that beckons their soul to the heavens of Earth.", 800, 450, 'White', 'pristina', 14)
        else:
            self.quote = Text(self.quotes[q], 800, 450, 'Blue', 'pristina', 80)
        # Black.png
        self.black = Picture('img/Black.png', 800, 450, 1)
        self.timer = 255
        self.timer_phase = "Fading out, words appearing"

    def while_loop(self):
        self.SCREEN.fill('Black')
        self.quote(self.SCREEN)
        self.black(self.SCREEN, self.timer)
        # Skip with left click.
        if self.left_click:
            self.running = False
        # Fading or unfading black. 4 and 3 are the fading and unfading speeds, respectively.
        if self.timer_phase == "Fading out, words appearing":
            self.timer -= 4
        else:
            self.timer += 3
        # Switch from fading to unfading. -43 is the delay.
        if self.timer <= -43:
            self.timer_phase = "Fading in, words disappearing"
        # End intro after fading complete. 43 is the delay.
        if self.timer > 255 + 43:
            self.running = False
