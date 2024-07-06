# Poker Game Engine
# Willam Carpenter
# June 2024

import numpy as np
import random

# class Deck     - a deck of cards 
# class Pot      - represents the game pot ... 
# class Dealer   - deals out cards from a deck  
# class Player   - one poker player that will have a given hand, etc. 
# class Game     - this will be a interesting program ... simulates a game and keeps all the game history (each hand, what the players played, bet, won, etc. lots of data)
# class Rankings - hand rankings 
# use tuples to create the deck

#%%
# Basic poker engine framework - strategy built on top of this 
# Strategy
# effective stack size, etc.

class Game:
    
    def __init__(self, little, big, buyin):
        
        self.little = little  # little blind 
        self.big    = big     # big blind 
        self.buyin  = buyin   # player buy-in
        # pot should be created and set to zero
        # define number of players in game and initilize their stacks
        
class Deck:
    
    '''
    Poker Deck 
    '''

    def __init__(self):

        self.cards = self.create_deck()
        self.size  = self.deck_size()

    def create_deck(self):
        # create the initial version of a deck
        
        card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        
        cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        
        deck = [(card, category) for category in card_categories for card in cards_list]
        
        return deck
    
    def __str__(self):
        s = ""
        for c in self.cards:
            s += "%s\n" % c
        return s    
    
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
    
    def __init__(self, stack, hand):
        self.stack = stack  # define the starting stack
        self.hand  = []     # empty hand
        
    def get_card(self, card):
        # throw error if hand is larger than two cards
        self.hand.append(card)
        
    def hand(self):
        return self.hand
    
    def first_card(self):
        return self.hand[0]
    
    def second_card(self):
        return self.hand[1]

    def stack_size(self):
        return self.stack
    
    def bet(self, betsize):
        
        if self.stack_size() < betsize:
            print("Caution: Bet larger than Player Pot.")
        
        self.stack = self.stack - bet    
                
class Pot:
    
    # constructor, set pot to 0 
    def __init__(self, size):
        
        self.size = 0

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
    game_deck = Deck()
    
    print(game_deck.cards)
    print("   ")
    
    print(type(game_deck.cards))
    
    print(game_deck.deck_size())
    print("   ")
    
    game_deck.shuffle()
    
    print(game_deck.cards)
    
    card = game_deck.take_card()
    print("   ")
    print(card)
    
    print(game_deck.deck_size())


