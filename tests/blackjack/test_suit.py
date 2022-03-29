import pytest

from blackjack.suit import Suit


class TestSuit:
    @pytest.mark.parametrize(
        "suit, expected",
        [
            (Suit.SPADE, 1),
            (Suit.HEART, 2),
            (Suit.DIAMOND, 3),
            (Suit.CLUB, 4),
        ],
    )
    def test_value(self, suit, expected):
        actual = suit.value
        assert actual == expected

    def test_lt(self):
        assert Suit.SPADE < Suit.HEART < Suit.DIAMOND < Suit.CLUB

    def test_gt(self):
        assert Suit.CLUB > Suit.DIAMOND > Suit.HEART > Suit.SPADE

    def test_le(self):
        assert Suit.SPADE <= Suit.HEART <= Suit.DIAMOND <= Suit.CLUB

    def test_ge(self):
        assert Suit.CLUB >= Suit.DIAMOND >= Suit.HEART >= Suit.SPADE
