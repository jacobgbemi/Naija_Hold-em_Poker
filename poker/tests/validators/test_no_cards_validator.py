import unittest

from poker.game.card import Card
from poker.game.validators import NoCardsValidator

class NoCardsValidatorTest(unittest.TestCase):
    """Unittest for No Card Validator"""
    def test_validates_that_no_cards_are_present(self):
        """check it's a list with no cards"""
        validator = NoCardsValidator(cards = [])

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_no_valid_cards(self):
        """check it's not valid"""
        validator = NoCardsValidator(cards = [])
        
        self.assertEqual(
            validator.valid_cards(),
            []
        ) 