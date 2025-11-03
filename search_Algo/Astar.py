from typing import List, Tuple, Dict, Optional
import heapq

Grid = List[List[int]]
State = Tuple[int, ...]  #flattens grid

def flatten(grid: Grid) -> State:
    return tuple(x for row in grid for x in row)


def unflatten(state: State, n: int) -> Grid:
    return [list(state[i * n:(i + 1) * n]) for i in range(n)]


def find_blank(state: State) -> int:
    return state.index(0)


def neighbors(state: State, n: int) -> List[tuple[str, State]]:
    """Return list of (move, next_state) from this state."""
    idx = find_blank(state)
    row, col = divmod(idx, n)
    res: List[tuple[str, State]] = []

    def swap(i: int, j: int) -> State:
        curr_state = list(state)
        curr_state[i], curr_state[j] = curr_state[j], curr_state[i]
        return tuple(curr_state)

    #up so swap with tile aboce
    if row > 0:
        res.append(("Up", swap(idx, idx - n)))
    #down
    if row < n - 1:
        res.append(("Down", swap(idx, idx + n)))
    #Left
    if col > 0:
        res.append(("Left", swap(idx, idx - 1)))
    #Right
    if col < n - 1:
        res.append(("Right", swap(idx, idx + 1)))
    return res

def A_star_search(start_state_grid: Grid, goal_grid: Grid) -> Dict[str, object]:
    return ["", []]