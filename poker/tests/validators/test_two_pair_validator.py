import unittest

from poker.game.card import Card
from poker.game.validators import TwoPairValidator

class TwoPairValidatorTest(unittest.TestCase):
    """Unittest for Two Pair Validator"""
    def setUp(self):
        """ set attributes at start for tests """
        self.five_of_clubs    = Card(rank = "5", suit = "Clubs")
        self.king_of_diamonds = Card(rank = "King", suit = "Diamonds")
        self.king_of_hearts   = Card(rank = "King", suit = "Hearts")
        self.ace_of_clubs     = Card(rank = "Ace", suit = "Clubs")
        self.ace_of_spades    = Card(rank = "Ace", suit = "Spades")

        self.cards = [
            self.five_of_clubs,
            self.king_of_diamonds,
            self.king_of_hearts,
            self.ace_of_clubs,
            self.ace_of_spades
        ]

    def test_validates_that_cards_have_at_least_two_pairs_of_same_rank(self):
        """check 2 cards of the same ranks exist"""
        validator = TwoPairValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_collection_of_cards_that_have_pairs(self):
        """check lsit of 2 cards of the same ranks"""
        validator = TwoPairValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.king_of_diamonds,
                self.king_of_hearts,
                self.ace_of_clubs,
                self.ace_of_spades
            ]
        )