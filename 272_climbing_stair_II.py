'''
A child is running up a staircase with n steps, and
can hop either 1 step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs.

Example
n=3
1+1+1=2+1=1+2=3=3

return 4
'''
class Solution:
    """
    @param: n: An integer
    @return: An integer
    """
    def climbStairs2(self, n):
        if n == 0:
            return 1
        if n <= 2:
            return n


        ways = [1, 1, 2]

        for i in range(3, n + 1):
            count = ways[0]  + ways[1] + ways[2]
            ways[0] = ways[1]
            ways[1] = ways[2]
            ways[2] = count

        return count
