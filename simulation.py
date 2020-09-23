# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23rd 2020

@author: TomasGadea
"""

import pygame
import time
import numpy as np

WIDTH, HEIGHT = 800, 800
nX, nY = 10, 10
xSize = WIDTH/nX
ySize = HEIGHT/nY

pygame.init()  # Initialize PyGame

screen = pygame.display.set_mode([WIDTH, HEIGHT])  # Set size of screen

BG_COLOR = (10, 10, 10)  # Define background color
LIVE_COLOR = (255, 255, 255)
DEAD_COLOR = (128, 128, 128)


pauseRun = False

running = True
while running:

    # newStatus = np.copy(status) # Copy status

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            pauseRun = not pauseRun

        """mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            x, y = int(np.floor(posX/xSize)), int(np.floor(posY/ySize))
            #newStatus[x,y] = np.abs(newStatus[x,y]-1)
            newStatus[x, y] = not mouseClick[2]"""

    screen.fill(BG_COLOR)  # Clean background


pygame.quit()
