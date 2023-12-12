from unittest import TestCase, main
from unittest.mock import patch
from test_helper import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins since he has a higher hand value than the user.

        This does not count as one of your tests.
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    # Make sure all your test functions start with test_ 
    # Follow indentation of test_example
    # WRITE ALL YOUR TESTS BELOW. Do not delete this line.
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins_and_hits1(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards the user ends up recieving cards that get a "blackjack" and the dealer gets a number less than 21 (17)
        The User wins since he is the one with a blackjack.
        '''
        output = run_test([1, 7, 3], ['y'], [5, 2, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 7\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 2\n" \
                   "Dealer has 7.\n" \
                   "Drew a 10\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins_and_stands2(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The User wins since he has a higher hand than the dealer.
        '''
        output = run_test([3, 7, 8], ['y', 'n'], [5, 2, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 7\n" \
                   "You have 10. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 2\n" \
                   "Dealer has 7.\n" \
                   "Drew a 10\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_push_1(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards, and they both end up with a blackjack
        The game ends with a Push since both user and dealer ends up with a blackjack
        '''
        output = run_test([1, 7, 3], ['y'], [5, 10, 6], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 7\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 10\n" \
                   "Dealer has 15\n" \
                   "Drew a 6\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push\n"


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins1(self, input_mock, randint_mock):
        '''
        The dealer has a blackjack and the user has a number less than 21 .
        The dealer wins since he has a blackjack and the user has a number less than 21 .
        '''
        output = run_test([2, 7, 8], ['y', 'n'], [7, 7, 7], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 7\n" \
                   "You have 9. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 17. Hit (y/n)? n\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 7\n" \
                   "Dealer has 14.\n" \
                   "Drew a 7\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins2(self, input_mock, randint_mock):
        '''
        The dealer and user receive cards. Both end up with hand value less than 21
        The dealer wins because his hand value is greater than that of the user, though less than 21
        '''
        output = run_test([8, 2, 7], ['y', 'n'], [5, 4, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an 8\n" \
                   "Drew a 2\n" \
                   "You have 10. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "You have 17. Hit (y/n)? n\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 4\n" \
                   "Dealer has 9\n" \
                   "Drew a 9\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins3(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards. The user ends up with a hand value greater than 21, Bust, and the dealer recieves cards that sum up to a 21(BLACKJACK)
        In this case, dealer wins
        '''
        output = run_test([10, 7, 7], ['y'], [5, 10, 6], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 7\n" \
                   "You have 17. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 10\n" \
                   "Dealer has 15\n" \
                   "Drew a 6\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins4(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins since he has a higher hand value.
        '''
        output = run_test([3, 7], ['n'], [5, 2, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 7\n" \
                   "You have 10. Hit (y/n)? n\n" \
                   "Final hand: 10.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 2\n" \
                   "Dealer has 7.\n" \
                   "Drew a 10\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)




    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_push_2(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards. Both end up recieving cards with hand value of 18
        The game ends in a push because both user and dealer end up with the same number less than 21
        '''
        output = run_test([1, 7], ['n'], [5, 10, 3], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 7\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 10\n" \
                   "Dealer has 15\n" \
                   "Drew a 3\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push\n"


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins5(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards. Both end up busting
        The Dealer wins becaue both user and dealer busts.
        '''
        output = run_test([13, 7, 7], ['y'], [5, 11, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew a 7\n" \
                   "You have 17. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a Jack\n" \
                   "Dealer has 15\n" \
                   "Drew a 10\n" \
                   "Final hand: 25.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins_and_stands3(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards. The user ends up recieving cards with hand value less than 21 and dealer busts(hand value is greater than 21)
        The user wins because he is the only one that does not bust.
        '''
        output = run_test([7, 7], ['n'], [1, 3, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 7\n" \
                   "You have 14. Hit (y/n)? n\n" \
                   "Final hand: 14.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 3\n" \
                   "Dealer has 14\n" \
                   "Drew a 10\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins_and_hits4(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards the user ends up recieving cards that get a "blackjack" and the dealer gets a number less than 21 (17)
        The User wins since he is the one with a blackjack.
        '''
        output = run_test([1, 7, 3], ['y'], [10, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 7\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 5\n" \
                   "Dealer has 15.\n" \
                   "Drew a 10\n" \
                   "Final hand: 25.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    # Write all your tests above this. Do not delete this line.

if __name__ == '__main__':
    main()
