"""
card
"""
from blackjack.suit import Suit


class Card:
    """
    Card
    """

    def __init__(self, suit: Suit, number: int) -> None:
        """init"""
        self.suit = suit
        self.number = number
