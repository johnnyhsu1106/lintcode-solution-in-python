'''
Given two arrays, write a function to compute their intersection.

Notice

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Have you met this question in a real interview? Yes
Example
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
'''

from collections import defaultdict
class Solution:

    """
    @param: nums1: an integer array
    @param: nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        result = []
        nums1_count = defaultdict(int)

        for num in nums1:
            nums1_count[num] += 1

        for num in nums2:
            if num in nums1_count and nums1_count[num] > 0:
                result.append(num)
                nums1_count[num] -= 1

        return result
