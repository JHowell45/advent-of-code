from day_1.puzzle_1 import calculate_frequence
from shared_functions import banner, generate_file_data


@banner("Day 1, Puzzle 1")
def run_puzzle_1():
    data = generate_file_data("./code/day_1/puzzle_data.txt")
    print(f"Final Frequency: {calculate_frequence(data)}")


run_puzzle_1()
