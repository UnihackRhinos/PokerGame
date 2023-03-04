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
        the_int = random.randint(0, len(deck) - 1)
        rand_card = deck[the_int]
        p1_hand.append(rand_card)
        deck.pop(the_int)
    for i in range(2):
        the_int = random.randint(0, len(deck) - 1)
        rand_card = deck[the_int]
        p2_hand.append(rand_card)
        deck.pop(the_int)


def flop():
    for i in range(3):
        the_int = random.randint(0, len(deck) - 1)
        rand_card = deck[the_int]
        runout.append(rand_card)
        deck.pop(the_int)


def turn():
    the_int = random.randint(0, len(deck) - 1)
    rand_card = deck[the_int]
    runout.append(rand_card)
    deck.pop(the_int)


def river():
    the_int = random.randint(0, len(deck) - 1)
    rand_card = deck[the_int]
    runout.append(rand_card)
    deck.pop(the_int)


def play_round():
    input("Are you ready to play poker? ")
    deal()
    print("Player 1's hand")
    print(p1_hand)
    print("Player 2's hand")
    print(p2_hand)
    betting()
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


def int_input(prompt="", restricted_to=None):
    while True:
        player_input = input(prompt)
        try:
            int_player_input = int(player_input)
        except ValueError:
            continue
        if restricted_to is None:
            break
        elif int_player_input in restricted_to:
            break
    return int_player_input


stack = 200
num_of_turns = 0
bigblind = 20
smallblind = 10
position = 0
pot = 0
other_stack = 0
round_over = False
win = False


def betting():
    global pot
    global stack
    committed = 0
    # preflop
    if position == 0:
        pot += bigblind
        stack -= bigblind
        committed += bigblind
    elif position == 1:
        pot += smallblind
        stack -= smallblind
        committed += smallblind
    if pot / 2 != committed:  #finds out if player is able to call
        choice = int_input("Call: 1, Raise: 2, Fold: 3. Please select option: ", [1, 2, 3])
        if choice == 1:
            committed += pot - committed
            stack -= committed
            pot += committed
        elif choice == 2:
            raise_amount = int_input("How much would you like to raise by? ", list(range(bigblind, stack + 1)))
            pot += raise_amount
            stack -= raise_amount
            committed += raise_amount
        elif choice == 3:
            round_over = True

    if pot / 2 == committed:  #finds out if player is able to check
        choice = int_input("Check: 1, Raise: 2, Fold: 3. Please select option: ", [1, 2, 3])
        if choice == 1:
            pass
        elif choice == 2:
            raise_amount = int_input("How much would you like to raise by? ", list(range(bigblind, stack + 1)))
            pot += raise_amount
            stack -= raise_amount
            committed += raise_amount
        elif choice == 3:
            round_over = True



betting()



