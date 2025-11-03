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

    #up so swap with tile above
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


def uniform_cost_search(start_state_grid: Grid, goal_grid: Grid) -> Dict[str, object]:
    """Run UCS and return trace plus solution path."""
    n = len(start_state_grid)
    start_state: State = flatten(start_state_grid)
    goal_state: State = flatten(goal_grid)

    #prio_queue
    prio_queue: list[tuple[int, int, State]] = []
    counter = 0
    heapq.heappush(prio_queue, (0, counter, start_state))

    #best known cost to a state
    g_cost: Dict[State, int] = {start_state: 0}

    #Parent pointers to reconstruct path: state -> (parent_state, move)
    parent: Dict[State, tuple[Optional[State], Optional[str]]] = {
        start_state: (None, None)
    }

    nodes_expanded = 0
    max_queue_size = 1

    while prio_queue:
        max_queue_size = max(max_queue_size, len(prio_queue))
        g, _, s = heapq.heappop(prio_queue)

        #If this popped cost isn't the best anymore
        if g != g_cost.get(s, float("inf")):
            continue

        if s == goal_state:
            #reconstruct path
            moves: List[str] = []
            states: List[State] = []
            cur = s
            while cur is not None:
                states.append(cur)
                p, mv = parent[cur]
                if mv is not None:
                    moves.append(mv)
                cur = p
            states.reverse()
            moves.reverse()
            path_grids = [unflatten(st, n) for st in states]
            return {
                "path": path_grids,
                "moves": moves,
                "cost": g,
                "nodes_expanded": nodes_expanded,
                "max_queue_size": max_queue_size,
                "goal_depth": g,
                "solved": True,
            }
        #keep track of # of nodes expanded
        nodes_expanded += 1
        for move, next_state in neighbors(s, n):
            new_g = g + 1  #costs 1 per move
            if new_g < g_cost.get(next_state, float("inf")):
                g_cost[next_state] = new_g
                parent[next_state] = (s, move)
                counter += 1
                heapq.heappush(prio_queue, (new_g, counter, next_state))

    #no solution 
    return {
        "path": [],
        "moves": [],
        "cost": None,
        "nodes_expanded": nodes_expanded,
        "max_queue_size": max_queue_size,
        "goal_depth": None,
        "solved": False,
    }
