import pygame
from pygame import mixer

class Bullet:
    def __init__(self, x, y):
        self.image = pygame.image.load('assets/Images/bullet.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10

    def move(self):
        self.rect.y -= self.speed
        bulletSound = mixer.Sound("assets/Sounds/laser.wav")
        bulletSound.play()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
