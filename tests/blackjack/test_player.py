import pytest

from blackjack.card import Card
from blackjack.player import Player
from blackjack.suit import Suit


class TestPlayer:
    class TestInit:
        def test_args_not_exists(self):
            player = Player()

            actual = player.cards
            expected = []
            assert actual == expected

        def test_args_exists(self):
            player = Player([Card(Suit.SPADE, 1)])

            actual = player.cards
            expected = [Card(Suit.SPADE, 1)]
            assert actual == expected

    class TestTotal:
        def test_total(self):
            player = Player([Card(Suit.SPADE, 1), Card(Suit.SPADE, 2)])

            actual = player.total
            expected = 3
            assert actual == expected

    class TestAppendCard:
        @pytest.fixture(autouse=True)
        def setup(self):
            self.player = Player()

        def test_append_card(self):
            player = Player()
            player.append_card(Card(Suit.SPADE, 1))

            actual = player.cards
            expected = [Card(Suit.SPADE, 1)]
            assert actual == expected

        def test_append_card_multiple(self):
            player = Player()
            player.append_card(Card(Suit.SPADE, 1))
            player.append_card(Card(Suit.SPADE, 2))

            actual = player.cards
            expected = [Card(Suit.SPADE, 1), Card(Suit.SPADE, 2)]
            assert actual == expected
