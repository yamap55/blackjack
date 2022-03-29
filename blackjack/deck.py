"""deck"""
from itertools import product
from random import Random
from typing import Optional

from blackjack.card import Card
from blackjack.suit import Suit


class Deck:
    """
    deck
    """

    def __init__(self, seed: Optional[int] = None) -> None:
        """init"""
        self.cards = [Card(suit, number) for suit, number in product(Suit, range(1, 14))]
        random = Random(seed) if seed is not None else Random()
        random.shuffle(self.cards)

    def pop(self) -> Card:
        """
        pop card

        Returns
        -------
        Card
            pop card
        """
        return self.cards.pop()
