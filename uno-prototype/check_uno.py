"""
* Name:: yukimecox
* Project:: Uno Prototype
*
* File:: check_uno.py
*
* Description:: This file simply checks if the player types UNO when
* they're at their last card. I would do threading to handle a timer
* to when they have to type UNO, but it's more complicated than I 
* initially thought. You can implement that later.
"""

def check_uno(player, deck, players):
    uno = input("\nType 'UNO'!: ").strip().lower()
    if (uno == 'uno'):
        print(f"{player} typed UNO!")
        return True
    else:
        print(f"{player} didn't type UNO. Drawing 2 cards.")
        # Don't call draw_cards(). Next player is not skipped.
        for _ in range(2):
            card = deck.deck.pop(0)
            players[player].append(card)
            deck.generate_cards(1)
        return False