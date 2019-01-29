'''
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right
which minimizes the sum of all numbers along its path.

Notice

You can only move either down or right at any point in time.
'''
class Solution:
    """
    @param: grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return -1

        m, n = len(grid), len(grid[0])
        dp = [[0] * n for x in range(m)]

        # initialize dp at starting point
        dp[0][0] = grid[0][0]
        # iniitalize dp at x direction (first column)
        for x in range(1, m):
            dp[x][0] = dp[x - 1][0] + grid[x][0]
        # initialize dp at y direction (first row)
        for y in range(1, n):
            dp[0][y] = dp[0][y - 1] + grid[0][y]
        # start to update the status
        for x in range(1, m):
            for y in range(1, n):
                dp[x][y] = min(dp[x - 1][y], dp[x][y - 1]) + grid[x][y]

        return dp[m - 1][n - 1]





# def main():
#     s = Solution()
#
#     grid = [[1,2],[1,1]]
#     print(s.minPathSum(grid))
# if __name__ == '__main__':
#     main()
