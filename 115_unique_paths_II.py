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
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0 or obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for x in range(m)]
        dp[0][0] = 1 # at staring point, the number of unique path is 1
        # at the first column except starting point,
        # the number of paths is determined by the previous paths from the point above
        for x in range(1, m):
            if obstacleGrid[x][0] == 1:
                break

            dp[x][0] = dp[x - 1][0]

        # at the first row except starting point,
        # the number of paths is determined by the previous paths from the point on the left
        for y in range(1, n):
            if obstacleGrid[0][y] == 1:
                break

            dp[0][y] = dp[0][y - 1]

        # update the number of paths at each point if no obstacle at point(x, y)
        for x in range(1, m):
            for y in range(1, n):
                if obstacleGrid[x][y] == 0:
                    dp[x][y] = dp[x - 1][y] + dp[x][y - 1]


        return dp[m - 1][n - 1]

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
