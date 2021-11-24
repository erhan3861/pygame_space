import random

import pygame

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background “image: Freepik.com”
background = pygame.image.load('space.jpg')
background = pygame.transform.scale(background, (800, 600))

# Title and icon
pygame.display.set_caption("Space Invaders")

# https://www.flaticon.com/search?word=space&type=icon
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("spaceship.png")
playerImg = pygame.transform.scale(playerImg, (64, 64))
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load("enemy.png")
enemyImg = pygame.transform.scale(enemyImg, (64, 64))
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 1
enemyY_change = 40


# blit means draw
def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game Loop
running = True
while running:
    # RGB red,Green,Blue
    screen.fill((100, 10, 200))
    # background Image
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if key stroke is pressed check whether its right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            playerX_change = 3
        if event.key == pygame.K_LEFT:
            playerX_change = -3

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            playerX_change = 0
    # 5 = 5 + -0.1 -> 5 = 5 - 0.1

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 1
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -1
        enemyY += enemyY_change

    print(str(enemyX), "y= ", enemyY)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

