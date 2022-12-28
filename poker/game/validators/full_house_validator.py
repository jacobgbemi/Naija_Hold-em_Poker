"""Hand Rank Validator for Full House"""
from poker.game.validators import ThreeOfAKindValidator, PairValidator


class FullHouseValidator():
    """
    Instantiation
    """
    def __init__(self, cards):
        self.cards = cards
        self.name = "Full House"

    def is_valid(self):
        """
        Return true for card list that have Three of a Kind and a Pair 
        """
        return ThreeOfAKindValidator(cards = self.cards).is_valid() and PairValidator(cards = self.cards).is_valid()

    def valid_cards(self):
        """
        Return a list of cards with Three of a Kind and a Pair
        """
        three_of_a_kind_cards = ThreeOfAKindValidator(cards = self.cards).valid_cards()
        pair_cards = PairValidator(cards = self.cards).valid_cards()
        all_cards = three_of_a_kind_cards + pair_cards
        all_cards.sort()
        return all_cards