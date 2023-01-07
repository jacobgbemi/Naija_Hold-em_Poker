#!/usr/bin/python3
"""
The Card Hand Name
"""

from .validators import (
    RoyalFlushValidator,
    StraightFlushValidator,
    FourOfAKindValidator,
    FullHouseValidator,
    FlushValidator,
    StraightValidator,
    ThreeOfAKindValidator,
    TwoPairValidator,
    PairValidator,
    HighCardValidator, 
    NoCardsValidator
)

class Hand():
    """
    Card Object
    """
    VALIDATORS = (
        RoyalFlushValidator,
        StraightFlushValidator,
        FourOfAKindValidator,
        FullHouseValidator,
        FlushValidator,
        StraightValidator,
        ThreeOfAKindValidator,
        TwoPairValidator,
        PairValidator,
        HighCardValidator, 
        NoCardsValidator
    )
    
    def __init__(self):
        """
        Hand Instantiation 
        """
        self.cards = []

    def __repr__(self):
        """
        Set hand computer representation output
        """
        card = [str(card) for card in self.cards]
        return ", ".join(card)

    def add_cards(self, cards):
        """
        Add cards and sort them in order of ranks and suits
        """
        copy = self.cards[:]
        copy.extend(cards)
        copy.sort()
        self.cards = copy

    def best_rank(self):
        """
        From a tuple of hand names 
        return index, hand name, and hand name card list
        """
        for index, validator_klass in enumerate(self.VALIDATORS):
            validator = validator_klass(cards = self.cards)
            if validator.is_valid():
                return (index, validator.name, validator.valid_cards())
