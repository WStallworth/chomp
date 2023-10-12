import pygame
import sys

#Initialize PyGame
pygame.init()

#Screen Dimensions:
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Defining Colors:
BLUE = (0,0,255)
BROWN = (224,161,52)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Blue Background with Brown Rectangle")

#Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Fill Screen with blue
    screen.fill(BLUE)

    #Draw the brown rectangle:
    rectangle_height = 150
    pygame.draw.rect(screen,BROWN,(0,SCREEN_HEIGHT - rectangle_height,SCREEN_WIDTH,rectangle_height))

    #Update the display
    pygame.display.flip()

#Quit pygame
pygame.quit()