import pygame
import random

class Enemy:
    def __init__(self, num_of_enemies):
        self.images = [pygame.image.load('assets/Images/aandBhat.jpg') for _ in range(num_of_enemies)]
        self.rects = [image.get_rect() for image in self.images]
        self.speed = 1
        self.num_of_enemies = num_of_enemies
        self.init_enemies()

    def init_enemies(self):
        for i in range(self.num_of_enemies):
            self.rects[i].x = random.randint(0, 736)
            self.rects[i].y = random.randint(50, 150)

    def move(self, screen_height):
        for rect in self.rects:
            rect.y += self.speed
            if rect.y > screen_height:
                self.reset_enemy(rect)

    def reset_enemy(self, rect):
        rect.y = random.randint(-500, -50)
        rect.x = random.randint(0, 736)

    def draw(self, screen):
        for rect in self.rects:
            screen.blit(self.images[self.rects.index(rect)], rect)

    def is_collision(self, bullet_rect):
        for rect in self.rects:
            if rect.colliderect(bullet_rect):
                return True
        return False

