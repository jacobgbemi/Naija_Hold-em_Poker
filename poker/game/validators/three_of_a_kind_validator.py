"""Hand Rank Validator for Three of a Kind"""
from poker.game.validators import RankValidator


class ThreeOfAKindValidator(RankValidator):
    """
    Three of a Kind Validator
    """
    def __init__(self, cards):
        """
        Instantiation
        """
        self.cards = cards
        self.name = "Three of a Kind"

    def is_valid(self):
        """
        Return true for card dict that have three cards of the same ranks
        """
        ranks_with_three_of_a_kind = self._ranks_with_count(3)
        return len(ranks_with_three_of_a_kind) == 1

    def valid_cards(self):
        """
        Return a list of sorted cards by ranks
        with three same ranks
        """
        ranks_with_pairs = self._ranks_with_count(3)
        cards = [card for card in self.cards if card.rank in ranks_with_pairs.keys()]
        return cards