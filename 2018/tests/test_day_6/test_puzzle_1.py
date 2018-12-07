"""Use this file to test the functions in day 6 puzzle 1."""
from src.day_6.puzzle_1 import get_largest_distance


def test_puzzle_1():
    """Use this function to test the function used for calculating the puzzle.

    This function is used for testing the function used for calculating the
    first puzzle.
    """
    test_data = ["1, 1" "1, 6" "8, 3" "3, 4" "5, 5" "8, 9"]
    assert get_largest_distance(test_data) == 17
