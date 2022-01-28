# Pygame Collision Detection practice, Erkiq King, January 26, 2022, 1:06pm, v1.1a-BUGFIX

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

# Run te game loop.
while True:
    #Check for events.
    for event in pygame.event.get()
        if event.type == QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            #change the keyboard variables.
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:  
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            #check to see if the player has stopped moving.
            if event.key == K_LEFT or event.key == K_a: 
                moveleft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s: 
                 moveDown = False
            if event.key == K_x: #Use x to teleport the player.
                player.top = random.randint(0, WINDOWHIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)        

        if event.type == MOUSEBUTTONUP:
            food.append(pygame.Rect(event.pos{0}, event.pos{1}, FOODSIZE, FOODSIZE))

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), FOODSIZE, FOODSIZE)) 


    #draw white background on Window Surface.
    windowsurface.fill(WHITE) 

    # Move the player. 
    if moveDown and player.bottom < WINDOWHIGHT
            player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH
        player.right += MOVESPEED

    #draw the player on the surface.
    pygame.draw.rect(windowsurface, BLACK, player) 

    # Check for player colliding with food(s)
    for food in foods [:]: 
        if player.colliderect(food):
            foods.remove(food)

    #Draw the food.
    for i in range(len(foods)):
        pygame.draw.rect(windowsurface, GREEN, foods[i])     