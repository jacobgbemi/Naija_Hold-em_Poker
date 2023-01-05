import unittest
from unittest.mock import MagicMock

from poker.game.card import Card
from poker.game.hand import Hand
from poker.game.player import Player

class PlayerTest(unittest.TestCase):
    """Unittest for Player"""
    def test_stores_name_and_hand(self):
        """check player's name and hand are stored"""
        hand = Hand()
        player = Player(name = "Boris", hand = hand)
        self.assertEqual(player.name, "Boris")
        self.assertEqual(player.hand, hand)

    def test_figures_out_own_best_hand(self):
        """check a player best hand is determined"""
        mock_hand = MagicMock()
        mock_hand.best_rank.return_value = "Straight Flush"

        player = Player(name = "Boris", hand = mock_hand)

        self.assertEqual(
            player.best_hand(),
            "Straight Flush"
        )
        
        mock_hand.best_rank.assert_called()

    def test_passes_new_cards_to_hand(self):
        """check adds new cards to hand"""
        mock_hand = MagicMock()
        player = Player(name = "Kimberly", hand = mock_hand)

        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "Queen", suit = "Diamonds")
        ]

        player.add_cards(cards)

        mock_hand.add_cards.assert_called_once_with(cards)

    def test_decides_to_continue_or_drop_out_of_game(self):
        """check a player want to fold or not"""
        player = Player(name = "Sharon", hand = Hand())
        self.assertEqual(
            player.wants_to_fold(),
            False
        )

    def test_is_sorted_by_best_hand(self):
        """ check players are sorted by best hand when the hand are not equal"""
        mock_hand1 = MagicMock()
        mock_hand1.best_rank.return_value = (0, "Royal Flush", [])

        mock_hand2 = MagicMock()
        mock_hand2.best_rank.return_value = (2, "Four of a Kind", [])

        player1 = Player(name = "Kimberly", hand = mock_hand1)
        player2 = Player(name = "Debbie", hand = mock_hand2)

        players = [player1, player2]

        self.assertEqual(
            max(players),
            player1
        )

    def test_is_sorted_by_best_hand_handname_equal(self):
        """ 
        check players are sorted by hand cards order 
        when the handname are equal
        """
        cards_1 = [
            Card(rank = "2", suit = "Spades"),
            Card(rank = "Queen", suit = "Diamonds"),
            Card(rank = "2", suit = "Hearts"),
            Card(rank = "Queen", suit = "Clubs")
        ]
        cards_2 = [
            Card(rank = "5", suit = "Spades"),
            Card(rank = "Queen", suit = "Diamonds"),
            Card(rank = "5", suit = "Hearts"),
            Card(rank = "Queen", suit = "Clubs")
        ]
        mock_hand1 = MagicMock()
        mock_hand1.best_rank.return_value = (9, "Pair", [cards_1, cards_2])

        mock_hand2 = MagicMock()
        mock_hand2.best_rank.return_value = (9, "Pair", [cards_1, cards_2])

        player1 = Player(name = "Kimberly", hand = mock_hand1)
        player2 = Player(name = "Debbie", hand = mock_hand2)

        players = [player1, player2]

        self.assertEqual(
            max(players),
            player1
        )



