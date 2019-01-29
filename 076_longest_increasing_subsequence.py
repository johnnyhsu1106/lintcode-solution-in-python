'''
Given a sequence of integers, find the longest increasing subsequence (LIS).

You code should return the length of the LIS.

Clarification
What's the definition of longest increasing subsequence?

The longest increasing subsequence problem is to find a subsequence of a given sequence
in which the subsequence's elements are in sorted order, lowest to highest,
and in which the subsequence is as long as possible.
This subsequence is not necessarily contiguous, or unique.

https://en.wikipedia.org/wiki/Longest_increasing_subsequence

Example
For [5, 4, 1, 2, 3], the LIS is [1, 2, 3], return 3
For [4, 2, 4, 5, 3, 7], the LIS is [2, 4, 5, 7], return 4

Challenge
Time complexity O(n^2) or O(nlogn)
'''
class Solution:
    """
    @param: nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return

        n = len(nums)
        dp = [1] * n # initialize DP

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)


# def main():
#     s = Solution()
#     nums = [5, 4, 1, 2, 3]
#     print(s.longestIncreasingSubsequence(nums))
#     nums= [4, 2, 4, 5, 3, 7]
#     print(s.longestIncreasingSubsequence(nums))
#
# if __name__ == '__main__':
#     main()
