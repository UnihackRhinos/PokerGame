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
    cardFile = rank + suit + ".png"
    card = pygame.image.load(cardFile).convert_alpha()
    # ----------------------------------------------
    #  locations of cards pixel wise
    #   first      (108, 142)
    #   second     (190, 142)
    #   third      (275, 142)
    #   fourth     (355, 142)
    #   fifth      (437, 142)
    # ----------------------------------------------
    location = (xcoord, ycoord)
    screen.blit(card, location)
    pygame.display.update()

def updateHUD(playerStack, oppStack, pot):
    playerText = font.render("stack: " + playerStack, True, (255,255,255))
    playerRect = pygame.Rect(220,350,80,50) #Rect(left, top, width, height)
    pygame.draw.rect(screen, (0,0,255),playerRect) # draw rectangle first so it doesn't cover text
    screen.blit(playerText, playerRect)

    oppText = font.render("stack: " + oppStack, True, (255,255,255))
    oppRect = pygame.Rect(220, 10, 80, 50)
    pygame.draw.rect(screen, (0,0,255),oppRect)
    screen.blit(oppText, oppRect)

    potText = font.render("pot: " + pot, True, (255,255,255))
    potRect = pygame.Rect(220, 100, 80, 40)
    pygame.draw.rect(screen, (255,0,0),potRect)
    screen.blit(potText, potRect)

def loadButtons(conditions):
    # conditions - boolean to determine if player can check or needs to call to not fold
    if conditions: # if 1 then needs to call, can also fold or bet
        screen.blit(betButtonText, betButtonRect)
        screen.blit(callButtonText, callButtonRect)
        screen.blit(foldButtonText, foldButtonRect)

        pygame.draw.rect(screen, (0,255,0),betButtonRect,2)
        pygame.draw.rect(screen, (0,255,0),callButtonRect,2)
        pygame.draw.rect(screen, (0,255,0),foldButtonRect,2)
        #update display
        pygame.display.flip()
    else: # bet check fold
        screen.blit(betButtonText, betButtonRect)
        screen.blit(checkButtonText, checkButtonRect)
        screen.blit(foldButtonText, foldButtonRect)

        pygame.draw.rect(screen, (0,255,0),betButtonRect,2)
        pygame.draw.rect(screen, (0,255,0),checkButtonRect,2)
        pygame.draw.rect(screen, (0,255,0),foldButtonRect,2)
        #update display
        pygame.display.flip()

# initialise the game and screen size
pygame.init()  # initialize pygame
pygame.font.init() # initialise fonts for text display

clock = pygame.time.Clock()

screen = pygame.display.set_mode((615, 410))


# Background and game title
bg = pygame.image.load('table.jpg').convert_alpha()

pygame.display.set_caption('Funny Fellows Poker')

font = pygame.font.SysFont('lucidasans', 15)

# defining buttons
betButtonText = font.render(" Bet ", True, (0,0,0))
betButtonRect = betButtonText.get_rect(topleft=(90,350))
checkButtonText = font.render(" Check ", True, (0,0,0))
checkButtonRect = checkButtonText.get_rect(topleft=(20,350))
callButtonText = font.render(" Call ", True, (0,0,0))
callButtonRect = callButtonText.get_rect(topleft=(20,350))
foldButtonText = font.render(" Fold ", True, (0,0,0))
foldButtonRect = foldButtonText.get_rect(topleft=(140,350))
printout = " "

def main():
    # game loop
    running = True
    net = Network() #network file 
    clock.tick(30)# run at 30 frames per second since not many moving parts
    screen.blit(bg, (0, 0)) # sets background to bg image
    
    player = int(net.getP())
    print("you are player: ",player)
    toAct = [0,0]
    loadButtons(0)
    
    while running:
        x, y = pygame.mouse.get_pos()
        updateHUD("100", "100", "10")
        displayCard("ace", "Spades", 108, 142)
        displayCard("Ace", "Diamonds", 190, 142)
        displayCard("Queen", "Hearts", 275, 142)
        displayCard("King", "Hearts", 355, 142)
        displayCard("Ace", "Hearts", 437, 142)       
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if toAct[player]: # remove to replace with backend deciding when acting
                    if betButtonRect.collidepoint(event.pos):
                        printout = font.render('You betted, Bitch', True, (0,0,0))
                        screen.blit(printout, (250,300))
                        screen.blit(bg, (0, 0)) # sets background to bg image
                        toAct = 0
                    if checkButtonRect.collidepoint(event.pos):
                        printout = font.render('You checked, Bitch', True, (0,0,0))
                        screen.blit(printout, (250,300))
                    if foldButtonRect.collidepoint(event.pos):
                        printout = font.render('You folded, Bitch', True, (0,0,0))
                        screen.blit(printout, (250,300))


        pygame.display.update()

main()
