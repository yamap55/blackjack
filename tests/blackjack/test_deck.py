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

        def test_range_1_13(self):
            numbers = set([c.number for c in self.deck.cards])

            assert min(numbers) == 1
            assert max(numbers) == 13

        def test_suits(self):
            actual = sorted(list(set([c.suit for c in self.deck.cards])))
            expected = sorted(list(Suit))
            assert actual == expected

    def test_shuffle_cards(self):
        deck = Deck(0)

        # samping
        actual = deck.cards[:5]
        expected = [
            Card(Suit.DIAMOND, 3),
            Card(Suit.SPADE, 13),
            Card(Suit.CLUB, 7),
            Card(Suit.CLUB, 3),
            Card(Suit.DIAMOND, 13),
        ]

        assert actual == expected

    class TestDraw:
        @pytest.fixture(autouse=True)
        def setup(self):
            self.deck = Deck()

        def test_not_args(self):
            card = self.deck.draw()

            assert card not in self.deck.cards
            assert len(self.deck.cards) == 51

        def test_empty_cards(self):

            self.deck.cards = []

            with pytest.raises(IndexError):
                self.deck.draw()

    class TestLen:
        @pytest.fixture(autouse=True)
        def setup(self):
            self.deck = Deck()

        def test_default(self):
            assert len(self.deck) == 52

        def test_after_draw(self):
            self.deck.draw()
            assert len(self.deck) == 51
