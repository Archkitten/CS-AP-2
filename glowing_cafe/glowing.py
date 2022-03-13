import pygame
import sys
from config import *
from drip import Drip


class Glowing:
    def __init__(self):
        # Pygame Window Constants (REQUIRED)
        self.CLOCK = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption(GAME_TITLE)
        self.SCREEN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.FONT = pygame.font.Font('font/PixelType.ttf', 32)
        # Dynamic Variables
        self.character = "Drip"

    def main_menu(self):
        # Local Variables
        running = True
        click = False

        TEXT_TITLE = self.FONT.render("Glowing Cafe", False, 'Black')

        BUTTON_LEVEL_0 = pygame.Rect(20, 50, 100, 25)
        BUTTON_LEVEL_0_TEXT = self.FONT.render("Level 0", False, 'White')

        TEXT_CHARACTER_SELECT = self.FONT.render("Character Select", False, 'Black')

        while running:
            # Redefine Variables
            mx, my = pygame.mouse.get_pos()
            # Drawing
            self.SCREEN.fill('White')

            self.SCREEN.blit(TEXT_TITLE, (20, 20))

            pygame.draw.rect(self.SCREEN, 'Black', BUTTON_LEVEL_0)
            self.SCREEN.blit(BUTTON_LEVEL_0_TEXT, (BUTTON_LEVEL_0.x + 10, BUTTON_LEVEL_0.y + 5))

            self.SCREEN.blit(TEXT_CHARACTER_SELECT, (WIN_WIDTH / 1.5, 20))

            pygame.draw.circle(self.SCREEN, 'Red', (mx, my), 5)
            # Conditionals
            if BUTTON_LEVEL_0.collidepoint((mx, my)):
                if click:
                    self.level_0()
            click = False
            # Event Loop
            for event in pygame.event.get():
                # Keyboard Presses
                if event.type == pygame.KEYDOWN:
                    # Escape Key
                    if event.key == pygame.K_ESCAPE:
                        running = False
                # Close Button
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            pygame.display.update()
            self.CLOCK.tick(FPS)

    def level_0(self):
        # Local variables
        running = True
        click = False
        BACKGROUND = pygame.transform.scale(pygame.image.load('background/unwind-cafe-world-3.png'), (WIN_WIDTH, WIN_HEIGHT))
        TEXT_TITLE = self.FONT.render("Level 0", False, 'Black')
        # Character Select
        if self.character == "Drip":
            player = Drip(WIN_WIDTH / 8, WIN_HEIGHT / 2)
        else:
            player = Drip(WIN_WIDTH / 8, WIN_HEIGHT / 2)
        while running:
            # Redefine Variables
            mx, my = pygame.mouse.get_pos()
            # Drawing
            self.SCREEN.blit(BACKGROUND, (0, 0))
            self.SCREEN.blit(TEXT_TITLE, (20, 20))

            player.main(self.SCREEN, mx, my)

            if click:
                pygame.draw.circle(self.SCREEN, 'Green', (mx, my), 5)
            else:
                pygame.draw.circle(self.SCREEN, 'Red', (mx, my), 5)

            # Event Loop
            for event in pygame.event.get():
                # Keyboard Presses
                if event.type == pygame.KEYDOWN:
                    # Escape Key
                    if event.key == pygame.K_ESCAPE:
                        running = False
                # Close Button
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        click = False
            pygame.display.update()
            self.CLOCK.tick(FPS)


g = Glowing()
g.main_menu()

pygame.quit()
sys.exit()
