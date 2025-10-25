import time
from typing import Dict, List


class TelemetrySystem:
    def __init__(self):
        # Métricas simples de ejemplo
        self.data: Dict[str, List[float]] = {
            "queue_times": [],
            "match_durations": [],
            "requests_per_minute": []
        }

        self.start_times: Dict[str, float] = {}

    def start_timer(self, event: str):
        """Inicia un cronómetro para un evento"""
        self.start_times[event] = time.time()

    def stop_timer(self, event: str):
        """Detiene el cronómetro y guarda la duración"""
        if event not in self.start_times:
            raise ValueError(f"No se inició el evento '{event}' antes de detenerlo.")
        duration = time.time() - self.start_times[event]
        if event == "match":
            self.data["match_durations"].append(duration)
        elif event == "queue":
            self.data["queue_times"].append(duration)
        del self.start_times[event]

    def record_request(self):
        """Simula el registro de una solicitud (para medir carga del sistema)"""
        timestamp = time.time()
        self.data["requests_per_minute"].append(timestamp)

    def get_average(self, metric: str) -> float:
        """Promedio de una métrica específica"""
        values = self.data.get(metric, [])
        if not values:
            return 0.0
        return sum(values) / len(values)
