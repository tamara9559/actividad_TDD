# ===========================================================
# Archivo: tournament.py
# Descripción:
# Este módulo gestiona el sistema de torneos (Tournament)
# basado en eliminación directa, utilizado para organizar
# competencias entre jugadores registrados en la plataforma.
#
# Incluye:
#   - Clase Tournament (gestión completa del flujo del torneo)
#
# ===========================================================

from typing import List, Dict, Tuple

class Tournament:
    """
    Sistema básico de gestión de torneos con eliminación directa (brackets).

    Esta clase permite registrar jugadores, crear emparejamientos automáticos
    en formato de torneo (por rondas), registrar resultados y avanzar rondas
    hasta determinar un ganador final.

    Está pensada como una funcionalidad dentro de una plataforma de videojuegos
    competitivos o sistema de gestión de eventos en línea.

    Atributos:
        id (str): Identificador único del torneo.
        players (List[str]): Lista de jugadores registrados.
        bracket_rounds (List[List[Tuple[str, str]]]): Rondas del torneo, donde cada
            ronda es una lista de enfrentamientos (pares de jugadores).
        results (Dict[Tuple[int, int], str]): Diccionario que almacena los ganadores
            de cada partida en cada ronda. Clave: (round_index, match_index).
    """

    def __init__(self, id_: str):
        """Inicializa un torneo con su identificador único y listas vacías."""
        self.id = id_
        self.players: List[str] = []
        self.bracket_rounds: List[List[Tuple[str, str]]] = []
        self.results: Dict[Tuple[int, int], str] = {}

    def register(self, player_id: str):
        """
        Registra un jugador en el torneo.

        Args:
            player_id (str): Identificador del jugador.

        Nota:
            No se permite registrar jugadores duplicados.
        """
        if player_id not in self.players:
            self.players.append(player_id)

    def create_bracket(self):
        """
        Crea el cuadro de emparejamientos (bracket) del torneo.

        Requisitos:
            - El número de jugadores debe ser una potencia de 2
              (2, 4, 8, 16, ...).

        Raises:
            ValueError: Si el número de jugadores no es una potencia de 2.
        """
        n = len(self.players)
        if n & (n - 1) != 0:
            raise ValueError("Número de jugadores debe ser potencia de 2 para este MVP.")

        # Primera ronda: emparejar jugadores de forma consecutiva
        first = []
        for i in range(0, n, 2):
            first.append((self.players[i], self.players[i + 1]))
        self.bracket_rounds = [first]

        # Crear rondas vacías siguientes (semifinales, final, etc.)
        rn = n // 2
        while rn >= 1:
            rn //= 2
            if rn >= 1:
                self.bracket_rounds.append([])

    def set_match_result(self, round_index: int, match_index: int, winner: str):
        """
        Registra el resultado de un enfrentamiento.

        Args:
            round_index (int): Índice de la ronda.
            match_index (int): Índice del partido dentro de la ronda.
            winner (str): ID del jugador ganador.
        """
        self.results[(round_index, match_index)] = winner

    def advance_round(self, round_index: int):
        """
        Avanza el torneo a la siguiente ronda con base en los ganadores registrados.

        Args:
            round_index (int): Índice de la ronda actual.

        Raises:
            ValueError: Si no se encuentran resultados para todos los enfrentamientos.
        """
        current_round = self.bracket_rounds[round_index]
        next_round = []

        # Validar que existan resultados para todos los matches
        for i, match in enumerate(current_round):
            key = (round_index, i)
            if key not in self.results:
                raise ValueError(f"Falta resultado para el partido {i} de la ronda {round_index}.")
            winner = self.results[key]
            next_round.append(winner)

        # Generar enfrentamientos para la siguiente ronda
        next_matches = []
        for i in range(0, len(next_round), 2):
            if i + 1 < len(next_round):
                next_matches.append((next_round[i], next_round[i + 1]))

        # Agregar la nueva ronda al bracket
        if round_index + 1 < len(self.bracket_rounds):
            self.bracket_rounds[round_index + 1] = next_matches
