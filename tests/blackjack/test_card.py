import pytest

from blackjack.card import Card
from blackjack.suit import Suit


class TestCard:
    class TestStr:
        @pytest.mark.parametrize(
            "suit, number, expected",
            [
                (Suit.SPADE, 2, "♠2"),
                (Suit.SPADE, 3, "♠3"),
                (Suit.SPADE, 4, "♠4"),
                (Suit.SPADE, 5, "♠5"),
                (Suit.SPADE, 6, "♠6"),
                (Suit.SPADE, 7, "♠7"),
                (Suit.SPADE, 8, "♠8"),
                (Suit.SPADE, 9, "♠9"),
                (Suit.SPADE, 10, "♠10"),
            ],
        )
        def test_pip_card(self, suit, number, expected):
            card = Card(suit, number)

            actual = str(card)
            assert actual == expected

        @pytest.mark.parametrize(
            "suit, number, expected",
            [
                (Suit.SPADE, 1, "♠A"),
                (Suit.SPADE, 11, "♠J"),
                (Suit.SPADE, 12, "♠Q"),
                (Suit.SPADE, 13, "♠K"),
            ],
        )
        def test_face_card(self, suit, number, expected):
            card = Card(suit, number)

            actual = str(card)
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

    class TestLT:
        def test_suit(self):
            card1 = Card(Suit.SPADE, 1)
            card2 = Card(Suit.HEART, 1)

            assert card1 < card2

        def test_number(self):
            card1 = Card(Suit.SPADE, 1)
            card2 = Card(Suit.SPADE, 2)

            assert card1 < card2

        def test_equal(self):
            card1 = Card(Suit.SPADE, 1)
            card2 = Card(Suit.SPADE, 1)

            assert not card1 < card2

    class TestGT:
        def test_suit(self):
            card1 = Card(Suit.HEART, 1)
            card2 = Card(Suit.SPADE, 1)

            assert card1 > card2

        def test_number(self):
            card1 = Card(Suit.SPADE, 2)
            card2 = Card(Suit.SPADE, 1)

            assert card1 > card2

        def test_equal(self):
            card1 = Card(Suit.SPADE, 1)
            card2 = Card(Suit.SPADE, 1)

            assert not card1 > card2

    class TestLE:
        def test_suit(self):
            card1 = Card(Suit.SPADE, 1)
            card2 = Card(Suit.HEART, 1)

            assert card1 <= card2

        def test_number(self):
            card1 = Card(Suit.SPADE, 1)
            card2 = Card(Suit.SPADE, 2)

            assert card1 <= card2

        def test_equal(self):
            card1 = Card(Suit.SPADE, 1)
            card2 = Card(Suit.SPADE, 1)

            assert card1 <= card2

    class TestGE:
        def test_suit(self):
            card1 = Card(Suit.HEART, 1)
            card2 = Card(Suit.SPADE, 1)

            assert card1 >= card2

        def test_number(self):
            card1 = Card(Suit.SPADE, 2)
            card2 = Card(Suit.SPADE, 1)

            assert card1 >= card2

        def test_equal(self):
            card1 = Card(Suit.SPADE, 1)
            card2 = Card(Suit.SPADE, 1)

            assert card1 >= card2
