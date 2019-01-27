'''
633. Find the Duplicate Number

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist.
Assume that there is only one duplicate number, find the duplicate one.

Example
Given nums = [5,5,4,3,2,1] return 5
Given nums = [5,4,4,3,2,1] return 4

Notice
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n^2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''

class Solution:
    """
    @param: nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, nums):
        if nums is None or len(nums) == 1:
            return -1

        start, end = 1, max(nums)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self._count_nums_less_than_target(nums, mid) <= mid:
                start = mid
            else:
                end = mid

        if self._count_nums_less_than_target(nums, start) <= start:
            return end
        return start

    def _count_nums_less_than_target(self, nums, target):
        total = 0
        for num in nums:
            if num <= target:
                total += 1
        return total
