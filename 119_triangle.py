'''
Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

 Notice

Bonus point if you are able to do this using only O(n) extra space,
where n is the total number of rows in the triangle.

Have you met this question in a real interview? Yes
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
        if not triangle or len(triangle) == 0:
            return -1

        # From Bottom to Top
        n = len(triangle)
        # initail the dp
        dp = [[0] * n  for i in range(n)]
        # from n - 1 leel
        for j in range(n):
            dp[n-1][j] = triangle[n-1][j]

        for i in range(n - 2, -1, -1): # from n - 2 level to 0 level
            for j in range(i + 1): # from 0 to i
                dp[i][j] = min(dp[i + 1][j] , dp[i + 1][j + 1]) + triangle[i][j]

        return dp[0][0]



    def minimumTotal_2(self, triangle):
        n = len(triangle)
        dp = [[0] * n  for i in range(n)]

        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]

        for i in range(1, n):
            for j in range(1, i):
                dp[i][j] = min(dp[i -1][j], dp[i - 1][j - 1]) + triangle[i][j]


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
