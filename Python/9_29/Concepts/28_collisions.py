#!/usr/bin/env python3

import math
from random import randint
import pygame

# Initialize pygame library
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('./src/background.png')

# Title Icon and name
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('./src/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('./src/player.png')
playerX = 370
playerY = 480
player_speed = 2
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('./src/enemy.png')
enemyX = randint(0, 736)
enemyY = randint(50, 150)
enemy_speed = 2
enemyX_change = enemy_speed
enemy_drop = 50

# Projectile
projectileImg = pygame.image.load('./src/projectile.png')
projectileX = 0
projectileY = 480
projectileY_change = 10
projectile_fired = False

score = 0

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_projectile(x, y):
    global projectile_fired
    projectile_fired = True
    screen.blit(projectileImg, (x+16, y + 10))

def isCollision(x1, y1, x2, y2):
    distance = math.sqrt((math.pow(x1-x2, 2) + math.pow(y1-y2, 2)))
    if distance < 27:
        return True
    else:
        return False

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
            if event.key == pygame.K_SPACE and not projectile_fired:
                projectileX = playerX
                fire_projectile(projectileX, projectileY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_change += player_speed
            if event.key == pygame.K_RIGHT:
                playerX_change -= player_speed
    # Have to redraw background on every frame
    screen.blit(background, (0, 0))

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
    enemy(enemyX, enemyY)

    # Projectile Movement
    if projectileY <= -32:
        projectileY = 480
        projectile_fired = False
    if projectile_fired:
        fire_projectile(projectileX, projectileY)
        projectileY -= projectileY_change

    # Collision
    collision = isCollision(enemyX,enemyY,projectileX,projectileY)
    if collision:
        projectileY = 480
        projectile_fired = False
        score += 1
        enemyX = randint(0, 736)
        enemyY = randint(50, 150)

    pygame.display.update()
