"""Use this functions to complete the day 5 puzzle 1 challenge."""
from pprint import pprint

from src.day_6.shared_functions import Manhatten


def get_largest_distance(data):
    man = Manhatten(data)
    print(repr(man))
    # pprint(man.graph)
    print()
    man.set_closest_points()
    # pprint(man.graph)
    print()
    return man.get_largest_distance()
