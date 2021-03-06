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
        return player.hands

    def get_player_cards(self) -> list[Card]:
        """get player cards"""
        return self._get_cards(self.player)

    def get_dealer_cards(self) -> list[Card]:
        """get dealer cards"""
        return self._get_cards(self.dealer)

    def get_table_cards(self) -> tuple[list[Card], list[Card]]:
        """
        get table cards

        Returns
        -------
        tuple[list[Card], list[Card]]
            player cards, dealer cards
        """
        return self.get_player_cards(), self.get_dealer_cards()

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

    def judge(self) -> str:
        """
        judge

        Returns
        -------
        str
            winner
        """
        if self.player.total > 21:
            self.dealer.win()
            self.player.lose()
            return self.dealer.name
        elif self.dealer.total > 21:
            self.player.win()
            self.dealer.lose()
            return self.player.name
        if self.player.total > self.dealer.total:
            self.player.win()
            self.dealer.lose()
            return self.player.name
        elif self.player.total < self.dealer.total:
            self.dealer.win()
            self.player.lose()
            return self.dealer.name
        else:
            self.player.draw()
            self.dealer.draw()
            return "draw"

    def play(self) -> None:
        """play"""
        try:
            while (
                input(
                    f"player hands{self._convert_prety_cards(self.get_player_cards())[0]} hit?[Y/n]: "  # noqa: E501
                )
                == "Y"
            ):
                self.append_player_card()
            self.dealer_play()
        except ValueError as e:
            print(e)
        winner = self.judge()
        player_cards, dealer_cards = self._convert_prety_cards(*self.get_table_cards())  # type: ignore # noqa: E501

        print(f"player hands: {player_cards}, dealer hands: {dealer_cards}")
        print(f"winner: {winner}")

    def _convert_prety_cards(self, *cards: list[Card]) -> tuple[str]:
        """
        convert prety cards

        Parameters
        ----------
        cards : list[Card]
            cards

        Returns
        -------
        str
            prety cards
        """
        return tuple([str([str(cc) for cc in c]).replace("'", "") for c in cards])


class BlackjackCard(Card):
    """blackjack card"""

    def __init__(self, card: Card) -> None:
        """init"""
        super().__init__(number=card.number, suit=card.suit)
        self.blackjack_value = 10 if self.number >= 10 else self.number


class BlackjackPlayer(Player):
    """blackjack player"""

    def __init__(self, player: Player) -> None:
        """init"""
        super().__init__(player.name, player.hands)

    @property
    def total(self) -> int:
        """total"""
        return sum(card.blackjack_value for card in self.hands)  # type: ignore


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
