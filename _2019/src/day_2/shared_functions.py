"""Use this file to include shared function for the day 1 puzzles."""
from os.path import abspath, realpath


def get_puzzle_input() -> str:
    """Use this function to get the puzzle data input in the correct format.

    This function is used for iterating over the puzzle data file and returning the
    values in the correct format.

    :yield: correctly formatted row of file.
    """
    with open(f"{abspath(f'{realpath(__file__)}/../puzzle_data.txt')}") as file:
        return file.read().replace("\n", "")
