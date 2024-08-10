# Poker Game Engine
# Willam Carpenter
# June 2024

# https://www.cs.emory.edu/~cheung/Courses/170/Syllabus/10/pokerCheck.html
# An excercise in object-oriented programming and game strategy. 
# Game engine underpins poker strategies and game data collection. 

import numpy as np
import random
import itertools

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
        self.round += self.round 
        # run initial betting for blinds
        self.blinds()
        
        # Deal out cards to the players
        for i in range(0,2):
            for j in range(0, len(self.players)):
                # get a card from the deck
                self.players[j].get_card(self.deck.take_card())
                
        # commence pre-flop bets
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
        
        # deal out the turn
        self.deck.take_card()
        self.commun.append(self.deck.take_card())
        
        # deal out the river 
        self.deck.take_card()
        self.commun.append(self.deck.take_card())
       
        
    def isflush(self, cards):
        
        pass
        
        assert len(cards) == 5
        
        c = sorted(cards, key=lambda x: x.suit, reverse=True)
        
        if c[0] == c[4]:
            flush_value = 0
            return [1, flush_value] 
        
        
        else:
            return False
        
        
    
    def evaluate(self, hand, community, hero):
        
        # idea is to find the best hand for a player and 'climb up' through
        # possible combinations which hopefully increases efficiency
        # comes after compare method for this code.
        
        score = 0     # hand 'score' at lowest possible combo
        
        # define all function names
        poker_hands = ['is_flush'
                       'is_straight',
                       'is_four',
                       'is_full',
                       'is_three', 
                       'is_two',
                       'is_one',
                       'high'    ]
        
        # get all possible hands for a player (21 total)
        card_hands = self.combinations(hand, community)
        
        assert len(card_hands) == 21
        
        
    
    
        
        
        
        
        
        return card_hands
    
        
    def combinations(self, hand, community):
        

        comb = []               # empty list of combinations w/ card objects 
        three_pairs = [list(ele) for ele in itertools.combinations(community,3)]
        
        comb.append(community)  # all community cards
        
        # adding all possible combos using one card from the player hand 
        for card in hand:
            for i in range(0,5):
                combo    = community[:]
                combo[i] = card
                # sorting cards by rank value
                combo    = sorted(combo, key=lambda x: x.value, reverse=False)
                
                comb.append(combo)
        
        for p in three_pairs:
            combo  = p[:] + hand[:]
            
            combo = sorted(combo, key=lambda x: x.value, reverse=False)
            comb.append(combo)

        return comb
        
        
class Card:
    
    '''
    Playing Card
    
    Creates individual playing cards that are used to create a deck and dealt
    to players.
    
    Compare method can be optimized further and is currently brute force.
    
    '''

    def __init__(self, rank, suit):
        self.rank  = rank 
        self.suit  = suit
        self.value = self.assign_value()
   
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
    def assign_value(self):
      
        try:
           v = int(self.rank)
           return v
       # Royal cards and the Ace
        except:
           if   self.rank =="Jack":  return 11
           elif self.rank =="Queen": return 12
           elif self.rank =="King":  return 13
           else:                     return 14
    
    # brute force hand evaluation (to be faster, implement an algorithm, etc.)    
    def evaluate(hand, community):
        
        '''
        Hand is a given player's hand.
        Community is the 5-card shared at the table.
        There will be 21 combinations to evaluate for the hand. But the 
        algorithm can be faster by tracking best hand encounterd so far.
        
        For each hand, compute the type of hand and the score of that type.
        
        '''
        
        cards = sorted(cards, key=lambda x: x.value, reverse=True)
        
        # this is where you do your math
        pass
        
    # at the end of a round, determine winner 
    def compare(hands, community):
        
        print("comparing!")
        return 0
        
     # lowest possible score, find the highest
        # Now look at each hand
        for hand in hands:
            person = 0
            score = 0
            # brute force evaluation
            result = evaluate(hand, community)
            
            if result > hero: 
                hero   = result
                person = se  
            else: continue  
            
            
             
            
            
            
            
            score = evaluate(cards)
            
            
            # sort by attribute
            # all the cards sorted
            
            
            
            
            
            
        # multiple hands and community cards, all card objects
        # find out what hand each player has and what's the highest
        # if multiple are the highest then compare the actual values of their 
        # hands side by side
        return 0
    
    
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
    
    def get_hand(self):
        # returning list of both cards a player holds
        return [self.first_card(), self.second_card()]
    
    def show_hand(self):
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


# Unit Testing 
if __name__ == "__main__":

    # Create new Game
    g = Game(10, 20, 300, 6)
    
    print("Blinds: ")
    print()
    print(g.bb)
    print(g.sb)
    
    # create a round, no betting but see that each player has cards
    g.play_round()
    
    # shows player
    print(g.players[0])
    
    print(g.players[0].show_hand())
    


