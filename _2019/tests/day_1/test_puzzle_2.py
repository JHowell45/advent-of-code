"""Use this file for testing the functions for day 1 puzzle 2."""
import pytest

from _2019.src.day_1.puzzle_2 import calculate_all_fuel_requirements


@pytest.mark.parametrize("mass,fuel", [(14, 2), (1969, 966), (100756, 50346)])
def test_calculate_all_fuel(mass: int, fuel: int):
    assert calculate_all_fuel_requirements(mass) == fuel
