'''
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node
to any node in the tree along the parent-child connections.

The longest consecutive path need to be from parent to child (cannot be the reverse).

Example
For example,

   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.

   2
    \
     3
    /
   2
  /
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    @param: root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):

        return self.helper(root, None, 0)



    def helper(self, root, parent, length_without_root):
        if not root:
            return 0

        length = length_without_root + 1 if parent and parent.val + 1 == root.val else 1
        left_length = self.helper(root.left, root, length)
        right_length = self.helper(root.right, root,length)

        return max(length, left_length, right_length)



# def main():
#     s = Solution()
#     root = TreeNode(1)
#     root.right = TreeNode(3)
#     root.right.left = TreeNode(2)
#     root.right.right = TreeNode(4)
#     root.right.right.right = TreeNode(5)
#
#     print(s.longestConsecutive(root))
#
# if __name__ == '__main__':
#     main()
