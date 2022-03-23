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
        self.MAX_HEALTH = 4
        self.uses_health_bar = False
        self.HEALTH_BAR_POSITION = 1
        self.i_frames = 0
        self.I_FRAMES = 60

        self.intro_counter = 0
        self.INTRO_DURATION = 1
        self.alive = "Intro"
        self.gravity = 0
        self.START_WIDTH = PLAYER_START_WIDTH
        self.START_HEIGHT = WIN_HEIGHT / 2

    # Main - Run all other functions.
    def main(self, screen, target_x, target_y, enemy_projectiles):
        if self.alive == "Intro":
            self.intro()
            self.intro_animate(screen)
            self.intro_bars(screen)
        elif self.alive == "Alive":
            keys = pygame.key.get_pressed()
            self.move(keys)
            self.animate(screen, keys)
            self.shoot(target_x, target_y, keys)
            self.detect_collisions(screen, enemy_projectiles)
            self.circle = (self.x, self.y)
            pygame.draw.circle(screen, self.color, self.circle, self.RADIUS)
        elif self.alive == "Ghost":
            self.ghost()
            self.ghost_collision()
            self.ghost_animate(screen)
        elif self.alive == "Dead":
            self.x = self.START_WIDTH
            self.y = self.START_HEIGHT
        self.display_projectiles(screen)

    # Intro
    def intro(self):
        self.intro_counter += 1
        if self.intro_counter == self.INTRO_DURATION:
            self.alive = "Alive"

    # Intro Animate
    def intro_animate(self, screen):
        pass

    # Intro Health Bars
    def intro_bars(self, screen):
        # Draw health bar based on health.
        if self.uses_health_bar:
            pygame.draw.rect(screen, self.COLOR,
                             (20, 20 * self.HEALTH_BAR_POSITION, (WIN_WIDTH - 40) / self.MAX_HEALTH * (self.intro_counter), 20))
        # Draw health blobs based on health.
        else:
            hearts = self.health
            while (hearts > 0):
                pygame.draw.circle(screen, self.COLOR, (35 * hearts, 30 * self.HEALTH_BAR_POSITION), 10)
                hearts -= 1

    # Move
    def move(self, keys):
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
    def animate(self, screen, keys):
        pass

    # Shoot
    def shoot(self, tx, ty, keys):
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

    def detect_collisions(self, screen, projectiles):
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

        # Draw health bar based on health.
        if self.uses_health_bar:
            pygame.draw.rect(screen, self.COLOR, (20, 20 * self.HEALTH_BAR_POSITION, (WIN_WIDTH - 40) / self.MAX_HEALTH * self.health, 20))
        # Draw health blobs based on health.
        else:
            hearts = self.health
            while (hearts > 0):
                pygame.draw.circle(screen, self.COLOR, (35 * hearts, 30 * self.HEALTH_BAR_POSITION), 10)
                hearts -= 1

        # Prevent health from going beyond max health. Also die after reaching zero health.
        if self.health > self.MAX_HEALTH:
            self.health = self.MAX_HEALTH
        if self.health <= 0:
            self.alive = "Ghost"

    # Ghost
    def ghost(self):
        self.gravity += 0.02
        self.y -= self.gravity

    # Ghost Collision
    def ghost_collision(self):
        if self.y <= -100:
            self.alive = "Dead"

    # Ghost Animate
    def ghost_animate(self, screen):
        pass
