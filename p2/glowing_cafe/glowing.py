import pygame
import sys
import random
from config import *
from blob import Blob
from drip import Drip
from ro import Ro
from boss import Boss


class Glowing:
    def __init__(self):
        # Pygame Window Constants (REQUIRED)
        self.CLOCK = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption(GAME_TITLE)
        self.SCREEN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.FONT = pygame.font.Font('font/PixelType.ttf', 32)
        # Dynamic Variables
        self.BLOB = False
        self.DRIP = False
        self.RO = False
        # Music
        self.arch_birthday_music = pygame.mixer.Sound('audio/Arch_Birthday.ogg')
        self.arch_birthday_music.set_volume(MUSIC_VOLUME)

    def main_menu(self):
        # Local Variables
        running = True
        click = False

        # Level Selection Variables

        TEXT_TITLE = self.FONT.render("Glowing Cafe", False, 'Black')

        BUTTON_LEVEL_0 = pygame.Rect(20, 50, 100, 25)
        BUTTON_LEVEL_0_TEXT = self.FONT.render("Level 0", False, 'White')

        # Character Selection Variables

        TEXT_CHARACTER_SELECT = self.FONT.render("Character Select", False, 'Black')

        BUTTON_BLOB = pygame.Rect(WIN_WIDTH / 1.5, 50, 150, 200)
        BUTTON_DRIP = pygame.Rect(WIN_WIDTH / 1.5, 275, 150, 200)
        BUTTON_RO = pygame.Rect(WIN_WIDTH / 1.5, 500, 150, 200)

        while running:
            # Redefine Variables
            mx, my = pygame.mouse.get_pos()
            # Drawing
            self.SCREEN.fill('White')

            self.SCREEN.blit(TEXT_TITLE, (20, 20))

            # Level Selection

            pygame.draw.rect(self.SCREEN, 'Black', BUTTON_LEVEL_0)
            self.SCREEN.blit(BUTTON_LEVEL_0_TEXT, (BUTTON_LEVEL_0.x + 10, BUTTON_LEVEL_0.y + 5))

            # Character Selection

            self.SCREEN.blit(TEXT_CHARACTER_SELECT, (WIN_WIDTH / 1.5, 20))

            if self.BLOB == False:
                pygame.draw.rect(self.SCREEN, 'Purple', BUTTON_BLOB)
            else:
                pygame.draw.rect(self.SCREEN, 'Green', BUTTON_BLOB)
            if self.DRIP == False:
                pygame.draw.rect(self.SCREEN, 'Yellow', BUTTON_DRIP)
            else:
                pygame.draw.rect(self.SCREEN, 'Green', BUTTON_DRIP)
            if self.RO == False:
                pygame.draw.rect(self.SCREEN, 'Gray', BUTTON_RO)
            else:
                pygame.draw.rect(self.SCREEN, 'Green', BUTTON_RO)

            # Mouse
            if click:
                pygame.draw.circle(self.SCREEN, 'Green', (mx, my), 5)
            else:
                pygame.draw.circle(self.SCREEN, 'Red', (mx, my), 5)
            # Conditionals
            if BUTTON_LEVEL_0.collidepoint((mx, my)):
                if click:
                    self.level_0()
            if BUTTON_BLOB.collidepoint((mx, my)):
                if click:
                    if self.BLOB == False:
                        self.BLOB = True
                    else:
                        self.BLOB = False
            if BUTTON_DRIP.collidepoint((mx, my)):
                if click:
                    if self.DRIP == False:
                        self.DRIP = True
                    else:
                        self.DRIP = False
            if BUTTON_RO.collidepoint((mx, my)):
                if click:
                    if self.RO == False:
                        self.RO = True
                    else:
                        self.RO = False
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
        # BACKGROUND = pygame.transform.scale(pygame.image.load('background/unwind-cafe-world-3.png'), (WIN_WIDTH, WIN_HEIGHT))
        # BACKGROUND = pygame.transform.scale(pygame.image.load('background/unwind-cafe-world-3.png'), (WIN_WIDTH, WIN_HEIGHT))
        # BACKGROUND = pygame.transform.scale(pygame.image.load('background/unwind-cafe-world-3.png'), (WIN_WIDTH, WIN_HEIGHT))
        TEXT_TITLE = self.FONT.render("Level 0", False, 'Black')
        # Music
        self.arch_birthday_music.play(loops=-1)
        # Character Select
        blob = Blob(PLAYER_START_WIDTH, BLOB_START_HEIGHT)
        drip = Drip(PLAYER_START_WIDTH, DRIP_START_HEIGHT)
        ro = Ro(PLAYER_START_WIDTH, RO_START_HEIGHT)
        boss = Boss(WIN_WIDTH / 1.2, WIN_HEIGHT / 2)
        # Scuffed Revive System
        players_that_can_revive_blob = []
        players_that_can_revive_drip = []
        players_that_can_revive_ro = []
        players_that_can_revive_boss = []
        if self.BLOB == True:
            players_that_can_revive_drip.append(blob)
            players_that_can_revive_ro.append(blob)
        if self.DRIP == True:
            players_that_can_revive_blob.append(drip)
            players_that_can_revive_ro.append(drip)
        if self.RO == True:
            players_that_can_revive_blob.append(ro)
            players_that_can_revive_drip.append(ro)
        while running:
            # Redefine Variables
            mx, my = pygame.mouse.get_pos()
            # Drawing
            # self.SCREEN.blit(BACKGROUND, (0, 0))
            # self.SCREEN.blit(BACKGROUND, (0, 0))
            # self.SCREEN.blit(BACKGROUND, (0, 0))
            self.SCREEN.fill('Black')
            # self.SCREEN.blit(BACKGROUND, (0, 0))
            # self.SCREEN.blit(BACKGROUND, (0, 0))
            # self.SCREEN.blit(BACKGROUND, (0, 0))
            self.SCREEN.blit(TEXT_TITLE, (20, 20))

            if self.BLOB == True:
                blob.main(self.SCREEN, boss.x, boss.y, boss.projectiles, players_that_can_revive_blob)
            if self.DRIP == True:
                drip.main(self.SCREEN, boss.x, boss.y, boss.projectiles, players_that_can_revive_drip)
            if self.RO == True:
                ro.main(self.SCREEN, boss.x, boss.y, boss.projectiles, players_that_can_revive_ro)

            # Player Projectiles
            player_projectiles = blob.projectiles + drip.projectiles + ro.projectiles
            # Boss Targeting System
            target = random.randint(1, 3)
            if target == 1:
                boss.main(self.SCREEN, blob.x, blob.y, player_projectiles, players_that_can_revive_boss)
            elif target == 2:
                boss.main(self.SCREEN, drip.x, drip.y, player_projectiles, players_that_can_revive_boss)
            elif target == 3:
                boss.main(self.SCREEN, ro.x, ro.y, player_projectiles, players_that_can_revive_boss)


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
        # Stop music if the while loop ends.
        self.arch_birthday_music.stop()


g = Glowing()
g.main_menu()

pygame.quit()
sys.exit()
