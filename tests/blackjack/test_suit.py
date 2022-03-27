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
        ]
    )
    def test_value(self, suit, expected):
        actual = suit.value
        assert actual == expected
