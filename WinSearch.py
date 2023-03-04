print("Start")

import random
import time

class Card:
    def __init__(self, suit, name, value, suit_num):
        self.suit = suit
        self.name = name
        self.value = value
        self.suit_num = suit_num

    def __str__(self):
        return (f"{self.name} of {self.suit}")

    def show(self):
        return (f"{self.name} of {self.suit}")


class Deck:
    suits = ["Clubs", "Spades", "Hearts", "Diamonds"]   #0, 1, 2, 3
    names = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suit_num = 0
        for i in Deck.suits:
            val = 0
            for j in Deck.names:
                self.cards.append(Card(i, j, Deck.values[val], suit_num))
                val += 1
            suit_num += 1



runout = []
p1_hand = []
p2_hand = []
def deal(deck):
    for i in range(2):
        the_int = random.randint(0, len(deck)-1)
        rand_card = deck[the_int]
        p1_hand.append(rand_card)
        deck.pop(the_int)
    for i in range(2):
        the_int = random.randint(0, len(deck)-1)
        rand_card = deck[the_int]
        p2_hand.append(rand_card)
        deck.pop(the_int)

def flop(deck):
    for i in range(3):
        the_int = random.randint(0, len(deck)-1)
        rand_card = deck[the_int]
        runout.append(rand_card)
        deck.pop(the_int)

def turn(deck):
    the_int = random.randint(0, len(deck)-1)
    rand_card = deck[the_int]
    runout.append(rand_card)
    deck.pop(the_int)

def river(deck):
    the_int = random.randint(0, len(deck)-1)
    rand_card = deck[the_int]
    runout.append(rand_card)
    deck.pop(the_int)


def BestHand(hand, runout):
    score = []
    hand_1 = hand + runout
    #Get suit numbers
    suits = [0,0,0,0]   #list of occurences of the 4 suits
    for card in hand_1:
        suits[card.suit_num] += 1

    for i in range(len(suits)):
        #Flush
        if suits[i] >= 5:       #if more than 5 cards of 1 suit
            cnt = 0
            while cnt < (len(hand_1)):     #Remove cards not of flush suit
                if hand_1[cnt].suit_num != i:
                    hand_1.remove(hand_1[cnt])
                else:
                    cnt += 1
            hand_1.sort(key=lambda x: x.value)     #Sort cards of similar suit
            isStraight= True    
            for i in range(len(hand_1) - 1):   
                if abs(hand_1[i].value - hand_1[i+1].value) != 1:      #if  not consecutive numbers --> flush
                    isStraight = False
            if isStraight:
            #Straight Flush (9, highest card)
                score.append(9)
                score.append(hand_1[len(hand_1)-1])  #Highest card in flush
                return score
            else:
            #Flush (not straight)   (6, highest card)   
                score.append(6) 
                for card in hand_1:
                    score.insert(1, card)
    hand_1.sort(reverse=True, key=lambda x: x.value)
            

    #Dictionary<int value, (Card, int quantity)>
    repitions = {}
    for card in hand_1:
        if(repitions.get(card.value) is None):
            repitions[card.value] = [card, 1]
        else:
            repitions[card.value][1] += 1

    most = hand_1[0].value
    for num in repitions.keys():
        if repitions[num][1] > repitions[most][1]:
            most = num

    #Four of a kind (8, number of 4, next highest card)
    if repitions[most][1] == 4:
        score.append(8)
        score.append(repitions[most][0])
        for card in hand_1:
            if card.value != most:
                score.append(card)
                return score
            
    if repitions[most][1] == 3:
        #3 of a kind (4, number of 3, next two highest cards)
        score.append(4)
        score.append(repitions[most][0])
        for card in hand_1:
            if card.value != most:
                score.append(card)
                if(len(score) == 4):
                    break
        #Full House (7, number of 3, number of 2)
        for num in repitions.keys():
            if(num != most and repitions[num][1] > 1):
                score = [7, repitions[most][0], repitions[num][0]]
                return score

    if len(score) > 0:
        if score[0] == 6:
            return score

    isStraight = 0
    highest = hand_1[0]
    for i in range(len(hand_1)-1):
        if abs(hand_1[i].value - hand_1[i+1].value) == 1:      #if  not consecutive numbers --> high card
            isStraight += 1
        else:
            highest = hand_1[i+1]
            isStraight = 0
    if isStraight >= 4:
        #Straight   (5, highest card)
        score = [5, highest]        
        return score

    if len(score) > 0:
        if score[0] == 4:
            return score

    if repitions[most][1] == 1:
            #High card  (1, cards from high to low)
            for card in hand_1:
                score.append(card)
                if len(score) == 5:
                    score.insert(0, 1)
                    return score
            score.insert(0, 1)
            return score

    pairs = []
    for num in repitions.keys():
        if repitions[num][1] == 2:
            pairs.append(num)
            
    #One pair   (2, pair number, next 3 highest cards)
    if len(pairs) == 1:
        score = [2, repitions[pairs[0]][0]]
        for card in hand_1:
            if card.value != pairs[0]:
                score.append(card)
                if len(score) == 5:
                    return score

    #Two pair   (3, pair numbers, next highest card)
    if len(pairs) >= 2:
        score = [3, repitions[pairs[0]][0], repitions[pairs[1]][0]]
        for card in hand_1:
            if card.value != pairs[0] and card.value != pairs[1]:
                score.append(card)
                return score
    #print(repitions)
    return score

