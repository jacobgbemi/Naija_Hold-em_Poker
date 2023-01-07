#!/usr/bin/python3
"""Hand Rank Validator for Four of a Kind"""
from poker.game.validators import RankValidator


class FourOfAKindValidator(RankValidator):
    """
    Four of a Kind Validator
    """
    def __init__(self, cards):
        """
        Instantiation
        """
        self.cards = cards
        self.name = "Four of a Kind"

    def is_valid(self):
        """
        Return true for card dict that have four cards of the same rank
        """
        ranks_with_four_of_a_kind = self._ranks_with_count(4)
        return len(ranks_with_four_of_a_kind) == 1

    def valid_cards(self):
        """
        Return a list of sorted cards by ranks
        with four same ranks
        """
        ranks_with_four_of_a_kind = self._ranks_with_count(4)
        cards = [card for card in self.cards if card.rank in ranks_with_four_of_a_kind.keys()]
        return cards
