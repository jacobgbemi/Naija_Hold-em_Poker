import unittest

from poker.game.card import Card
from poker.game.validators import FlushValidator

class FlushValidatorTest(unittest.TestCase):
    """Unittest for Flush Validator"""
    def setUp(self):
        """set attributes at start of test """
        self.two_of_hearts   = Card(rank = "2", suit = "Hearts")
        self.five_of_hearts  = Card(rank = "5", suit = "Hearts")
        self.seven_of_hearts = Card(rank = "7", suit = "Hearts")
        self.eight_of_hearts = Card(rank = "8", suit = "Hearts")
        self.ten_of_hearts   = Card(rank = "10", suit = "Hearts")
        self.ace_of_hearts   = Card(rank = "Ace", suit = "Hearts")

        self.cards = [
            self.two_of_hearts,
            self.five_of_hearts,
            self.seven_of_hearts,
            self.eight_of_hearts,
            self.ten_of_hearts,
            Card(rank = "Jack", suit = "Clubs"),
            self.ace_of_hearts
        ]

    def test_validates_that_five_cards_of_same_suit_exist_in_collection(self):
        """check 5 cards of the same suit exist"""
        validator = FlushValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_the_five_highest_cards_with_the_same_suit(self):
        """check list of 5 highest cards with the same suit """
        validator = FlushValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.five_of_hearts,
                self.seven_of_hearts,
                self.eight_of_hearts,
                self.ten_of_hearts,
                self.ace_of_hearts
            ]
        )
