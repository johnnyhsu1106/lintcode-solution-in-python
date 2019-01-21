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
        if not matrix or m == 0 or n == 0 or k <= 0 or k > m * n:
            return

        # Create a matrix called visited_matrix, default value is False,\
        # Initialize the min heap as tuple of list, element = (value, i, j)
        # In Python, if you pass the tuple, heap will be automatically using the first value of each element in tuple
        # Element could be list or tuple
        min_heap = []
        visited_matrix = [[False] * n for i in range(m)]

        heappush(min_heap, (matrix[0][0], 0, 0))
        visited_matrix[0][0] = True
        count = 0 # the number of smallest number

        while min_heap:
            value, x, y = heappop(min_heap)
            count += 1

            if count == k:
                return value

            dx = [1, 0]
            dy = [0, 1]

            for i in range(len(dx)):
                new_x = x + dx[i]
                new_y = y + dy[i]

                if self._is_bound(new_x, new_y, m ,n) and not visited_matrix[new_x][new_y]:
                    heappush(min_heap, (matrix[new_x][new_y], new_x, new_y))
                    visited_matrix[new_x][new_y] = True


    def _is_bound(self, x, y, matrix):
        return 0 <= x <= m - 1 and 0 <= y <= n - 1


# def main():
#     matrix = [[1,5,7],
#               [3,7,8],
#               [4,8,9]]
#     s = Solution()
#     print(s.kthSmallest(matrix, 4))
# if __name__ == '__main__':
#     main()
