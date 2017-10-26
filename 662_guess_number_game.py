'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

Example
n = 10, I pick 4 (but you don't know)

Return 4. Correct !
'''
"""
The guess API is already defined for you.
@param num, your guess
@return -1 if my number is lower, 1 if my number is higher, otherwise return 0
you can call Guess.guess(num)
"""

class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess
    def guessNumber(self, n):
        start,  end = 1,  n

        while start + 1 < end:
            mid = start + (end - start) // 2
            result = Guess.guess(mid)
            if result == 0:
                return mid
            elif result == 1:
                start = mid
            else:
                end = mid

        if Guess.guess(start) == 0:
            return start

        if Guess.guess(end) == 0:
            return end
