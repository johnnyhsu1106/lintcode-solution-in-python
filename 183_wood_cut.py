'''
Given n pieces of wood with length L[i] (integer array).
Cut them into small pieces to guarantee
you could have equal or more than k pieces with the same length.
What is the longest length you can get from the n pieces of wood?
Given L & k, return the maximum length of the small pieces.

Notice

You couldn't cut wood into float length.

If you couldn't get >= k pieces, return 0.

Example
For L=[232, 124, 456], k=7, return 114.

Challenge
O(n log Len), where Len is the longest length of the wood.
'''
class Solution:
    """
    @param: L: Given n pieces of wood with length L[i]
    @param: k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        if not L or k <= 0 or k > sum(L):
            return 0

        start, end = 1, max(L) # define the range

        while start + 1 < end:
            mid = start + (end - start) // 2

            if self._count_piece(L, mid) >= k:
                start = mid
            else:
                end = mid

        if self._count_piece(L, end) >= k:
            return end

        return start


    def _count_piece(self, L, length):
        piece = 0

        for wood_length in L:
            piece += wood_length // length

        return piece



# def main():
#     s = Solution()
#     L = [232, 124, 456]
#     k = 7
#     print(s.woodCut(L, k))
#
# if __name__ == '__main__':
#     main()
