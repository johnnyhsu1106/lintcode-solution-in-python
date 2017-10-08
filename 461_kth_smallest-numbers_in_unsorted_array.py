"""
Kth Smallest Numbers in Unsorted Array

Find the kth smallest numbers in an unsorted integer array.

Example
Given [3, 4, 1, 2, 5], k = 3, the 3rd smallest numbers are [1, 2, 3].

Challenge
An O(nlogn) algorithm is acceptable, if you can do it in O(n), that would be great.
"""

from heapq import heappop
class Solution:
    """
    @param: k: An integer
    @param: nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest_1(self, k, nums):

        nums.sort()
        return nums[k-1]


    def kthSmallest_2(self, k, nums):
        
        for i in range(k):
            kth_smallest = heappop(nums)
            print(kth_smallest)
        return kth_smallest

#
# def main():
#     nums = [3, 4, 1, 2, 5]
#     k = 3
#     s = Solution()
#     print(s.kthSmallest_1(k ,nums))
#     print(s.kthSmallest_2(k, nums))
#
# if __name__ == '__main__':
#     main()
