'''
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose
all prime factors are in the given prime list primes of size k.
For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is
the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

 Notice

1 is a super ugly number for any given primes.
The given numbers in primes are in ascending order.
0 < k ≤ 100, 0 < n ≤ 10^6, 0 < primes[i] < 1000

Example
Given n = 6, primes = [2, 7, 13, 19] return 13
'''
from heapq import heappush, heappop
class Solution:
    """
    @param: n: a positive integer
    @param: primes: the given prime list
    @return: the nth super ugly number
    """
    def nthSuperUglyNumber(self, n, primes):
        if n == 0 or len(primes) == 0:
            return -1

        min_heap = [1]
        visited = set([1])
        count = 0

        while len(min_heap) != 0:
            ugly_num = heappop(min_heap)
            count += 1
            if count == n:
                return ugly_num

            for prime in primes:
                new_ugly_num = ugly_num * prime
                if new_ugly_num not in visited:
                    heappush(min_heap, new_ugly_num)
                    visited.add(new_ugly_num)


# def main():
#     s = Solution()
#     n = 6
#     primes = [2, 7, 13, 19]
#     print(s.nthSuperUglyNumber(n, primes))
#
# if __name__ == '__main__':
#     main()
