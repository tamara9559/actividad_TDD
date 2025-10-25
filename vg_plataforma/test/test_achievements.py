import pytest
from achievements import AchievementSystem


def test_first_win_achievement():
    a = AchievementSystem()
    a.register_win("player1")

    assert "FIRST_WIN" in a.get_achievements("player1")
    assert "FIVE_WINS" not in a.get_achievements("player1")


def test_five_wins_achievement():
    a = AchievementSystem()

    for _ in range(5):
        a.register_win("player1")

    assert "FIRST_WIN" in a.get_achievements("player1")
    assert "FIVE_WINS" in a.get_achievements("player1")


def test_tournament_win_achievement():
    a = AchievementSystem()
    a.register_tournament_win("player2")

    assert "TOURNAMENT_WIN" in a.get_achievements("player2")
