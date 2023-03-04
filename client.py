import pygame
from network import Network
import sys
import time

def winLosePrint(player, win, potSize):
    if player == (win - 1) :
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
            textRect = text.get_rect(topleft=(350,350))
            screen.blit(text, textRect)
            pygame.draw.rect(screen, (255,0,0),textRect)
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
    playerRect = pygame.Rect(500,350,96,60) #Rect(left, top, width, height)
    pygame.draw.rect(screen, (90,150,0),playerRect) # draw rectangle first so it doesn't cover text
    screen.blit(playerText, playerRect)

    oppText = font.render("stack: " + oppStack, True, (255,255,255))
    oppRect = pygame.Rect(500, 10, 96, 60)
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
    loadButtons(0)
    winLosePrint(0, 600)
    
    while running:
        x, y = pygame.mouse.get_pos()
        mackasRules = net.send("pull_request") #pull request, where everything is stored
        #if mackasRules.player_has_folded and mackasRules.position[player]:

        # check if it's time to flop, turn, river
        if mackasRules.betting_round == 1:
            net.send("flop")
        if mackasRules.betting_round == 2:
            print("not mitch's fault")
            net.send("turn")
        if mackasRules.betting_round == 3:
            net.send("river")
        if mackasRules.betting_round == 4:
            net.send("winner")
            time.sleep(0.1)
            winLosePrint(player, mackasRules.winner, mackasRules.pot)

        # read who's turn it is to act
        if mackasRules.num_of_actions[player] == mackasRules.num_of_actions[(player + 1) % 2]:
            toAct = mackasRules.position[player]
        else:
            toAct = (mackasRules.num_of_actions[player] < mackasRules.num_of_actions[(player + 1) % 2])
        if toAct:
            print("your turn")
            print(mackasRules.num_of_actions)
        # read the stacks and pot and update the display
        updateHUD(str(mackasRules.stack[player]),str(mackasRules.stack[(player + 1) % 2]),str(mackasRules.pot))
        # read the cards in players hand and those on the board
        if len(mackasRules.runout):
            for i in range(len(mackasRules.runout)):
                displayCard(mackasRules.runout[i].name,mackasRules.runout[i].suit, 108+85*i, 145)
        else:
            net.send("preflop")
            time.sleep(0.1)

        mackasRules = net.send("pull_request")
        displayCard(mackasRules.hand[player][0].name, mackasRules.hand[player][0].suit, 230, 340)
        displayCard(mackasRules.hand[player][1].name, mackasRules.hand[player][1].suit, 310, 340)
        #displayCard(mackasRules.hand[player][1].suit, mackasRules.hand[player][1].value, 230, 340)
        #updateHUD(str(1000), "1000", "0")
        #displayCard("Ace", "Spades", 108, 142)
        #displayCard("Ace", "Diamonds", 190, 142)
        #displayCard("Queen", "Hearts", 275, 142)
        #displayCard("King", "Hearts", 355, 142)
        #displayCard("Ace", "Hearts", 437, 142)   
        #displayCard("Ace", "Hearts", 230, 340)  
        #displayCard("Ace", "Hearts", 320, 340)   
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if toAct: # remove to replace with backend deciding when acting
                    # function of each button needs to be connected to backend
                    if betButtonRect.collidepoint(event.pos):
                        #toAct = 0
                        net.send("halfPotBet") # request
                    if fullPotButtonRect.collidepoint(event.pos):
                        #toAct = 0
                        net.send("fullPotBet") # request
                    if allInButtonRect.collidepoint(event.pos):
                        #toAct = 0
                        net.send("allIn") # request
                        print("going all in (not mitch's fault)")
                    if checkButtonRect.collidepoint(event.pos):
                        #toAct = 0
                        net.send("check") #request
                    if foldButtonRect.collidepoint(event.pos):
                        #toAct = 0
                        net.send("fold") #request


        pygame.display.update()

main()
