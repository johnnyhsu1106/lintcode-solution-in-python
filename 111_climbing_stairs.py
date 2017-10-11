'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Have you met this question in a real interview? Yes
Example
Given an example n=3 , 1+1+1=2+1=1+2=3

return 3
'''
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        if n <=  1:
            return n

        ways = [0] * (n + 1)
        ways[0] = 1
        ways[1] = 1
        for i in range(2, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]

        return ways[n]


    def climbStairs_1(self, n):
        if n <=  1:
            return 1

        ways = [1, 1]
        for i in range(2, n + 1):
            count = ways[0] + ways[1]
            ways[0] = ways[1]
            ways[1] = count
        return count


    def climbStairs_2(self, n):
        if n <=  1:
            return n

        last = 1
        last_last = 1
        for i in range(2, n + 1):
            last, last_last = last_last, last + last_last
        return last_last


# def main():
#     s = Solution()
#     print(s.climbStairs(3))
#     print(s.climbStairs_2(3))
# if __name__ == '__main__':
#     main()
