# ===========================================================
# Archivo: test_tournament.py
# Descripción:
# Este archivo contiene las pruebas unitarias del módulo
# "tournament", encargado de administrar los torneos dentro
# del sistema de videojuegos.
#
# El módulo gestiona el registro de jugadores, la creación de
# brackets automáticos (emparejamientos), la asignación de
# ganadores y el avance entre rondas hasta definir al campeón.
#
# Este conjunto de pruebas valida la lógica de creación y
# avance de rondas en formato eliminatorio.
#
# ===========================================================

import pytest
from tournament import Tournament


# -----------------------------------------------------------
# Prueba principal: Validar creación y avance del bracket
# -----------------------------------------------------------
def test_tournament_bracket_advance():
    """
    Verifica que el sistema de torneos cree brackets correctos
    y permita avanzar entre rondas conforme se registran los
    resultados de los enfrentamientos.

    Flujo verificado:
    1. Registro de jugadores.
    2. Creación de brackets.
    3. Simulación de resultados.
    4. Avance a la siguiente ronda.
    """

    # Se crea una instancia del torneo con ID 't1'
    t = Tournament('t1')

    # Se registran 4 jugadores
    players = ['a', 'b', 'c', 'd']
    for p in players:
        t.register(p)

    # Se genera el bracket inicial con los jugadores registrados
    t.create_bracket()

    # Validación: con 4 jugadores debe haber 2 rondas (semifinal y final)
    assert len(t.bracket_rounds) == 2, \
        "El número de rondas generadas en el bracket no es correcto."

    # Se simulan los resultados de la primera ronda (semifinales)
    t.set_match_result(0, 0, winner='a')   # Gana 'a' contra 'b'
    t.set_match_result(0, 1, winner='c')   # Gana 'c' contra 'd'

    # Se avanza a la siguiente ronda (final)
    t.advance_round(0)

    # Validación: la segunda ronda debe incluir a los ganadores 'a' y 'c'
    assert any('a' in m and 'c' in m for m in t.bracket_rounds[1]), \
        "Los ganadores no fueron correctamente transferidos a la siguiente ronda."
