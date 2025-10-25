# ===========================================================
# Archivo: achievement_system.py
# Descripción:
# Este módulo implementa el sistema de logros de la plataforma
# de videojuegos. Su función principal es registrar victorias,
# contabilizar progresos y otorgar logros especiales a los
# jugadores cuando cumplen ciertos hitos dentro del sistema.
#
# Ejemplos de logros:
#   - FIRST_WIN: primera victoria registrada.
#   - FIVE_WINS: cinco victorias acumuladas.
#   - TOURNAMENT_WIN: victoria en un torneo.
#
# El sistema está diseñado para integrarse con otros módulos
# como "tournament" (para registrar victorias en torneos) y
# "matchmaking" (para registrar partidas ganadas).
#
# ===========================================================

from typing import Dict, List


class AchievementSystem:
    """
    Clase principal encargada de gestionar los logros de los jugadores.

    Responsabilidades:
    - Registrar victorias individuales o de torneos.
    - Contabilizar la cantidad total de victorias por jugador.
    - Asignar logros según reglas predefinidas.
    - Permitir la consulta de los logros actuales de un jugador.
    """

    def __init__(self):
        """
        Inicializa las estructuras internas del sistema de logros.
        """
        # Diccionario que asocia cada jugador con una lista de logros obtenidos.
        self.achievements: Dict[str, List[str]] = {}

        # Reglas base del sistema de logros (clave = código del logro).
        self.rules = {
            "FIRST_WIN": "Primera victoria obtenida",
            "FIVE_WINS": "Cinco victorias acumuladas",
            "TOURNAMENT_WIN": "Ganó un torneo"
        }

        # Contador de victorias por jugador.
        self.win_count: Dict[str, int] = {}

    # -----------------------------------------------------------
    # Registro de victorias individuales
    # -----------------------------------------------------------
    def register_win(self, player_id: str):
        """
        Registra una victoria individual y evalúa los logros alcanzados.

        Args:
            player_id (str): ID único del jugador.

        Lógica:
        - Incrementa el contador de victorias.
        - Si es la primera victoria, otorga el logro "FIRST_WIN".
        - Si alcanza cinco victorias, otorga el logro "FIVE_WINS".
        """
        # Incrementar contador de victorias del jugador
        self.win_count[player_id] = self.win_count.get(player_id, 0) + 1

        # Asegurar que el jugador tenga una lista de logros asignada
        self.achievements.setdefault(player_id, [])

        # Logro por primera victoria
        if self.win_count[player_id] == 1 and "FIRST_WIN" not in self.achievements[player_id]:
            self.achievements[player_id].append("FIRST_WIN")

        # Logro por cinco victorias
        if self.win_count[player_id] == 5 and "FIVE_WINS" not in self.achievements[player_id]:
            self.achievements[player_id].append("FIVE_WINS")

    # -----------------------------------------------------------
    # Registro de victoria en torneo
    # -----------------------------------------------------------
    def register_tournament_win(self, player_id: str):
        """
        Registra un logro especial cuando el jugador gana un torneo.

        Args:
            player_id (str): ID único del jugador.
        """
        self.achievements.setdefault(player_id, [])
        if "TOURNAMENT_WIN" not in self.achievements[player_id]:
            self.achievements[player_id].append("TOURNAMENT_WIN")

    # -----------------------------------------------------------
    # Consulta de logros
    # -----------------------------------------------------------
    def get_achievements(self, player_id: str) -> List[str]:
        """
        Devuelve la lista de logros actuales del jugador.

        Args:
            player_id (str): ID del jugador.

        Returns:
            List[str]: Lista de códigos de logros obtenidos.
        """
        return self.achievements.get(player_id, [])
