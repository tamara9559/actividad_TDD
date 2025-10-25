from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Player:
    id: str
    rating: int


class Matchmaker:
    def __init__(self):
     self.queue: List[Player] = []


    def enqueue(self, player: Player):
     self.queue.append(player)


def find_matches(self) -> List[Tuple[Player, Player]]:
    # algoritmo simple: emparejar por diferencia mínima de rating
    matches = []
    used = set()
    for i, p in enumerate(self.queue):
     if p.id in used:
      continue
     best_j = None
     best_diff = None
     for j in range(i + 1, len(self.queue)):
      q = self.queue[j]
      if q.id in used:
        continue
      diff = abs(p.rating - q.rating)
      if best_diff is None or diff < best_diff:
        best_diff = diff
        best_j = j
    if best_j is not None:
     matches.append((p, self.queue[best_j]))
     used.add(p.id)
     used.add(self.queue[best_j].id)
    # mantener en cola los no emparejados
    self.queue = [p for p in self.queue if p.id not in used]
    return matches


def update_ratings(self, p1: Player, p2: Player, winner_id: str) -> Tuple[int, int]:
    # ELO simplificado
    k = 30
    r1 = p1.rating
    r2 = p2.rating
    expected1 = 1 / (1 + 10 ** ((r2 - r1) / 400))
    expected2 = 1 - expected1
    s1 = 1.0 if winner_id == p1.id else 0.0
    s2 = 1.0 if winner_id == p2.id else 0.0
    new_r1 = round(r1 + k * (s1 - expected1))
    new_r2 = round(r2 + k * (s2 - expected2))
    return new_r1, new_r2