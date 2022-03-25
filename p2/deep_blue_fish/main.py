from ui_elements import *
from config import *
import pygame
import sys


class Main:
    def __init__(self):
        # Pygame Window Constants (REQUIRED)
        self.CLOCK = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption(GAME_TITLE)
        self.SCREEN = pygame.display.set_mode((WIN_WIDTH * WIN_SCALE, WIN_HEIGHT * WIN_SCALE))

    def __call__(self):
        # print(pygame.font.get_fonts())
        title = Text("Deep Blue Fish", pygame.font.SysFont('pristina', 64), 'Blue', WIN_WIDTH / 2, 200)
        # While Loop
        while True:
            self.SCREEN.fill('Black')
            title(self.SCREEN)
            # Event For Loop
            for event in pygame.event.get():
                # Close Button
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.CLOCK.tick(FPS)
