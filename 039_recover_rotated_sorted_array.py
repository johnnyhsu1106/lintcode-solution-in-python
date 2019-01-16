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
        # write your code here
        mid = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                mid = i
                
        if mid != 0:
            self.swap(nums, 0, mid)
            self.swap(nums, mid + 1, len(nums) - 1)
            self.swap(nums, 0, len(nums) - 1)

    def swap(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
