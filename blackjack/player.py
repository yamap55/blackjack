"""player"""

from typing import Optional

from blackjack.card import Card


class Player:
    """player"""

    def __init__(self, cards: Optional[list[Card]] = None) -> None:
        """init"""
        self.cards = cards or []

    @property
    def total(self) -> int:
        """total"""
        return sum(card.number for card in self.cards)

    def append_card(self, card: Card) -> None:
        """append card"""
        self.cards.append(card)
