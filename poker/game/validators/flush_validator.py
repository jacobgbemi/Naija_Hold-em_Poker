""" Hand Rank Validator for Flush"""


class FlushValidator():
    """
    Flush Validator
    """
    def __init__(self, cards):
        """
        Instantiation
        """
        self.cards = cards
        self.name = "Flush"

    def is_valid(self):
        """
        Return true for card list that have five or more same suit
        """
        return len(self._suits_that_occur_5_or_more_times) == 1

    def valid_cards(self):
        """
        Return last five cards in a list of sorted cards by suits
        with same suit equal to or more than five
        """
        cards = [card for card in self.cards if card.suit in self._suits_that_occur_5_or_more_times.keys()]
        return cards[-5:]

    @property
    def _suits_that_occur_5_or_more_times(self):
        """
        Suit that has more than five counts
        """
        return {
            suit: suit_count
            for suit, suit_count in self._card_suit_counts.items()
            if suit_count >= 5
        }

    @property
    def _card_suit_counts(self):
        """
        Count suits in a card collection
        """
        card_suit_counts = {}
        for card in self.cards:
            card_suit_counts.setdefault(card.suit, 0)
            card_suit_counts[card.suit] += 1
        return card_suit_counts