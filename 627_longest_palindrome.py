'''
Given a string which consists of lowercase or uppercase letters,
find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

 Notice

Assume the length of given string will not exceed 1010.

Have you met this question in a real interview? Yes
Example
Given s = "abccccdd" return 7

One longest palindrome that can be built is "dccaccd", whose length is 7.
'''
from collections import defaultdict
class Solution:
    """
    @param: s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        hashset = set()

        for char in s:
            if char in hashset:
                hashset.discard(char)
            else:
                hashset.add(char)

        remove = len(hashset)

        if remove > 0:
            remove -= 1

        return len(s) - remove

# def main():
#     s = Solution()
#     string = 'Aa'
#     print(s.longestPalindrome(string))
#
#     string = 'abccccdd'
#     print(s.longestPalindrome(string))
#     string = 'NTrQdQGgwtxqRTSBOitAXUkwGLgUHtQOmYMwZlUxqZysKpZxRoehgirdMUgy'
#     print(s.longestPalindrome(string) )
#
#
# if __name__ == '__main__':
#     main()
