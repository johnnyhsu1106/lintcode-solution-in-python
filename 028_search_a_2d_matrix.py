'''
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Have you met this question in a real interview? Yes
Example
Consider the following matrix:

[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
Given target = 3, return true.
'''

class Solution:
    """
    @param: matrix: matrix, a list of lists of integers
    @param: target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        m = len(matrix)
        n = len(matrix[0])
        start, end = 0, m * n - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            i, j = mid // n, mid % n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                start = mid
            else:
                end = mid

        if matrix[start // n][start % n] == target:
            return True
        if matrix[end // n][end % n] == target:
            return True
        return False


# def main():
#     s = Solution()
#     matrix = [[5]]
#     print(s.searchMatrix(matrix, 5))
#
#     matrix = [[1, 3, 5, 7],
#               [10, 11, 16, 20],
#              [23, 30, 34, 50]]
#     print(s.searchMatrix(matrix, 3))
#
#
# if __name__ == '__main__':
#     main()
