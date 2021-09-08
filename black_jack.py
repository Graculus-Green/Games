import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6,
          "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10,
          "Queen":10, "King":10, "Ace":11}

class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank] # from global dictionary

    def __str__(self):
        #assumes str
        return self.rank + " of " + self.suit

class Deck():

    def __init__(self):

        self.deck = []

        for suit in suits:
            for rank in ranks:
                #create the card object
                created_card = Card(suit,rank)
                self.deck.append(created_card)

    def shuff(self):

        random.shuffle(self.deck)

    def deal(self):

        delt_card = self.deck.pop()
        return delt_card

    def __str__(self):

        deck_cont = ""
        for card in self.deck:
            deck_cont += "\n   "+ card.__str__()
        return "Deck contains " + deck_cont

class Hand:

    def __init__(self):
        self.cards = [] # empty list of cards
        self.value = 0
        self.aces = 0 # as aces are a special case

    def add_card (self, card):
        self.cards.append(card)
        self.value += values[card.rank] # takes the value from dictionary
        if card.rank == "Ace":
            self.aces += 1

    def adjust_aces(self):

        while self.value >21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:

    def __init__(self):
        self.pot = 100
        self.bet = 0

    def win_bet(self):
        self.pot += self.bet

    def lose_bet(self):
        self.pot -= self.bet

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("\nHow much would you like to place?\n"))
        except ValueError:
            print("\nPlease input an int.")
        else:
            if chips.bet > chips.pot:
                print("Max you can place is ", chips.pot) # , gives as new line
            else:
                break

def twist(deck,hand):

    hand.add_card(deck.deal())
    hand.adjust_aces()


def stick_or_twist(deck, hand):

    global playing

    while True:
        q = input("\nStick or Twist?\n")

        if q[0].lower() == "t":
            print ("\nTwist\n")
            twist(deck,hand)

        elif q[0].lower() == "s":
            print ("\nStick!\n")
            playing = False
            break
        else:
            print("\nI don't understand that, sorry")
            continue

        break

def show_some(player, dealer):
    print("Dealer's hand:")
    print("< First card hidden >")
    print("", dealer.cards[1])
    print("\nPlayer's hand:", *player.cards, sep ="\n") # print all cards seperated by a line


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep = "\n")
    print("\nDealer's Hand:", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep = "\n")
    print("\nPlayer's Hand:", player.value)

def player_busts(player, dealer, chips):
    chips.lose_bet()
    print("\n Player busts!")

def player_wins(player, dealer, chips):
    chips.win_bet()
    print("\nPlayer wins!")

def dealer_busts(player, dealer, chips):
    chips.win_bet()
    print("\nHouse busts!")

def dealer_wins(player, dealer, chips):
    chips.lose_bet()
    print("\nHouse wins!")

def push(player, dealer, chips):
    print("\nThat's a tie, bets are pushed!")


player_pot = Chips()
playing = True

while True:

    deck = Deck()
    deck.shuff()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    print("\nPlayer pot is ",player_pot.pot)
    take_bet(player_pot)

    show_some(player_hand, dealer_hand)

    while playing:

        stick_or_twist(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_pot)
            break

    if player_hand.value <= 21:

        while dealer_hand.value <17:
            twist(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_pot)

        elif player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_pot)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_pot)

        elif dealer_hand.value == player_hand.value:
            push(player_hand, dealer_hand, player_pot)

        else:
            player_wins(player_hand, dealer_hand, player_pot)
    else:
        player_busts(player_hand, dealer_hand, player_pot)

    print("New pot is: ", player_pot.pot)

    if player_pot =< 0:
        playing = False
        print("\nYou're out mate, bad luck.\n")
        break

    again = input("\nWould you like another shot?\nY/N:\n")

    while not (again[0].lower()=="y" or again[0].lower() == "n"):
        print("\nI don't understand.\n")
        again = input("\nWould you like another shot?\nY/N:\n")

    if again[0].lower() == "y":
        playing = True
        continue
    elif again[0].lower() == "n":
        playing = False
        print("\nCheers for playing.\n")
        break
