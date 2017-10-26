'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

Example
The brackets must close in the correct order, "()" and "()[]{}" are all valid
but "(]" and "([)]" are not.
'''

class Solution:
    """
    @param: s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        if len(s) <= 1:
            return False

        parentheses_map = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for char in s:
            if char in parentheses_map:
                stack.append(char)
            else:
                if len(stack) == 0 or parentheses_map[stack.pop()] != char:
                    return False

        return len(stack) == 0
