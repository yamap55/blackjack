"""blackjack"""
from blackjack.card import Card
from blackjack.deck import Deck
from blackjack.player import Player


class _Blackjack:
    def __init__(self, player: Player, dealer: Player, deck: Deck) -> None:
        """init"""
        self.player = player
        self.dealer = dealer
        self.deck = deck

    def _get_cards(self, player: Player) -> list[Card]:
        """get cards"""
        return player.cards

    def get_player_cards(self) -> list[Card]:
        """get player cards"""
        return self._get_cards(self.player)

    def get_dealer_cards(self) -> list[Card]:
        """get dealer cards"""
        return self._get_cards(self.dealer)

    def append_player_card(self) -> None:
        """append player card"""
        self.player.append_card(self.deck.draw())

        if self.player.total > 21:
            raise ValueError("player bust")

    def append_dealer_card(self) -> None:
        """append dealer card"""
        self.dealer.append_card(self.deck.draw())

    def dealer_play(self) -> None:
        """dealer play"""
        while self.dealer.total < 17:
            self.append_dealer_card()

        if self.dealer.total > 21:
            raise ValueError("dealer bust")

    def get_winner(self) -> str:
        """get winner"""
        # TODO: 勝負！みたいなメソッド名にする
        if self.player.total > 21:
            return "dealer"
        elif self.dealer.total > 21:
            return "player"
        elif self.player.total > self.dealer.total:
            return "player"
        elif self.player.total < self.dealer.total:
            return "dealer"
        else:
            return "draw"


class Blackjack:
    """blackjack"""

    def __init__(self, player: Player, dealer: Player, deck: Deck) -> None:
        """init"""
        self.player = player
        self.dealer = dealer
        self.deck = deck

    def play(self) -> _Blackjack:
        """play"""
        self.player.append_card(self.deck.draw())
        self.player.append_card(self.deck.draw())
        self.dealer.append_card(self.deck.draw())
        self.dealer.append_card(self.deck.draw())

        return _Blackjack(self.player, self.dealer, self.deck)
