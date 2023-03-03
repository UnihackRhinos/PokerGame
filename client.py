import pygame
from network import Network
import sys

def displayCard(rank, suit, xcoord, ycoord):
    # displayCard(rank, suit)
    # rank- the cards value ace to king
    # suit- the cards suit, clubs hearts etc.
    # xcoord/ycoord- location of top left of image
    # function takes two strings and combines them to 
    # create an image name to then display in a given location 
    cardFile = rank + suit + ".jpg"
    location = (xcoord, ycoord)
    screen.blit(cardFile, location)
    pygame.display.update()

# initialise the game and screen size
pygame.init()  # initialize pygame

clock = pygame.time.Clock()

screen = pygame.display.set_mode((615, 410))


# Background and game title
bg = pygame.image.load('table.jpg').convert_alpha()

pygame.display.set_caption('Funny Fellows Poker')


def main():
    # game loop
    running = True
    net = Network() #network file 
    clock.tick(30)# run at 30 frames per second since not many moving parts
    screen.blit(bg, (0, 0)) # sets background to bg image
    
    player = int(net.getP())
    print("you are player: ",player)
    
    while running:
        x, y = pygame.mouse.get_pos()       
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()


        pygame.display.update()
