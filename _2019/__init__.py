try:
    from _2019.src.day_1 import (
        day_1_puzzle_1_solution,
        day_1_puzzle_2_solution,
    )
except ImportError:
    from src.day_1 import (
        day_1_puzzle_1_solution,
        day_1_puzzle_2_solution,
    )
try:
    from _2019.src.day_2 import day_2_puzzle_1_solution
except ImportError:
    from src.day_2 import day_2_puzzle_1_solution


def main():
    print(f"Day 1, Puzzle 1: {day_1_puzzle_1_solution()}")
    print(f"Day 1, Puzzle 2: {day_1_puzzle_2_solution()}")
    print(f"Day 2, Puzzle 1: {day_2_puzzle_1_solution()}")


if __name__ == "__main__":
    main()
