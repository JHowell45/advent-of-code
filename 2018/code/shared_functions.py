"""Use the functions in this file in all of the other code files.

This file contains the functions that will be used across all of the challenges
and code.
"""
from os.path import abspath


def generate_file_data(filepath):
    with open(abspath(filepath), "r") as f:
        for line in f:
            yield line


def banner(puzzle_title):
    title_length = len(puzzle_title)
    banner_length = 30

    def dec(function):
        def func(*args, **kwargs):
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
