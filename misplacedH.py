# function takes in 2D lists(present and goal) of int and detacts misplaced huristics
from typing import List

def getMisplacedHuristic(curr: List[List[int]], goal: List[List[int]], n: int) -> int:
    """param: [ curr: List[List[int]], goal: List[List[int]], n: int ]; output: huristicCount:int"""
    huristicCount = 0

    for row in range(n):
        for col in range(n):
            # if puzzle's column is not 0 (ignored) and does not matches the goal state column
            if curr[row][col] != 0 and curr[row][col] != goal[row][col]:
                huristicCount += 1

    return huristicCount