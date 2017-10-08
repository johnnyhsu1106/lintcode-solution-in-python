'''
Given a binary tree, return the preorder traversal of its nodes' values.

Example
Given:

    1
   / \
  2   3
 / \
4   5
return [1,2,4,5,3].

Challenge
Can you do it without recursion?
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal_1(self, root):
        result = []
        self.traverse(root, result)
        return result


    def traverse(self, node, result):
        if not node:
            return
        result.append(node.val)
        self.traverse(node.left, result)
        self.traverse(node.right, result)


    #Solution 2: Divide and Conquer

    def preorderTraversal(self, root):
        result = []
        if not root:
            return []

        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        return [root.val] + left + right
