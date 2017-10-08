'''
Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position,
find the shortest path to a destination position, return the length of the route.
Return -1 if knight can not reached.

Notice

source and destination must be empty.
Knight can not enter the barrier.

Clarification
If the knight is at (x, y), he can get to the following positions in one step:

(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)
Example
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return 2

[[0,1,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return 6

[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return -1
'''
from collections import deque


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    """
    @param: grid: a chessboard included 0 (false) and 1 (true)
    @param: source: a point
    @param: destination: a point
    @return: the shortest path
    """
    def shortestPath(self, grid, source, destination):

        m = len(grid)
        n = len(grid[0])

        if grid is None or m == 0 or n == 0:
            return -1

        dx = [1, 1, -1, -1, 2, 2, -2, -2]
        dy = [2, -2, 2, -2, 1, -1, 1, -1]

        queue = deque()
        queue.append(source)
        step = 0

        while queue:
            size = len(queue)
            for i in range(size):
                point = queue.popleft()
                if point.x == destination.x and point.y == destination.y:
                    return step

                for i in range(8):
                    new_point = Point(point.x + dx[i], point.y + dy[i])

                    if self.is_bound(new_point, grid) and grid[new_point.x][new_point.y] == 0:
                        queue.append(new_point)
                        grid[new_point.x][new_point.y] = 1
            step += 1

        return -1


    def is_bound(self, point, grid):
        m = len(grid)
        n = len(grid[0])
        return 0 <= point.x <= m - 1 and 0 <= point.y <= n - 1

# def main():
#     s = Solution()
#     grid = [[0,0,0],
#             [0,0,0],
#             [0,0,0]]
#     source = Point(2, 0)
#     destination = Point(2, 2)
#     print(s.shortestPath(grid, source, destination))
#
#
# if __name__ == '__main__':
#     main()
