'''
Write an efficient algorithm that searches for a value in an m x n matrix,
return the occurrence of it.

This matrix has the following properties:

Integers in each row are sorted from left to right.
Integers in each column are sorted from up to bottom.
No duplicate integers in each row or column.

Example
Consider the following matrix:

[
  [1, 3, 5, 7],
  [2, 4, 7, 8],
  [3, 5, 9, 10]
]
Given target = 3, return 2.

Challenge
O(m+n) time and O(1) extra space
'''
class Solution:
    """
    @param: matrix: A list of lists of integers
    @param: target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        count = 0
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        m, n = len(matrix), len(matrix[0])

        row, col = m - 1, 0
        while row >= 0 and col < n:
            if matrix[x][y] < target:
                col += 1
            elif matrix[x][y] > target:
                row -= 1
            else:
                count += 1
                row -= 1
                col += 1
        return count


# def main():
#     s= Solution()
#     matrix = [[1, 3, 5, 7],
#               [2, 4, 7, 8],
#               [3, 5, 9, 10]]
#     target = 3
#     print(s.searchMatrix(matrix, target))
#
# if __name__ == '__main__':
#     main()
