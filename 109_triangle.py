'''
Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

Notice

Bonus point if you are able to do this using only O(n) extra space,
where n is the total number of rows in the triangle.

Example
Given the following triangle:

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
'''

class Solution:
    """
    @param: triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal_1(self, triangle):
        if not triangle:
            return -1

        # From Bottom to Top
        n = len(triangle)
        dp = [[0] * n  for i in range(n)] # initail the dp
        # in last row
        for y in range(n):
            dp[n - 1][y] = triangle[n - 1][y]

        for x in range(n - 2, -1, -1): # from n - 2 level to 0 level
            for y in range(x + 1): # from 0 to x
                dp[x][y] = min(dp[x + 1][y] , dp[x + 1][y + 1]) + triangle[x][y]

        return dp[0][0]



    def minimumTotal_2(self, triangle):
        if not triangle:
            return -1

        n = len(triangle)
        # From Top to Bottom
        dp = [[0] * n  for i in range(n)]
        dp[0][0] = triangle[0][0]

        for x in range(1, n):
            dp[x][0] = dp[x - 1][0] + triangle[x][0]
            dp[x][x] = dp[x - 1][x - 1] + triangle[x][x]

        for x in range(1, n):
            for y in range(1, x):
                dp[x][y] = min(dp[x - 1][y], dp[x - 1][y - 1]) + triangle[x][y]


        return min(dp[n-1])


# def main():
#     s = Solution()
#     triangle = [ [2],
#                 [3,4],
#                [6,5,7],
#               [4,1,8,3]]
#     print(s.minimumTotal_1(triangle))
#     print(s.minimumTotal_2(triangle))
#
# if __name__ == '__main__':
#     main()
