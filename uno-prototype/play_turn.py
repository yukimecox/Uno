"""
* Name:: yukimecox
* Project:: Uno Prototype
*
* File:: play_turn.py
*
* Description:: Logic that will have each player play a turn.
* We can validate each card they play, as well as handling cases
* where they are special cards.
"""

import special_card_effect
import check_uno

def play_turn(player, hand, top_card, deck, players, i, direction):
    print(f"\n{player}'s turn!")
    # Display the player's hand
    print(f"Your hand:\n{', '.join(str(card) for card in hand)}")
    print(f"Top card: {top_card}")

    while True:
        play = input("Enter card to play ('draw' to draw card; 'quit' to end game). Must be element input from 0: ").strip()
        # Nothing was played. In other words, no cards match top card.
        if (play == 'draw'):
            card = deck.deck.pop(0)
            hand.append(card)
            print(f"You drew: {card}")
            deck.generate_cards(1)
            return (i + direction) % len(players), top_card, direction
        elif (play == 'quit'):
            print("You decided to quit, I guess.\n")
            exit()
        
        if (play.isdigit() and (0 <= int(play) < len(hand))):
            play_card = hand[int(play)] # Choose this card
            # If play_card matches top_card, or if it's a special card.
            if (play_card.colour == top_card.colour or
                play_card.value == top_card.value or
                play_card.value in ['Wild', 'Wild Draw Four']):
                    hand.remove(play_card)
                    print(f"{player} played: {play_card}")

                    if (play_card.value in ['Wild', 'Wild Draw Four', 'Reverse', 'Skip', 'Draw Two']):
                        # Handle special card logic.
                        next_i, next_card, new_direction = special_card_effect.special_card_effect(
                            play_card,
                            players,
                            i,
                            deck,
                            play_card,
                            direction
                        )

                        if (len(hand) == 1):
                            check_uno.check_uno(player, deck, players)

                        return next_i, next_card, new_direction

                    # WET method for each case
                    if (len(hand) == 1):
                        check_uno.check_uno(player, deck, players)

                    return (i + direction) % len(players), play_card, direction
            else:
                print("Invalid card. Try again.")
        else:
            print("Invalid move. Try again.")