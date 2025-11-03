from typing import List
from helpers.input import PuzzleInput
from helpers.misplacedH import getMisplacedHuristic
from helpers.euclideanH import getEuclideanHuristic 
from search_Algo.uniformCS import uniform_cost_search
from search_Algo.Astar import a_star_search

def grid_print(grid: List[List[int]]) -> str:
    return "\n".join(" ".join(f"{x:2d}" for x in row) for row in grid)

builder = PuzzleInput()
builder.take_input()
start_state = builder.get_puzzle()
goal = builder.get_goal()

# print("Misplaced huristics " + str(getMisplacedHuristic(builder.get_puzzle(), builder.get_goal(), builder.get_n())))
# euclidean_dist = getEuclideanHuristic(builder.get_puzzle(), builder.get_goal(), builder.get_n())
# euclidean_dist = round(euclidean_dist, 3)
# print("Euclidean Huristic(rounded): " + str(euclidean_dist))

while True:
    try:
        search_choice = int(input("\nEnter your choice of algorithm:\n\t1. Uniform Cost Search\n\t2. A* with the Misplaced Tile heuristic\n\t3. A* with the Euclidean distance heuristic\n\n--> "))
        if search_choice is 1 or search_choice is 2 or search_choice is 3:
            break
        print("Please choose between option [1, 2, 3]\n")
        continue
    except ValueError:
        print(f"It is not an appropriate value. \nPlease choose between option [1, 2, 3]\n")


if search_choice is 1:
    result = uniform_cost_search(start_state, goal)
elif search_choice is 2:
    result = a_star_search(start_state, goal, "misplaced")
else:
    result = a_star_search(start_state, goal, "euclidean")


if result["solved"]:
    print("\n=== Uniform Cost Search Solution ===")
    print(f"Cost (moves): {result['cost']}")
    print(f"Goal depth:   {result['goal_depth']}")
    print(f"Nodes expanded: {result['nodes_expanded']}")
    print(f"Max queue size: {result['max_queue_size']}")
    print("\nMoves:", " -> ".join(result["moves"]) or "(none)")
    print("\nPath:")
    for i, grid in enumerate(result["path"]):
        print(f"\nStep {i}:")
        print(grid_print(grid))
else:
    print("No solution found.")