# ===========================================================
# Archivo: test_telemetry.py
# Descripción:
# Este archivo contiene las pruebas unitarias del módulo
# "telemetry", encargado de registrar y medir métricas de
# rendimiento dentro de la plataforma de videojuegos (VG_Plataforma).
#
# La telemetría se utiliza para monitorear tiempos de espera,
# duración de partidas y cantidad de solicitudes por minuto,
# proporcionando datos útiles para optimización y análisis.
#
# Estas pruebas validan que las métricas se registren
# correctamente y que los cálculos de promedio sean precisos.
#
# ===========================================================

import time
import pytest
from vg_plataforma.telemetry import TelemetrySystem


# -----------------------------------------------------------
# Prueba 1: Medición del tiempo en cola (queue)
# -----------------------------------------------------------
def test_queue_time_measurement():
    """
    Verifica que el sistema de telemetría mida correctamente
    el tiempo que los jugadores pasan en cola antes de ser
    emparejados.
    """

    # Se crea una instancia del sistema de telemetría
    t = TelemetrySystem()

    # Inicia el cronómetro para el evento "queue"
    t.start_timer("queue")

    # Simula el tiempo de espera de un jugador en cola
    time.sleep(0.1)

    # Finaliza el cronómetro y guarda el resultado
    t.stop_timer("queue")

    # Se obtiene el promedio de tiempo en cola registrado
    avg_time = t.get_average("queue_times")

    # Validación: el promedio debe ser mayor que cero
    assert avg_time > 0, "El tiempo promedio en cola no fue calculado correctamente."


# -----------------------------------------------------------
# Prueba 2: Medición de la duración de una partida
# -----------------------------------------------------------
def test_match_duration_measurement():
    """
    Verifica que el sistema registre correctamente la duración
    de una partida y almacene los resultados en la métrica
    correspondiente ("match_durations").
    """

    t = TelemetrySystem()

    # Inicia el cronómetro para una partida
    t.start_timer("match")

    # Simula la duración de una partida
    time.sleep(0.1)

    # Detiene el cronómetro
    t.stop_timer("match")

    # Verifica que se haya registrado una sola duración de partida
    assert len(t.data["match_durations"]) == 1, "No se registró la duración de la partida."

    # Verifica que el promedio calculado sea válido
    assert t.get_average("match_durations") > 0, "El promedio de duración no es válido."


# -----------------------------------------------------------
# Prueba 3: Registro de solicitudes por minuto
# -----------------------------------------------------------
def test_record_requests():
    """
    Verifica que el sistema registre correctamente las solicitudes
    entrantes al servidor (requests per minute), simulando la
    frecuencia con la que los usuarios interactúan con la API.
    """

    t = TelemetrySystem()

    # Se simulan tres solicitudes entrantes
    for _ in range(3):
        t.record_request()

    # Validación: deben haberse registrado tres solicitudes
    assert len(t.data["requests_per_minute"]) == 3, \
        "El número de solicitudes registradas no coincide."
