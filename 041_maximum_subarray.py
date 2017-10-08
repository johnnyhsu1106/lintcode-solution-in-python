'''
Given an array of integers, find a contiguous subarray which has the largest sum.

 Notice

The subarray should contain at least one number.

Have you met this question in a real interview? Yes
Example
Given the array [−2,2,−3,4,−1,2,1,−5,3], the contiguous subarray [4,−1,2,1] has the largest sum = 6.
'''

class Solution:
    """
    @param: nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    #  Greedy
    def maxSubArray_1(self, nums):
        if not nums or len(nums) == 0:
            return 0

        current_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(current_sum + nums[i], nums[i])
            max_sum = max(current_sum, max_sum)
        return max_sum


    def maxSubArray_2(self, nums):
        # prefix sum...
        # p[0] = 0
        # p[1] = 0 + nums[0]
        # p[2] = 0 + nums[0] + nums[1]
        # p[k] = 0 + nums[0] + nums[1]+..... + nums[k-1], sum of k elements
        # =================================================================
        # nums[i:j+1] = p[j+1] - p[i]

        # max_subarry_sum[k] = p[k] - min(p[k-1],p[k-2,...,p[1], p[0]])
        # max()

        if not nums or len(nums) == 0:
            return 0

        max_sum = float('-inf')
        min_sum = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            max_sum = max(max_sum, total - min_sum)
            min_sum = min(min_sum, total)
        return max_sum




# def main():
#     s = Solution()
#     nums = [-2, 2, -3, 4, -1, 2, 1, -5, 3]
#     pre_sum = [0]
#     total = 0
#     for num in nums:
#         total += num
#         pre_sum.append(total)
#     print(pre_sum)
#     # print(s.maxSubArray_1(nums))
#     print(s.maxSubArray_2(nums))
#
# if __name__ == '__main__':
#     main()
