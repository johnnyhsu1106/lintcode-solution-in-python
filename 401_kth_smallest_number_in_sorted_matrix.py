"""
Find the kth smallest number in at row and column sorted matrix.

Example
Given k = 4 and a matrix:

[
  [1 ,5 ,7],
  [3 ,7 ,8],
  [4 ,8 ,9],
]
return 5

Challenge
Solve it in O(k log n) time where n is the bigger one between row size and column size.
"""
from heapq import heappop, heappush
class Solution:
    """
    @param: matrix: a matrix of integers
    @param: k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        '''
        idea: the combination of min heap and bfs
        '''

        m, n = len(matrix), len(matrix[0])

        # Create a matrix called visited_matrix, default value is False,\
        # Initialize the min heap as tuple of list, element = (value, i, j)
        # In Python, if you pass the tuple, heap will be automatically using the first value of each element in tuple
        # Element could be list or tuple
        visited_matrix = [[False] * n for i in range(m)]
        visited_matrix[0][0] = True

        min_heap = []
        heappush(min_heap, (matrix[0][0], 0, 0))
        count = 0 # the number of smallest number

        while min_heap:
            kth_smallest, x, y = heappop(min_heap)
            count += 1
            dx = [1, 0]
            dy = [0, 1]

            if count == k:
                return kth_smallest

            for i in range(2):
                new_x = x + dx[i]
                new_y = y + dy[i]

                if self._is_bound(new_x, new_y, matrix) and not visited_matrix[new_x][new_y]:
                    visited_matrix[new_x][new_y] = True
                    heappush(min_heap, (matrix[new_x][new_y], new_x, new_y))



    def _is_bound(self, x, y, matrix):
        return 0 <= x <= len(matrix) - 1 and 0 <= y <= len(matrix[0]) - 1


# def main():
#     matrix = [[1,5,7],
#               [3,7,8],
#               [4,8,9]]
#     s = Solution()
#     print(s.kthSmallest(matrix, 4))
# if __name__ == '__main__':
#     main()
