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

    class TestEqual:
        def test_equal(self):
            card1 = Card(Suit.SPADE, 1)
            card2 = Card(Suit.SPADE, 1)

            assert card1 == card2

        def test_not_equal_suit(self):
            card1 = Card(Suit.SPADE, 1)
            card2 = Card(Suit.HEART, 1)

            assert card1 != card2

        def test_not_equal_number(self):
            card1 = Card(Suit.SPADE, 1)
            card2 = Card(Suit.SPADE, 2)

            assert card1 != card2

        def test_not_equal_not_card(self):
            card1 = Card(Suit.SPADE, 1)
            card2 = 1

            assert card1 != card2
