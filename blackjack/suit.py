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
