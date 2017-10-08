'''
Given a binary tree, find all paths that sum of the nodes
in the path equals to a given number target.

A valid path is from root node to any of the leaf nodes.

Example
Given a binary tree, and target = 5:

     1
    / \
   2   4
  / \
 2   3
return

[
  [1, 2, 2],
  [1, 4]
]
'''


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        result = []
        path = []
        if not root:
            return result

        path.append(root.val)
        self.dfs(root, path, target - root.val, result)

        return result

    def dfs(self, root, path, remain, result):

        if not root.left and not root.right:
            if remain == 0:
                result.append(path + [])

        # go to left
        if root.left:
            path.append(root.left.val)
            self.dfs(root.left, path, remain - root.left.val, result)
            path.pop()

        # go to right
        if root.right:
            path.append(root.right.val) # add the path
            self.dfs(root.right, path, remain - root.right.val, result)
            path.pop() # remove from path, back tracking


# def main():
#     s = Solution()
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(4)
#     root.left.left = TreeNode(2)
#     root.left.right = TreeNode(3)
#     target = 5
#     print(s.binaryTreePathSum(root, target))
#
#
# if __name__ == '__main__':
#     main()
