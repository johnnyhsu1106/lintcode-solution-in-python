'''
Given a binary tree, return all root-to-leaf paths.

Example
Given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

[
  "1->2->5",
  "1->3"
]
'''

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths_1(self, root):
        # Divide and Conquer
        paths = []
        # if root is None, return []
        if not root:
            return []
        # if root is leave, reterun [str(root.val)]
        if not root.left and not root.right:
            paths.append(str(root.val))
            return paths

        # Divide
        left_paths = self.binaryTreePaths(root.left)
        right_paths = self.binaryTreePaths(root.right)
        # Conquer (Merge)
        for path in left_paths:
            paths.append(str(root.val) + '->' + path)
        for path in right_paths:
            paths.append(str(root.val) + '->' + path)

        return paths



    def binaryTreePaths_2(self, root):
        # use dfs
        if not root:
            return []
        result = []
        path = []
        path.append(str(root.val))
        self.dfs(root, path, result)
        return result


    def dfs(self, root, path, result):
        if not root.left and not root.right:
            result.append(''.join(path))

        if root.left:
            path.append('->')
            path.append(str(root.left.val))
            self.dfs(root.left, path, result)
            path.pop()
            path.pop()

        if root.right:
            path.append('->')
            path.append(str(root.right.val))
            self.dfs(root.right, path, result)
            path.pop()
            path.pop()




# def main():
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(3)
#     root.left.right = TreeNode(5)
#
#     s = Solution()
#     print(s.binaryTreePaths_2(root))
#
#
# if __name__ == '__main__':
#     main()
