import time
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
        print("\nEnter your choice of algorithm:")
        print("\t1. Uniform Cost Search")
        print("\t2. A* with the Misplaced Tile heuristic")
        print("\t3. A* with the Euclidean distance heuristic")
        print(f"\t4. Turn off path display (currently: {is_path_hidden})")
        print("\t5. Reset the Puzzle")
        print("\t6. Quit")
        search_choice = int(input(f"\n--> "))
        if search_choice not in [1, 2, 3, 4, 5, 6]:
            print("Please choose between option [1, 2, 3, 4, 5, 6]\n")
            continue

    except ValueError:
        print(f"It is not an appropriate value. \nPlease choose between option [1, 2, 3, 4, 5, 6]\n")
        continue

    search: str = ""
    if search_choice == 6:      # QUIT
        break
    elif search_choice == 5:    # RESET PUZZLE
        builder.take_input()
        start_state = builder.get_puzzle()
        goal = builder.get_goal()
        continue    # result the loop with new puzzle
    elif search_choice == 4:    # TOGGLE DISPLAY
        try:
            is_path_hidden = bool(1 - is_path_hidden)
        except:
            print("ERR")
        print("Path Display Option Toggled")
        continue
    elif search_choice == 1:    # UCS
        start_time = time.time()  # Record start time
        result = uniform_cost_search(start_state, goal)
        end_time = time.time()    # Record end time
        search = "Uniform Cost Search"
    elif search_choice == 2:    # A* with misplaced huristic
        start_time = time.time()  # Record start time
        result = a_star_search(start_state, goal, "misplaced")
        end_time = time.time()    # Record end time
        search = "A Star Search with Misplaced Tile Huristic"
    else:                       # A* with euclidean huristic
        start_time = time.time()  # Record start time
        result = a_star_search(start_state, goal, "euclidean")
        end_time = time.time()    # Record end time
        search = "A Star Search with Euclidean Huristic"

    # Calculate elapsed time
    elapsed_time = end_time - start_time

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
            print(f"Time: {elapsed_time:.4f} seconds")
            print("\nMoves:", " -> ".join(result["moves"]) or "(none)")

        else:
            print("No solution found.")
            print(f"Nodes expanded: {result['nodes_expanded']}")
            print(f"Max queue size: {result['max_queue_size']}")
            print(f"Time: {elapsed_time:.4f} seconds")
        
        

    except TypeError:
        print(f"Type Error Occured: {result}")
    except ValueError:
        print(f"It is not an appropriate value. \nPlease choose between option [1, 2, 3, 4, 5, 6]\n")
        continue