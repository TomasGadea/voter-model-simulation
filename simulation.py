# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23rd 2020

@author: TomasGadea
"""

import pygame
import numpy as np
import time

WIDTH, HEIGHT = 800, 800
nX, nY = 10, 10
xSize = WIDTH / nX
ySize = HEIGHT / nY

pygame.init()  # Initialize PyGame

screen = pygame.display.set_mode([WIDTH, HEIGHT])  # Set size of screen

BG_COLOR = (255, 255, 255)  # Define background color

pause = False
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)  # Clean background

    for x in range(0, nX):
        for y in range(0, nY):

            poly = [(x*xSize, y*ySize),
                    ((x+1)*xSize, y*ySize),
                    ((x+1)*xSize, (y+1)*ySize),
                    (x*xSize, (y+1)*ySize)]

            pygame.draw.polygon(screen, (200, 200, 200), poly, 1)

    time.sleep(0.1)
    pygame.display.flip()


pygame.quit()
