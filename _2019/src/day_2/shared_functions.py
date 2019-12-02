"""Use this file to include shared function for the day 1 puzzles."""
from os.path import abspath, realpath
from typing import List, Union


class IntCode:
    """Use this class for creating the IntCode for performing the state computations.

    This class is used for creating an IntCode computer for calculating the final
    states for a given input state.
    """

    def __init__(self, initial_state: Union[List[int], str]) -> None:
        if isinstance(initial_state, str):
            self.initial_state = [int(opcode) for opcode in initial_state.split(",")]
        else:
            self.initial_state = initial_state
        self.__final_state = None

    @classmethod
    def from_file(cls):
        return cls(initial_state=get_puzzle_input())

    @property
    def final_state(self) -> List[int]:
        """Use this function for providing the final state property for this instance.

        This function is used for generating and returning the final state attribute
        for the IntCode class instance.

        :return: the final state.
        """
        final_state = self.initial_state
        for instruction_pointer in range(0, len(self.initial_state), 4):
            opcode = self.initial_state[instruction_pointer]
            if opcode == 1 or opcode == 2:
                first_parameter = self.initial_state[
                    self.initial_state[instruction_pointer + 1]
                ]
                second_parameter = self.initial_state[
                    self.initial_state[instruction_pointer + 2]
                ]
                third_parameter = self.initial_state[instruction_pointer + 3]
                if opcode == 1:
                    final_state[third_parameter] = first_parameter + second_parameter
                else:
                    final_state[third_parameter] = first_parameter * second_parameter
            elif opcode == 99:
                return final_state
            else:
                raise ValueError(f"Incorrect opcode '{opcode}'!!")
        return final_state

    def __repr__(self):
        """Use this function for generating a representation for the class instance.

        This function is used for generating the string representation for the
        current IntCode class instance.

        :return: the string representation for the class instance.
        """
        return (
            f"<{self.__class__.__name__} Initial State: {self.initial_state}, "
            f"Final State: {self.final_state}>"
        )


def get_puzzle_input() -> str:
    """Use this function to get the puzzle data input in the correct format.

    This function is used for iterating over the puzzle data file and returning the
    values in the correct format.

    :yield: correctly formatted row of file.
    """
    with open(f"{abspath(f'{realpath(__file__)}/../puzzle_data.txt')}") as file:
        return file.read().replace("\n", "")
