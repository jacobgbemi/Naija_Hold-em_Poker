#!/usr/bin/python3
"""Hand Rank Validator for No Card"""
class NoCardsValidator():
    """
    No Card Validator
    """
    def __init__(self, cards):
        """
        Instantiation
        """
        self.cards = cards
        self.name = "No Cards"

    def is_valid(self):
        """
        Return true for card list that is empty
        """
        return len(self.cards) == 0

    def valid_cards(self):
        """
        Return empty list
        """
        return []
