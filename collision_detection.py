# Pygame Collision Detection practice, Erkiq King, January 04, 2022, 2:29pm, v0.3

from myFirstPygame import GREEN
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
