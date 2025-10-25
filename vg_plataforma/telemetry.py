# ===========================================================
# Archivo: telemetry.py
# Descripción:
# Este módulo implementa el sistema de telemetría (TelemetrySystem)
# encargado de recopilar y analizar métricas de rendimiento dentro
# de la plataforma de videojuegos.
#
# Incluye:
#   - Clase TelemetrySystem (gestión de métricas y cálculos promedio)
#
# ===========================================================

import time
from typing import Dict, List

class TelemetrySystem:
    """
    Sistema de Telemetría para monitorear métricas de rendimiento del sistema.

    Esta clase permite medir tiempos de espera en cola, duración de partidas
    y registrar solicitudes procesadas, simulando un sistema básico de métricas
    de rendimiento para plataformas de videojuegos o aplicaciones en línea.

    Atributos:
        data (Dict[str, List[float]]):
            Diccionario que almacena listas de métricas por tipo:
            - "queue_times": tiempos de espera en cola.
            - "match_durations": duraciones de partidas.
            - "requests_per_minute": registros de solicitudes por minuto.

        start_times (Dict[str, float]):
            Diccionario temporal que almacena el tiempo de inicio de cada evento.
    """

    def __init__(self):
        """Inicializa el sistema de telemetría con estructuras vacías para las métricas."""
        self.data: Dict[str, List[float]] = {
            "queue_times": [],
            "match_durations": [],
            "requests_per_minute": []
        }
        self.start_times: Dict[str, float] = {}

    def start_timer(self, event: str):
        """
        Inicia un cronómetro para un evento determinado.

        Args:
            event (str): Nombre del evento que se desea cronometrar.
                         Ejemplos: "queue", "match".
        """
        self.start_times[event] = time.time()

    def stop_timer(self, event: str):
        """
        Detiene el cronómetro de un evento y almacena la duración registrada.

        Args:
            event (str): Nombre del evento a detener.

        Raises:
            ValueError: Si el evento no fue iniciado previamente con `start_timer()`.
        """
        if event not in self.start_times:
            raise ValueError(f"No se inició el evento '{event}' antes de detenerlo.")

        duration = time.time() - self.start_times[event]

        # Clasificar el tipo de métrica según el evento
        if event == "match":
            self.data["match_durations"].append(duration)
        elif event == "queue":
            self.data["queue_times"].append(duration)

        # Eliminar evento del registro temporal
        del self.start_times[event]

    def record_request(self):
        """
        Registra una nueva solicitud entrante en el sistema.

        Simula la captura de peticiones para medir la carga o el tráfico
        del sistema durante un periodo de tiempo.
        """
        timestamp = time.time()
        self.data["requests_per_minute"].append(timestamp)

    def get_average(self, metric: str) -> float:
        """
        Calcula el promedio de una métrica almacenada.

        Args:
            metric (str): Clave de la métrica a evaluar. Puede ser:
                          "queue_times", "match_durations" o "requests_per_minute".

        Returns:
            float: Valor promedio de la métrica seleccionada. Retorna 0.0 si no hay datos.
        """
        values = self.data.get(metric, [])
        if not values:
            return 0.0
        return sum(values) / len(values)

