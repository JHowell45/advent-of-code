"""Functions used for solving the first puzzle for day 1."""


def calculate_frequency(freq_changes: list) -> int:
    """Use this function to calculate the frequency given a list of values.

    This function takes a list of frequencies and processes the values before
    returning the final frequency.

    :param freq_changes: the list of frequency changes to be based.
    :return: the sum of all of the frequencies
    """
    return sum([int(freq) for freq in freq_changes])
