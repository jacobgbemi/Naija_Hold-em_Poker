import unittest
from unittest.mock import patch

from poker.game.card import Card
from poker.game.deck import Deck

class DeckTest(unittest.TestCase):
    """Unittest for Deck"""
    def test_has_length_that_is_equal_to_count_of_cards(self):
        """check deck length is equal number of cards"""
        deck = Deck()
        self.assertEqual(
            len(deck),
            0
        )

    def test_stores_no_cards_at_start(self):
        """check deck is empty at start"""
        deck = Deck()
        self.assertEqual(
            deck.cards,
            []
        )

    def test_adds_cards_to_its_collection(self):
        """check cards is added to deck"""
        card = Card(rank = "Ace", suit = "Spades")
        deck = Deck()
        deck.add_cards([card])

        self.assertEqual(
            deck.cards,
            [card]
        )

    @patch('random.shuffle')
    def test_shuffles_cards_in_random_order(self, mock_shuffle):
        """Test deck is shuffled"""
        deck = Deck()

        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "8", suit = "Diamonds")
        ]

        deck.add_cards(cards)

        deck.shuffle()

        mock_shuffle.assert_called_once_with(cards)

    
    def test_removes_specified_number_of_cards_from_deck(self):
        """check a given number of card is removed from deck"""
        ace   = Card(rank = "Ace", suit = "Spades"),
        eight = Card(rank = "8", suit = "Diamonds")
        cards = [ace, eight]

        deck = Deck()
        deck.add_cards(cards)

        self.assertEqual(
            deck.remove_cards(1),
            [ace]
        )

        self.assertEqual(
            deck.cards,
            [eight]
        )
