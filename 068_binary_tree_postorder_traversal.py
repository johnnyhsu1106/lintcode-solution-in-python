'''
Given a binary tree, return the postorder traversal of its nodes' values.

Have you met this question in a real interview? Yes
Example
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3


return [3,2,1].

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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal_1(self, root):
        '''
        idea: traverse recursively
        '''
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, node, result):
        if not node:
            return
        self.traverse(node.left, result)
        self.traverse(node.right, result)
        result.append(node.val)


    def postorderTraversal(self, root):
        '''
        idea: divide and conquer
        '''
        result = []
        if not root:
            return []

        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)

        return left + right + [root.val]
