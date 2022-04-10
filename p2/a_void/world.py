from util import *
from player import Player
from fg import Foreground


class World(Menu):
    def __init__(self):
        super().__init__()
        self.fg = Foreground()
        self.player = Player(800, 430, 0.1)

    def while_loop(self):
        # Background
        self.screen.fill('Black')
        self.image = pygame.image.load('img/AlexBackground.png').convert_alpha()
        self.screen.blit(self.image, (0, 0))
        self.player(self.screen, self.fg.tile_map)
        self.fg.print_screen(self.screen, self.player.bx, self.player.by)
