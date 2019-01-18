'''
Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

Notice

Have you consider that the string might be empty?
This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

Example
"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Challenge
O(n) time without extra memory.
'''

class Solution:
    """
    @param: s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        if s.strip() == '':
            return True


        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalpha() and not s[left].isdigit():
                left += 1
            while left < right and not s[right].isalpha() and not s[right].isdigit():
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


# def main():
#     s = Solution()
#     string = '1a2'
#     print(s.isPalindrome(string))
#
# if __name__ == '__main__':
#     main()
