from typing import List
from misplacedH import getMisplacedHuristic


class PuzzleInput:
    """Handles user input and construction of an n x n puzzle grid. """

    def __init__(self):
        self.n = 0
        self.puzzle: List[List[int]] = []
        self.unused_nums: List[int] = []
        self.goal_state: List[List[int]] = []

    def print_int_list(self) -> None:
        """Print available numbers (non -1)."""
        print(" ".join(str(x) for x in self.unused_nums if x != -1), end=" ")

    def print_puzzle(self) -> None:
        """Display puzzle as a formatted grid."""
        if not self.puzzle:
            print("(empty puzzle)")
            return

        max_num = self.n * self.n - 1
        width = len(str(max_num)) + 1  # For alignment

        for row in self.puzzle:
            print("".join(f"{val:>{width}}" for val in row))
        print()

    def print_goal_state(self) -> None:
        """Display goal state."""
        if not self.goal_state:
            print("(goal state not defined)")
            return

        max_num = self.n * self.n - 1
        width = len(str(max_num)) + 1  # For alignment

        for row in self.goal_state:
            print("".join(f"{val:>{width}}" for val in row))
        print()

    def check_val(self, val: int) -> bool:
        """Check if value is unused; mark as used (-1) if valid."""
        for i in range(len(self.unused_nums)):
            if self.unused_nums[i] == val:
                self.unused_nums[i] = -1
                return True
        return False

    def take_input(self) -> None:
        """Prompt user to enter puzzle size and fill it interactively."""
        print("Taking input for n x n puzzle.\n")
        self.n = int(input("\tFirst, please enter the size of n: "))

        print(f"\nTaking input for {self.n} x {self.n} puzzle.")
        size = self.n * self.n

        # define goal state according to n
        self.goal_state = [[0 for _ in range(self.n)] for _ in range(self.n)]
        count = 1
        for row in range(self.n):
            for col in range(self.n):
                self.goal_state[row][col] = count
                count += 1
        self.goal_state[self.n - 1][self.n - 1] = 0

        self.unused_nums = [i for i in range(size)]
        print("\nUnused Numbers: { ", end="")
        self.print_int_list()
        print("}")

        # initialize puzzle with zeros
        self.puzzle = [[0 for _ in range(self.n)] for _ in range(self.n)]

        print("\nNow, please enter:")

        for row in range(self.n):
            for col in range(self.n):
                print("Available options: ", end="")
                self.print_int_list()
                print()

                while True:
                    try:
                        val = int(input(f"\trow: [{row + 1}], column: [{col + 1}] : "))
                        if self.check_val(val):
                            break
                        else:
                            print(f"{{ {val} }} already exists or is not a valid option.\n\tTry again: ", end="")
                    except ValueError:
                        print("\tInvalid input, please enter an integer.")

                self.puzzle[row][col] = val
                print()
                self.print_puzzle()

        print("\nResult:")
        self.print_puzzle()

        print("\nGoal:")
        self.print_goal_state()
        
    def get_n(self) -> int:
        """Return n value of the puzzle."""
        return self.n

    def get_puzzle(self) -> List[List[int]]:
        """Return the 2D puzzle list."""
        return self.puzzle

    def get_goal(self) -> List[List[int]]:
        """Return the 2D goal_state list."""
        return self.goal_state


# in case this is imported in other python file
if __name__ == "__main__":
    builder = PuzzleInput()
    builder.take_input()
    print("misplaced huristics " + str(getMisplacedHuristic(builder.get_puzzle(), builder.get_goal(), builder.get_n())))
