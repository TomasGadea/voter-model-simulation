# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25th 2020

@author: TomasGadea
"""


import numpy as np
import random
import argparse


# GLOBAL VARIABLES:

N = 10
k = 2


def parseArgs():

    parser = argparse.ArgumentParser(description="Stepping Stones.")

    	# add arguments
    parser.add_argument('--N', dest='N', required=False)
    parser.add_argument('--k', dest='k', required=False)
    args = parser.parse_args()

    	# set grid size
    if args.N and int(args.N) > 8:
        global N
        N = int(args.N)

    	# set number of alleles
    if args.k and int(args.k) > 1:
        global k
        k = int(args.k)

def randomGrid(N, k):
    grid = np.zeros((N, N))

    for i in range(N):
        for j in range(N):
            a = random.randint(0, k-1)
            grid[i, j] = a

    return grid

def customGrid(N):
    grid = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
    return grid

def chessGrid(N):
    grid = np.zeros((N, N))

    for i in range(N):
        for j in range(N):
            if (i+j) % 2 == 0:
                grid[i, j] = 1

    return grid


def occurrences(grid, k):
    return [np.count_nonzero(grid == num) for num in range(k)]

def main():

    parseArgs()

        # Create grid:
    grid = customGrid(N)
    print("Random grid:")
    print(grid)

    countList= occurrences(grid, k)

    print(countList)




    # data structure to store colors 'alive' and its count
    # begin loop, update grid, make counts
    # (abstreure el loop anterior per poder fer múltiples simulacions per estudiar stats)
    # run multiple tests
    # create stats
    # make conjectures


main()
