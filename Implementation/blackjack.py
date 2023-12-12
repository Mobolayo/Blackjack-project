# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from blackjack_helper import *

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
hand_value = draw_starting_hand("YOUR") 
while hand_value < 21:
        should_hit = input('You have ' + str(hand_value) + ". Hit (y/n)? ")
        if should_hit == 'n':
            break
        elif should_hit == 'y':
            hand_value += draw_card()
        else:
            print("Sorry I didn't get that.")
print_end_turn_status(hand_value)
dealer_hand = draw_starting_hand("DEALER")
while dealer_hand < 17:
    print('Dealer has ' + str(dealer_hand)+ ".")
    dealer_hand = dealer_hand + draw_card()

print_end_turn_status(dealer_hand)
print_end_game_status(hand_value, dealer_hand)
