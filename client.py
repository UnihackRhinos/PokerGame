import pygame
from network import Network
import sys

def winLosePrint(win, potSize):
    if win:
        text = font.render("you won " + potSize, True, (255,255,255))
    else:
        if potSize >0 <20:
            text = font.render("you lost your on campus lunch money", True, (255,255,255))
        elif potSize >19 <50:
            text = font.render("you lost money to buy groceries", True, (255,255,255))
        elif potSize >49 <100:
            text = font.render("you lost a full tank of petrol", True, (255,255,255))
        elif potSize >99 <250:
            text = font.render("you lost about a weeks rent", True, (255,255,255))
        elif potSize >249 <500:
            text = font.render("you lost two eight hour shifts at maccas pay", True, (255,255,255))
        elif potSize >499 <999:
            text = font.render("you lost enough money to get a new laptop, call 1800 858 858 if you need help with gambling", True, (255,255,255))
            screen.blit(text, (250,300))



def displayCard(rank, suit, xcoord, ycoord):
    # displayCard(rank, suit)
    # rank- the cards value ace to king
    # suit- the cards suit, clubs hearts etc.
    # xcoord/ycoord- location of top left of image
    # function takes two strings and combines them to 
    # create an image name to then display in a given location 
    cardFile = 'Card images\\' + rank + suit + ".png"
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
    playerRect = pygame.Rect(500,350,80,50) #Rect(left, top, width, height)
    pygame.draw.rect(screen, (90,150,0),playerRect) # draw rectangle first so it doesn't cover text
    screen.blit(playerText, playerRect)

    oppText = font.render("stack: " + oppStack, True, (255,255,255))
    oppRect = pygame.Rect(500, 10, 80, 50)
    pygame.draw.rect(screen, (255,0,0),oppRect)
    screen.blit(oppText, oppRect)

    potText = font.render("pot: " + pot, True, (255,255,255))
    potRect = pygame.Rect(500, 100, 80, 40)
    pygame.draw.rect(screen, (0,0,255),potRect)
    screen.blit(potText, potRect)

def loadButtons(conditions):
    # conditions - boolean to determine if player can check or needs to call to not fold
    if conditions: # if 1 then needs to call, can also fold or bet
        screen.blit(betButtonText, betButtonRect)
        screen.blit(callButtonText, callButtonRect)
        screen.blit(foldButtonText, foldButtonRect)
        screen.blit(fullPotButtonText, fullPotButtonRect)
        screen.blit(allInButtonText, allInButtonRect)

        pygame.draw.rect(screen, (0,255,0),betButtonRect,2)
        pygame.draw.rect(screen, (0,255,0),callButtonRect,2)
        pygame.draw.rect(screen, (0,255,0),foldButtonRect,2)
        pygame.draw.rect(screen, (0,255,0),fullPotButtonRect,2)
        pygame.draw.rect(screen, (0,255,0),allInButtonRect,2)
        #update display
        pygame.display.flip()
    else: # bet check fold
        screen.blit(betButtonText, betButtonRect)
        screen.blit(checkButtonText, checkButtonRect)
        screen.blit(foldButtonText, foldButtonRect)
        screen.blit(fullPotButtonText, fullPotButtonRect)
        screen.blit(allInButtonText, allInButtonRect)

        pygame.draw.rect(screen, (0,255,0),betButtonRect,2)
        pygame.draw.rect(screen, (0,255,0),checkButtonRect,2)
        pygame.draw.rect(screen, (0,255,0),foldButtonRect,2)
        pygame.draw.rect(screen, (0,255,0),fullPotButtonRect,2)
        pygame.draw.rect(screen, (0,255,0),allInButtonRect,2)
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
betButtonText = font.render(" Bet 1/2 Pot ", True, (0,0,0))
betButtonRect = betButtonText.get_rect(topleft=(20,80))
fullPotButtonText = font.render(" Bet Pot ", True, (0,0,0))
fullPotButtonRect = fullPotButtonText.get_rect(topleft=(20,110))
allInButtonText = font.render(" All In ", True, (0,0,0))
allInButtonRect = allInButtonText.get_rect(topleft=(20,140))
checkButtonText = font.render(" Check ", True, (0,0,0))
checkButtonRect = checkButtonText.get_rect(topleft=(20,50))
callButtonText = font.render(" Call ", True, (0,0,0))
callButtonRect = callButtonText.get_rect(topleft=(20,50))
foldButtonText = font.render(" Fold ", True, (0,0,0))
foldButtonRect = foldButtonText.get_rect(topleft=(20,20))
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
    winLosePrint(0, 600)
    
    while running:
        x, y = pygame.mouse.get_pos()
        mackasRules = net.send("pull_request") #pull request, where everything is stored
        updateHUD("100", "100", "10")
        displayCard("Ace", "Spades", 108, 142)
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
                    # function of each button needs to be connected to backend
                    if betButtonRect.collidepoint(event.pos):
                        screen.blit(bg, (0, 0)) # sets background to bg image
                        toAct = 0
                        net.send("halfPotBet") # request
                    if fullPotButtonRect.collidepoint(event.pos):
                        screen.blit(bg, (0, 0)) # sets background to bg image
                        toAct = 0
                        net.send("fullPotBet") # request
                    if allInButtonRect.collidepoint(event.pos):
                        screen.blit(bg, (0, 0)) # sets background to bg image
                        toAct = 0
                        net.send("allIn") # request
                    if checkButtonRect.collidepoint(event.pos):
                        screen.blit(bg, (0, 0)) # sets background to bg image
                        toAct = 0
                        net.send("check") #request
                    if foldButtonRect.collidepoint(event.pos):
                        screen.blit(bg, (0, 0)) # sets background to bg image
                        toAct = 0
                        net.send("fold") #request


        pygame.display.update()

main()
