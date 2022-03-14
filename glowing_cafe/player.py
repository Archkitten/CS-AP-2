import pygame
from config import *
from star import Star


class Player:
    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.RADIUS = 10
        self.SPEED = 7
        self.COLOR = 'White'
        self.circle = (self.x, self.y)

        self.projectiles = []
        self.projectile_counter = 0
        self.PROJECTILE_COOLDOWN = 1

    # Main - Run all other functions.
    def main(self, screen, target_x, target_y):
        self.move()
        self.animate()
        self.shoot(target_x, target_y)
        self.display_projectiles(screen)
        self.circle = (self.x, self.y)
        pygame.draw.circle(screen, self.COLOR, self.circle, self.RADIUS)

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
        # Speed modifiers:
        # If the player is going diagonal divide their speed by 1/math.sqrt(2).
        # If the player is shooting, divide their speed by 2.
        current_speed = self.SPEED
        if key_count >= 2:
            current_speed *= 0.7071
        if keys[pygame.K_SPACE]:
            current_speed *= 0.5
        # If the character is trying to go out of bounds, don't move.
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.x <= 0 + self.RADIUS:
                self.x -= 0
            else:
                self.x -= current_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.x >= WIN_WIDTH - self.RADIUS:
                self.x += 0
            else:
                self.x += current_speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.y <= 0 + self.RADIUS:
                current_speed = 0
            self.y -= current_speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.y >= WIN_HEIGHT - self.RADIUS:
                current_speed = 0
            self.y += current_speed

    # Animate
    def animate(self):
        pass

    # Shoot
    def shoot(self, tx, ty):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.projectile_counter == self.PROJECTILE_COOLDOWN:
            self.projectiles.append(Star(self.x, self.y, tx, ty))

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
