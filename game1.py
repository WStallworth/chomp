import pygame
import random
import sys

#Initialize PyGame
pygame.init()

#Screen Dimensions:
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 64


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Sandy Beach with Sea Grass")

#Creating a function to draw the background
def draw_background(screen):
    #load our tiles
    water = pygame.image.load("assets/sprites/water.png").convert()
    seagrass = pygame.image.load("assets/sprites/seagrass.png").convert()
    sand = pygame.image.load("assets/sprites/sand_top.png").convert()
    #Use PNG transparncy
    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    #Fill the Screen
    for x in range(0,SCREEN_WIDTH, TILE_SIZE):
        for y in range(0,SCREEN_HEIGHT,TILE_SIZE):
            screen.blit(water,(x,y))

    #Draw the sand bottom
    for x in range(0,SCREEN_WIDTH,TILE_SIZE):
        screen.blit(sand,(x,SCREEN_HEIGHT-TILE_SIZE))

    #draw seagrass
    for _ in range(7):
        x = random.randint(0,SCREEN_WIDTH)
        y = SCREEN_HEIGHT-TILE_SIZE*2
        screen.blit(seagrass,(x,y))

#Main Loop:
running = True
background = screen.copy()
draw_background(background)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #draw background
    screen.blit(background,(0,0))

    #flip background
    pygame.display.flip()

pygame.quit()
