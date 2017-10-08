'''
Given k sorted integer arrays, merge them into one sorted array.


Example
Given 3 sorted arrays:

[
  [1, 3, 5, 7],
  [2, 4, 6],
  [0, 8, 9, 10, 11]
]
return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].
'''
from heapq import heappush, heappop
class Solution:
    """
    @param: arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        '''
        If average array length is n
        Time: O(nklogk)
        Space: O(k)
        '''
        if not arrays or len(arrays) == 0:
            return []

        result = []
        min_heap = []

        for idx, array in enumerate(arrays):
            if len(array) != 0:
                heappush(min_heap, (array[0], idx, 0))

        while min_heap:
            value, x, y = heappop(min_heap)
            result.append(value)
            if y + 1 < len(arrays[x]):
                heappush(min_heap, (arrays[x][y + 1], x, y + 1))

        return result



    def mergekSortedArrays_sort(self, arrays):
        '''
        Time: O(nklognk)
        Space: O(1) if used Quick Sort
        '''
        result = []
        for array in arrays:
            for num in array:
                result.append(num)
        return sorted(result)
