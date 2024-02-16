# import math
# import random
# import pygame
# from pygame import mixer

# # Initialize pygame
# pygame.init()

# # Set up the screen
# screen = pygame.display.set_mode((800, 600))

# # Background
# background = pygame.image.load('assets/Images/background.jpg')

# # Sound
# mixer.music.load("assets/Sounds/background.wav")
# mixer.music.play(-1)

# # Caption and Icon
# pygame.display.set_caption("Space Invader")
# icon = pygame.image.load('assets/Images/ufo.png')
# pygame.display.set_icon(icon)

# # Player
# playerImg = pygame.image.load('assets/Images/player.png')
# playerX = 370
# playerY = 480
# playerX_change = 0

# # Enemy
# num_of_enemies = 6
# enemyImg = [pygame.image.load('assets/Images/enemy.png') for _ in range(num_of_enemies)]
# enemyX = [random.randint(0, 736) for _ in range(num_of_enemies)]
# enemyY = [random.randint(50, 150) for _ in range(num_of_enemies)]
# enemyX_change = [0.5 for _ in range(num_of_enemies)]  # Initial enemy speed
# enemyY_change = [3 for _ in range(num_of_enemies)]

# # Bullet
# bulletImg = pygame.image.load('assets/Images/bullet.png')
# bulletX = 0
# bulletY = 480
# bulletY_change = 10
# bullet_state = "ready"

# #power-up
# powerupImg = pygame.image.load('assets/Images/powerup.png')
# powerupX = 0
# powerupY = 0
# powerup_state = "ready"  # Indicates whether the power-up is currently active or not
# powerup_timer = 0  # Timer to track the duration of the power-up

# # Score
# score_value = 0
# font = pygame.font.Font('freesansbold.ttf', 32)
# textX = 10
# textY = 10

# # Game Over
# over_font = pygame.font.Font('freesansbold.ttf', 64)

# def show_score(x, y):
#     score = font.render("Score : " + str(score_value), True, (255, 255, 255))
#     screen.blit(score, (x, y))

# def game_over_text():
#     over_text = over_font.render("GAME OVER", True, (255, 255, 255))
#     screen.blit(over_text, (200, 250))

# def player(x, y):
#     screen.blit(playerImg, (x, y))

# def enemy(x, y, i):
#     screen.blit(enemyImg[i], (x, y))

# def fire_bullet(x, y):
#     global bullet_state
#     bullet_state = "fire"
#     screen.blit(bulletImg, (x + 16, y + 10))

# def isCollision(enemyX, enemyY, bulletX, bulletY):
#     distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
#     if distance < 27:
#         return True
#     else:
#         return False

# # Game Loop
# running = True
# while running:

#     screen.fill((0, 0, 0))
#     screen.blit(background, (0, 0))

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 playerX_change = -5
#             elif event.key == pygame.K_RIGHT:
#                 playerX_change = 5
#             elif event.key == pygame.K_SPACE:
#                 if bullet_state == "ready":
#                     bulletSound = mixer.Sound("assets/Sounds/laser.wav")
#                     bulletSound.play()
#                     bulletX = playerX
#                     fire_bullet(bulletX, bulletY)

#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                 playerX_change = 0

#     playerX += playerX_change

#     if playerX <= 0:
#         playerX = 0
#     elif playerX >= 736:
#         playerX = 736

#     for i in range(num_of_enemies):
#         if enemyY[i] > 440:
#             for j in range(num_of_enemies):
#                 enemyY[j] = 2000
#             game_over_text()
#             break

#         enemyX[i] += enemyX_change[i]
#         if enemyX[i] <= 0:
#             enemyX_change[i] = 2
#             enemyY[i] += enemyY_change[i]
#         elif enemyX[i] >= 736:
#             enemyX_change[i] = -2
#             enemyY[i] += enemyY_change[i]

#         # Collision
#         collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
#         if collision:
#             explosionSound = mixer.Sound("assets/Sounds/explosion.wav")
#             explosionSound.play()
#             bulletY = 480
#             bullet_state = "ready"
#             score_value += 1
#             enemyX[i] = random.randint(0, 736)
#             enemyY[i] = random.randint(50, 150)

#         enemy(enemyX[i], enemyY[i], i)

#     if bulletY <= 0:
#         bulletY = 480
#         bullet_state = "ready"

#     if bullet_state == "fire":
#         fire_bullet(bulletX, bulletY)
#         bulletY -= bulletY_change

#     player(playerX, playerY)
#     show_score(textX, textY)
#     pygame.display.update()

# pygame.quit()
import pygame
from pygame import mixer
from player import Player
from enemy import Enemy
from bullet import Bullet



# # Initialize pygame
# pygame.init()

# # Set up the screen
# screen = pygame.display.set_mode((800, 600))

# # Background
# background = pygame.image.load('assets/Images/background.jpg')

# # Sound
# mixer.music.load("assets/Sounds/background.wav")
# mixer.music.play(-1)

# # Create player object
# player = Player(370, 480)

# # Create enemy object
# num_of_enemies = 6
# enemy = Enemy(num_of_enemies)

# # Bullets
# bullets = []

# # Game Loop
# running = True
# while running:
#     screen.blit(background, (0, 0))

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 bulletSound = mixer.Sound("assets/Sounds/laser.wav")
#                 bulletSound.play()
#                 player.fire_bullet()

#     player.move(800)
#     enemy.move(600)
#     player.update_bullets(600)

#     # Check for collisions
#     for bullet in player.bullets:
#         if enemy.is_collision(bullet.rect):
#             explosionSound = mixer.Sound("assets/Sounds/explosion.wav")
#             explosionSound.play()
#             player.bullets.remove(bullet)

#     player.draw(screen)
#     enemy.draw(screen)

#     pygame.display.update()

# pygame.quit()
import pygame
from pygame import mixer
from player import Player
from enemy import Enemy
from bullet import Bullet

# Initialize pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))

# Font
font = pygame.font.Font(None, 36)

# Background
background = pygame.image.load('assets/Images/background.jpg')

# Sound
mixer.music.load("assets/Sounds/background.wav")
mixer.music.play(-1)

# Create player object
player = Player(370, 480)

# Create enemy object
num_of_enemies = 6
enemy = Enemy(num_of_enemies)

# Game Loop
running = True
score = 0
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bulletSound = mixer.Sound("assets/Sounds/laser.wav")
                bulletSound.play()
                player.fire_bullet()

    player.move(800)
    enemy.move(600)
    player.update_bullets(600)

    # Check for collisions
    for bullet in player.bullets:
        if enemy.is_collision(bullet.rect):
            explosionSound = mixer.Sound("assets/Sounds/explosion.wav")
            explosionSound.play()
            player.bullets.remove(bullet)
            score += 1  # Increase score when collision occurs

    player.draw(screen)
    enemy.draw(screen)

    # Render and display the score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
