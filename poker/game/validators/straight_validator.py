#!/usr/bin/python3
"""Hand Rank Validator for Straight"""
from poker.game.validators import FiveCardRanksInARowValidator


class StraightValidator(FiveCardRanksInARowValidator):
    """
    Straight Validator
    """
    def __init__(self, cards):
        """
        Instantiation
        """
        self.cards = cards
        self.name = "Straight"

    def is_valid(self):
        """
        Return true for card list that have at least a list of five cards with
        consecutive ranks
        """
        return len(self._collections_of_five_straight_cards_in_a_row) >= 1

    def valid_cards(self):
        """
        Return last list of sorted cards with five consecutive ranks
        in a list
        """
        return self._collections_of_five_straight_cards_in_a_row[-1]
