 # DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from random import randint
# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

# Prints the given card's official name in the form "Drew a(n) ___".
# If the input card is invalid, prints "BAD CARD"
# 
# Parameters:
#   card_rank: The numeric representation of a card (1-13)
#
# Return:
#   none
def print_card_name(card_rank):
    # Implement card_name function here
    if card_rank == 1:
        card_name = "Ace"
    elif card_rank == 11:
        card_name = "Jack"
    elif card_rank == 12:
        card_name = "Queen"
    elif card_rank == 13:
        card_name = "King"
    else:
        card_name = str(card_rank)

    if card_rank == 1 or card_rank == 8:
        print('Drew an ' + card_name)
    elif card_rank > 13:
        print("BAD CARD")
    else:
        print('Drew a ' + card_name)
# Draws a new random card, prints its name, and returns its value.
# 
# Parameters:
#   none
#
# Return:
#   an int representing the value of the card. All cards are worth
#   the same as the card_rank except Jack, Queen, King, and Ace.
def draw_card():
    # Implement draw_card function here
    card_rank = randint(1, 13)
    if card_rank > 13:
        print("BAD CARD")
    elif card_rank == 1:
        card_name = "Ace"
    elif card_rank == 11:
        card_name = "Jack"
    elif card_rank == 12:
        card_name = "Queen"
    elif card_rank == 13:
        card_name = "King"
    else:
        card_name = str(card_rank)

    if card_rank == 1 or card_rank == 8:
        print('Drew an ' + card_name)
    else:
        print('Drew a ' + card_name)
    if card_rank == 11 or card_rank == 12 or card_rank == 13:
        card_value = 10
    elif card_rank == 1:
        card_value = 11
    else:
        card_value = card_rank
    return card_value
# Prints the given message formatted as a header. A header looks like:
# -----------
# message
# -----------
# 
# Parameters:
#   message: the string to print in the header
#
# Return:
#   none
def print_header(message):
    # Implement print_header function here
    print('-----------')
    print(message)
    print('-----------')
# Prints turn header and draws a starting hand, which is two cards.
# 
# Parameters:
#   name: The name of the player whose turn it is.
#
# Return:
#   The hand total, which is the sum of the two newly drawn cards.
def draw_starting_hand(name):
    # Implement draw_starting_hand function here
    print_header(name + " TURN")
    card_rank = randint(1, 13)
    if card_rank > 13 or card_rank < 1:
        print("BAD CARD")
    elif card_rank == 1:
        card_name = "Ace"
    elif card_rank == 11:
        card_name = "Jack"
    elif card_rank == 12:
        card_name = "Queen"
    elif card_rank == 13:
        card_name = "King"
    else:
        card_name = str(card_rank)

    if card_rank == 1 or card_rank == 8:
        print('Drew an ' + card_name)
    else:
        print('Drew a ' + card_name)
    if card_rank == 11 or card_rank == 12 or card_rank == 13:
        card_value = 10
    elif card_rank == 1:
        card_value = 11
    else:
        card_value = card_rank
    
    card_rank1 = randint(1, 13)
    if card_rank1 > 13:
        print("BAD CARD")
    elif card_rank1 == 1:
        card_name1 = "Ace"
    elif card_rank1 == 11:
        card_name1 = "Jack"
    elif card_rank1 == 12:
        card_name1 = "Queen"
    elif card_rank1 == 13:
        card_name1 = "King"
    else:
        card_name1 = str(card_rank1)

    if card_rank1 == 1 or card_rank1 == 8:
        print('Drew an ' + card_name1)
    else:
        print('Drew a ' + card_name1)
    if card_rank1 == 11 or card_rank1 == 12 or card_rank1 == 13:
        card_value1 = 10
    elif card_rank1 == 1:
        card_value1 = 11
    else:
        card_value1 = card_rank1
    hand_value = card_value1 + card_value
    return hand_value
# Prints the hand total and status at the end of a player's turn.
# 
# Parameters:
#   hand_value: the sum of all of a player's cards at the end of their turn.
#
# Return:
#   none
def print_end_turn_status(hand_value):
    # Implement print_end_turn_status function here
    # hand_value = card_value + card_value1
    print("Final hand: " + str(hand_value) + ".")
    if hand_value == 21:
        print("BLACKJACK!")
    elif hand_value > 21:
        print("BUST.")
# Prints the end game banner and the winner based on the final hands.
# 
# Parameters:
#   user_hand: the sum of all cards in the user's hand
#   dealer_hand: the sum of all cards in the dealer's hand
#
# Return:
#   none
def print_end_game_status(user_hand, dealer_hand):
    # Implement print_end_game_status function here
    print('-----------')
    print("GAME RESULT")
    print('-----------')
    if (user_hand > 21 and dealer_hand > 21) or (dealer_hand == 21 and user_hand != 21) or (user_hand > 21 and dealer_hand < 21) or (user_hand > 21 and dealer_hand > 21 and dealer_hand == user_hand) or (user_hand < 21 and dealer_hand < 21 and dealer_hand > user_hand):
        print("Dealer wins!")
    elif user_hand == dealer_hand:
        print("Push.")
    elif (user_hand > dealer_hand and user_hand <= 21) or (user_hand == 21 and dealer_hand < 21) or (user_hand == 21 and dealer_hand > 21) or (user_hand < 21 and dealer_hand > 21):
        print("You win!")
