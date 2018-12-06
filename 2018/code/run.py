from day_1.puzzle_1 import calculate_frequence
from day_1.puzzle_2 import find_repeat_frequency
from shared_functions import banner, generate_file_data


@banner("Day 1, Puzzle 1")
def run_day_1_puzzle_1():
    data = generate_file_data("./code/day_1/puzzle_data.txt")
    print(f"Final Frequency: {calculate_frequence(data)}")


@banner("Day 1, Puzzle 2")
def run_day_1_puzzle_2():
    data = list(generate_file_data("./code/day_1/puzzle_data.txt"))
    print(f"Final Frequency: {find_repeat_frequency(data)}")


def main():
    run_day_1_puzzle_1()
    run_day_1_puzzle_2()


if __name__ == "__main__":
    main()
