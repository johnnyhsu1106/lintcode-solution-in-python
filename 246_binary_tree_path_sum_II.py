'''
Your are given a binary tree in which each node contains a value.
Design an algorithm to get all paths which sum to a given value.
The path does not need to start or end at the root or a leaf,
but it must go in a straight line down.

Have you met this question in a real interview? Yes
Example
Given a binary tree:

    1
   / \
  2   3
 /   /
4   2
for target = 6, return

[
  [2, 4],
  [1, 3, 2]
'''


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
    def binaryTreePathSum2(self, root, target):
        if not root:
            return []

        result = []
        path = []
        self.dfs(root, path, 0, target, result)

        return result



    def dfs(self, root, path, level, target , result):
        if not root:
            return

        path.append(root.val)
        temp = target

        # BSF
        for i in range(level, -1, -1):
            temp -= path[i]
            if temp == 0:
                result.append(path[i:])

        self.dfs(root.left, path, level + 1, target, result)
        self.dfs(root.right, path, level + 1, target, result)

        path.pop()


# def main():
#     s = Solution()
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(3)
#     # root.left.left = TreeNode(4)
#     # root.right.left = TreeNode(2)
#
#     print(s.binaryTreePathSum2(root, 3))
#
# if __name__ == '__main__':
#     main()
