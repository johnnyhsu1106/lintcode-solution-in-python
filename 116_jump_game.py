'''
Given an array of non-negative integers,
you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Notice

This problem have two method which is Greedy and Dynamic Programming.

The time complexity of Greedy method is O(n).

The time complexity of Dynamic Programming method is O(n^2).

We manually set the small data set to allow you pass the test in both ways.
This is just to let you learn how to use this problem in dynamic programming ways.
If you finish it in dynamic programming ways,
you can try greedy method to make it accept again.

Have you met this question in a real interview? Yes
Example
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''
class Solution:
    """
    @param: A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        if not A or len(A) == 0:
            return False

        n = len(A)
        can = [False] * n
        can[0] = True
        #  can[i] is determind by the can[0].. can[i - 1]
        #  can[j] = True and A[j] (jump distance) >= i - j (the distance between i and j)
        for i in range(1, len(A)):
            for j in range(i):

                if can[j] and A[j] >= i - j:
                    can[i] = True
                    break

        return can[len(A) -1]
