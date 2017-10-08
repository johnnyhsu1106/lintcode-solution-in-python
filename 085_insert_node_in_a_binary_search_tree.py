'''
Given a binary search tree and a new tree node,
insert the node into the tree. You should keep the tree still be a valid binary search tree.

Notice

You can assume there is no duplicate values in this tree + node.

Example
Given binary search tree as follow, after Insert node 6, the tree should be:

  2             2
 / \           / \
1   4   -->   1   4
   /             / \
  3             3   6
Challenge
Can you do it without recursion?s
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
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        '''
        idea:
        divide and conquer
        '''
        if not root:
            return node

        if node.val < root.val:
            root.left = self.insertNode(root.left, node)
        else:
            root.right = self.insertNode(root.right, node)
        return root


    def insertNode_1(self, root, node):
        '''
        idea: traverse recursively
        '''
        if not root:
            return node

        if node.val < root.val:
            if root.left:
                self.insertNode(root.left, node)
            else:
                root.left = node
        else:
            if root.right:
                self.insertNode(root.right, node)
            else:
                root.right = node

        return root
