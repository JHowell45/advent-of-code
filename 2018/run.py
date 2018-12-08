from src.day_1.puzzle_1 import calculate_frequence
from src.day_1.puzzle_2 import find_repeat_frequency
from src.day_6.puzzle_1 import get_largest_distance
from src.shared_functions import banner, generate_file_data


@banner("Day 1, Puzzle 1")
def run_day_1_puzzle_1():
    data = generate_file_data("./src/day_1/puzzle_data.txt")
    print(f"Final Frequency: {calculate_frequence(data)}")


@banner("Day 1, Puzzle 2")
def run_day_1_puzzle_2():
    data = list(generate_file_data("./src/day_1/puzzle_data.txt"))
    print(f"First Frequency reached twice: {find_repeat_frequency(data)}")


@banner("Day 6, Puzzle 1")
def run_day_6_puzzle_1():
    data = generate_file_data("./src/day_6/puzzle_data.txt")
    print(f"Largest Area: {get_largest_distance(data)}")


def main():
    run_day_1_puzzle_1()
    run_day_1_puzzle_2()
    run_day_6_puzzle_1()


if __name__ == "__main__":
    main()
