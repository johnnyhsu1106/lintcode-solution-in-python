'''
Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

 Notice

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with maximum average.


Example
Given a binary tree:

     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2
return the node 11.
'''


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param: root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def __init__(self):
        self.max_avg = float('-inf')
        self.subtree = None

    def findSubtree2(self, root):
        self.subtree_avg(root)
        return self.subtree

    def subtree_avg(self, node):
        if not node:
            return 0, 0

        left_sum, left_size = self.subtree_avg(node.left)
        right_sum, right_size = self.subtree_avg(node.right)
        total_sum = left_sum + right_sum + node.val
        total_size = left_size + right_size + 1
        avg = total_sum / total_size

        # keep track of the node with the maximum average during recurssion
        if avg >= self.max_avg:
            self.max_avg = avg
            self.subtree = node

        return total_sum, total_size
