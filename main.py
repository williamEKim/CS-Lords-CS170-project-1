from typing import List
from input_output.PuzzleInput import PuzzleInput
from classes.Actions import EightPuzzleActions
from helpers.misplacedH import getMisplacedHuristic
from helpers.euclideanH import getEuclideanHuristic
from algorithms.ucs import uniformCostSearch 

builder = PuzzleInput()
builder.take_input()
goal = ((1,2,3),
        (4,5,6),
        (7,8,0))

state = ((1,2,3),
         (4,5,6),
         (7,0,8))  # blank swapped with 8 => distance > 0

# print("Misplaced huristics " + str(getMisplacedHuristic(state, state, builder.get_n())))
# euclidean_dist = getEuclideanHuristic(state, goal, builder.get_n())
# euclidean_dist = round(euclidean_dist, 3)
# print("Euclidean Huristic(rounded): " + str(euclidean_dist))

print("Misplaced huristics " + str(getMisplacedHuristic(builder.get_puzzle(), builder.get_goal(), builder.get_n())))
euclidean_dist = getEuclideanHuristic(builder.get_puzzle(), builder.get_goal(), builder.get_n())
euclidean_dist = round(euclidean_dist, 3)
print("Euclidean Huristic(rounded): " + str(euclidean_dist))
domain = EightPuzzleActions(builder.get_puzzle(), builder.get_goal(), builder.get_n())
goalNode, num_nodes_expanded, max_queue = uniformCostSearch(domain)
print("Goal Node: ", goalNode.state)
print("Path cost to goal: ", goalNode.g)
print("Number of nodes expanded: ", num_nodes_expanded)
print("Max queue size: ", max_queue) 