"""
Given a string s,
find the length of the longest substring T that contains at most k distinct characters.

Example
For example, Given s = "eceba", k = 3,

T is "eceb" which its length is 4.

Challenge
O(n), n is the size of the string s.
"""
from collections import defaultdict
class Solution:
    """
    @param: s: A string
    @param: k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):

        max_length = 0
        lookup = defaultdict(int)
        i = 0
        j = 0
        for i in range(len(s)):
            # if len(lookup) < k , keep searching next char
            # if s[j] in look, this char alread in lookup. keep searching next char, unitl find char not in lookup
            while j < len(s) and (len(lookup) < k or s[j] in lookup):
                lookup[s[j]] += 1
                j += 1
            max_length = max(max_length, j - i)
            if s[i] in lookup:
                if lookup[s[i]] > 1:
                    lookup[s[i]] -= 1
                else:
                    del lookup[s[i]]
        return max_length

# def main():
#     s = Solution()
#     print(s.lengthOfLongestSubstringKDistinct('eceba', 3) )
#     print(s.lengthOfLongestSubstringKDistinct('abbcc', 3) )
# if __name__ == '__main__':
#     main()
