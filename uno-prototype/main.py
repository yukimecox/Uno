"""
* Name:: yukimecox
* Project:: Uno Prototype
*
* File:: main.py
*
* Description:: Main driver of the code that starts the game.
"""

from create_deck import Deck
import deal_cards
import play_turn

n = int(input("Enter number of players: "))
try:
    # initialize deck
    deck = Deck()
    deck.create_deck(n, k = 14 * n)
except ValueError as e:
    print(e)

top_card = deck.deck.pop(0)
print(f"Game starts!")

players = deal_cards.deal_cards(deck.deck, n)

direction = 1
i = 0
# iterate infinitely until someone wins
while True:
    # ensure that we increment each player, regardless of direction
    player = list(players.keys())[i % len(players)] 
    hand = players[player]
    next_i, next_card, new_direction = play_turn.play_turn(
        player, 
        hand, 
        top_card, 
        deck, 
        players, 
        i, 
        direction
    )

    # update play for next turn
    i = next_i
    direction = new_direction
    top_card = next_card
    
    if not hand:
        print(f"{player} wins!")
        break