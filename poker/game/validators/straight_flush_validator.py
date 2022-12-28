"""Hand Rank Validator for Straiht Flush """
from poker.game.validators import FiveCardRanksInARowValidator


class StraightFlushValidator(FiveCardRanksInARowValidator):
    """
    Straight Flush Validator
    """
    def __init__(self, cards):
        """
        Instantiation
        """
        self.cards = cards
        self.name = "Straight Flush"

    def is_valid(self):
        """
        Return true for card list that have at least five cards of the same suit
        """
        for five_cards in self._collections_of_five_straight_cards_in_a_row:
            unique_suits_in_next_five_cards = { card.suit for card in five_cards }
            if len(unique_suits_in_next_five_cards) == 1:
                return True

        return False

    def valid_cards(self):
        """
        Return the last five cards in a card list with five or more same suits
        """
        return self._straight_flush_card_batches[-1]

    @property
    def _straight_flush_card_batches(self):
        """
        Return a list of sorted cards by suits
        with five or more cards of the same suits
        """
        return [
            five_cards
            for five_cards in self._collections_of_five_straight_cards_in_a_row
            if len({ card.suit for card in five_cards }) == 1
        ]