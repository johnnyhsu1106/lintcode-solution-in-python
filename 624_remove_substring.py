# '''
# Given a string s and a set of n substrings.
# You are supposed to remove every instance of those n substrings from s
# so that s is of the minimum length and output this minimum length.
#
# Have you met this question in a real interview? Yes
# Example
# Given s = ccdaabcdbb, substrs = ["ab", "cd"]
# Return 2
#
# Explanation:
# ccdaabcdbb -> ccdacdbb -> cabb -> cb (length = 2)
# '''
#
# from collections import deque
# class Solution:
#     """
#     @param: s: a string
#     @param: dict: a set of n substrings
#     @return: the minimum length
#     """
#     def minLength(self, s, dict):
#         # write your code here
#         for substring in dict:
#             s = self.remove_sub(s, substring)
#         return len(s)
#
#     def remove_sub(self, s, substring):
#         if len(s) == 0:
#             return
#
#         index = s.find(substring)
#         if index == -1:
#             return
#         s = s[0:index] + s[index + len(substring):]
#         return self.remove_sub(s, substring)
#
# def main():
