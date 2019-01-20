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
    def mergekSortedArrays_heap(self, arrays):
        '''
        N is the total number of integers.
        k is the number of arrays.
        Time: O(nlogk)
        Space: O(k)
        '''
        if not arrays:
            return []

        result = []
        min_heap = []

        for row in range(len(arrays)):
            if arrays[row]:
                num = arrays[row][0]
                heappush(min_heap, (num, row, 0))

        while min_heap:
            num, row, col = heappop(min_heap)
            result.append(num)
            if col < len(arrays[row]) - 1:
                heappush(min_heap, (arrays[row][col+ 1], row, col + 1))

        return result
            

    def mergekSortedArrays_merge(self, arrays):
        if len(arrays) == 0:
            return []
        if len(arrays) == 1:
            return arrays[0]

        mid = len(arrays) // 2
        left = self.mergekSortedArrays_merge(arrays[0:mid])
        right = self.mergekSortedArrays_merge(arrays[mid:])

        return self.merge_two_arrays(left, right)


    def merge_two_arrays(self, arr1, arr2):
        result = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1

        while i < len(arr1):
            result.append(arr1[i])
            i += 1

        while j < len(arr2):
            result.append(arr2[j])
            j   += 1

        return result


    def mergekSortedArrays_sort(self, arrays):
        '''
        Time: O(nlognn)
        Space: O(1) if used Quick Sort
        '''
        result = []
        for array in arrays:
            for num in array:
                result.append(num)
        return sorted(result)



# def main():
#     s = Solution()
#     arrays = [[1, 3, 5, 7],
#               [2, 4, 6],
#               [0, 8, 9, 10, 11]]
#     print(s.mergekSortedArrays_heap(arrays))
#     print(s.mergekSortedArrays_merge(arrays))
#
# if __name__ == '__main__':
#     main()
