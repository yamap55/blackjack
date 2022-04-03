from abc import ABC

from blackjack.player import Player


class Game(ABC):
    def play(self) -> None:
        pass

    # def __init__(self, player:Player):
    #     self.player = player
    #     self.dealer = dealer
    #     self.deck = Deck()
    #     self.deck.shuffle()

    # def play(self):
    #     self.deck.shuffle()
    #     self.player.hand = Hand()
    #     self.dealer.hand = Hand()
    #     self.player.hand.add_card(self.deck.deal())
    #     self.player.hand.add_card(self.deck.deal())
    #     self.dealer.hand.add_card(self.deck.deal())
    #     self.dealer.hand.add_card(self.deck.deal())
    #     self.player.show_hand()
    #     self.dealer.show_hand()
    #     while self.player.hand.value < 21:
    #         self.player.hit(self.deck)
    #         self.player.show_hand()
    #         if self.player.hand.value > 21:
    #             print("You busted!")
    #             break
    #     if self.player.hand.value <= 21:
    #         while self.dealer.hand.value < 17:
    #             self.dealer.hit(self.deck)
    #             self.dealer.show_hand()
    #             if self.dealer.hand.value > 21:
    #                 print("Dealer busted!")
    #                 break
    #         if self.dealer.hand.value > self.player.hand.value:
    #             print("Dealer wins!")
    #         elif self.dealer.hand.value < self.player.hand.value:
    #             print("You win!")
    #         else:
    #             print("It's a tie!")
