#!/usr/bin/env python3

from random import randint
import pygame

# Initialize pygame library
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title Icon and name
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('./src/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('./src/player.png')
playerX = 370
playerY = 480
player_speed = 0.3
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('./src/enemy.png')
enemyX = randint(0,736)
enemyY = randint(50,150)
enemy_speed = 0.3
enemyX_change = enemy_speed
enemy_drop = 50


def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))


running = True

# Game Loop
while running:
    # Look through all events in the game
    for event in pygame.event.get():
        # If the quit button is pressed stop the game
        if event.type == pygame.QUIT:
            running = False

    # If keystroke is pressed check whether its right or left and move playerX accordingly
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= player_speed
            if event.key == pygame.K_RIGHT:
                playerX_change += player_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_change += player_speed
            if event.key == pygame.K_RIGHT:
                playerX_change -= player_speed
    # Have to redraw background on every frame
    screen.fill((0, 0, 0))
    
    # Player Movement
    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736
    player(playerX, playerY)

    # Enemy Movement
    if enemyX <= 0:
        enemyX_change = enemy_speed
        enemyY += enemy_drop
    elif enemyX >= 736:
        enemyX_change = -enemy_speed
        enemyY += enemy_drop
    enemyX += enemyX_change
    enemy(enemyX,enemyY)
    pygame.display.update()
