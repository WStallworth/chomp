import random
import pygame
import sys
#Imports
from background import draw_background
from game_parameters import *

#Initialize pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Collecting Pygame events")

#clock objext
clock = pygame.time.Clock()

#Main loop
running = True
background = screen.copy()
draw_background(background)

while running:
    #quit condition
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("Huzzah! You pressed key up")
            if event.key == pygame.K_DOWN:
                print("You pressed the down key")

    #draw background
    screen.blit(background, (0, 0))

    # update the display
    pygame.display.flip()

    #limit frame rate:
    #clock.tick(60)

#quit pygame
pygame.quit()
sys.exit()

