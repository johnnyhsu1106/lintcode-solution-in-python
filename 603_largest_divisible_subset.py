'''
Given a set of distinct positive integers,
find the largest subset
such that every pair (Si, Sj) of elements in this subset satisfies:
Si % Sj = 0 or Sj % Si = 0.

Notice

If there are multiple solutions, return any subset is fine.

Example
Given nums = [1,2,3], return [1,2] or [1,3]

Given nums = [1,2,4,8], return [1,2,4,8]
'''
class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset
    """
    def largestDivisibleSubset(self, nums):
        if not nums or len(nums) <= 1:
            return []

        # n = len(nums)
        # nums.sort()
        # dp = [[] for i in range(n)]
        # # initialize
        # for i in range(n):
        #     dp[i].append(nums[i])
        #
        # for i in range(n):
        #     for j in range(i):
        #         if nums[i] % nums[j] == 0:
        #             dp[i].append(nums[j])
        # max_size = 0
        # for i in range(n):
        #     if len(dp[i]) > max_size:
        #         max_size = len(dp[i])
        #         largest_sub = dp[i]
        #
        # return largest_sub.sort()


# def main():
#     s = Solution()
#     nums = [1,2,3]
#     print(s.largestDivisibleSubset(nums))
# if __name__ == '__main__':
#     main()
