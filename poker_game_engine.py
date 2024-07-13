# Poker Game Engine
# Willam Carpenter
# June 2024

import numpy as np
import random

# class Deck      - a deck of cards 
# class Pot       - represents the game pot ... 
# class Dealer    - deals out cards from a deck  
# class Player    - one poker player that will have a given hand, etc. 
# class Game      - this will be a interesting program ... simulates a game and keeps all the game history (each hand, what the players played, bet, won, etc. lots of data)
# class Rankings  - hand rankings 
# use tuples to create the deck

# Card deck constraints
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']


class Game:
    
    '''
    Poker Game Simulation 
    
    Rounds can be played until one player wins or a defined number to end game.
    Results should be stored down in some kind of format for data.
    
    '''
    
    def __init__(self, little, big, buyin, numplay):
        
        self.little  = little                  # little blind amt
        self.big     = big                     # big blind amt
        self.buyin   = buyin                   # player buy-in which will be their stack sizes
        
        # now each player will have a seat too (from to 1 to num)
        self.players = create_players(numplay) # based on number of players
        
        self.pot     = Pot(0)                  # empty Pot object

    def create_players(num, buyin):
        
        players = [] # empty list
        
        for i in range(0, num):
            hand = [] # player starts with empty hand
            players.append(buyin, hand) 

    def play_round(self):
        
        
        # initialize a POT
        self.pot = Pot(0)
        
        
        
        
        # 'create a deck' and shuffle it (dealer is doing this)
        # create a new pot 
        # create a new empty set of community cards
        # determine who is the sb and bb 
        # commence initial sb and bb into pot
        # commence dealing cards
        # commence first round of betting from players pre-flop
        # commence flop 
        # commence betting round 
        # etc
        
        pass
        
        
        # pot should be created and set to zero
        # define number of players in game and initilize their stacks
        # need to define intial empty set of community cards
        # need to define a deck for the game?? then this deck can be reshuffled

        
class Card:
    
    '''
    Playing Card
    
    Creates individual playing cards that are used to create a deck and dealt
    to players.
    
    '''

    def __init__(self, rank, suit):
        self.rank = rank 
        self.suit = suit
   
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck:
    
    '''
    Poker Deck class 
    
    create_deck  : initialize a deck of 52 playing cards
    deck_size    : show current size of deck (could be less than 52 in game)
    shuffle      : mix up the card objects in the deck
    take_card    : pop the card from the stack (fully removes it)
    see_card     : displays the top card (does not remove it)
    
    '''

    def __init__(self):

        self.cards = self.create_deck()
        self.size  = self.deck_size()

        
    def create_deck(self):
        
        # empty deck list
        deck = []
        
        # create the deck and fill with card objects 
        for suit in SUITS:
            for rank in RANKS:
                deck.append(Card(rank, suit))  # card object
     
        return deck
    
    def __str__(self):
        # string method to display current deck if needed
        d = ''
        
        for c in self.cards:
            d = d + str(c) + ' | '
        
        return d
        
    def deck_size(self):
        return len(self.cards)  # should return 52 cards unless deck is smaller
  
    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.cards)
    
    def take_card(self):
        # removes last card in deck, i.e. deals the card
        return self.cards.pop() 
    
    def see_card(self):
        # shows first card in deck, does not remove 
        return self.cards[0]
        
class Player:
    
    '''
    Poker Player Object 
    
    Stack starts as the game 'buy-in'; all players have same size stack
    Each player has a seat at the table and seats do not change during a game
    
    
    ''' 
    
    def __init__(self, stack, hand, seat):
        self.stack = stack  # define the starting stack
        self.hand  = []     # empty hand
        self.seat  = seat   # seat number, players do not move seats in game
        
    def get_card(self, card):
        # throw error if hand is larger than two cards
        self.hand.append(card)
        
    def hand(self):
        return self.hand # two card objects
    
    def first_card(self):
        return self.hand[0]
    
    def second_card(self):
        return self.hand[1]

    def stack_size(self):
        return self.stack
    
    def bet(self, betsize):
        
        if self.stack_size() < betsize:
            print("Exception: Bet larger than player stack.")
        
        self.stack = self.stack - bet    
                
class Pot:
    
    # constructor, set pot to 0 
    def __init__(self, size):
        
        self.size = size

    # function purely for adding a pot blind 
    def add_blind(self, blind):
        
        self.size = self.size + blind
    
    def add_bet(self, bet):
        
        self.size = self.size + bet
   
    def pot_size(self):
        
        return self.size 

# Testing 
if __name__ == "__main__":

    # creates a fresh deck of 52 cards, not shuffled 
    d = Deck()
    
    print(d)
    print("   ")
    
    print("Size of the created deck: ", d.deck_size())
    print("   ")
    
    print("Shuffling deck...")
    d.shuffle()
    print("    ")
    print("New Deck:")
    print("         ")
    print(d)
    
    
    print("Removing card from the deck...")    
    
    # taking a card object
    card = d.take_card()
    print("   ")
    # showing the card object here in a string format
    print("Card removed: ", card)
    
    
    print("    ")
    print(d.deck_size())


