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

# repeat until user quits
is_path_hidden: bool = False
while True:
    # Flag to turn off path display
    try:
        search_choice = int(input(f"\nEnter your choice of algorithm:\n\t1. Uniform Cost Search\n\t2. A* with the Misplaced Tile heuristic\n\t3. A* with the Euclidean distance heuristic\n\t4. Turn off path display (currently: {is_path_hidden})\n\t5. Quit\n\n--> "))
        if not(search_choice == 1 or search_choice == 2 or search_choice == 3 or search_choice == 4 or search_choice == 5):
            print("Please choose between option [1, 2, 3, 4]\n")
            continue

    except ValueError:
        print(f"It is not an appropriate value. \nPlease choose between option [1, 2, 3]\n")

    search: str = ""
    if search_choice == 5:
        break
    elif search_choice == 4:
        try:
            is_path_hidden = bool(1 - is_path_hidden)
        except:
            print("ERR")
        print("Path Display Option Toggled")
        continue
    elif search_choice == 1:
        result = uniform_cost_search(start_state, goal)
        search = "Uniform Cost Search"
    elif search_choice == 2:
        result = a_star_search(start_state, goal, "misplaced")
        search = "A Star Search with Misplaced Tile Huristic"
    else:
        result = a_star_search(start_state, goal, "euclidean")
        search = "A Star Search with Euclidean Huristic"


    try:
        if result["solved"]:
            if search_choice == 1 and not is_path_hidden:  # UCS
                for i, grid in enumerate(result["path"]):
                    print(f"\nStep {i}, with g(n) = {i}:")
                    print(grid_print(grid))

            elif not is_path_hidden:  # A* (misplaced or Euclidean)
                g_val = 0
                h_val = 0
                for i, (grid, h_value) in enumerate(zip(result["path"], result["h_values"])):
                    print(f"\nStep {i}, with g(n) = {i} and h(n) = {h_value}:")
                    print(grid_print(grid))

                
            print(f"\n=== {search} Solution ===")
            print(f"Cost (moves): {result['cost']}")
            print(f"Goal depth:   {result['goal_depth']}")
            print(f"Nodes expanded: {result['nodes_expanded']}")
            print(f"Max queue size: {result['max_queue_size']}")
            print("\nMoves:", " -> ".join(result["moves"]) or "(none)")

        else:
            print("No solution found.")

    except TypeError:
        print(f"Type Error Occured: {result}")