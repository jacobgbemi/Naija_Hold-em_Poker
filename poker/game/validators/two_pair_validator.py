"""Hand Rank Validator for Two Pair"""
from poker.game.validators import RankValidator


class TwoPairValidator(RankValidator):
    """
    Two Pair Validator
    """
    def __init__(self, cards):
        """
        Instantiation
        """
        self.cards = cards
        self.name = "Two Pair"

    def is_valid(self):
        """
        Return true for card dict that have two cards of the same ranks
        """
        ranks_with_pairs = self._ranks_with_count(2)
        return len(ranks_with_pairs) >= 2

    def valid_cards(self):
        """
        Return a list of sorted cards by ranks
        with two same ranks
        """
        ranks_with_pairs = self._ranks_with_count(2) # { "King": 2, "Ace": 2}
        cards = [card for card in self.cards if card.rank in ranks_with_pairs.keys()]
        return cards