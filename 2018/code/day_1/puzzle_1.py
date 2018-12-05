"""Functions used for solving the first puzzle for day 1."""


def calculate_frequence(freq_changes):
    """Use this function to calculate the frequency given a list of values.

    This function takes a list of frequences and processes the values before
    returning the final frequency.

    :param freq_changes: the lsit of frequency changes to be based.
    :type freq_changes: list
    :return: the sum of all of the frequencies
    :rtype: int
    """
    return sum([int(freq) for freq in freq_changes])
