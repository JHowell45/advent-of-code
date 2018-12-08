"""Use this file for creating fixtures for the puzzles for day 6.

This file contains the test fixtures for the classes and functions for the
shared puzzles day six.
"""
import pytest

from src.day_6.shared_functions import ParsePoints


@pytest.fixture(params=["242, 164", "82, 142"])
def parse_points_class(request):
    return ParsePoints(request.param)
