# Poker Game Engine
# Willam Carpenter
# April 2024


import numpy as np
import random

# class Deck - a deck of cards 
# class Pot - represents the game pot ... 
# class Dealer - deals out cards from a deck  
# class Player - one poker player that will have a given hand, etc. 
# class Game - this will be a interesting program ... simulates a game and keeps all the game history (each hand, what the players played, bet, won, etc. lots of data)
# class Rankings - hand rankings 
# use tuples to create the deck


class Deck:
    
    '''
    Poker Deck 
    '''

    def __init__(self):

        suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
        typs  = ['Ace', 'Queen', 'King', 'Jack' '2', '3', '4', '5', '6', '7', '8', '9', '10']


        self.cards = [(card, category) for category in suits for card in typs] 
        self.size  = len(self.cards)


    def size(self):
        return self.size    
  
    def shuffle(self):
        # shuffle the deck
        return random.shuffle(self.cards)
    
    def hand(self):
        # deal a two-card hand to a player
        pass    

    def card(self):
        # pop a card from the top of the deck
        pass


def main():
    game_deck = Deck()
    game_deck = game_deck.shuffle()
    print(type(game_deck))

if __name__ == "__main__":

    main()


