"""
The Poker Deck
"""
import random


class Deck():
    """
    Deck Object
    """
    def __init__(self):
        """
        Deck Instantiation
        """
        self.cards = []

    def __len__(self):
        """
        Set lenght of cards in the deck
        """
        return len(self.cards)

    def add_cards(self, cards):
        """
        Add cards to the deck
        """
        self.cards.extend(cards)

    def remove_cards(self, number):
        """
        Remove a given number of cards from the deck
        """
        cards_to_remove = self.cards[:number]
        del self.cards[:number]
        return cards_to_remove

    def shuffle(self):
        """
        Shuffle cards in the deck
        """
        random.shuffle(self.cards)