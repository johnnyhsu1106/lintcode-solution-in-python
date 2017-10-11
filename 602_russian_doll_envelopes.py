'''
You have a number of envelopes with widths and heights given as a pair of integers (w, h).
One envelope can fit into another if and only
if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example
Given envelopes = [[5,4],[6,4],[6,7],[2,3]],
the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
'''
class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        if not envelopes or len(envelopes) == 0 or len(envelopes[0]) == 0:
            return 0

        envelopes.sort()

        n = len(envelopes)

        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)



# def main():
#     s = Solution()
#     envelopes = [[5,4],[6,4],[6,7],[2,3]]
#     print(s.maxEnvelopes(envelopes))
#
# if __name__ == '__main__':
#     main()
