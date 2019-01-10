'''
Given a binary tree, return the inorder traversal of its nodes' values.

Have you met this question in a real interview? Yes
Example
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3

return [1,3,2].

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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal_1(self, root):
        # recursion
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, node, result):
        if not node:
            return

        self.traverse(node.left, result)」」
        result.append(node.val)
        self.traverse(node.right, result)




    def inorderTraversal_2(self, root):
        # divide and conquer
        result = []
        if not root:
            return []

        left = self.inorderTraversal_2(root.left)
        right = self.inorderTraversal_2(root.right)
        result.extend(left)
        result.append(root.val)
        result.extend(right)
        return result
