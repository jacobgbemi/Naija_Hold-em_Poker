#!/usr/bin/python3
"""Hand Rank Validator for a Pair"""
from poker.game.validators import RankValidator


class PairValidator(RankValidator):
    """
    A Pair Validator
    """
    def __init__(self, cards):
        """
        Instantiation
        """
        self.cards = cards
        self.name = "Pair"

    def is_valid(self):
        """
        Return true for card list that have at least two cards of the same rank
        """
        ranks_with_pairs = self._ranks_with_count(2)
        return len(ranks_with_pairs) == 1

    def valid_cards(self):
        """
        Return a list of cards with at least two same rank
        """
        ranks_with_pairs = self._ranks_with_count(2)
        cards = [card for card in self.cards if card.rank in ranks_with_pairs.keys()]
        return cards
