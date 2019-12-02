from itertools import combinations
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

    @property
    def final_state(self) -> List[int]:
        """Use this function for providing the final state property for this instance.

        This function is used for generating and returning the final state attribute
        for the IntCode class instance.

        :return: the final state.
        """
        return self.__generate_final_state(initial_state=self.initial_state)

    def __generate_final_state(self, initial_state: List[int]) -> List[int]:
        """Use this function for generating the final state for a given input.

        This function is used for generating the final state for the given initial
        state.

        :return: the final state.
        """
        final_state = initial_state
        for instruction_pointer in range(0, len(initial_state), 4):
            opcode = initial_state[instruction_pointer]
            if opcode == 1 or opcode == 2:
                first_param = initial_state[initial_state[instruction_pointer + 1]]
                second_param = initial_state[initial_state[instruction_pointer + 2]]
                third_parameter = initial_state[instruction_pointer + 3]
                if opcode == 1:
                    final_state[third_parameter] = first_param + second_param
                else:
                    final_state[third_parameter] = first_param * second_param
            elif opcode == 99:
                return final_state
            else:
                raise ValueError(f"Incorrect opcode '{opcode}'!!")
        return final_state

    def calculate_verb_and_noun(self, output: int) -> int:
        for noun, verb in combinations(range(100), 2):
            updated_initial_state = self.initial_state
            updated_initial_state[1] = noun
            updated_initial_state[2] = verb
            try:
                new_final_state = self.__generate_final_state(
                    initial_state=updated_initial_state
                )
            except ValueError:
                pass
            else:
                if new_final_state == output:
                    return 100 * noun + verb

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
