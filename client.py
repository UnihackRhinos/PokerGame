import pygame
import sys


# initialise the game and screen size
pygame.init()  # initialize pygame

clock = pygame.time.Clock()

screen = pygame.display.set_mode((615, 410))


# Background and game title
bg = pygame.image.load('table.jpg').convert_alpha()

pygame.display.set_caption('Funny Fellows Poker')

# game loop
while True:
    # run at 30 frames per second since not many moving parts
    clock.tick(30)

    screen.blit(bg, (0, 0))

    x, y = pygame.mouse.get_pos()


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()


    pygame.display.update()
