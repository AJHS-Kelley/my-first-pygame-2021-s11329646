# Pygame Collision Detection practice, Erkiq King, January 24, 2022, 1:55pm, v0.5

import pygame, sys, random
from pygame.locals import *

# Setup Pygame
pygame.init()
mainClock = pygame.time.Clock() 

#setup the pygame window
WINDOWWIDTH = 400
WINDOWHIGHT = 400
windowsurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHIGHT), 0, 32)
pygame.display.set_caption('Collision Detection 2022')

#setup colors.
BLACK = ( 0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# setup the player and food data structures
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300, 100, 50, 50)
foods = {}

for i in range(20)
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE),random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))
    
# Movement Variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6