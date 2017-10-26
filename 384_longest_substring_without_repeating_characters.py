'''
Given a string, find the length of the longest substring without repeating characters.

Example
For example, the longest substring without repeating letters for "abcabcbb" is "abc",
which the length is 3.

For "bbbbb" the longest substring is "b", with the length of 1.

Challenge
O(n) time
'''

class Solution:
    """
    @param: s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):

        seen = set()
        j = 0
        longest_length = 0
        for i in range(len(s)):
            while j < len(s) and s[j] not in seen:
                seen.add(s[j])
                j += 1
            longest_length = max(longest_length, j - i)
            seen.discard(s[i])
        return longest_length
