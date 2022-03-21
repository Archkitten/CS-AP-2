import pygame
import math
from config import *
from projectile import Bullet


class Player:
    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.RADIUS = 10
        self.SPEED = 7
        self.SLOW_PERCENT = 0.5
        self.COLOR = 'White'
        self.color = 'White'
        self.circle = (self.x, self.y)

        self.projectiles = []
        self.projectile_counter = 0
        self.PROJECTILE_COOLDOWN = 1

        self.KEY_SHOOT = pygame.K_SPACE
        self.KEY_LEFT = pygame.K_LEFT
        self.KEY_RIGHT = pygame.K_RIGHT
        self.KEY_UP = pygame.K_UP
        self.KEY_DOWN = pygame.K_DOWN

        self.health = 4
        self.i_frames = 0
        self.I_FRAMES = 60

        self.alive = True

    # Main - Run all other functions.
    def main(self, screen, target_x, target_y, enemy_projectiles):
        if self.alive:
            self.move()
            self.animate()
            self.shoot(target_x, target_y)
            self.display_projectiles(screen)
            self.detect_collisions(enemy_projectiles)
            self.circle = (self.x, self.y)
            pygame.draw.circle(screen, self.color, self.circle, self.RADIUS)

    # Move
    def move(self):
        keys = pygame.key.get_pressed()
        # Check for diagonal movement.
        key_count = 0
        if keys[self.KEY_LEFT]:
            key_count += 1
        if keys[self.KEY_RIGHT]:
            key_count += 1
        if keys[self.KEY_UP]:
            key_count += 1
        if keys[self.KEY_DOWN]:
            key_count += 1
        # Speed modifiers:
        # If the player is going diagonal divide their speed by 1/math.sqrt(2).
        # If the player is shooting, divide their speed by 2.
        current_speed = self.SPEED
        if key_count >= 2:
            current_speed *= 0.7071
        if keys[self.KEY_SHOOT]:
            current_speed *= self.SLOW_PERCENT
        # If the character is trying to go out of bounds, don't move.
        if keys[self.KEY_LEFT]:
            if self.x <= 0 + self.RADIUS:
                self.x -= 0
            else:
                self.x -= current_speed
        if keys[self.KEY_RIGHT]:
            if self.x >= WIN_WIDTH - self.RADIUS:
                self.x += 0
            else:
                self.x += current_speed
        if keys[self.KEY_UP]:
            if self.y <= 0 + self.RADIUS:
                current_speed = 0
            self.y -= current_speed
        if keys[self.KEY_DOWN]:
            if self.y >= WIN_HEIGHT - self.RADIUS:
                current_speed = 0
            self.y += current_speed

    # Animate
    def animate(self):
        pass

    # Shoot
    def shoot(self, tx, ty):
        keys = pygame.key.get_pressed()
        if keys[self.KEY_SHOOT] and self.projectile_counter == self.PROJECTILE_COOLDOWN:
            self.projectiles.append(Bullet(self.x, self.y, tx, ty))

        if self.projectile_counter >= self.PROJECTILE_COOLDOWN:
            self.projectile_counter = 0
        self.projectile_counter += 1

    # Display and Delete Projectiles
    def display_projectiles(self, screen):
        for projectile in self.projectiles:
            if projectile.x < 0 - projectile.RADIUS or projectile.x > WIN_WIDTH + projectile.RADIUS:
                self.projectiles.remove(projectile)
            elif projectile.y < 0 - projectile.RADIUS or projectile.y > WIN_HEIGHT + projectile.RADIUS:
                self.projectiles.remove(projectile)
            projectile.main(screen)

    def detect_collisions(self, projectiles):
        for projectile in projectiles:
            distance = math.sqrt((self.x - projectile.x) ** 2 + (self.y - projectile.y) ** 2)
            if distance <= self.RADIUS and self.i_frames == 0:
                self.health -= 1
                self.i_frames = self.I_FRAMES

        # Change color upon getting hit.
        if self.i_frames > 0:
            self.color = 'Red'
        else:
            self.color = self.COLOR

        # Reduce i_frames by 1 every frame, also prevent i_frames from going negative.
        self.i_frames -= 1
        if self.i_frames < 0:
            self.i_frames = 0

        # Die after reaching zero health.
        if self.health <= 0:
            self.alive = False
