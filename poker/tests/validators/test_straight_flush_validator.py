import unittest

from poker.game.card import Card
from poker.game.validators import StraightFlushValidator

class StraightFlushValidatorTest(unittest.TestCase):
    """Unittest for Straight Flush Validator"""
    def test_there_are_no_five_consecutive_cards_with_same_suit(self):
        """check no 5 consecutive cards with same suits"""
        cards = [
            Card(rank = "3", suit = "Clubs"),
            Card(rank = "4", suit = "Clubs"),
            Card(rank = "5", suit = "Clubs"),
            Card(rank = "6", suit = "Clubs"),
            Card(rank = "7", suit = "Diamonds"),
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = StraightFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_there_are_five_consecutive_cards_with_same_suit(self):
        """check 5 consecutive cards with same suits exist"""
        cards = [
            Card(rank = "3", suit = "Clubs"),
            Card(rank = "4", suit = "Clubs"),
            Card(rank = "5", suit = "Clubs"),
            Card(rank = "6", suit = "Clubs"),
            Card(rank = "7", suit = "Clubs"),
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = StraightFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_list_of_five_consecutive_cards_with_same_suit(self):
        """check lsit of 5 consecutive cards with same suits"""
        three = Card(rank = "3", suit = "Clubs")
        four  = Card(rank = "4", suit = "Clubs")
        five  = Card(rank = "5", suit = "Clubs")
        six   = Card(rank = "6", suit = "Clubs")
        seven = Card(rank = "7", suit = "Clubs")

        cards = [
            three,
            four,
            five,
            six,
            seven,
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = StraightFlushValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                three,
                four,
                five,
                six,
                seven
            ]
        )
