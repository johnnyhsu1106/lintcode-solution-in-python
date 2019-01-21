'''
Find K-th largest element in N arrays.

Notice
You can swap elements in the array

Have you met this question in a real interview? Yes
Example
In n=2 arrays [[9,3,2,4,7],[1,2,3,4,8]], the 3rd largest element is 7.
In n=2 arrays [[9,3,2,4,8],[1,2,3,4,2]], the 1st largest element is 9,
2nd largest element is 8, 3rd largest element is 7 and etc.
'''
from heapq import heappop, heappush
class Solution:

    """
    @param: arrays: a list of array
    @param: k: An integer
    @return: an integer, K-th largest element in N arrays
    """
    def KthInArrays_1(self, arrays, k):
        '''
        BFS + Max Heap

        N is number of Arrays
        L is average number of element in each array
        Space: O(N)
        Time: NLlog(L) + Klog(N)

        idea: please see the question 486 merge k sorted arrays
        the same concept, but for this question, you have to sort each array first.
        '''
        if not arrays or len(arrays) == 0 or k <= 0:
            return

        # sort each array in arrays
        for array in arrays:
            array.sort(reverse = True)

        # use the max heap and bfs
        # initialize it by puting all first one element in each array into max heap
        max_heap = []
        for x in range(len(arrays)):
            if len(arrays[x]) != 0:
                heappush(max_heap, (-arrays[x][0], x, 0))

        count = 0

        while max_heap:
            value, x, y = heappop(max_heap)
            count += 1

            if count == k:
                return -value

            if self._is_bound(x, y + 1, arrays):
                heappush(max_heap, (-arrays[x][y + 1], x, y + 1))



    def _is_bound(self, x, y, arrays):
        return 0 <= y <= len(arrays[x]) - 1



    def KthInArrays_2(self, arrays, k):
        '''
        Traverse + Min Heap

        N is number of Arrays
        L is average number of element in each array
        Space: O(K)
        Time: NLlog(K)
        '''
        if not arrays or len(arrays) == 0 or k <= 0:
            return

        min_heap =[]
        count = 0

        for array in arrays:
            for element in array:
                heappush(min_heap, element)
                count += 1

                if count > k:
                    heappop(min_heap)

        return min_heap[0]
