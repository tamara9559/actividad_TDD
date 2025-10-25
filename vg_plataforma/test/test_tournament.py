import pytest
from tournament import Tournament

def test_tournament_bracket_advance():
    t = Tournament('t1')
    # registrar 4 jugadores
    players = ['a', 'b', 'c', 'd']
    for p in players:
     t.register(p)


    t.create_bracket()
    # Simular resultados de cuartos a semifinal y final
    # Hay 2 rondas (4 -> 2 -> 1)
    assert len(t.bracket_rounds) == 2


    # Usar avance manual
    t.set_match_result(0, 0, winner='a')
    t.set_match_result(0, 1, winner='c')

    t.advance_round(0)
    # Comprobar que la siguiente ronda contiene a 'a' y 'c'
    assert any('a' in m and 'c' in m for m in t.bracket_rounds[1])