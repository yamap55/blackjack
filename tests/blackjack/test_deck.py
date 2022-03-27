import pytest

from blackjack.card import Card
from blackjack.deck import Deck
from blackjack.suit import Suit


class TestDeck:
    class TestCards:
        @pytest.fixture(autouse=True)
        def setup(self):
            self.deck = Deck()

        def test_len(self):
            actual = len(self.deck.cards)
            expected = 52
            assert actual == expected

        def test_unique(self):
            original_cards = self.deck.cards
            unique_cards = list(set(self.deck.cards))
            actual = sorted(original_cards)
            expected = sorted(unique_cards)
            assert actual == expected

# TODO: add unittest 1..13 number
