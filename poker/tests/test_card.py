import unittest
from poker.game.card import Card

class CardTest(unittest.TestCase):
    """ Unittest for Card """
    def test_has_rank(self):
        """check card has a given rank"""
        card = Card(rank = "Queen", suit = "Hearts")
        self.assertEqual(card.rank, "Queen")

    def test_has_suit(self):
        """check card has a given suit"""
        card = Card(rank = "2", suit = "Clubs")
        self.assertEqual(card.suit, "Clubs")

    def test_knows_its_rank_index(self):
        """check card knows its rank index"""
        card = Card(rank = "Jack", suit = "Hearts")
        self.assertEqual(card.rank_index, 9)

    def test_has_string_representation_with_rank_and_suit(self):
        """check card has string representation with rank and suit"""
        card = Card("5", "Diamonds")
        self.assertEqual(str(card), "5_of_Diamonds.png")

    def test_has_technical_representation(self):
        """check card has technical representation"""
        card = Card("5", "Diamonds")
        self.assertEqual(repr(card), "Card('5', 'Diamonds')")

    def test_card_has_four_possible_suit_options(self):
        """check card has four possible suit"""
        self.assertEqual(
            Card.SUITS,
            ("Hearts", "Clubs", "Spades", "Diamonds")
        )

    def test_card_has_thirteen_possible_rank_options(self):
        """check card has thirteen rank options"""
        self.assertEqual(
            Card.RANKS,
            (
                "2", "3", "4", "5", "6", "7", "8", "9", "10",
                "Jack", "Queen", "King", "Ace"
            )
        )

    def test_card_only_allows_for_valid_rank(self):
        """check card only allow valid rank"""
        with self.assertRaises(ValueError):
            Card(rank = "Two", suit = "Hearts")

    def test_card_only_allows_for_valid_suit(self):
        """check card only allow valid suit"""
        with self.assertRaises(ValueError):
            Card(rank = "2", suit = "Dots")

    def test_can_create_standard_52_cards(self):
        """check method can create 52 cards"""
        cards = Card.create_standard_52_cards()
        self.assertEqual(len(cards), 52)

        self.assertEqual(
            cards[0],
            Card(rank = "2", suit = "Hearts")
        )

        self.assertEqual(
            cards[-1],
            Card(rank = "Ace", suit = "Diamonds")
        )

    def test_figures_out_if_two_cards_are_equal(self):
        """check if two cards are equal"""
        self.assertEqual(
            Card(rank = "2", suit = "Hearts"),
            Card(rank = "2", suit = "Hearts")
        )

    def test_card_can_sort_itself_with_another_one(self):
        """check if a card can sort itself with another one"""
        queen_of_spades = Card(rank = "Queen", suit = "Spades")
        king_of_spades = Card(rank = "King", suit = "Spades")
        evaluation = queen_of_spades < king_of_spades
        self.assertEqual(
            evaluation,
            True,
            "The sort algorithm is not sorting the lower card first"
        )

    def test_sorts_cards(self):
        """check card are sort in order"""
        two_of_spades = Card(rank = "2", suit = "Spades")
        five_of_diamonds = Card(rank = "5", suit = "Diamonds")
        five_of_hearts = Card(rank = "5", suit = "Hearts")
        eight_of_hearts = Card(rank = "8", suit = "Hearts")
        ace_of_clubs = Card(rank = "Ace", suit = "Clubs")

        unsorted_cards = [
            five_of_hearts,
            five_of_diamonds,
            two_of_spades,
            ace_of_clubs,
            eight_of_hearts
        ]

        unsorted_cards.sort()

        self.assertEqual(
            unsorted_cards,
            [
                two_of_spades,
                five_of_diamonds,
                five_of_hearts,
                eight_of_hearts,
                ace_of_clubs
            ]
        )

