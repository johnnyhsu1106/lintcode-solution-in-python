'''
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.

Notice
LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with minimum sum
and the given binary tree is not an empty tree.

Example
Given a binary tree:

     1
   /   \
 -5     2
 / \   /  \
0   2 -4  -5
return the node 1.
'''

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self):
        return str(self.val)

class Solution:
    """
    @param: root: the root of binary tree
    @return: the root of the minimum subtree
    """
    # use class variable to store the value. All the instance of class share the class variables
    # or you can use __init__(self) to declare instance varible ....

    def __init__(self):
        self.subtree_sum_min = float('inf')
        self.subtree = None

    def findSubtree(self, root):
        self.subtree_sum(root)
        return self.subtree

    def subtree_sum(self, root):
        '''
        idea:
        divide and conquer
        '''
        if not root:
            return 0
        # divide
        left_sum = self.subtree_sum(root.left)
        right_sum = self.subtree_sum(root.right)
        # conquer
        total = left_sum + right_sum + root.val

        #
        if total <= self.subtree_sum_min:
            self.subtree_sum_min = total
            self.subtree = root

        return total


# def main():
#     '''
#     Given a binary tree:
#
#          1
#        /   \
#      -5     2
#      / \   /  \
#     0   2 -4  -5
#     return the node 1.
#     '''
#     root = TreeNode(1)
#     root.left = TreeNode(-5)
#     root.right = TreeNode(2)
#     root.left.left = TreeNode(0)
#     root.left.right = TreeNode(2)
#     root.right.left = TreeNode(-4)
#     root.right.left = TreeNode(-5)
#
#     s = Solution()
#     print(s.findSubtree(root))
#
#
# if __name__ == '__main__':
#     main()
