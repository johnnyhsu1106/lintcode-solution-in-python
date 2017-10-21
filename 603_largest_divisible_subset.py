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
            return nums

        n = len(nums)
        nums.sort()
        dp = [1 for i in range(n)] # a list for the length of subset if requirement is met.
        pre_index = [-1 for i in range(n)] # a list for the pre_indexvious index if requirement is met.

        # initialize
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        pre_index[i] = j

        max_i, index = 0 , -1
        for i in range(n):
            if dp[i] > max_i:
                max_i = dp[i]
                index = i

        result = []
        for i in range(max_i):
            result.append(nums[index])
            index = pre_index[index]

        return result



# def main():
#     s = Solution()
#     nums = [1,2,3]
#     print(s.largestDivisibleSubset(nums))
#
#     nums = [1,2,4,8]
#     print(s.largestDivisibleSubset(nums))
# if __name__ == '__main__':
#     main()
