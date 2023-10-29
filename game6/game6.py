import pygame
import random
import sys

from game_parameters import *
from fish import Fish, fishes
from background import draw_background
from player import Player

#Initialize pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Adding a player fish on the screen")

#Clock object
clock = pygame.time.Clock()

#Main loop
running = True
background = screen.copy()
draw_background(background)

#Draw green fish on screen(technically off)
for _ in range(5):
    fishes.add(Fish(random.randint(SCREEN_WIDTH,SCREEN_WIDTH*1.5),random.randint(TILE_SIZE,SCREEN_HEIGHT-(TILE_SIZE*2))))

#create a player fish
player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

#Initialzie score for game
score = 0
score_font = pygame.font.Font("../assets/fonts/hollowpoint.ttf", 30)
text = score_font.render(f"Score : {score}",True,(0,0,0))

#Loading sound effects:
chomp = pygame.mixer.Sound("../assets/sounds/chomp.wav")

while running:
    #quit condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Control fish with keyboard
        player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()
            if event.key == pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()
    # draw background
    screen.blit(background, (0, 0))

    # Update fish location
    fishes.update()
    player.update()

    #Check for player and fish collision:
    result = pygame.sprite.spritecollide(player,fishes,True)
    if result:
        #play chomp sound
        pygame.mixer.Sound.play(chomp)
        score += len(result)
        for _ in range(len(result)):
            fishes.add(Fish(random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 50),
                            random.randint(TILE_SIZE, SCREEN_HEIGHT - (TILE_SIZE * 2))))

    # check if any fish are off the screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width:  # can also use tilesize
            fishes.remove(fish)  # remoivng the fish from the sprite group
            fishes.add(Fish(random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 50),
                            random.randint(TILE_SIZE, SCREEN_HEIGHT - (TILE_SIZE * 2))))

    # Draw the fish

    fishes.draw(screen)
    player.draw(screen)

    #Draw the score on the screen:
    text = score_font.render(f"Score : {score}", True, (0, 0, 0))
    screen.blit(text,((SCREEN_WIDTH-TILE_SIZE*3),0))
    # update the display
    pygame.display.flip()

    # limit frame rate:
    clock.tick(60)

# quit pygame
pygame.quit()
sys.exit()