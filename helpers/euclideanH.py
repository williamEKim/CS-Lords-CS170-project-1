# function that takes 2 2D arrays and reuturn Euclidean Huristic
# d = sqrt( (x2 - x1)^2 + (y2 - y1)^2 )

from typing import List
import math

def getEuclideanHuristic(curr: List[List[int]], goal: List[List[int]], n: int) -> float:
    """param: [List[List[int]], List[List[int]], int]; return: float"""
    huristicCount = 0.0

    # define 2D coordinate List that each row represent the value we are looking for and 4 columns on each row as a 2D coordinate [curr(0, 1) recorded as 0, 1] of value in each Lists
    coordinates = List[List[int]]
    coordinates = [[0 for _ in range(4)] for _ in range(pow(n, 2))]

    for i in range(pow(n, 2)):
        for row in range(n):
            for col in range(n):
                if curr[row][col] == i:
                    coordinates[i][0] = row
                    coordinates[i][1] = col
                if goal[row][col] == i:
                    coordinates[i][2] = row
                    coordinates[i][3] = col

    # we don't want to put 0 in huristic (ignore)
    for i in range(1, pow(n, 2)):
        x_dist = coordinates[i][2] - coordinates[i][0]
        y_dist = coordinates[i][3] - coordinates[i][1]
        huristicCount += math.sqrt( pow(x_dist, 2) + pow(y_dist, 2) )
        # print("huristic for " + str(i) + " is between ( " + str(coordinates[i][0]) + ", " + str(coordinates[i][1]) + " ), ( " + str(coordinates[i][2]) + ", " + str(coordinates[i][3]) + " )")

    return huristicCount