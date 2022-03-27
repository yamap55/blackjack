"""deck"""
from itertools import product

from blackjack.card import Card
from blackjack.suit import Suit


class Deck:
    def __init__(self) -> None:
        """init"""
        self.cards = [Card(suit, number) for suit, number in product(Suit, range(1, 14))]
