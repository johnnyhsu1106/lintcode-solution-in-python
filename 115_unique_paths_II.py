'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

 Notice

m and n will be at most 100.


Example
For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
'''
class Solution:
    """
    @param: obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):

        if not obstacleGrid or len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0

        # initialize
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        paths = [[0] * n for i in range(m)]

        if obstacleGrid[0][0] == 1:
            paths[0][0] = 0
        else:
            paths[0][0] = 1

        for x in range(1, m):
            if obstacleGrid[x][0] == 1:
                break
            paths[x][0] = paths[x - 1][0]

        for y in range(1, n):
            if obstacleGrid[0][y] == 1:
                break
            paths[0][y] = paths[0][y - 1]

        # DP
        for x in range(1, m):
            for y in range(1, n):
                if obstacleGrid[x][y] == 0:
                    paths[x][y] = paths[x][y - 1] + paths[x - 1][y]
                else:
                    paths[x][y] = 0

        return paths[m - 1][n - 1]


# def main():
#     s = Solution()
#     obstacleGrid = [[0]]
#     print(s.uniquePathsWithObstacles(obstacleGrid) == 1)
#
#     obstacleGrid = [[0,0],[0,0],[0,0],[1,0],[0,0]]
#     print(s.uniquePathsWithObstacles(obstacleGrid) == 3)
#
#     obstacleGrid = [[0,0,0],
#                     [0,1,0],
#                     [0,0,0]]
#     print(s.uniquePathsWithObstacles(obstacleGrid) == 2)
#
# if __name__ == '__main__':
#     main()
