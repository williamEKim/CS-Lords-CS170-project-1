from typing import List
from helpers.input import PuzzleInput
from helpers.misplacedH import getMisplacedHuristic
from helpers.euclideanH import getEuclideanHuristic

builder = PuzzleInput()
builder.take_input()
print("Misplaced huristics " + str(getMisplacedHuristic(builder.get_puzzle(), builder.get_goal(), builder.get_n())))
euclidean_dist = getEuclideanHuristic(builder.get_puzzle(), builder.get_goal(), builder.get_n())
euclidean_dist = round(euclidean_dist, 3)
print("Euclidean Huristic(rounded): " + str(euclidean_dist))