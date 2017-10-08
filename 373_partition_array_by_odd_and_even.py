'''
Partition an integers array into odd number first and even number second.

Example
Given [1, 2, 3, 4], return [1, 3, 2, 4]

Challenge
Do it in-place.
'''
class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            while left < right and nums[left] % 2 == 1:
                left += 1
            while left < right and nums[right] % 2 == 0:
                right -= 1

            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

# def main():
#     s = Solution()
#     # nums = [1, 2, 3, 4]
#     # s.partitionArray(nums)
#     # print(nums)
#     nums = [2147483644,2147483645,2147483646,2147483647]
#     s.partitionArray(nums)
#     print(nums)
#
# if __name__ == '__main__':
#     main()
