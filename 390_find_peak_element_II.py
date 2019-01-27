'''
There is an integer matrix which has the following features:

The numbers in adjacent positions are different.
The matrix has n xs and m yumns.
For all i < m, A[0][i] < A[1][i] && A[n - 2][i] > A[n - 1][i].
For all j < n, A[j][0] < A[j][1] && A[j][m - 2] > A[j][m - 1].
We define a position P is a peek if:

A[j][i] > A[j+1][i] && A[j][i] > A[j-1][i] && A[j][i] > A[j][i+1] && A[j][i] > A[j][i-1]
Find a peak element in this matrix. Return the index of the peak.

Notice

The matrix may contains multiple peeks, find any of them.


Example
Given a matrix:

[
  [1 ,2 ,3 ,6 ,5],
  [16,41,23,22,6],
  [15,17,24,21,7],
  [14,18,19,20,10],
  [13,14,11,10,9]
]
return index of 41 (which is [1,1]) or index of 24 (which is [2,2])

Challenge
Solve it in O(n+m) time.

If you come up with an algorithm that
you thought it is O(n log m) or O(m log n),
can you prove it is actually O(n+m) or propose a similar but O(n+m) algorithm?
'''

class Solution:
    """
    @param: A: An integer matrix
    @return: The index of the peak
    """
    def findPeakII(self, A):
        if not A or len(A) == 0 or len(A[0]) == 0:
            return [-1, -1]

        left, right = 0, len(A[0]) - 1
        up, down = 0, len(A) - 1

        while left + 1 < right or up + 1 < down: #  use or, not and.
            # see  x, y direcetion, who has wider range (binary search)
            if right - left > down - up:
                y = left + (right - left) //  2
                x = self.find_x_peak(A, y, up, down)

                if self.is_peak(A, x, y):
                    return [x, y]
                elif A[x][y] < A[x][y - 1]:
                    right = y
                elif A[x][y] < A[x][y + 1]:
                    left = y
            else:
                x = up + (down - up) // 2
                y = self.find_y_peak(A, x, left, right)

                if self.is_peak(A, x, y):
                    return [x, y]
                elif A[x][y] < A[x - 1][y]:
                    down = x
                else:
                    up = x


    def find_x_peak(self, A, y, up, down):
        max_value = float('-inf')
                
        for x in range(up, down + 1):
            if A[x][y] > max_value:
                max_value = A[x][y]
                x_peak = x

        return x_peak


    def find_y_peak(self, A, x, left, right):
        max_value = float('-inf')

        for y in range(left, right + 1):
            if A[x][y] > max_value:
                max_value = A[x][y]
                y_peak = y

        return y_peak


    def is_peak(self, A, x, y):
        return A[x][y] > max(A[x - 1][y], A[x + 1][y], A[x][y - 1], A[x][y + 1])



# def main():
#     s = Solution()
#     A = [ [1 ,2 ,3 ,6 ,5],
#           [16,41,23,22,6],
#           [15,17,24,21,7],
#           [14,18,19,20,10],
#           [13,14,11,10,9]]
#     print(s.findPeakII(A));
#
# if __name__ == '__main__':
#     main()
