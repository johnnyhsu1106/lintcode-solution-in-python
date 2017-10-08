'''
Given a target number and an integer array
A sorted in ascending order, find the index i in A such that A[i] is closest to the given target.
Return -1 if there is no element in the array.

Notice
There can be duplicate elements in the array, and we can return any of the indices with same value.
Example
Given [1, 2, 3] and target = 2, return 1.

Given [1, 4, 6] and target = 3, return 1.

Given [1, 4, 6] and target = 5, return 1 or 2.

Given [1, 3, 3, 4] and target = 2, return 0 or 1 or 2.
'''


class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def closestNumber(self, A, target):
        '''
        idea:
        key word: sorted array......binary search
        '''
        if len(A) == 0:
            return -1

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid

        if (target - A[start]) < (A[end] - target):
            return start
        else:
            return end



# 
# def main():
#     s = Solution()
#     print(s.closestNumber([1, 2, 3],0))
#     print(s.closestNumber([1, 4, 6],3))
#     print(s.closestNumber([1, 4, 6],5))
#     print(s.closestNumber([1, 3, 3, 4],2))
#     print(s.closestNumber([1, 4, 6, 10, 20], 21))
#     print(s.closestNumber([1, 3, 5, 7, 9],1))
# if __name__ == '__main__':
#     main()
