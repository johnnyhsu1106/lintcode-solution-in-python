'''
Given an array of non-negative integers,
you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2.
(Jump 1 step from index 0 to 1, then 3 steps to the last index.)
'''
class Solution:
    """
    @param: A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        if not A:
            return 0

        n = len(A)
        steps = [0 for i in range(n)]
        steps[0] = 0
        
        for i in range(1, n):
            steps[i] = float('inf')

        for i in range(1, n):
            for j in range(i):
                if steps[j] != float('inf') and A[j] >= i - j:
                    steps[i] = min(steps[i], steps[j] + 1)

        return steps[n - 1]


# def main():
#     s = Solution()
#     A = [2,3,1,1,4]
#     print(s.jump(A))
#
# if __name__ == '__main__':
#     main()
