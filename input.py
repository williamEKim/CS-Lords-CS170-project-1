from typing import List


def print_int_array(arr: List[int]) -> None:
    """Print non -1 values in a list."""
    print(" ".join(str(x) for x in arr if x != -1), end=" ")

def print_vector_puzzle(puzzle: List[List[int]]) -> None:
    """Print the puzzle in grid form with formatted spacing."""
    n = len(puzzle)
    max_num = n * n - 1
    width = len(str(max_num)) + 1  # +1 for padding
    for row in puzzle:
        print("".join(f"{val:>{width}}" for val in row))
    print()

def check_val(unused_nums: List[int], val: int) -> bool:
    """Return True if val is available and mark it as used (-1)."""
    for i in range(len(unused_nums)):
        if unused_nums[i] == val:
            unused_nums[i] = -1
            return True
    return False

def main():
    print("Taking input for n x n puzzle.\n")
    n = int(input("\tFirst, please enter the size of n: "))

    print(f"\nTaking input for {n} x {n} puzzle.")

    size = n * n
    unused_nums = [i for i in range(size)]
    print("\nUnused Numbers: { ", end="")
    print_int_array(unused_nums)
    print("}")

    puzzle = [[0 for _ in range(n)] for _ in range(n)]
    count = 0

    print("\nNow, please enter:")

    for row in range(n):
        for col in range(n):
            print("Available options: ", end="")
            print_int_array(unused_nums)
            print()

            while True:
                try:
                    val = int(input(f"\trow: [{row + 1}], column: [{col + 1}] : "))
                    if check_val(unused_nums, val):
                        break
                    else:
                        print(f"{{ {val} }} already exists or is not valid option\n\tTry again: ", end="")
                except ValueError:
                    print("\tInvalid input, please enter an integer.")

            puzzle[row][col] = val
            print()
            print_vector_puzzle(puzzle)

    print("\nResult:")
    print_vector_puzzle(puzzle)

# in case this is imported in other python file
if __name__ == "__main__":
    main()
