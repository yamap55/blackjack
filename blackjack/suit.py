"""
Suit
"""
from enum import Enum


class Suit(Enum):
    """
    Suit
    """

    SPADE = 1
    HEART = 2
    DIAMOND = 3
    CLUB = 4

    def __str__(self) -> str:
        """str"""
        cls_name = self.__class__.__name__
        return f"{cls_name}.{self.name}"

    def __repr__(self) -> str:
        """repr"""
        cls_name = self.__class__.__name__
        return f"{cls_name}.{self.name}"

    def __lt__(self, other: object) -> bool:
        """lt"""
        if not isinstance(other, Suit):
            raise TypeError(f"not supported instance {type(other)}")
        return self.value < other.value

    def __le__(self, other) -> bool:
        """le"""
        return self.__lt__(other) or self == other

    def __gt__(self, other) -> bool:
        """gt"""
        return not self.__le__(other)

    def __ge__(self, other) -> bool:
        """ge"""
        return not self.__lt__(other)
