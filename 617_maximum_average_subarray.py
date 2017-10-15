'''
Given an array with positive and negative numbers,
find the maximum average subarray which length should be greater or equal to given length k.

Notice

It's guaranteed that the size of the array is greater or equal to k.

Example
Given nums = [1, 12, -5, -6, 50, 3], k = 3

Return 15.667 // (-6 + 50 + 3) / 3 = 15.667
'''
class Solution:
    """
    @param: nums: an array with positive and negative numbers
    @param: k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        left, right = min(nums), max(nums)

        while right - left > 1e-6:
            mid = (left + right) / 2.0
            if self.is_valid(nums, mid, k):
                left = mid
            else:
                right = mid

        return left


    def is_valid(self, nums, mid ,k):
        min_pre = 0
        pre_sum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1] - mid
            if i >= k and pre_sum[i] - min_pre >= 0:
                return True
            if i >= k:
                min_pre = min(min_pre, pre_sum[i - k + 1])

        return False



    def maxAverage_2(self, nums, k):
        #  not good idea: brute force
        if nums is None or len(nums) == 0:
            return float('inf')

        max_avg = float('-inf')
        for l in range(k , len(nums) + 1):
            for i in range(len(nums) - l + 1):
                max_avg = max(max_avg, sum(nums[i : i + l]) / l)

        return max_avg


# def main():
#     s = Solution()
#     nums = [1, 12, -5, -6, 50, 3]
#     k = 3
#     print(s.maxAverage(nums, k))
#
# if __name__ == '__main__':
#     main()
