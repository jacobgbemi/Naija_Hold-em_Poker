"""
The Poker Players
"""

class Player():
    """
    The Player Object
    """
    def __init__(self, name, hand):
        """
        Instantiation
        """
        self.name = name
        self.hand = hand

    def __gt__(self, other):
        """
        Set which hand name is greatest hand
        """
        current_player_best_validator_index = self.best_hand()[0]  # 0
        other_player_best_validator_index = other.best_hand()[0]   # 2
        current_player_cards = self.best_hand()[2]
        other_player_cards = other.best_hand()[2]

        if current_player_best_validator_index == other_player_best_validator_index and\
                other_player_cards < current_player_cards:
            return current_player_best_validator_index

        if current_player_best_validator_index < other_player_best_validator_index:
            return current_player_best_validator_index

    def best_hand(self):
        """
        Determine which player has the greatest hand
        """
        return self.hand.best_rank()

    def add_cards(self, cards):
        """
        Give players cards
        """
        self.hand.add_cards(cards)

    def wants_to_fold(self):
        """
        Determine player has quit game
        """
        return False 