"""Use this file for testing the functions for day 1 puzzle 1."""
import pytest

from _2019.src.day_1.shared_functions import calculate_fuel


@pytest.mark.parametrize("mass,fuel", [(12, 2), (14, 2), (1969, 654), (100756, 33583)])
def test_calculate_fuel(mass: int, fuel: int):
    assert calculate_fuel(mass) == fuel
