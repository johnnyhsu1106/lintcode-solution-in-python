'''
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Notice

You may assume that A has enough space (size that is greater or equal to m + n)
to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

Example
A = [1, 2, 3, empty, empty], B = [4, 5]

After merge, A will be filled as [1, 2, 3, 4, 5]
'''
class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        i = m - 1
        j = n - 1
        index = m + n - 1

        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[index] = A[i]
                i -= 1
            else:
                A[index] = B[j]
                j -= 1
            index -= 1

        while i >= 0:
            A[index] = A[i]
            index -= 1
            i -= 1

        while j >= 0:
            A[index] = B[j]
            index -= 1
            j -= 1



# def main():
#     s = Solution()
#     A = [1, 2, 3, 'empty', 'empty']
#     B = [4, 5]
#     s.mergeSortedArray(A, 3, B, 2)
#     print(A)
#
# if __name__ == '__main__':
#     main()
