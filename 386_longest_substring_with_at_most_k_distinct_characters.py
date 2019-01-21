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
        char_count = defaultdict(int)
        j = 0

        for i in range(len(s)):
            # if len(char_count) < k , keep searching next char
            # if s[j] in char_count,  keep searching next char, unit l find char not in char_count
            while j < len(s) and (len(char_count) < k or s[j] in char_count):
                char_count[s[j]] += 1
                j += 1

            max_length = max(max_length, j - i)
            # remove the s[i] from char_count
            if char_count[s[i]] > 1:
                char_count[s[i]] -= 1
            else:
                del char_count[s[i]]

        return max_length

# def main():
#     s = Solution()
#     print(s.lengthOfLongestSubstringKDistinct('eceba', 3) )
#     print(s.lengthOfLongestSubstringKDistinct('abbcc', 3) )
# if __name__ == '__main__':
#     main()
