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
        paths = [[0] * n for i in range(m)]
        # initial rows
        paths[0][0] = 1
        for i in range(1, m):
            paths[i][0] = 1
        # initail columns
        for j in range(1, n):
            paths[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i -1][j] + paths[i][j - 1]

        return paths[m - 1][n - 1]


# 
# def main():
#     s = Solution()
#     print(s.uniquePaths(3, 3))
#
# if __name__ == '__main__':
#     main()
