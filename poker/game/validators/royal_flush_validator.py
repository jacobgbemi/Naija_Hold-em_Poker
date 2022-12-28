"""Hand Rank Validator for Royal Flush"""
from poker.game.validators import StraightFlushValidator


class RoyalFlushValidator():
    """
    Royal Flush Validator
    """
    def __init__(self, cards):
        """
        Instantiation
        """
        self.cards = cards
        self.name = "Royal Flush"

    def is_valid(self):
        """
        Return true for card list that Straight Flush with last card
        equal to Ace
        """
        straight_flush_validator = StraightFlushValidator(cards = self.cards)
        if straight_flush_validator.is_valid():
            straight_flush_cards = straight_flush_validator.valid_cards()
            is_royal = straight_flush_cards[-1].rank == "Ace"
            return is_royal

        return False

    def valid_cards(self):
        """
        Return a list of cards with Straight Flush
        """
        return StraightFlushValidator(cards = self.cards).valid_cards()


        