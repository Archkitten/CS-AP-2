import pygame
from config import *


class Drip:
    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.SPEED = 7
        self.rect = (self.x, self.y, PLAYER_HIT_BOX_WIDTH, PLAYER_HIT_BOX_HEIGHT)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    # Main - Run all other functions.
    def main(self, screen):
        self.move()
        pygame.draw.rect(screen, 'Yellow', self.rect)

    # Move
    def move(self):
        keys = pygame.key.get_pressed()
        # Check for diagonal movement.
        key_count = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            key_count += 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            key_count += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            key_count += 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            key_count += 1
        # If the character is trying to go out of bounds, don't move.
        # If the player is going diagonal divide their speed by 1/math.sqrt(2).
        # Otherwise, move the player normally.
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.x <= 0:
                self.x -= 0
            elif key_count >= 2:
                self.x -= self.SPEED * 0.7071
            else:
                self.x -= self.SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.x >= WIN_WIDTH:
                self.x += 0
            elif key_count >= 2:
                self.x += self.SPEED * 0.7071
            else:
                self.x += self.SPEED
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.y <= 0:
                self.y -= 0
            elif key_count >= 2:
                self.y -= self.SPEED * 0.7071
            else:
                self.y -= self.SPEED
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.y >= WIN_HEIGHT:
                self.y += 0
            elif key_count >= 2:
                self.y += self.SPEED * 0.7071
            else:
                self.y += self.SPEED
