"""
The Game Round
"""


class GameRound():
    """
    Game Round
    """
    def __init__(self, deck, players):
        """
        Game Round Instantiation
        """
        self.deck = deck
        self.players = players

    def play(self):
        """
        Playing the game - all rounds combined
        """
        self._shuffle_deck()
        self._deal_initial_two_cards_to_each_player()
        self._make_bets()

        self._deal_flop_cards()
        self._make_bets()

        self._deal_turn_card()
        self._make_bets()

        self._deal_river_card()
        self._make_bets()

    def _shuffle_deck(self):
        """
        Shuffle deck after each round
        """
        self.deck.shuffle()

    def _deal_initial_two_cards_to_each_player(self):
        """
        Deal first two different cards to each player
        """
        for player in self.players:
            two_cards = self.deck.remove_cards(2)
            player.add_cards(two_cards)

    def _make_bets(self):
        """
        Player decide to fold or not
        """
        for player in self.players:
            if player.wants_to_fold():
                self.players.remove(player)

    def _deal_community_cards(self, number):
        """
        Deal same number of cards to each player
        """
        community_cards = self.deck.remove_cards(number)
        for player in self.players:
            player.add_cards(community_cards)

    def _deal_flop_cards(self):
        """
        Deal same three cards to each player
        """
        self._deal_community_cards(3)

    def _deal_turn_card(self):
        """
        Deal same one card to each player
        """
        self._deal_community_cards(1)

    def _deal_river_card(self):
        """
        Deal same another one card to each player
        """
        self._deal_community_cards(1)


        