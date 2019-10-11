import pygame
from pygame.sprite import Sprite


# this file handles the bullet that the ship fires
class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):
        # creates a bullet from the ship
        super().__init__()
        self.screen = screen
        # Create bullet at (0, 0) then set to correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # Store bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # move bullet
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        # draw bullet
        pygame.draw.rect(self.screen, self.color, self.rect)
