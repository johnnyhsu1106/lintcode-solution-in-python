'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example
Given binary tree A = {3,9,20,#,#,15,7}, B = {3,#,20,15,7}

A)  3            B)    3
   / \                  \
  9  20                 20
    /  \                / \
   15   7              15  7
The binary tree A is a height-balanced binary tree, but B is not.
'''

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        balance, height = self.validtate(root)
        return balance

    def validtate(self, node):
        '''
        return a tuple, (boolean: balance, int: height)
        '''
        if not node:
            return True, 0

        left_balance, left_height = self.validtate(node.left)
        right_balance, right_height = self.validtate(node.right)

        if not left_balance or not right_balance:
            return False, max(left_height, right_height) + 1
            # reutrn False, 0     .... is fine, we don't care the depth any more.
            # once one subtree is not balance..... it will return Fasle from each subtree node

        return abs(left_height - right_height) <= 1, max(left_height, right_height) + 1


# def main():
#     '''
#     A)  3            B)    3
#        / \                  \
#       9  20                 20
#         /  \                / \
#        15   7              15  7
#     '''
#     root= TreeNode(3)
#     root.right = TreeNode(20)
#     root.right.left = TreeNode(15)
#     root.right.right = TreeNode(7)
#
#     s = Solution()
#     print(s.isBalanced(root))
#
#     root.left = TreeNode(9)
#     print(s.isBalanced(root))
#
# if __name__ == '__main__':
#     main()
