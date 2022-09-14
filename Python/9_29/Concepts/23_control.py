#!/usr/bin/env python3

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


def player(x, y):
    screen.blit(playerImg, (x, y))


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
    player(playerX, playerY)
    pygame.display.update()
