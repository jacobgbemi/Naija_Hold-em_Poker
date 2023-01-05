import unittest

from poker.game.card import Card
from poker.game.validators import FullHouseValidator

class FullHouseValidatorTest(unittest.TestCase):
    """Unittest for Full House Validator"""
    def setUp(self):
        """set attributes at start for tests"""
        self.three_of_clubs   = Card(rank = "3", suit = "Clubs")
        self.three_of_hearts  = Card(rank = "3", suit = "Hearts")
        self.three_of_spades  = Card(rank = "3", suit = "Spades")
        self.nine_of_diamonds = Card(rank = "9", suit = "Diamonds")
        self.nine_of_spades   = Card(rank = "9", suit = "Spades")

        self.cards = [
            self.three_of_clubs,
            self.three_of_hearts,
            self.three_of_spades,
            Card(rank = "5", suit = "Diamonds"),
            self.nine_of_diamonds,
            self.nine_of_spades,
            Card(rank = "Queen", suit = "Clubs")
        ]

    def test_that_cards_have_two_of_the_same_rank_and_three_of_another_rank(self):
        """check 2 cards of the same rank and 3 cards of another rank exist"""
        validator = FullHouseValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_of_2_cards_of_the_same_rank_and_3_cards_of_the_same_rank(self):
        """check list of 2 cards of the same rank and 3 cards of another rank exist"""
        validator = FullHouseValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.three_of_clubs,
                self.three_of_hearts,
                self.three_of_spades,
                self.nine_of_diamonds,
                self.nine_of_spades
            ]
        )