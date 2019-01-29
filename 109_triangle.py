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
        '''
        idea: from Bottom to Top
        '''
        if not triangle:
            return -1

        n = len(triangle)
        # initail the dp matrix to store status
        dp = [[0] * n  for x in range(n)]
        # initialize the dp in the last row
        for y in range(n):
            dp[n - 1][y] = triangle[n - 1][y]
        # update dp status
        for x in range(n - 2, -1, -1): # from n - 2 level to 0 level
            for y in range(x + 1): # from 0 to x
                dp[x][y] = min(dp[x + 1][y] , dp[x + 1][y + 1]) + triangle[x][y]

        return dp[0][0]



    def minimumTotal_2(self, triangle):
        '''
        idea: from Top to Bottom
        '''
        if not triangle:
            return -1

        n = len(triangle)
        # initialize dp matrix to store the status
        dp = [[0] * n  for x in range(n)]
        # initialize dp in starting point
        dp[0][0] = triangle[0][0]
        # initialize dp for (x, 0) and (x, x), x from 1 to n - 1
        for x in range(1, n):
            dp[x][0] = dp[x - 1][0] + triangle[x][0]
            dp[x][x] = dp[x - 1][x - 1] + triangle[x][x]
        # update the dp status
        for x in range(2, n):
            for y in range(1, x):
                dp[x][y] = min(dp[x - 1][y], dp[x - 1][y - 1]) + triangle[x][y]

        return min(dp[n - 1])


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
