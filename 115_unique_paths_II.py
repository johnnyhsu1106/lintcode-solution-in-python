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

        if obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # initialize
        paths = [[0] * n for i in range(m)]

        for i in range(m):
            if  obstacleGrid[i][0] == 0:
                paths[i][0] = 1
            else:
                break

        for j in range(n):
            if obstacleGrid[0][j] == 0:
                paths[0][j] = 1
            else:
                break
        # DP
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    paths[i][j] = paths[i][j - 1] + paths[i - 1][j]
                else:
                    paths[i][j] = 0

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
