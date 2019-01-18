'''
Given a rotated sorted array, recover it to sorted array in-place.

Clarification
What is rotated array?

For example, the orginal array is [1,2,3,4],
The rotated array of it can be [1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]
Example
[4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]

Challenge
In-place, O(1) extra space and O(n) time.
'''

class Solution:
    """
    @param: nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        breakpoint = -1
        size = len(nums)

        for i in range(size - 1):
            if nums[i] > nums[i + 1]:
                breakpoint = i

        if breakpoint == -1:
            return

        self.swap(nums, 0, breakpoint)
        self.swap(nums, breakpoint + 1, size - 1)
        self.swap(nums, 0, size - 1)


    def swap(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
