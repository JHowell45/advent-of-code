"""Use this file for creating fixtures for the puzzles for day 6.

This file contains the test fixtures for the classes and functions for the
shared puzzles day six.
"""
import pytest

from src.day_6.shared_functions import ParsePoints


@pytest.fixture
def x_parse_point_value():
    return 242


@pytest.fixture
def y_parse_point_value():
    return 164


@pytest.fixture
def parse_point_string(x_parse_point_value, y_parse_point_value):
    return f"{x_parse_point_value}, {y_parse_point_value}"


@pytest.fixture()
def parse_points_class(parse_point_string):
    return ParsePoints(parse_point_string)
