from typing import List, Dict, Tuple


class Tournament:
    def __init__(self, id_: str):
        self.id = id_
        self.players: List[str] = []
        self.bracket_rounds: List[List[Tuple[str, str]]] = []
        # almacenar resultados como dict {(round_index, match_index): winner}
        self.results: Dict[Tuple[int, int], str] = {}


    def register(self, player_id: str):
     if player_id not in self.players:
      self.players.append(player_id)


def create_bracket(self):
    # soporta solo potencias de 2 para simplicidad
    n = len(self.players)
    if n & (n - 1) != 0:
        raise ValueError('Número de jugadores debe ser potencia de 2 para este MVP')
    # Primera ronda: parejas consecutivas
    first = []
    for i in range(0, n, 2):
        first.append((self.players[i], self.players[i+1]))
    self.bracket_rounds = [first]
    # crear rondas vacías posterior hasta la final
    rn = n // 2
    while rn >= 1:
        rn //= 2
        if rn >= 1:
          self.bracket_rounds.append([])


    def set_match_result(self, round_index: int, match_index: int, winner: str):
        self.results[(round_index, match_index)] = winner


    def advance_round(self, round_index: int):
        # calcular ganadores de la ronda y poblar la siguiente
        current_round = self.bracket_rounds[round_index]