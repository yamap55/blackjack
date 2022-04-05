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

    __VISUAL_NUMBER = {
        1: "A",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "J",
        12: "Q",
        13: "K",
    }

    def __str__(self) -> str:
        """str"""
        return f"{self.suit.emoji}{self.__VISUAL_NUMBER[self.number]}"

    def __repr__(self) -> str:
        """repr"""
        return str({"suit": self.suit.name, "number": self.number})

    def __lt__(self, other: object) -> bool:
        """lt"""
        if not isinstance(other, Card):
            raise TypeError(f"not supported instance {type(other)}")
        if self.suit != other.suit:
            return self.suit < other.suit
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
