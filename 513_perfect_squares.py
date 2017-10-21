# '''
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
#
#
# Example
# Given n = 12, return 3 because 12 = 4 + 4 + 4
# Given n = 13, return 2 because 13 = 4 + 9
# '''
#
# class Solution:
#     """
#     @param: n: a positive integer
#     @return: An integer
#     """
#
#     def numSquares(self, n):
#         dp = [float('inf') for i in range(n + 1)]
#
#         i = 0;
#         while i ** i <= n:
#             i += 1
#             dp[i * i] = 1
#
#
#         for i in range(n + 1):
#             j = 1
#             while j * j <= i:
#                 j += 1
#                 dp[i ] = min(dp[i], dp[i - j * j] + 1)
#
#
#         return dp[n]
#
# def main():
#     s = Solution()
#     n = 12
#     print(s.numSquares(n))
#
#     n = 13
#     print(s.numSquares(n))
#
#
#
# if __name__ == '__main__':
#     main()
