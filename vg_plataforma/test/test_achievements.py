# ===========================================================
# Archivo: test_achievements.py
# Descripción:
# Este archivo contiene las pruebas unitarias del módulo
# AchievementSystem, que forma parte del sistema de videojuegos.
#
# Las pruebas siguen el enfoque TDD (Test-Driven Development),
# validando que los logros se asignen correctamente a los jugadores
# según sus victorias o triunfos en torneos.
#
# ===========================================================

import pytest
from achievements import AchievementSystem


# -----------------------------------------------------------
# Prueba 1: Verifica el logro por primera victoria
# -----------------------------------------------------------
def test_first_win_achievement():
    # Se crea una instancia del sistema de logros
    a = AchievementSystem()

    # Se registra una primera victoria del jugador "player1"
    a.register_win("player1")

    # Se comprueba que el logro 'FIRST_WIN' se haya asignado
    assert "FIRST_WIN" in a.get_achievements("player1")

    # Se asegura que aún no tenga el logro de 5 victorias
    assert "FIVE_WINS" not in a.get_achievements("player1")


# -----------------------------------------------------------
# Prueba 2: Verifica el logro por cinco victorias consecutivas
# -----------------------------------------------------------
def test_five_wins_achievement():
    # Se inicializa el sistema de logros
    a = AchievementSystem()

    # Se registran 5 victorias del mismo jugador
    for _ in range(5):
        a.register_win("player1")

    # Se comprueba que tenga el logro por primera victoria
    assert "FIRST_WIN" in a.get_achievements("player1")

    # Se comprueba que también tenga el logro de cinco victorias
    assert "FIVE_WINS" in a.get_achievements("player1")


# -----------------------------------------------------------
# Prueba 3: Verifica el logro por ganar un torneo
# -----------------------------------------------------------
def test_tournament_win_achievement():
    # Se crea el sistema de logros
    a = AchievementSystem()

    # Se registra un triunfo en torneo del jugador "player2"
    a.register_tournament_win("player2")

    # Se valida que el logro 'TOURNAMENT_WIN' se haya otorgado
    assert "TOURNAMENT_WIN" in a.get_achievements("player2")

