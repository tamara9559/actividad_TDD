# ===========================================================
# Archivo: matchmaking.py
# Descripción:
# Este módulo implementa el sistema de emparejamiento (Matchmaker)
# de la plataforma de videojuegos. Su objetivo es emparejar jugadores
# con niveles de habilidad similares utilizando un sistema de calificación
# tipo ELO y mantener una cola de espera dinámica.
#
# Incluye:
#   - Clase Player (modelo de jugador)
#   - Clase Matchmaker (gestión de emparejamientos y actualización de rating)
#
# ===========================================================

from dataclasses import dataclass
from typing import List, Tuple


# -----------------------------------------------------------
# Modelo de datos: Jugador
# -----------------------------------------------------------
@dataclass
class Player:
    """
    Representa a un jugador dentro del sistema de emparejamiento.

    Atributos:
        id (str): Identificador único del jugador.
        rating (int): Nivel de habilidad del jugador (ELO aproximado).
    """
    id: str
    rating: int


# -----------------------------------------------------------
# Clase principal: Matchmaker
# -----------------------------------------------------------
class Matchmaker:
    """
    Sistema de emparejamiento simple basado en rating ELO.

    Funcionalidades:
    - Mantiene una cola de jugadores buscando partida.
    - Encuentra emparejamientos según diferencias mínimas de rating.
    - Actualiza calificaciones tras cada partida.
    """

    def __init__(self):
        """
        Inicializa la cola de jugadores.
        """
        self.queue: List[Player] = []

    # -------------------------------------------------------
    # Agregar jugador a la cola
    # -------------------------------------------------------
    def enqueue(self, player: Player):
        """
        Agrega un jugador a la cola de emparejamiento.

        Args:
            player (Player): Jugador que desea buscar partida.
        """
        self.queue.append(player)

    # -------------------------------------------------------
    # Encontrar emparejamientos por similitud de rating
    # -------------------------------------------------------
    def find_matches(self) -> List[Tuple[Player, Player]]:
        """
        Empareja jugadores en base a la menor diferencia de rating posible.

        Returns:
            List[Tuple[Player, Player]]: Lista de tuplas con pares de jugadores emparejados.
        """
        matches = []
        used = set()

        # Recorre la cola para buscar el mejor emparejamiento posible
        for i, p in enumerate(self.queue):
            if p.id in used:
                continue

            best_j = None
            best_diff = None

            # Buscar el jugador con menor diferencia de rating
            for j in range(i + 1, len(self.queue)):
                q = self.queue[j]
                if q.id in used:
                    continue

                diff = abs(p.rating - q.rating)
                if best_diff is None or diff < best_diff:
                    best_diff = diff
                    best_j = j

            # Si se encontró pareja, agregar a la lista de matches
            if best_j is not None:
                matches.append((p, self.queue[best_j]))
                used.add(p.id)
                used.add(self.queue[best_j].id)

        # Mantener en cola los jugadores no emparejados
        self.queue = [p for p in self.queue if p.id not in used]

        return matches

    # -------------------------------------------------------
    # Actualizar ratings según resultado de la partida
    # -------------------------------------------------------
    def update_ratings(self, p1: Player, p2: Player, winner_id: str) -> Tuple[int, int]:
        """
        Actualiza los ratings de los jugadores tras una partida
        utilizando un sistema ELO simplificado.

        Args:
            p1 (Player): Primer jugador.
            p2 (Player): Segundo jugador.
            winner_id (str): ID del jugador ganador.

        Returns:
            Tuple[int, int]: Nuevos ratings (p1, p2).
        """
        k = 30  # factor de ajuste ELO
        r1 = p1.rating
        r2 = p2.rating

        # Expectativas de victoria (según fórmula ELO)
        expected1 = 1 / (1 + 10 ** ((r2 - r1) / 400))
        expected2 = 1 - expected1

        # Resultado real (1 si gana, 0 si pierde)
        s1 = 1.0 if winner_id == p1.id else 0.0
        s2 = 1.0 if winner_id == p2.id else 0.0

        # Nuevos ratings
        new_r1 = round(r1 + k * (s1 - expected1))
        new_r2 = round(r2 + k * (s2 - expected2))

        return new_r1, new_r2
