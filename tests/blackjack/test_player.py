import pytest

from blackjack.card import Card
from blackjack.player import Player
from blackjack.suit import Suit


class TestPlayer:
    @pytest.fixture
    def player(self):
        return Player()

    class TestInit:
        def test_hands_args_not_exists(self, player: Player):
            actual = player.hands
            expected = []
            assert actual == expected

        def test_hands_args_exists(self):
            player = Player(hands=[Card(Suit.SPADE, 1)])

            actual = player.hands
            expected = [Card(Suit.SPADE, 1)]
            assert actual == expected

        def test_game_count(self, player: Player):
            actual = player.game_count
            expected = 0
            assert actual == expected

        def test_win_count(self, player: Player):
            actual = player.win_count
            expected = 0
            assert actual == expected

        def test_name_default(self, player: Player):
            actual = player.name
            expected = "player"
            assert actual == expected

        def test_name_args(self):
            player = Player(name="test")

            actual = player.name
            expected = "test"
            assert actual == expected

    class TestTotal:
        def test_total(self):
            player = Player(hands=[Card(Suit.SPADE, 1), Card(Suit.SPADE, 2)])

            actual = player.total
            expected = 3
            assert actual == expected

    class TestAppendCard:
        def test_append_card(self, player: Player):
            player.append_card(Card(Suit.SPADE, 1))

            actual = player.hands
            expected = [Card(Suit.SPADE, 1)]
            assert actual == expected

        def test_append_card_multiple(self, player: Player):
            player.append_card(Card(Suit.SPADE, 1))
            player.append_card(Card(Suit.SPADE, 2))

            actual = player.hands
            expected = [Card(Suit.SPADE, 1), Card(Suit.SPADE, 2)]
            assert actual == expected

    class TestWin:
        @pytest.fixture(autouse=True)
        def setup(self, player: Player):
            self.player = player
            self.player.win()

        def test_win_count(self):
            actual = self.player.win_count
            expected = 1
            assert actual == expected

        def test_game_count(self):
            actual = self.player.game_count
            expected = 1
            assert actual == expected

    class TestLose:
        @pytest.fixture(autouse=True)
        def setup(self, player: Player):
            self.player = player
            self.player.lose()

        def test_win_count(self):
            actual = self.player.win_count
            expected = 0
            assert actual == expected

        def test_game_count(self):
            actual = self.player.game_count
            expected = 1
            assert actual == expected

    class TestDraw:
        @pytest.fixture(autouse=True)
        def setup(self, player: Player):
            self.player = player
            self.player.draw()

        def test_win_count(self):
            actual = self.player.win_count
            expected = 0
            assert actual == expected

        def test_game_count(self):
            actual = self.player.game_count
            expected = 1
            assert actual == expected
