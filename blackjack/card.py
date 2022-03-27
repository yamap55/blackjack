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

    def __str__(self) -> str:
        """str"""
        return f"Card: {self.suit.name} {self.number}"

    def __repr__(self) -> str:
        """repr"""
        return str({"suit": self.suit.name, "number": self.number})
