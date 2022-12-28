"""Hand Rank Validator for High Card"""


class HighCardValidator():
    """
    High Card Validator
    """
    def __init__(self, cards):
        """
        Instantiation
        """
        self.cards = cards
        self.name = "High Card"

    def is_valid(self):
        """
        Return true for card list that have at least two cards
        """
        return len(self.cards) >= 2

    def valid_cards(self):
        """
        Get the last card in a list
        """
        return self.cards[-1:]