class Solution:
    """
    @param: nums: an array with positive and negative numbers
    @param: k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        left, right = min(nums), max(nums)

        while right - left >= 1e-6:
            mid = left + (right - left) / 2.0

            if self._is_valid(mid, nums, k):
                left = mid
            else:
                right = mid

        return left


    def _is_valid(self, num, nums, k):
        min_presum = 0
        pre_sum = [0 for i in range(len(nums) + 1)]
        pre_sum[0] = 0

        for i in range(1, len(nums)+ 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1] - num

            if i >= k and pre_sum[i] - min_presum >= 0:
                return True
            if i >= k:
                min_presum = min(min_presum, pre_sum[i - k + 1])

        return False

# def main():
#     s = Solution()
#     nums = [1, 12, -5, -6, 50, 3]
#     k = 3
#     print(s.maxAverage(nums, k))
#
# if __name__ == '__main__':
#     main()
