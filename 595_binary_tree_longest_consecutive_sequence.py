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
    def __init__(self):
        self.longest_path = 0

    def longestConsecutive(self, root):
        #  Traverse + Divide Conquer
        self.helper(root)
        return self.longest_path


    def helper(self, root):
        if not root:
            return 0

        left_path = self.helper(root.left)
        right_path = self.helper(root.right)

        subtree_path = 1

        if root.left and root.val + 1 == root.left.val:
            subtree_path = max(subtree_path, left_path + 1)
        if root.right and root.val + 1 == root.right.val:
            subtree_path = max(subtree_path, right_path + 1)

        self.longest_path = max(self.longest_path, subtree_path)

        return subtree_path




    def longestConsecutive_2(self, root):
        #  Traverse + Divide Conquer
        return self.helper_2(root, None, 0)


    def helper_2(self, node, parent, length_without_root):
        if not node:
            return 0

        length = length_without_root + 1 if parent and parent.val + 1 == node.val else 1
        left_length = self.helper_2(node.left, node, length)
        right_length = self.helper_2(node.right, node,length)

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
