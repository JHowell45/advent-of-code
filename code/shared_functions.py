"""Use the functions in this file in all of the other src files.

This file contains the functions that will be used across all of the challenges and
for every year.
"""
from os.path import abspath


def generate_file_data(file_path: str):
    """Use this function to return the data a line at a time.

    This function is used for returning the data from the text file one line at
    a time, the data is being returned as generator.

    :param file_path: the path to the data file to use.
    """
    with open(abspath(file_path), "r") as f:
        for line in f:
            yield line


def banner(puzzle_title: str):
    """Use this function as a banner decorator for wrapping the puzzle answers.

    This function is used for decorating the functions for running the puzzle
    functions to help separate out the results and display the information.

    :param puzzle_title: the title for the banner.
    :return: the results of the wrapped function.
    """
    title_length = len(puzzle_title)
    banner_length = 30

    def dec(function):
        def func(*args, **kwargs):
            print("\n|{1}| {0} |{1}|\n".format(puzzle_title, "-" * banner_length))
            result = function(*args, **kwargs)
            print("\n|{}|\n".format("-" * ((banner_length * 2) + title_length + 4)))
            return result

        return func

    return dec
