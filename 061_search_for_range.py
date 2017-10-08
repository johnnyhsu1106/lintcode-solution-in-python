'''
Given a sorted array of n integers, find the starting and ending position of a given target value.

If the target is not found in the array, return [-1, -1].

Example
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

Challenge
O(log n) time.
'''

class Solution:
    """
    @param: A: an integer sorted array
    @param: target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    '''
    idea:
    please see the 014 first position of target, 458 last position of target
    Find the search range, which means find the first position of and last position of target.
    Use two times binary search

    '''
    def searchRange(self, A, target):

        if len(A) == 0:
            return [-1, -1]

        # Find the first position of target
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid

        if A[start] == target:
            left = start
        elif A[end] == target:
            left = end
        else:
            return [-1, -1]

        # Find the last position of target
        start, end = left, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid

        if A[end] == target:
            right = end
        else:
            right = start

        return [left, right]
