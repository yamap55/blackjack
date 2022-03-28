import pytest

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

        def test_range_1_13(self):
            numbers = set([c.number for c in self.deck.cards])

            assert min(numbers) == 1
            assert max(numbers) == 13

        def test_suits(self):
            actual = sorted(list(set([c.suit for c in self.deck.cards])))
            expected = sorted(list(Suit))
            assert actual == expected
