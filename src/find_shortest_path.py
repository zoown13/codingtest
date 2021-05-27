#!/bin/python3

from collections import deque


#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#


def minimumMoves(grid, startX, startY, goalX, goalY):
    # Write your code here
    q = deque()
    q.append((startX, startY, 0, -1))
    visited = {(startX, startY): 0}
    x, y = [-1, 0, 0, 1], [0, 1, -1, 0]

    def is_valid(x, y, new_dist):
        return len(grid) > x >= 0 and len(grid) > y >= 0 and grid[x][y] == '.' and (
                    (x, y) not in visited or ((x, y) in visited and new_dist <= visited[(x, y)]))

    while q:

        data = q.popleft()

        for k in range(4):
            dist = 0 if (x[k], y[k]) == (x[data[3]], y[data[3]]) else 1

            # check whether it is first data from queue
            if data[3] == -1:
                dist = 1

            if is_valid(data[0] + x[k], data[1] + y[k], data[2] + dist):
                visited[(data[0] + x[k], data[1] + y[k])] = data[2] + dist
                q.append((data[0] + x[k], data[1] + y[k], data[2] + dist, k))

    return visited[(goalX, goalY)]


if __name__ == '__main__':

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)
