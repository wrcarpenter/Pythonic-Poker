# Poker Engine Testing 

from importlib import reload
import poker_game_engine as game_engine

if __name__ == "__main__":
        
    reload(game_engine)
        
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

    
    
    
    
    




