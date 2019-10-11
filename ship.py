import pygame


# file that has all the ship assets and the setup for it
class Ship(pygame.sprite.Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load ship image and set rect attributes
        self.ship_image = pygame.image.load('images/ship.bmp')
        self.image = self.ship_image
        self.death_images = [
            pygame.image.load('images/ship_death/ship_death1.bmp'),
            pygame.image.load('images/ship_death/ship_death2.bmp'),
            pygame.image.load('images/ship_death/ship_death3.bmp'),
            pygame.image.load('images/ship_death/ship_death4.bmp'),
            pygame.image.load('images/ship_death/ship_death5.bmp'),
            pygame.image.load('images/ship_death/ship_death6.bmp'),
            pygame.image.load('images/ship_death/ship_death7.bmp'),
            pygame.image.load('images/ship_death/ship_death8.bmp')
        ]
        self.death_index = None
        self.last_frame = None
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # sound
        self.ship_death_sound = pygame.mixer.Sound('ship_death.wav')
        self.ship_shoot = pygame.mixer.Sound('ship_shoot.wav')
        self.ship_death_sound.set_volume(0.5)
        self.ship_shoot.set_volume(0.5)
        self.channel = ai_settings.ship_channel
        # Moving status flags
        self.moving_right = False
        self.moving_left = False
        # Store center as decimal
        self.center = float(self.rect.centerx)
        self.dead = False

    def fire_weapon(self):
        self.channel.play(self.ship_shoot)

    def update(self):
        # Move right/left based on moving status flags, unless the ship is at the edge of the screen
        if not self.dead:
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.center += self.ai_settings.ship_speed_factor
            if self.moving_left and self.rect.left > 0:
                self.center -= self.ai_settings.ship_speed_factor

            self.rect.centerx = self.center
        else:
            time_test = pygame.time.get_ticks()
            if abs(time_test - self.last_frame) > 250:
                self.death_index += 1
                if self.death_index < len(self.death_images):
                    self.image = self.death_images[self.death_index]
                    self.last_frame = time_test
                else:
                    self.dead = False
                    self.image = self.ship_image

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def death(self):
        self.dead = True
        self.death_index = 0
        self.image = self.death_images[self.death_index]
        self.last_frame = pygame.time.get_ticks()
        self.channel.play(self.ship_death_sound)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
