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

#Load our game font
custom_font = pygame.font.Font("assets/fonts/hollowpoint.ttf",80)

#Creating a function to draw the background
def draw_background(surf):
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
    text = custom_font.render("Chomp",True,(255,0,0))
    surf.blit(text,(SCREEN_WIDTH/2 - text.get_width()/2,0))


def draw_fishes(surf):
    text = custom_font.render("Chomp",True,(255,0,0))
    #Load fish tiles from sprites
    green_fish = pygame.image.load("assets/sprites/green_fish.png").convert()
    green_fish.set_colorkey((0,0,0)) # Set transparency
    num_green = random.randint(1,5)
    for _ in range(num_green):
        x = random.randint(0,SCREEN_WIDTH-TILE_SIZE)
        y = random.randint(text.get_height(),SCREEN_HEIGHT-(TILE_SIZE*2))
        flip = random.randint(0,1)
        if flip == 0:
            surf.blit(green_fish,(x,y))
        else:
            #green_fish = pygame.transform.flip(green_fish,True,False)
            surf.blit(pygame.transform.flip(green_fish,True,False), (x, y))

    #puffer fish
    puffer_fish = pygame.image.load("assets/sprites/puffer_fish.png").convert()
    puffer_fish.set_colorkey((0, 0, 0))  # Set transparency
    num_puffer = random.randint(1, 5)
    for _ in range(num_puffer):
        x = random.randint(0, SCREEN_WIDTH - TILE_SIZE)
        y = random.randint(text.get_height(), SCREEN_HEIGHT - (TILE_SIZE * 2))
        flip = random.randint(0,1)
        if flip == 0:
            surf.blit(puffer_fish, (x, y))
        else:
            #puffer_fish = pygame.transform.flip(puffer_fish,True,False)
            surf.blit(pygame.transform.flip(puffer_fish,True,False), (x, y))

#Main Loop:
running = True
background = screen.copy()
draw_background(background)

draw_fishes(background)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #draw background
    screen.blit(background,(0,0))

    #flip background
    pygame.display.flip()

pygame.quit()