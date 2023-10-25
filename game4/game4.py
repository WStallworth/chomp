import pygame
import random
import sys

from fish import Fish, fishes
#Initialize PyGame
pygame.init()

#Screen Dimensions:
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 64


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("A school of moving fish")

#clock objext
clock = pygame.time.Clock()


#Load our game font
custom_font = pygame.font.Font("../assets/fonts/hollowpoint.ttf", 80)



#Creating a function to draw the background
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
    text = custom_font.render("Chomp",True,(255,0,0))
    surf.blit(text,(SCREEN_WIDTH/2 - text.get_width()/2,0))

#Main loop
running = True
background = screen.copy()
draw_background(background)

#draw a fish on the screen
for _ in range(5):
    fishes.add(Fish(random.randint(SCREEN_WIDTH,SCREEN_WIDTH*1.5),random.randint(TILE_SIZE,SCREEN_HEIGHT-(TILE_SIZE*2))))
while running:
    #quit condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # draw background
    screen.blit(background, (0, 0))

    #Update fish location
    fishes.update()

    #check if any fish are off the screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width: # can also use tilesize
            fishes.remove(fish) #remoivng the fish from the sprite group
            fishes.add(Fish(random.randint(SCREEN_WIDTH,SCREEN_WIDTH + 50),random.randint(TILE_SIZE,SCREEN_HEIGHT-(TILE_SIZE*2))))

    #Draw the fish
    fishes.draw(screen)

    #update the display
    pygame.display.flip()

    #limit frame rate:
    clock.tick(60)

#quit pygame
pygame.quit()
sys.exit()