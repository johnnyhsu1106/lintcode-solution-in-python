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
    Please see the problem 401 as well. The whole concept is like the one in problem 401
    Image there is a matrix, each element is the sume of A[i] and B[j], 0 <= i < m, 0 <= j < n.
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
        
        m, n = len(A), len(B)
        visited = [[False] * n for _ in range(m)]
        # Initialize the min heap and change the status of visited
        visited[0][0] = True
        #  The node format: (A[i] + B[j], i, j)
        min_heap = [(A[0] + B[0], 0, 0)]
        for step in range(k):
            kth_smallest, i, j = heappop(min_heap)
            # push element into min heap (below)
            if i + 1 < m and not visited[i + 1][j]:
                visited[i + 1][j] = True
                heappush(min_heap, (A[i+1] + B[j], i + 1, j))
            # push element into min heap (right)
            if j + 1 < n and not visited[i][j + 1]:
                visited[i][j + 1] = True
                heappush(min_heap, (A[i] + B[j+1], i, j + 1))

        return kth_smallest



# def main():
#     s = Solution()
#     A = [1, 7, 11]
#     B = [2, 4, 6]
#     print(s.kthSmallestSum(A, B, 3))
#
#
# if __name__ == '__main__':
#     main()
