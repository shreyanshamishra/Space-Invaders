import pygame
from bullet import Bullet
class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load('assets/Images/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3
        self.bullet_speed = 10
        self.bullets = []

    def move(self, screen_width):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Boundary checking
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= screen_width - self.rect.width:
            self.rect.x = screen_width - self.rect.width

    def fire_bullet(self):
        bullet = Bullet(self.rect.x + self.rect.width // 2, self.rect.y)
        self.bullets.append(bullet)

    def update_bullets(self, screen_height):
        for bullet in self.bullets:
            bullet.move()
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for bullet in self.bullets:
            bullet.draw(screen)
