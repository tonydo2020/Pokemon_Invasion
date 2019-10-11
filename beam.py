import pygame


# this file handles the beam that the alien fires, different from the beam that the ship fires
class Beam(pygame.sprite.Sprite):
    def __init__(self, ai_settings, screen, alien):
        super().__init__()
        self.screen = screen

        # Initialize beam image
        self.image = pygame.image.load('images/alien_beam_resized.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.bottom

        # Y position and speed factor
        self.y = float(self.rect.y)
        self.speed_factor = ai_settings.beam_speed_factor

    def update(self):
        # move beam
        self.y += self.speed_factor
        self.rect.y = self.y

    def blitme(self):
        # draw beam
        self.screen.blit(self.image, self.rect)
