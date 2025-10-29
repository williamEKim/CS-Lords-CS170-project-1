from typing import List


class PuzzleInput:
    """Handles user input and construction of an n x n puzzle grid. """

    def __init__(self):
        self.n = 0
        self.puzzle: List[List[int]] = []
        self.unused_nums: List[int] = []

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

    def get_puzzle(self) -> List[List[int]]:
        """Return the 2D puzzle array."""
        return self.puzzle


# in case this is imported in other python file
if __name__ == "__main__":
    builder = PuzzleInput()
    builder.take_input()
