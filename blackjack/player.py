"""player"""

from typing import Optional

from blackjack.card import Card


class Player:
    """player"""

    def __init__(self, hands: Optional[list[Card]] = None) -> None:
        """init"""
        self.hands = hands or []

    @property
    def total(self) -> int:
        """total"""
        return sum(card.number for card in self.hands)

    def append_card(self, card: Card) -> None:
        """append card"""
        self.hands.append(card)
