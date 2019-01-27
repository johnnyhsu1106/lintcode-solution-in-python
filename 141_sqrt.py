'''
mplement int sqrt(int x).

Compute and return the square root of x.

Example
sqrt(3) = 1
sqrt(4) = 2
sqrt(5) = 2
sqrt(10) = 3

Challenge
O(log(x))
'''
class Solution:
    """
    @param: x: An integer
    @return: The sqrt of x
    """
    def sqrt(x):
        '''
        idea: binary search.
        Time: O(logn)
        '''
        start, end = 1, x

        while start + 1 < end:
            mid = start + (end - start) / 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid
            else:
                end = mid

        #  the value closet to the x (last number that number * number <= x)
        if end * end <= x:
            return int(end)
            
        return int(start)


    def sqrt_1(self, x):
        '''
        Time: O(n*1/2)
        '''
        i = 1
        while i * i <= x:
            i += 1
        return i - 1
