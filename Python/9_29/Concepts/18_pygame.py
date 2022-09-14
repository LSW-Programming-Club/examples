#!/usr/bin/env python3

import pygame

# Initialize pygame library
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800,600))


running = True

# Game Loop
while running:
    # Look through all events in the game
    for event in pygame.event.get():
        # If the quit button is pressed stop the game
        if event.type == pygame.QUIT:
            running = False
