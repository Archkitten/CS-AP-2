from p2.deep_blue_fish.util.config import *


class Text:
    def __init__(self, text, x, y, color, font):
        self.text = font.render(text, True, color)
        self.text_rect = self.text.get_rect(center=(x * WIN_SCALE, y * WIN_SCALE))

    def __call__(self, screen):
        screen.blit(self.text, self.text_rect)

class Picture:
    def __init__(self):
        pass

    def __call__(self):
        pass
