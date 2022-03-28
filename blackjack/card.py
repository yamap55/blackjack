"""
card
"""
from dataclasses import dataclass

from blackjack.suit import Suit


@dataclass(frozen=True)
class Card:
    """
    Card
    """

    suit: Suit
    number: int

    def __str__(self) -> str:
        """str"""
        return f"Card: {self.suit.name} {self.number}"

    def __repr__(self) -> str:
        """repr"""
        return str({"suit": self.suit.name, "number": self.number})

    def __lt__(self, other: object) -> bool:
        """lt"""
        if not isinstance(other, Card):
            return NotImplemented
        if self.suit != other.suit:
            return self.suit.value < other.suit.value
        return self.number < other.number

    def __eq__(self, other) -> bool:
        """eq"""
        if not isinstance(other, Card):
            return False
        return self.suit == other.suit and self.number == other.number

    def __ne__(self, other) -> bool:
        """ne"""
        return not self.__eq__(other)

    def __le__(self, other) -> bool:
        """le"""
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other) -> bool:
        """gt"""
        return not self.__le__(other)

    def __ge__(self, other) -> bool:
        """ge"""
        return not self.__lt__(other)
