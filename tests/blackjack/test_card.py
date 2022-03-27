from blackjack.card import Card
from blackjack.suit import Suit


class TestCard:
    def test_str(self):
        card = Card(Suit.SPADE, 1)

        actual = str(card)
        expected = "Card: SPADE 1"
        assert actual == expected

    def test_repr(self):
        card = Card(Suit.SPADE, 1)

        actual = card.__repr__()
        expected = "{'suit': 'SPADE', 'number': 1}"
        assert actual == expected
