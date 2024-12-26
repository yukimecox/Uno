"""
* Name:: yukimecox
* Project:: Uno Prototype
*
* File:: deal_cards.py
*
* Description:: Deal 7 cards exactly to each player.
* Return the list of players that are going to play.
"""

def deal_cards(deck, num_players):
    players = {f"Player {i + 1}": [deck.pop() for _ in range(7)] for i in range(num_players)}
    return players