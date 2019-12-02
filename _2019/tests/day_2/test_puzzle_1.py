"""Use this file for testing the functions for day 2 puzzle 1."""
import pytest

from _2019.src.day_2.puzzle_1 import IntCode


@pytest.mark.parametrize(
    "initial_state,final_state",
    [
        ("1,0,0,0,99", "2,0,0,0,99"),
        ("2,3,0,3,99", "2,3,0,6,99"),
        ("2,4,4,5,99,0", "2,4,4,5,99,9801"),
        ("1,1,1,4,99,5,6,0,99", "30,1,1,4,2,5,6,0,99"),
    ],
)
def test_calculate_fuel(initial_state: str, final_state: str):
    assert ",".join([str(x) for x in IntCode(initial_state).final_state]) == final_state
