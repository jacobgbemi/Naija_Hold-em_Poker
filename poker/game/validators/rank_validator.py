"""Validator for counting ranks in a list of cards"""


class RankValidator():
    def _ranks_with_count(self, count):
        """
        Return a dict of rank: rank count in a card list
        """
        return {
            rank: rank_count
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == count
        }

    @property
    def _card_rank_counts(self):
        """
        Return a set of the number of card rank in a card list
        """
        card_rank_counts = {}
        for card in self.cards:
            card_rank_counts.setdefault(card.rank, 0)
            card_rank_counts[card.rank] += 1
        return card_rank_counts