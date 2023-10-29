import pygame
from game_parameters import *
import random

def draw_background(surf):
    #load our tiles
    water = pygame.image.load("../assets/sprites/water.png").convert()
    seagrass = pygame.image.load("../assets/sprites/seagrass.png").convert()
    sand = pygame.image.load("../assets/sprites/sand_top.png").convert()
    #Use PNG transparncy
    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    #Fill the Screen
    for x in range(0,SCREEN_WIDTH, TILE_SIZE):
        for y in range(0,SCREEN_HEIGHT,TILE_SIZE):
            surf.blit(water,(x,y))

    #Draw the sand bottom
    for x in range(0,SCREEN_WIDTH,TILE_SIZE):
        surf.blit(sand,(x,SCREEN_HEIGHT-TILE_SIZE))

    #draw seagrass
    for _ in range(7):
        x = random.randint(0,SCREEN_WIDTH)
        y = SCREEN_HEIGHT-TILE_SIZE*2
        surf.blit(seagrass,(x,y))

    #Draw text
    custom_font = pygame.font.Font("../assets/fonts/hollowpoint.ttf", 64)
    text = custom_font.render("Chomp",True,(255,0,0))
    surf.blit(text,(SCREEN_WIDTH/2 - text.get_width()/2,0))