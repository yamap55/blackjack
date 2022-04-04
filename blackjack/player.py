"""player"""

from typing import Optional

from blackjack.card import Card


class Player:
    """player"""

    def __init__(self, name: Optional[str] = None, hands: Optional[list[Card]] = None) -> None:
        """init"""
        self.name = name or "player"
        self.hands = hands or []
        self.game_count = 0
        self.win_count = 0

    @property
    def total(self) -> int:
        """total"""
        return sum(card.number for card in self.hands)

    def append_card(self, card: Card) -> None:
        """append card"""
        self.hands.append(card)

    def win(self) -> None:
        """win"""
        self.win_count += 1
        self.game_count += 1

    def lose(self) -> None:
        """lose"""
        self.game_count += 1

    def draw(self) -> None:
        """draw"""
        self.game_count += 1
