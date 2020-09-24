# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23rd 2020

@author: TomasGadea
"""

import pygame
import numpy as np
import time
import random

def outputStats(total, nBlue, nRed, iterations):

    print("iteration:", iterations)

    t = (4*total//10)
    b = (4*nBlue//10)
    r = (4*nRed//10)
    print("B: [", b*"*", (t-b)*".", "]", nBlue, '%', sep='')
    print("R: [", r*"*", (t-r)*".", "]", nRed, '%', sep='')



WIDTH, HEIGHT = 500, 500
nX, nY = 10, 10
xSize = WIDTH / nX
ySize = HEIGHT / nY

pygame.init()  # Initialize PyGame

screen = pygame.display.set_mode([WIDTH, HEIGHT])  # Set size of screen

red = (255, 160, 122)
blue = (65, 105, 225)

status = np.zeros((nX, nY))

pauseRun = True
running = True

iterations = 0

while running:
    iterations += 1

    for x in range(0, nX):
        for y in range(0, nY):
            poly = [(x*xSize, y*ySize),
                    ((x+1)*xSize, y*ySize),
                    ((x+1)*xSize, (y+1)*ySize),
                    (x*xSize, (y+1)*ySize)]

            if status[x, y] == 1:
                pygame.draw.polygon(screen, blue, poly, 0)
            else:
                pygame.draw.polygon(screen, red, poly, 0)






    newStatus = np.copy(status)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            pauseRun = not pauseRun

        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            x, y = int(np.floor(posX/xSize)), int(np.floor(posY/ySize))
            newStatus[x, y] = not mouseClick[2]


    if not pauseRun:

        # pick a random position x, y
        randX = random.randint(0, nX-1)
        randY = random.randint(0, nY-1)




        # change that position to either 1 of their 4 neighbours at random
        neighbour = random.randint(1, 4) # 1 up, 2 right, 3 down, 4 left
        if neighbour == 1:
            newStatus[randX, randY] = status[(randX-1) % (nX-1), randY]

        elif neighbour == 2:
            newStatus[randX, randY] = status[randX, (randY+1) % (nY-1)]

        elif neighbour == 3:
            newStatus[randX, randY] = status[(randX+1) % (nX-1), randY]

        elif neighbour == 4:
            newStatus[randX, randY] = status[randX, (randY-1) % (nY-1)]

        nBlue = int(np.sum(status))
        nRed = status.size - nBlue

        outputStats(status.size, nBlue, nRed, iterations)
        print()

        if nBlue == status.size:
            running = False
            print("BLUE-DOMINATION in", iterations, "iterations")
        elif nRed == status.size:
            running = False
            print("RED-DOMINATION in", iterations, "iterations")



    status = np.copy(newStatus)
    time.sleep(0.01)
    pygame.display.flip()


pygame.quit()
