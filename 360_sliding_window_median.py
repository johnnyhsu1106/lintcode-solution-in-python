'''
Given an array of n integer, and a moving window(size k),
move the window at each iteration from the start of the array,
find the median of the element inside the window at each moving.
(If there are even numbers in the array,
return the N/2-th number after sorting the element in the window. )

Example:

For array [1,2,7,8,5], moving window size k = 3. return [2,7,7]

At first the window is at the start of the array like this

[ | 1,2,7 | ,8,5] , return the median 2;

then the window move one step forward.

[1, | 2,7,8 | ,5], return the median 7;

then the window move one step forward again.

[1,2, | 7,8,5 | ], return the median 7;

Challenge
O(nlog(n)) time
'''

from heapq import heappush, heappop, heapify
class Solution:
    """
    @param: nums: A list of integers
    @param: k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        if not nums or k == 0:
            return []

        if k == 1:
            return nums

        medians = []
        max_heap, min_heap = [],[]

        for i in range(k):
            self._add_num_to_heaps(nums[i], max_heap, min_heap)
            self._balance_heaps(max_heap, min_heap)

        self._add_median_to_medians(medians, max_heap)


        for i in range(k, len(nums)):
            add_num = nums[i]
            remove_num = nums[i - k]

            self._add_num_to_heaps(add_num, max_heap, min_heap)
            self._remove_num_from_heaps(remove_num, max_heap, min_heap)
            self._balance_heaps(max_heap, min_heap)
            self._add_median_to_medians(medians, max_heap)

        return medians


    def _add_num_to_heaps(self, num, max_heap, min_heap):
        if len(max_heap) == 0 or num < - max_heap[0]:
            heappush(max_heap, -num)
        else:
            heappush(min_heap, num)


    def _remove_num_from_heaps(self, num, max_heap, min_heap):
        if num <= - max_heap[0]:
            max_heap.remove(-num)
            heapify(max_heap)
        else:
            min_heap.remove(num)
            heapify(min_heap)


    def _balance_heaps(self, max_heap, min_heap):
        while len(max_heap) > len(min_heap) + 1:
            heappush(min_heap, - heappop(max_heap))

        while len(max_heap) < len(min_heap):
            heappush(max_heap, - heappop(min_heap))


    def _add_median_to_medians(self, medians, max_heap):
        medians.append(- max_heap[0])



# def main():
#     s = Solution()
#     nums = [1,2,7,8,5]
#     k = 3
#     print(s.medianSlidingWindow(nums, k))
# if __name__ == '__main__':
#     main()
