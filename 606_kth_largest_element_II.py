'''
Find K-th largest element in an array. and N is much larger than k.

Notice
You can swap elements in the array

Example
In array [9,3,2,4,8], the 3rd largest element is 4.

In array [1,2,3,4,5], the 1st largest element is 5, 2nd largest element is 4,
3rd largest element is 3 and etc.
'''
from heapq import heappush, heappop
class Solution:
    """
    @param: nums: an integer unsorted array
    @param: k: an integer from 1 to n
    @return: the kth largest element
    """
    def kthLargestElement2(self, nums, k):
        max_heap = []
        for num in nums:
            heappush(max_heap, -num)

        for i in range(k):
            result = -heappop(max_heap)
        return result


# def main():
#     s = Solution()
#     nums = [9,3,2,4,8]
#     k = 3
#     print(s.kthLargestElement2(nums, k))
#
# if __name__ == '__main__':
#     main()
