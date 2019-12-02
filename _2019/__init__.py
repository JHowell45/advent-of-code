try:
    from _2019.src.day_1 import (
        calculate_total_fuel_requirement,
        calculate_total_fuel_for_mass_and_fuel,
    )
except ImportError:
    from src.day_1 import (
        calculate_total_fuel_requirement,
        calculate_total_fuel_for_mass_and_fuel,
    )
try:
    from _2019.src.day_2 import IntCode, day_2_puzzle_1_solution
except ImportError:
    from src.day_2 import IntCode, day_2_puzzle_1_solution


def main():
    print(f"Day 1, Puzzle 1: {calculate_total_fuel_requirement()}")
    print(f"Day 1, Puzzle 2: {calculate_total_fuel_for_mass_and_fuel()}")
    print(f"Day 2, Puzzle 1: {day_2_puzzle_1_solution()}")


if __name__ == "__main__":
    main()
