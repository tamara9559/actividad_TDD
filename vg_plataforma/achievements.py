from typing import Dict, List


class AchievementSystem:
    def __init__(self):
        # Diccionario de jugadores y sus logros
        self.achievements: Dict[str, List[str]] = {}
        # Reglas simples de ejemplo
        self.rules = {
            "FIRST_WIN": "Primera victoria obtenida",
            "FIVE_WINS": "Cinco victorias acumuladas",
            "TOURNAMENT_WIN": "Ganó un torneo"
        }

        # Contador de victorias por jugador
        self.win_count: Dict[str, int] = {}

    def register_win(self, player_id: str):
        """Registra una victoria y evalúa logros alcanzados"""
        self.win_count[player_id] = self.win_count.get(player_id, 0) + 1
        self.achievements.setdefault(player_id, [])

        # Logro por primera victoria
        if self.win_count[player_id] == 1 and "FIRST_WIN" not in self.achievements[player_id]:
            self.achievements[player_id].append("FIRST_WIN")

        # Logro por cinco victorias
        if self.win_count[player_id] == 5 and "FIVE_WINS" not in self.achievements[player_id]:
            self.achievements[player_id].append("FIVE_WINS")

    def register_tournament_win(self, player_id: str):
        """Logro especial por ganar un torneo"""
        self.achievements.setdefault(player_id, [])
        if "TOURNAMENT_WIN" not in self.achievements[player_id]:
            self.achievements[player_id].append("TOURNAMENT_WIN")

    def get_achievements(self, player_id: str) -> List[str]:
        """Devuelve los logros actuales del jugador"""
        return self.achievements.get(player_id, [])
