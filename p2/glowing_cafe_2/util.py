import pygame
import sys
import json


class Config:
    data = {
        'GAME_TITLE': "Glowing Cafe 2",
        'GAME_ICON': 'img/Zap.png',
        'WIN_SCALE': 0.80,
        'TPS': 60,
        'MUSIC_VOLUME': 0.5,
    }

    @classmethod
    def load_data(cls):
        print('Loading disabled')
        # try:
        #     with open('config.txt') as config_file:
        #         Config.data = json.load(config_file)
        # except FileNotFoundError:
        #     pass
        # except:
        #     pass

    @classmethod
    def save_data(cls):
        print('Saving disabled')
        # with open("config.txt", 'w') as config_file:
        #     json.dump(Config.data, config_file)


class Menu:
    def __init__(self):
        # Pygame Window Constants (REQUIRED)
        self.clock = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption(Config.data['GAME_TITLE'])
        pygame.display.set_icon(pygame.image.load(Config.data['GAME_ICON']))
        win_width = 1600 * Config.data['WIN_SCALE']
        win_height = 900 * Config.data['WIN_SCALE']
        self.screen = pygame.display.set_mode((win_width, win_height))
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
        pygame.display.update()
        self.clock.tick(Config.data['TPS'])


class Text:
    def __init__(self, text, x, y, color, font, font_size):
        self.x = x
        self.y = y
        self.FONT = pygame.font.SysFont(font, int(font_size * Config.data['WIN_SCALE']))
        self.text_surf = self.FONT.render(text, True, color)
        self.text_rect = self.text_surf.get_rect(center=(self.x * Config.data['WIN_SCALE'], self.y * Config.data['WIN_SCALE']))

    def __call__(self, screen):
        screen.blit(self.text_surf, self.text_rect)
