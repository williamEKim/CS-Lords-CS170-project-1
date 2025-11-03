from helpers.misplacedH import getMisplacedHuristic
from helpers.euclideanH import getEuclideanHuristic 
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


def a_star_search(start_state_grid: Grid, goal_grid: Grid, heuristic) -> Dict[str, object]:
    n = len(start_state_grid)
    start_state = flatten(start_state_grid)
    goal_state = flatten(goal_grid)

    # depending on choice of huristic, set the huristic algorithm (by default misplaced tile)
    def h(state: State) -> float:
        grid = unflatten(state, n)
        if heuristic == "euclidean":
            return getEuclideanHuristic(grid, goal_grid, n)
        else:
            return getMisplacedHuristic(grid, goal_grid, n)

    prio_queue = []
    heapq.heappush(prio_queue, (h(start_state), 0, start_state))

    g_cost: Dict[State, int] = {start_state: 0}
    h_cost: Dict[State, float] = {start_state: h(start_state)}

    parent = {start_state: (None, None)}

    nodes_expanded = 0
    max_queue_size = 1


    while prio_queue:
        max_queue_size = max(max_queue_size, len(prio_queue))
        _, g, s = heapq.heappop(prio_queue) # not using f
        if s == goal_state:
            #reconstruct path
            moves: List[str] = []
            states: List[State] = []
            h_values: List[float] = []  # list of (g, h)

            cur = s
            while cur is not None:
                states.append(cur)
                # Append g and h for this state
                h_values.append(h_cost.get(cur, 0.0))

                p, mv = parent[cur]
                if mv is not None:
                    moves.append(mv)
                cur = p
            
            # reverse to match the order of path
            states.reverse()
            moves.reverse()
            h_values.reverse()
            path_grids = [unflatten(st, n) for st in states]

            return {
                "path": path_grids,
                "moves": moves,
                "cost": g,
                "h_values": h_values,
                "nodes_expanded": nodes_expanded,
                "max_queue_size": max_queue_size,
                "goal_depth": g,
                "solved": True,
            }

        #keep track of # of nodes expanded
        nodes_expanded += 1
        for move, next_state in neighbors(s, n):
            new_g = g + 1
            new_h = h(next_state) # now, we are using new huristic for A star instead of counter
            if new_g < g_cost.get(next_state, float("inf")):
                g_cost[next_state] = new_g
                h_cost[next_state] = new_h
                parent[next_state] = (s, move)
                new_f = new_g + new_h 
                heapq.heappush(prio_queue, (new_f, new_g, next_state))


    # if there is no solution
    return {
            "path": [],
            "moves": [],
            "h_values": [],
            "cost": 0,
            "nodes_expanded": nodes_expanded,
            "max_queue_size": max_queue_size,
            "goal_depth": g,
            "solved": False,
    }