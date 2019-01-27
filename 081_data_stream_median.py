'''
Numbers keep coming, return the median of numbers at every time a new number added.

What's the definition of Median?
- Median is the number that in the middle of a sorted array.
If there are n numbers in a sorted array A, the median is A[(n - 1) / 2].
For example, if A=[1,2,3], median is 2. If A=[1,19], median is 1.

Example
For numbers coming list: [1, 2, 3, 4, 5], return [1, 1, 2, 2, 3].

For numbers coming list: [4, 5, 1, 3, 2, 6, 0], return [4, 4, 4, 3, 3, 3, 3].

For numbers coming list: [2, 20, 100], return [2, 2, 20].

Challenge
Total run time in O(nlogn).
'''
from heapq import heappush, heappop

class Solution:
    """
    @param: nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # Time: O(nlogn)
        # Space: O(n)

        '''
        idea:
        1. use Python build-in data structure heapq to maintain max_heap and min_heap
        However, heapq supports only min_heap, the way to maintain max_heap is
        convert the number (positive becomes negative, negative becomes positive),
        then push into max_heap by using heappush(max_heap, item)
        Then when we use heappop(max_heap) or max_heap[0] to get/seek the max,
        We need to converse it again.

        2. maintain the size of max_heap and min_heap such that
        len(max_heap) == len(min_heap) or len(max_heap) = len(min_heap) + 1 are satisfied.
        so we can get median by seek the max from max_heap(meadian = - max_heap[0])

        Definition: median = A[(n - 1) / 2], according to problem statement.
        '''
        max_heap, min_heap = [], []
        medians = []

        for num in nums:
            self._add_num_to_heaps(max_heap, min_heap, num)
            self._balance_heaps(max_heap, min_heap)
            self._add_median_to_medians(medians, max_heap)

        return medians


    def _add_num_to_heaps(self, max_heap, min_heap, num):
        # if len(max_heap) == 0:
        #     heappush(max_heap, - num)
        #     return
        #
        # if num >= - max_heap[0]:
        #     heappush(min_heap, num)
        # else:
        #     heappush(max_heap, - num)

        # # for the first element, it should belogn to max heap
        if len(max_heap) == 0 or num < - max_heap[0]:
            heappush(max_heap, - num)
        else:
            heappush(min_heap, num)


    def _balance_heaps(self, max_heap, min_heap):
        # make sure len(max_heap) = len(min_heap) or len(max_heap) = len(min_heap) + 1
        # you can use if statement or while statement, both work
        # becasue only one number is added to heap at one time.
        while len(max_heap) < len(min_heap):
            heappush(max_heap, - heappop(min_heap))

        while len(max_heap) > len(min_heap) + 1:
            heappush(min_heap, - heappop(max_heap))


    def _add_median_to_medians(self, medians, max_heap):
        medians.append(- max_heap[0])


# def main():
#     s = Solution()
#     nums = [1, 2, 3, 4, 5]
#     print(s.medianII(nums) == [1, 1, 2, 2, 3])
#
#     nums = [4, 5, 1, 3, 2, 6, 0]
#     print(s.medianII(nums) == [4, 4, 4, 3, 3, 3, 3])
#
#     nums = [2, 20, 100]
#     print(s.medianII(nums) == [2, 2, 20])
#
#     nums = [5,-10,4]
#     print(s.medianII(nums) == [5, -10, 4])
#
# if __name__ == '__main__':
#     main()
