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


class Game:
    bigblind = 20
    smallblind = 10

    def __init__(self, player):
        self.player = player
        self.deck = Deck().cards
        self.runout = []
        self.hand = [[], []]
        self.stack = [200, 200]
        self.num_of_actions = [0, 0]
        self.position = [0, 1]
        self.pot = 0
        self.hand_over = False
        self.committed = 0
        self.owed = [0, 0]
        self.betting_round = 0
        self.player_has_folded = False

    def deal(self):
        for i in range(2):
            the_int = random.randint(0, len(self.deck) - 1)
            rand_card = self.deck[the_int]
            self.hand[0].append(rand_card)
            self.deck.pop(the_int)
        for i in range(2):
            the_int = random.randint(0, len(self.deck) - 1)
            rand_card = self.deck[the_int]
            self.hand[1].append(rand_card)
            self.deck.pop(the_int)

    def flop(self):
        for i in range(3):
            the_int = random.randint(0, len(self.deck) - 1)
            rand_card = self.deck[the_int]
            self.runout.append(rand_card)
            self.deck.pop(the_int)

    def turn(self):
        the_int = random.randint(0, len(self.deck) - 1)
        rand_card = self.deck[the_int]
        self.runout.append(rand_card)
        self.deck.pop(the_int)

    def river(self):
        the_int = random.randint(0, len(self.deck) - 1)
        rand_card = self.deck[the_int]
        self.runout.append(rand_card)
        self.deck.pop(the_int)

    def blinds(self):
        if self.position[self.player] == 0:  # not dealer and bigblind
            self.pot += self.bigblind
            self.stack[self.player] -= self.bigblind
            self.committed += self.bigblind
        elif self.position[self.player] == 1:  # is dealer and smallblind
            self.pot += self.smallblind
            self.stack[self.player] -= self.smallblind
            self.committed += self.smallblind
            self.owed[self.player] = 10

    def betting(self, choice, raise_amount = bigblind):
        if self.owed[self.player]:  # finds out if player is able to call
            if choice == 1:     #if player chooses to call
                self.committed += self.owed[self.player]
                self.stack[self.player] -= self.owed[self.player]
                self.pot += self.owed[self.player]
                self.owed[self.player] = 0
                self.num_of_actions[self.player] += 1
            elif choice == 2:   #if player chooses to raise
                self.committed += raise_amount + self.owed[self.player]
                self.stack[self.player] -= (raise_amount + self.owed[self.player])
                self.pot += raise_amount + self.owed[self.player]
                self.owed[self.player] = 0
                self.owed[(self.player + 1) % 2] = raise_amount
                self.num_of_actions[self.player] += 1
            elif choice == 3:   #if player chooses to fold
                self.hand_over = True
                self.player_has_folded = True

        elif self.owed[self.player] == 0 and self.num_of_actions[self.player] >= 1:  # finds out if player is able to check
            if choice == 1:
                self.num_of_actions[self.player] += 1

            elif choice == 2:  # if player chooses to raise
                self.committed += raise_amount + self.owed[self.player]
                self.stack[self.player] -= (raise_amount + self.owed[self.player])
                self.pot += raise_amount + self.owed[self.player]
                self.owed[self.player] = 0
                self.owed[(self.player + 1) % 2] = raise_amount
                self.num_of_actions[self.player] += 1
            elif choice == 3:  # if player chooses to fold
                self.hand_over = True
                self.player_has_folded = True

        else:
            self.betting_round += 1


    def play_game(self):
        while not self.hand_over:
            self.blinds()
            self.deal()
            self.betting()
            self.flop()
            self.betting()
            self.turn()
            self.betting()
            self.river()
            self.betting()

game1 = Game(1).play_game
game1()

