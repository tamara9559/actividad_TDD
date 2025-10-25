# ===========================================================
# Archivo: test_matchmaking.py
# Descripción:
# Este archivo contiene las pruebas unitarias del módulo
# "matchmaking", encargado de emparejar jugadores según su
# nivel de habilidad (ELO) y actualizar sus puntuaciones
# después de cada partida.
#
# Las pruebas siguen la metodología TDD (Test-Driven Development),
# validando que el emparejamiento sea justo y que el cálculo
# del nuevo rating funcione correctamente después de un juego.
#
# ===========================================================

import pytest
from matchmaking import Matchmaker, Player


# -----------------------------------------------------------
# Prueba 1: Emparejamiento por rating similar
# -----------------------------------------------------------
def test_matchmaker_pairs_similar_rating():
    """
    Verifica que el sistema de matchmaking empareje correctamente
    a jugadores con niveles de habilidad similares, y deje en cola
    a los que no tengan una coincidencia cercana.
    """

    # Se crea una instancia del sistema de emparejamiento
    m = Matchmaker()

    # Se crean tres jugadores con diferentes niveles de rating
    p1 = Player(id="p1", rating=1200)
    p2 = Player(id="p2", rating=1210)
    p3 = Player(id="p3", rating=1500)

    # Se agregan los jugadores a la cola de emparejamiento
    m.enqueue(p1)
    m.enqueue(p2)
    m.enqueue(p3)

    # Se ejecuta el proceso de búsqueda de coincidencias
    matches = m.find_matches()

    # Validación: debe emparejar a los jugadores p1 y p2 (ratings cercanos)
    assert any(
        (a.id == 'p1' and b.id == 'p2') or (a.id == 'p2' and b.id == 'p1')
        for a, b in matches
    ), "El sistema no emparejó correctamente a los jugadores con rating similar."

    # Validación adicional: el jugador p3 debe quedar sin pareja (no fue emparejado)
    assert all(
        'p3' not in (a.id, b.id) for a, b in matches
    ), "El jugador con rating alto no debería haber sido emparejado aún."


# -----------------------------------------------------------
# Prueba 2: Actualización del rating después de una partida
# -----------------------------------------------------------
def test_rating_update_after_game():
    """
    Verifica que el sistema de emparejamiento actualice los
    ratings correctamente después de una partida utilizando
    la fórmula ELO simplificada.
    """

    # Se crea una instancia del sistema
    m = Matchmaker()

    # Se crean dos jugadores con el mismo rating inicial
    p1 = Player(id='p1', rating=1200)
    p2 = Player(id='p2', rating=1200)

    # Se simula una partida donde p1 es el ganador
    new_r1, new_r2 = m.update_ratings(p1, p2, winner_id='p1')

    # El rating del ganador debe aumentar
    assert new_r1 > 1200, "El rating del jugador ganador no aumentó correctamente."

    # El rating del perdedor debe disminuir
    assert new_r2 < 1200, "El rating del jugador perdedor no disminuyó correctamente."
