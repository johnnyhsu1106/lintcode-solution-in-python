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

        m, n = len(matrix), len(matrix[0])

        # Create a matrix called visited, default value is False,\
        visited = [[False] * n for i in range(m)]
        visited[0][0] = True
        # Initialize the min heap as tuple of list, element = (value, i, j)
        # In Python, heap will be automatically using the first value of each element in list
        # Element could be list or tuple
        min_heap = []
        heappush(min_heap, (matrix[0][0], 0, 0))

        for step in range(k):
            kth_smallest, x, y = heappop(min_heap)
            dx = [1, 0]
            dy = [0, 1]

            for i in range(2):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if self.is_bound(new_x, new_y, matrix) and not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    heappush(min_heap, (matrix[new_x][new_y], new_x, new_y))
        return kth_smallest


    def is_bound(self, x, y, matrix):
        m, n = len(matrix), len(matrix[0])
        return 0 <= x <= m - 1 and 0 <= y <= n - 1


# def main():
#     matrix = [[1,5,7],
#               [3,7,8],
#               [4,8,9]]
#     s = Solution()
#     print(s.kthSmallest(matrix, 4))
# if __name__ == '__main__':
#     main()
