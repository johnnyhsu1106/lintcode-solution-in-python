'''
A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?

Notice
m and n will be at most 100.

Example
Given m = 3 and n = 3, return 6.
Given m = 4 and n = 5, return 35.
'''
class Solution:
    """
    @param: m: positive integer (1 <= m <= 100)
    @param: n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        paths = [[0] * n for x in range(m)]
        # initial dp at starting point
        paths[0][0] = 1
        # initialize dp at firsts column
        for x in range(1, m):
            paths[x][0] = paths[x - 1][0]
        # initail dp at first row
        for y in range(1, n):
            paths[0][y] = paths[0][y - 1]
        # update the dp's status
        for x in range(1, m):
            for y in range(1, n):
                paths[x][y] = paths[x -1][y] + paths[x][y - 1]

        return paths[m - 1][n - 1]



# def main():
#     s = Solution()
#     print(s.uniquePaths(3, 3))
#
# if __name__ == '__main__':
#     main()
