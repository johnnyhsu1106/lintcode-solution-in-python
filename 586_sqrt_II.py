'''
Implement double sqrt(double x) and x >= 0.

Compute and return the square root of x.

Notice

You do not care about the accuracy of the result, we will help you to output results.

Example
Given n = 2 return 1.41421356
'''

class Solution:
    """
    @param: x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        eps = 1e-12

        start, end = 0.0, x
        if x < 1.0:
            end = 1.0

        while end - start > eps:
            mid = start + (end - start) / 2

            if mid * mid < x:
                start = mid
            else:
                end = mid

        return start



# def main():
#     s = Solution()
#     print(s.sqrt(1))
# if __name__ == '__main__':
#     main()
