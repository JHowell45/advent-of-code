"""Functions used for solving the second puzzle for day 1."""


def find_repeat_frequency(freq: list, limit: int = 10000, verbose: bool = False) -> int:
    """Use this function to return a repeated frequency.

    This function is used for returning the repeated frequency value from the list of
    frequencies.

    :param freq: the list of frequency changes to make.
    :param limit: the max number of rounds to execute.
    :param verbose: whether to display additional info.
    :return: the repeated frequency.
    """
    result_freq = 0
    frequencies_appeared = {result_freq}
    rounds = 0

    while rounds < limit:
        if verbose:
            print(f"Current round : {rounds}")
        for freq in freq:
            result_freq += int(freq)
            if result_freq in frequencies_appeared:
                return result_freq
            else:
                frequencies_appeared.add(result_freq)
        else:
            rounds += 1
