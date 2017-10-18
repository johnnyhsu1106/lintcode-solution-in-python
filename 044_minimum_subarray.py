'''
Given an array of integers, find the subarray with smallest sum.

Return the sum of the subarray.

Notice

The subarray should contain one integer at least.

Example
For [1, -1, -2, 1], return -3.
'''
class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # prefix sum: p[k] = nums[0] + nums[1] + ...+ nums[k]
        # prefix min subarray sum from k to 0:
        # p[k] - max(p[k-1],p[k-2,...,p[1], p[0]]) for k = 1 ~ n-1
        # find the 
        # p[0] = nums[0] - 0

        if not nums or len(nums) == 0:
            return 0

        max_sum = 0
        min_sum = float('inf')
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            min_sum = min(min_sum, total - max_sum)
            max_sum = max(max_sum, total)

        return min_sum


# def main():
#     s = Solution()
#     nums = [1, -1, -2, 1]
#     print(s.minSubArray(nums))
# if __name__ == '__main__':
#     main()
