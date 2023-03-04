import random
import time

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        return (f"{self.value} of {self.suit}")


class Deck:
    suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
    values = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for i in Deck.suits:
            for j in Deck.values:
                self.cards.append(Card(i, j).show())

deck = Deck().cards
runout = []
p1_hand = []
p2_hand = []
def deal():
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

def flop():
    for i in range(3):
        the_int = random.randint(0, len(deck)-1)
        rand_card = deck[the_int]
        runout.append(rand_card)
        deck.pop(the_int)

def turn():
    the_int = random.randint(0, len(deck)-1)
    rand_card = deck[the_int]
    runout.append(rand_card)
    deck.pop(the_int)

def river():
    the_int = random.randint(0, len(deck)-1)
    rand_card = deck[the_int]
    runout.append(rand_card)
    deck.pop(the_int)

p1_stack = 0
p2_stack = 0
num_of_turns = 0
def betting():



def play_round():
    input("Are you ready to play poker? ")
    deal()
    print("Player 1's hand")
    print(p1_hand)
    print("Player 2's hand")
    print(p2_hand)
    time.sleep(3)
    flop()
    print('')
    print('The Flop')
    print(runout)
    time.sleep(3)
    turn()
    print('')
    print('The Turn')
    print(runout)
    time.sleep(3)
    river()
    print('')
    print('The River')
    print(runout)

class Player():
    def __init__(self, name, money=500):
        self.name = name
        self.money = money



