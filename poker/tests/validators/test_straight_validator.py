import unittest

from poker.game.card import Card
from poker.game.validators import StraightValidator

class StraightValidatorTest(unittest.TestCase):
    """Unittest for Straight Validator"""
    def setUp(self):
        """set attributes to start for tests"""
        two        = Card(rank = "2", suit = "Spades")
        six        = Card(rank = "6", suit = "Hearts")
        self.seven = Card(rank = "7", suit = "Diamonds")
        self.eight = Card(rank = "8", suit = "Spades")
        self.nine  = Card(rank = "9", suit = "Clubs")
        self.ten   = Card(rank = "10", suit = "Clubs")
        self.jack  = Card(rank = "Jack", suit = "Hearts")

        self.cards = [
            two,
            six,
            self.seven,
            self.eight,
            self.nine,
            self.ten,
            self.jack
        ]

    def test_determines_if_there_are_five_cards_in_a_row(self):
        """check 5 cards of consecutive ranks exits"""
        validator = StraightValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_does_not_deem_two_consecutive_cards_as_straight(self):
        """check does not consider 2 consecutive cards as straight"""
        cards = [
            Card(rank = "6", suit = "Hearts"),
            Card(rank = "7", suit = "Diamonds")
        ]

        validator = StraightValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_returns_five_highest_cards_in_a_row(self):
        """check lsit of 5 cards of consecutive ranks"""
        validator = StraightValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.seven,
                self.eight,
                self.nine,
                self.ten,
                self.jack
            ]
        )
