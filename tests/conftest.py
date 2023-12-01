import pytest

from core.data_capture import DataCapture


@pytest.fixture(scope="session")
def max_number():
    return 1000000


@pytest.fixture(scope="session")
def list_of_numbers(max_number):
    return range(max_number)


@pytest.fixture(scope="session")
def data_capture(list_of_numbers):
    capture = DataCapture()
    for number in list_of_numbers:
        capture.add(number)
    return capture


@pytest.fixture(scope="session")
def stats_builder(data_capture):
    return data_capture.build_stats()
