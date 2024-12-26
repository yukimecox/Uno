"""
* Name:: yukimecox
* Project:: Uno Prototype
*
* File:: test.py
*
* Description:: A separate file that will test the probability of a
* top card being a special card. It should be 0% based on the 
* create_deck() logic in the create_deck.py file.
"""

from create_deck import Deck

def test(num_test=5000, num_players=4):
    count = 0
    # Iterate however many times we can test if special card is in top deck.
    for _ in range(num_test):
        deck = Deck()
        deck.create_deck(num_players, k = 14 * num_players)
        first_card = deck.deck[0]

        if (first_card.value in ['Wild', 'Wild Draw Four']):
            count += 1
    
    p = (count / num_test) * 100
    print(f"Tests run: {num_test}")
    print(f"Special cards as first card: {count}")
    print(f"Probability of special first card: {p:.2f}%")

# If this is called in the terminal, do so here.
if __name__ == "__main__":
    test()