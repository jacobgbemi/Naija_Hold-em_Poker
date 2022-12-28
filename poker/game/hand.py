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
        self.cards = []

    def __repr__(self):
        card = [str(card) for card in self.cards]
        return ", ".join(card)
        

    # def hand_list(self):
    #     hand_list = str(player.hand).split(", ")

    def add_cards(self, cards):
        copy = self.cards[:]
        copy.extend(cards)
        copy.sort()
        self.cards = copy

    def best_rank(self):
        for index, validator_klass in enumerate(self.VALIDATORS):
            validator = validator_klass(cards = self.cards)
            if validator.is_valid():
                return (index, validator.name, validator.valid_cards())