'''
Ugly number is a number that only have factors 2, 3 and 5.

Design an algorithm to find the nth ugly number.
The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

Notice

Note that 1 is typically treated as an ugly number.

Example
If n=9, return 10.

Challenge
O(n log n) or O(n) time.
'''
from heapq import heappush, heappop
class Solution:
    """
    @param: n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        if n <= 1:
            return n

        primes = [2, 3, 5]
        min_heap = [1]
        visited = set()

        for i in range(n):
            result = heappop(min_heap)
            for j in range(len(primes)):
                if result * primes[j] not in visited:
                    heappush(min_heap, result * primes[j])
                    visited.add(result * primes[j])

        return result



# def main():
#     s = Solution()
#     print(s.nthUglyNumber(9))
#
#
# if __name__ == '__main__':
#     main()
