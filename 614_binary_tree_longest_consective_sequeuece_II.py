# '''
# Given a binary tree, find the length of the longest consecutive sequence path.
# The path could be start and end at any node in the tree
#
# Have you met this question in a real interview? Yes
# Example
#     1
#    / \
#   2   0
#  /
# 3
# Return 4 // 0-1-2-3
#
#
# '''
# class Solution:
#     """
#     @param: root: the root of binary tree
#     @return: the length of the longest consecutive sequence path
#     """
#     def longestConsecutive2(self, root):
#         return self.helper(root, None, 0)
#
#
#     def helper(self, node, parent, length):
#
#
