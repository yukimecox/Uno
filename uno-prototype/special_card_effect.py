"""
* Name:: yukimecox
* Project:: Uno Prototype
*
* File:: special_card_effect.py
*
* Description:: This file handles any special card logic the user plays.
"""

"""
Helper function to draw cards whether the player play a +2 or +4. 
Return the next player that their cards were drawn.
"""
def draw_cards(players, deck, i, direction, four_or_two, num_players):
    next_i = (i + direction) % num_players
    next_player = f"Player {next_i + 1}"  
    
    for _ in range(four_or_two):
        drawn_card = deck.deck.pop(0)
        players[next_player].append(drawn_card)
        deck.generate_cards(1)
    
    print(f"{next_player} drew {four_or_two} cards!")
    return next_i

def special_card_effect(card, players, i, deck, top_card, direction):
    num_players = len(players) # might be unnecessary
    
    if (card.value in ['Wild', 'Wild Draw Four']):
        new_colour = input("Choose a color (Red, Yellow, Green, Blue): ").strip().capitalize()
        card.colour = new_colour
        print(f"Color changed to {new_colour}")
        
        if card.value == 'Wild Draw Four':
            next_i = (i + direction) % num_players
            draw_cards(players, deck, i, direction, 4, num_players)
            return (next_i + direction), card, direction
        return (i + direction) % num_players, card, direction

    """
    Switch-case the rest of the special logic. The reason we didn't do so for Wilds
    is because they're related. By themselves, and it would be repeated logic.
    """
    match(card.value):
        case 'Reverse':
            direction *= -1 # Do not reverse the list! create this variable to flip order
            print("Player order reversed!")
            return (i + direction) % num_players, top_card, direction
        
        case 'Skip':
            print("Next player's turn skipped!")
            return (i + (2 * direction)) % num_players, top_card, direction

        case 'Draw Two':
            next_i = (i + direction) % num_players
            draw_cards(players, deck, i, direction, 2, num_players)
            return (next_i + direction), top_card, direction