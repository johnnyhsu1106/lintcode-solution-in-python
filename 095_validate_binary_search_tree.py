'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
A single node tree is a BST

Example
An example:

  2
 / \
1   4
   / \
  3   5
The above binary tree is serialized as {2,1,4,#,#,3,5} (in level order).
'''

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST_1(self, root):
        # Divide and Conquer
        minimum = float('-inf')
        maximum = float('inf')

        return self.helper(root, minimum, maximum)

    def helper(self, root, minimum, maximum):
        if not root:
            return True

        is_left_validated = self.helper(node.left, minimum, node.val)
        is_right_validated = self.helper(node.right, node.val, maximum)
        is_validated = node.val > minimum and node.val < maximum

        return is_left_validated and is_right_validated and is_validated
#
# def main():
#     root = TreeNode(-1)
#     s = Solution()
#     print(s.isValidBST(root))
#
# if __name__ == '__main__':
#     main()
