"""
Given two integer arrays sorted in ascending order and an integer k.
Define sum = a + b, where a is an element from the first array and b is an element from the second one.
Find the kth smallest sum out of all possible sums.

Example
Given [1, 7, 11] and [2, 4, 6].

For k = 3, return 7.
For k = 4, return 9.
For k = 8, return 15.

Challenge
Do it in either of the following time complexity:

O(k log min(n, m, k)). where n is the size of A, and m is the size of B.
O( (m + n) log maxValue). where maxValue is the max number in A and B.
"""
from heapq import heappop, heappush
class Solution:

    """
    @param: A: an integer arrays sorted in ascending order
    @param: B: an integer arrays sorted in ascending order
    @param: k: An integer
    @return: An integer
    """
    '''
    idea:
    BFS + Heap
    Please see the problem 401 as well. The whole concept is like the one in problem 401
    Image there is a matrix, each element is the sume of A[i] and B[j], 0 <= i <= m - 1, 0 <= j <= n - 1.
    sum_matrix[i][j] = A[i] + B[j]

    For example:
    A = [1, 7, 11],i(col)
    B = [2, 4, 6], j(row)

    sum_marix =
    [ [3, 5, 7],
      [9, 11, 13],
      [13, 15, 17]
    ]

    '''
    def kthSmallestSum(self, A, B, k):
        if not A or not B or k == 0:
            return

        m, n = len(A), len(B)
        visited_matrix = [[False] * n for i in range(m)]
        # Initialize the min heap and change the status of visited_matrix

        #  The node format: (A[i] + B[j], i, j)
        min_heap = [(A[0] + B[0], 0, 0)]
        visited_matrix[0][0] = True
        count = 0
        directions = [(1, 0), (0, 1)]

        dx = [1, 0]
        dy = [0, 1]

        while min_heap:
            value, x, y = heappop(min_heap)
            count += 1

            if count == k:
                return value

            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                
                if self._is_bound(new_x, new_y, m, n) and not visited_matrix[new_x][new_y]:
                    heappush(min_heap, (A[new_x] + B[new_y], new_x, new_y))
                    visited_matrix[new_x][new_y] = True


    def _is_bound(self, row, col, m, n):
        return 0 <= row <= m - 1 and 0 <= col <= n - 1

# def main():
#     s = Solution()
#     A = [1, 7, 11]
#     B = [2, 4, 6]
#     print(s.kthSmallestSum(A, B, 3))
#
#
# if __name__ == '__main__':
#     main()
