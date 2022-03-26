from p2.deep_blue_fish.util.config import *
import pygame
import sys


class UIMenu:
    def __init__(self):
        # Pygame Window Constants (REQUIRED)
        self.CLOCK = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption(GAME_TITLE)
        self.SCREEN = pygame.display.set_mode((1600 * WIN_SCALE, 900 * WIN_SCALE))
        # Running
        self.running = True
        # Click
        self.left_click = False
        self.mx, self.my = pygame.mouse.get_pos()

    # Call other functions
    def __call__(self):
        while self.running:
            self.mx, self.my = pygame.mouse.get_pos()
            # While Loop
            self.while_loop()
            # Event For Loop
            for event in pygame.event.get():
                self.event_loop(event)
            # Update
            self.update()

    def while_loop(self):
        pass

    def event_loop(self, event):
        # X PROGRAM
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # KEYBOARD PRESSES
        if event.type == pygame.KEYDOWN:
            # Escape Key
            if event.key == pygame.K_ESCAPE:
                pass
        # MOUSE
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.left_click = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.left_click = False

    def update(self):
        pygame.display.update()
        self.CLOCK.tick(FPS)
