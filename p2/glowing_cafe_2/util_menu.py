from config import Config
import pygame
import sys


class Menu:
    def __init__(self):
        # Pygame Window Constants (REQUIRED)
        self.clock = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption(Config.data['GAME_TITLE'])
        pygame.display.set_icon(pygame.image.load(Config.data['GAME_ICON']))
        win_width = 3200 * Config.data['WIN_SCALE']
        win_height = 1800 * Config.data['WIN_SCALE']
        self.window = pygame.display.set_mode((win_width, win_height))
        self.screen = pygame.transform.scale(self.window, (win_width, win_height))
        # Running
        self.running = True
        # Timer
        self.timer = 0
        # Click
        self.left_click = False
        self.mx, self.my = pygame.mouse.get_pos()

    # Call other functions
    def __call__(self):
        while self.running:
            self.mx, self.my = pygame.mouse.get_pos()
            # While Loop
            self.while_loop()
            self.timer += 1
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
            Config.save_data()
            pygame.quit()
            sys.exit()
        # KEYBOARD PRESSES
        if event.type == pygame.KEYDOWN:
            # Escape Key
            if event.key == pygame.K_ESCAPE:
                self.running = False
        # MOUSE
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.left_click = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.left_click = False

    def update(self):
        # Window Resize
        self.window.blit(self.screen, (0, 0))
        # Update (Required)
        pygame.display.update()
        self.clock.tick(Config.data['FPS'])
