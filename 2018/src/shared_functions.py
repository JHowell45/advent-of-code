"""Use the functions in this file in all of the other code files.

This file contains the functions that will be used across all of the challenges
and code.
"""
from os.path import abspath


def generate_file_data(filepath):
    """Use this function to return the data a line at a time.

    This function is used for returning the data from the text file one line at
    a time, the data is being returned as geenrator.

    :param filepath: the path to the data file to use.
    :type filepath: str
    """
    with open(abspath(filepath), "r") as f:
        for line in f:
            yield line


def banner(puzzle_title):
    """Use this function as a banner decorator for wrapping the puzzle answers.

    This function is used for decorating the functions for running the puzzle
    functions to help separate out the results and display the information.

    :param puzzle_title: the title for the banner.
    :type puzzle_title: str
    :return: the results of the wrapped function.
    :rtype:
    """
    title_length = len(puzzle_title)
    banner_length = 30

    def dec(function):
        """Use this function to add as a decorator for wrapping the function.

        This function is used for adding a wrapping function to the decorated
        function.

        :param function: the function to wrap.
        :type function:
        :return: the results of the wrapped function.
        :rtype:
        """

        def func(*args, **kwargs):
            """Use this function to add a banner to the wrapped function.

            This function is used for wrapping the wrapped function in
            additional functionality.

            :return: the results of the wrapped function.
            :rtype:
            """
            print(
                "\n|{1}| {0} |{1}|\n".format(puzzle_title, "-" * banner_length)
            )
            result = function(*args, **kwargs)
            print(
                "\n|{}|\n".format(
                    "-" * ((banner_length * 2) + title_length + 4)
                )
            )
            return result

        return func

    return dec
