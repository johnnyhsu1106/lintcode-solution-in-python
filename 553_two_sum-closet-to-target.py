'''
Given an array nums of n integers,
find two integers in nums such that the sum is closest to a given number, target.

Return the difference between the sum of the two integers and the target.

Example
Given array nums = [-1, 2, 1, -4], and target = 4.

The minimum difference is 1. (4 - (2 + 1) = 1).

Challenge
Do it in O(nlogn) time complexity.
'''
class Solution:
    """
    @param: nums: an integer array
    @param: target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        diff = float('inf')
        nums.sort()
        left, right = 0, len(nums) - 1

        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                return 0
            elif total > target:
                right -= 1
            else:
                left += 1

            diff = min(diff, abs(target - total))

        return diff



# def main():
#     s = Solution()
#     nums = [-1, 2, 1, -4]
#     target = 4
#     print(s.twoSumClosest(nums, target))
#
#
# if __name__ == '__main__':
#     main()
