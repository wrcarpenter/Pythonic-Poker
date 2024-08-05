# Poker Engine Testing 
# W Carpenter
# August 2024


from importlib import reload
import poker_game_engine as engine

if __name__ == "__main__":
        
    # In case new changes were made
    reload(engine)
        
    # Create new Game
    # Small blind, big blind, buy-in amount, number of players
    g = engine.Game(10, 20, 300, 6)
    
    print("Blinds: ")
    print()
    print(g.bb)
    print(g.sb)
    
    # create a round, no betting but see that each player has cards
    g.play_round()
    
    # shows player
    # print(g.players[0])
    #print(g.players[0].show_hand())
    
    # Looking at a players cards
    for item in g.players[0].get_hand():
        print(item)
        print(item.card_value)

    


    
    
    




