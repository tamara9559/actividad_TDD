import time
import pytest
from telemetry import TelemetrySystem


def test_queue_time_measurement():
    t = TelemetrySystem()

    t.start_timer("queue")
    time.sleep(0.1)
    t.stop_timer("queue")

    avg_time = t.get_average("queue_times")
    assert avg_time > 0


def test_match_duration_measurement():
    t = TelemetrySystem()

    t.start_timer("match")
    time.sleep(0.1)
    t.stop_timer("match")

    assert len(t.data["match_durations"]) == 1
    assert t.get_average("match_durations") > 0


def test_record_requests():
    t = TelemetrySystem()

    for _ in range(3):
        t.record_request()

    assert len(t.data["requests_per_minute"]) == 3
