# Poker Game Engine
# Willam Carpenter
# June 2024

# An excercise in object-oriented programming and game strategy. 
# Game engine underpins poker strategies and game data collection. 

import numpy as np
import random

# Card deck constraints
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']


class Game:
    
    '''
    Poker Game Simulation 
    
    Rounds can be played until one player wins or a defined number to end game.
    Results should be stored down in some kind of format for data.
    
    Blinds are made before dealing cards and are mandatory from players.
    
    No 'dealer' object exists here but that might not be necessary. 
    
    A betting cap could be added for individual rounds but that adds another
    layer of complexity to the game.
    
    There is no min-raise set either.
    
    
    '''
    
    def __init__(self, small, big, buyin, numplay):
        
        self.small   = small    # little blind amt
        self.big     = big      # big blind amt
        self.buyin   = buyin    # player buy-in which will be their stack sizes
        self.sb      = 0        # small blind position, first next to dealer
        self.bb      = 1        # big blind position, next to sb
        self.fb      = 2        # first bet position
        self.numplay = numplay
        
        self.pot     = Pot(0)   # empty Pot object
        self.deck    = Deck()   # deck object
        self.round   = 0        # no rounds played
        
        self.commun  = []       # empty community of cards 
        
        # now each player will have a seat too (from to 1 to num)
        self.players = self.create_players(numplay, buyin) # based on number of players


    def create_players(self, numplay, buyin):
        
        players = []  # empty list
        hand    = []
        
        for i in range(0, numplay):
            # player starts with an empty hand
            p    = Player(buyin, hand, i)
            # Create a player and assign them a seat
            players.append(p)
       
        return players    
            
    def update_blinds(self, small, big):
        # its possible that blinds are updated during the game
        self.small = small
        self.big   = big

    def reset(self):
        
        # clear pot
        self.pot = Pot(0)
        # create and shuffle deck
        self.deck = Deck()
        self.deck.shuffle()
        
        # make all players active
        for i in range(0, self.numplay):
            self.players[i].fold = False
        

    def blinds(self):
        
        # Players make blinds (i.e. bets before seeing any cards)
        self.players[self.sb].bet(self.small)
        self.players[self.bb].bet(self.big)
        
        # update blinds (could be a function)
        if self.sb == self.numplay - 1: self.sb = 0
        else: self.sb += 1
        
        if self.bb == self.numplay - 1: self.bb = 0 
        else: self.bb +=1 
                
        # dealer collects blinds
        self.pot.add_blind(self.small) 
        self.pot.add_blind(self.big)
        

    def play_round(self):
        
        # initial table rest before cards dealt and betting 
        self.reset()
        # update playing round
        self.round += self.round # update to record game rounds 
        # run initial betting for blinds
        self.blinds()
        
        # Deal out cards to the players
        for i in range(0,2):
            for j in range(0, len(self.players)):
                # get a card from the deck
                self.players[j].get_card(self.deck.take_card())
                
        # commence pre-flop bets
        # define current bet stage
        # four options: check, raise, call, fold
        curr_bet = 0
        for i in range(0, self.numplay):
            # check if folded 
            if self.players[i].fold is not True:
                pass
            else: 
                pass
                
        # Deal out 3 flop cards to commumnity
        # Burn card
        self.deck.take_card()
        # Deal out flop
        for i in range(0,3):
            self.commun.append(self.deck.take_card())
        
        # next round of betting here
        
        # players make pre-flop bets
        # need to handle the event of bet, raise, reraise, etc.
    
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
    
    Player is where the poker strategy is stored in the 'strat' method right now.
    
    ''' 
    
    def __init__(self, stack, hand, seat):
        self.stack = stack    # define the starting stack
        self.hand  = []       # empty hand
        self.seat  = seat+1   # seat number, players do not move seats in game
        self.fold  = False
    
    def __str__(self):
                
        p = "Player " + str(self.seat) + "\n" + str(self.hand[0]) + " | " + str(self.hand[1])
        
        return p 
        
    def strat(self, game):
        # this is where a player needs all game information to make a decision
        # pass in a game object and analyze it
        pass
   
    def fold(self):
        return self.fold
   
    def get_card(self, card):
        # throw error if hand is larger than two cards
        self.hand.append(card)
        
    def hand(self):
        h = ''
        for c in self.hand:
            h = h + str(c) + " | "
        return h # two card objects
    
    def first_card(self):
        return self.hand[0]
    
    def second_card(self):
        return self.hand[1]

    def stack_size(self):
        return self.stack
    
    def bet(self, betsize):
        
        if self.stack_size() < betsize:
            print("Exception: Bet larger than player stack.")
        
        self.stack = self.stack - betsize    
          
class Pot:
    
    # constructor, set pot to 0 
    def __init__(self, size):
        
        self.size = size

    # function purely for adding a pot blind for readability  
    def add_blind(self, blind):
        
        self.size = self.size + blind
    
    # add player bet
    def add_bet(self, bet):
        
        self.size = self.size + bet
   
    def pot_size(self):
        
        return self.size 

# Testing 
if __name__ == "__main__":
    
    g = Game(10, 20, 300, 6)

    
    print(g.pot.pot_size())
    print('-------------')
    

    print(g.deck)
    
    print(g.sb)
    print(g.bb)
    print(g.buyin)
    print(type(g.small))
    
    print(g.players[0].stack_size())
    print(g.players[1].stack_size())
    
    
    print('New pot')
    print(g.pot.pot_size())

    print(g.players[0].fold)
    g.players[0].fold = True
    print(g.players[0].fold)


    g.play_round()
    
    for i in range(0, len(g.players)):    
        print(g.players[i])
        print("__________\n")
    
    
    
    # create a game
    # for person in g.players:
    #   print(person)

    # # creates a fresh deck of 52 cards, not shuffled 
    # d = Deck()
    
    # print(d)
    # print("   ")
    
    # print("Size of the created deck: ", d.deck_size())
    # print("   ")
    
    # print("Shuffling deck...")
    # d.shuffle()
    # print("    ")
    # print("New Deck:")
    # print("         ")
    # print(d)
    
    
    # print("Removing card from the deck...")    
    
    # # taking a card object
    # card = d.take_card()
    # print("   ")
    # # showing the card object here in a string format
    # print("Card removed: ", card)
    
    
    # print("    ")
    # print(d.deck_size())


