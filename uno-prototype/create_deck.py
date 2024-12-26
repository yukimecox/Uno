"""
* Name:: yukimecox
* Project:: Uno Prototype
*
* File:: create_deck.py
*
* Description:: Create a Card and Deck objects to be used by all players.
* They also must have some attributes to characterize each object for use.
"""

import random

class Card:
    def __init__ (self, colour, value):
        self.colour = colour
        self.value = value
    
    # This says return the representation of the card.
    def __str__(self):
        return f"{self.colour} {self.value}" if self.colour else self.value
    
class Deck:
    def __init__(self):
        self.colours = ['Red', 'Yellow', 'Green', 'Blue']
        self.values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw Two']
        self.special_cards = ['Wild', 'Wild Draw Four']
        self.deck = []

    # Performs the shuffling of the deck anyway without explicitly declaring it in create_deck.
    def generate_cards(self, k):
        for _ in range(k):
            colour = random.choice(self.colours)
            value = random.choice(self.values + self.special_cards)
            card = Card(colour if (value in self.values) else None, value)
            self.deck.append(card)

    # Let n = # players; k = # cards to generate to deck.
    def create_deck(self, n, k):
        if (n < 2 or n > 4):
            raise ValueError("ERR: Number of players must be between 2 and 4.\n")

        self.generate_cards(k) 

        # Iterate the whole deck if special card is in top card. Swap them if found.
        top_card = self.deck[0]
        if top_card.value in self.special_cards:
            for i in range(1, len(self.deck)):
                if self.deck[i].value not in self.special_cards:
                    self.deck[0], self.deck[i] = self.deck[i], self.deck[0]
                    break

        return self.deck
    
    # Create a deck here.
    def __str__(self):
        return ', '.join([str(card) for card in self.deck])