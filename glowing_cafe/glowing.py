import pygame
import sys
from config import *


class Glowing:
    def __init__(self):
        # Pygame Window Constants (REQUIRED)
        self.CLOCK = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption(GAME_TITLE)
        self.SCREEN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.FONT = pygame.font.Font('font/PixelType.ttf', 32)
        # Dynamic Variables

    def main_menu(self):
        # Local Variables
        running = True
        title = self.FONT.render("Glowing Cafe", False, 'Black')
        while running:
            # Drawing
            self.SCREEN.fill('Black')
            self.SCREEN.blit(title, (WIN_WIDTH / 2, WIN_HEIGHT / 2))
            # Event Loop
            for event in pygame.event.get():
                # Close Button
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Keyboard Presses
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            pygame.display.update()
            self.CLOCK.tick(FPS)


g = Glowing()
g.main_menu()

pygame.quit()
sys.exit()
