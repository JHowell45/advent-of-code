"""Use this file to include shared function for the day 1 puzzles."""
from os.path import abspath, realpath
from typing import Generator


def calculate_fuel(mass: int) -> int:
    """Use this function for calculating the fuel requirements for a module.

    This function is used for calculating the fuel requirements for a module based on
    its mass.

    :param mass: the mass of the module.
    :return: the calculated fuel.
    """
    return int(mass / 3) - 2


def get_puzzle_input() -> Generator[int, None, None]:
    """Use this function to get the puzzle data input in the correct format.

    This function is used for iterating over the puzzle data file and returning the
    values in the correct format.

    :yield: correctly formatted row of file.
    """
    with open(f"{abspath(f'{realpath(__file__)}/../puzzle_data.txt')}") as f:
        for line in f:
            yield int(line)
