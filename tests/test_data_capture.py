import time

from core.data_capture import DataCapture


def test_less(stats_builder):
    assert stats_builder.less(100) == 99


def test_between(stats_builder):
    assert stats_builder.between(100, 200) == 101


def test_greater(stats_builder, max_number):
    assert stats_builder.greater(900) == max_number - 900


def test_stats_builder_time(stats_builder):
    start = time.time()
    stats_builder.less(100)
    stats_builder.between(100, 200)
    stats_builder.greater(900)
    end = time.time()
    assert end - start < 0.1


def test_data_cature_with_repeated_numbers():
    capture = DataCapture()
    capture.add(2)
    capture.add(2)
    capture.add(2)
    capture.add(4)
    capture.add(4)

    stats = capture.build_stats()

    assert stats.less(3) == 3
    assert stats.between(3, 5) == 2
    assert stats.greater(3) == 2