def FindWinner(hand_1, hand_2):
    player = 0
    hand_num = 0
    win_hand = []
    output = ""
    if hand_1[0] != hand_2[0]:
        if hand_1[0] > hand_2[0]:
            player = 1
            win_hand = hand_1
            hand_num = hand_1[0]
        elif hand_1[0] < hand_2[0]:
            player = 2
            win_hand = hand_2
            hand_num = hand_2[0]
    else:
        i = 1
        while i < len(hand_1):
            if hand_1[i].value > hand_2[i].value:
                player = 1
                win_hand = hand_1
                hand_num = hand_1[0]
                break
            elif hand_1[i].value < hand_2[i].value:
                player = 2
                win_hand = hand_2
                hand_num = hand_2[0]
                break
            i += 1

    if player == 0:
        return "Draw"

    if win_hand[0] == 1:
        output = f"Player {player} wins with {win_hand[1].name} {win_hand[2].name} high"
    elif win_hand[0] == 2:
        output = f"Player {player} wins with a pair of {win_hand[1].name}s"
    elif win_hand[0] == 3:
        output = f"Player {player} wins with pairs of {win_hand[1].name}s and {win_hand[2].name}s"
    elif win_hand[0] == 4:
        output = f"Player {player} wins with three {win_hand[1].name}s"
    elif win_hand[0] == 5:
        output = f"Player {player} wins with a straight to {win_hand[1].name}"
    elif win_hand[0] == 6:
        output = f"Player {player} wins with a flush high {win_hand[1].name}"
    elif win_hand[0] == 7:
        output = f"Player {player} wins with a {win_hand[1].name} {win_hand[2].name} full house"
    elif win_hand[0] == 8:
        output = f"Player {player} wins with Four {win_hand[1].name}s"
    elif win_hand[0] == 9:
        output = f"Player {player} wins with a straight flush to {win_hand[1].name}"

    return output

    


p1_stack = 0
p2_stack = 0
num_of_turns = 0
def betting():
    print("filler")


def play_round():
    for i in range(50):
        #input("Are you ready to play poker? ")
        pile = Deck().cards
        p1_hand.clear()
        p2_hand.clear()
        runout.clear()
        deal(pile)

        print("Player 1's hand")
        output = ""
        for card in p1_hand:
            output += str(card) + ", "
        print(output)
        output = ""

        print("Player 2's hand")
        for card in p2_hand:
            output += str(card) + ", "
        print(output)
        output = ""

        #time.sleep(3)
        flop(pile)
        print('')

        print('The Flop')
        for card in runout:
            output += str(card) + ", "
        print(output)
        output = ""

        #time.sleep(3)
        turn(pile)
        print('')

        print('The Turn')
        for card in runout:
            output += str(card) + ", "
        print(output)
        output = ""

        #time.sleep(3)
        river(pile)
        print('')

        print('The River')
        for card in runout:
            output += str(card) + ", "
        print(output)

        print('')
        print(FindWinner(BestHand(p1_hand, runout), BestHand(p2_hand, runout)))
        print("~~~")
    
class Player():
    def __init__(self, name, money=500):
        self.name = name
        self.money = money




#flush = []
#flush.append(Card("Hearts", "Five", 4, 2))
#flush.append(Card("Clubs", "Six", 5, 0))
#flush.append(Card("Hearts", "Six", 5, 2))
#flush.append(Card("Clubs", "Eight", 7, 0))
#flush.append(Card("Hearts", "Ten", 9, 2))
#hand = [] 
#hand.append(Card("Spades", "Nine", 8, 1))
#hand.append(Card("Diamonds", "Ten", 9, 3))
#print(BestHand(flush, hand))
play_round()
