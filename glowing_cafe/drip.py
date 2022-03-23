import pygame
from config import *
from player import Player
from projectile import Star
from spritesheet import SpriteSheet


class Drip(Player):
    # Constructor
    def __init__(self, x, y):
        super().__init__(x, y)
        self.SPEED = 7
        self.SLOW_PERCENT = 0.5
        self.COLOR = 'Yellow'

        self.PROJECTILE_COOLDOWN = 30

        self.KEY_SHOOT = pygame.K_c
        self.KEY_LEFT = pygame.K_a
        self.KEY_RIGHT = pygame.K_d
        self.KEY_UP = pygame.K_w
        self.KEY_DOWN = pygame.K_s

        self.health = 4
        self.MAX_HEALTH = 4
        self.HEALTH_BAR_POSITION = 3

        self.SPRITE_SHEET = SpriteSheet('img/CharacterAkhil.png')
        self.sprite_sheet_x = 0
        self.sprite_sheet_y = 0
        self.image = self.SPRITE_SHEET.get_sprite(self.sprite_sheet_x * 200, self.sprite_sheet_y * 250, 200, 250)
        self.animation_frame = 0
        self.ANIMATION_COOLDOWN = 3

        self.INTRO_DURATION = 68

    # Intro Animate
    def intro_animate(self, screen):
        # Slide In
        self.x = PLAYER_START_WIDTH - (self.INTRO_DURATION - self.intro_counter) * 2.5
        # Part One - Words
        if self.intro_counter < 40:
            # :flushed:
            self.sprite_sheet_y = int(self.intro_counter / 4)
            intro_words = self.SPRITE_SHEET.get_sprite(100, self.sprite_sheet_y * 53 + 1355, 200, 50)
            intro_words = pygame.transform.scale(intro_words, (200 * 0.4, 53 * 0.4))
            screen.blit(intro_words, (self.x - 40, self.y - 60))
            # Body
            intro_image = self.SPRITE_SHEET.get_sprite(25, 1180, 310, 160)
            intro_image = pygame.transform.scale(intro_image, (310 * 0.4, 160 * 0.4))
            screen.blit(intro_image, (self.x - 60, self.y - 35))
        # Part Two - Cube
        elif self.intro_counter >= 40 and self.intro_counter < 47:
            intro_image = self.SPRITE_SHEET.get_sprite(380, 1000, 310, 400)
            intro_image = pygame.transform.scale(intro_image, (310 * 0.4, 400 * 0.4))
            screen.blit(intro_image, (self.x - 60, self.y - 110))
        elif self.intro_counter >= 47 and self.intro_counter < 54:
            intro_image = self.SPRITE_SHEET.get_sprite(685, 1080, 230, 270)
            intro_image = pygame.transform.scale(intro_image, (230 * 0.4, 270 * 0.4))
            screen.blit(intro_image, (self.x - 60, self.y - 70))
        elif self.intro_counter >= 54 and self.intro_counter < 61:
            intro_image = self.SPRITE_SHEET.get_sprite(915, 1080, 230, 270)
            intro_image = pygame.transform.scale(intro_image, (230 * 0.4, 270 * 0.4))
            screen.blit(intro_image, (self.x - 60, self.y - 70))
        else:
            intro_image = self.SPRITE_SHEET.get_sprite(1145, 1080, 230, 270)
            intro_image = pygame.transform.scale(intro_image, (230 * 0.4, 270 * 0.4))
            screen.blit(intro_image, (self.x - 60, self.y - 70))

    # Shoot
    def shoot(self, tx, ty, keys):
        if keys[self.KEY_SHOOT] and self.projectile_counter == self.PROJECTILE_COOLDOWN:
            # Cannot shoot if hurt.
            if self.i_frames == 0:
                self.projectiles.append(Star(self.x + 10, self.y - 35, tx, ty))

        if self.projectile_counter >= self.PROJECTILE_COOLDOWN:
            self.projectile_counter = 0
        self.projectile_counter += 1

    # Animate
    def animate(self, screen, keys):
        # Conditionals
        # Hurt Animation (Priority)
        if self.i_frames > 0:
            if self.i_frames > 40:
                self.sprite_sheet_x = 0
            elif self.i_frames > 30:
                self.sprite_sheet_x = 1
            elif self.i_frames > 20:
                self.sprite_sheet_x = 2
            elif self.i_frames > 10:
                self.sprite_sheet_x = 3
            self.sprite_sheet_y = 2
        # Shooting Animation
        elif keys[self.KEY_SHOOT]:
            # Animation Cooldown
            if self.animation_frame == self.ANIMATION_COOLDOWN:
                self.sprite_sheet_x += 1
                self.animation_frame = 0
            else:
                self.animation_frame += 1
            # self.sprite_sheet_x += 1
            self.sprite_sheet_y = 1
            # If animation is complete, loop it.
            if self.sprite_sheet_x > 5 * 1:
                self.sprite_sheet_x = 0
        # Idle Animation
        else:
            self.sprite_sheet_x = 0
            self.sprite_sheet_y = 0

        self.image = self.SPRITE_SHEET.get_sprite(self.sprite_sheet_x * 200, self.sprite_sheet_y * 250, 200, 250)
        self.image = pygame.transform.scale(self.image, (200 * 0.4, 250 * 0.4))
        screen.blit(self.image, (self.x - 40, self.y - 65))

    # Ghost Animate
    def ghost_animate(self, screen):
        # Animation Cooldown
        if self.animation_frame == 15:
            self.sprite_sheet_x += 1
            self.animation_frame = 0
        else:
            self.animation_frame += 1
        # If animation is complete, loop it.
        if self.sprite_sheet_x > 1:
            self.sprite_sheet_x = 0
        self.sprite_sheet_y = 3

        self.image = self.SPRITE_SHEET.get_sprite(self.sprite_sheet_x * 200, self.sprite_sheet_y * 250, 200, 250)
        self.image = pygame.transform.scale(self.image, (200 * 0.4, 250 * 0.4))
        screen.blit(self.image, (self.x - 40, self.y - 65))
