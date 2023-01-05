import unittest

from poker.game.card import Card
from poker.game.validators import ThreeOfAKindValidator


class ThreeOfAKindValidatorTest(unittest.TestCase):
    """Unittest Three of a Kind Validator"""
    def setUp(self):
        """set attributes at start for tests"""
        five                  = Card(rank = "5", suit = "Clubs")
        self.king_of_clubs    = Card(rank = "King", suit = "Clubs")
        self.king_of_diamonds = Card(rank = "King", suit = "Diamonds")
        self.king_of_hearts   = Card(rank = "King", suit = "Hearts")
        ace                   = Card(rank = "Ace", suit = "Spades")

        self.cards = [
            five,
            self.king_of_clubs,
            self.king_of_diamonds,
            self.king_of_hearts,
            ace
        ]

    def test_validates_that_cards_have_exactly_three_of_the_same_rank(self):
        """check 3 cards of same rank exist"""
        validator = ThreeOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_three_of_a_kind_cards_from_card_collection(self):
        """check lsit of 3 cards of same rank exist"""
        validator = ThreeOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.king_of_clubs,
                self.king_of_diamonds,
                self.king_of_hearts
            ]
        )
