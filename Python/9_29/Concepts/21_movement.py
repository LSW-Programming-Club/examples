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

def player(x,y):
    screen.blit(playerImg,(x,y))


running = True

# Game Loop
while running:
    # Look through all events in the game
    for event in pygame.event.get():
        # If the quit button is pressed stop the game
        if event.type == pygame.QUIT:
            running = False
    # Have to redraw background on every frame
    screen.fill((0, 0, 0))
    # Move the player to the right 0.1 pixels every frame
    playerX += 0.1
    player(playerX,playerY)
    pygame.display.update()
