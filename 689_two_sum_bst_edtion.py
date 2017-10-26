'''
Given a binary search tree and a number n,
find two numbers in the tree that sums up to n.

Notice

Without any extra space.


Example
Given a binary search tree:

    4
   / \
  2   5
 / \
1   3
and a number n = 3
return [1, 2] or [2, 1]
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
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        # extra space: O(n)
        if root is None:
            return []

        nums = self.in_order_traverse(root)
        start, end = 0, len(nums) - 1

        while start < end:
            if nums[start] + nums[end] == n:
                return [nums[start], nums[end]]
            elif nums[start] + nums[end] > n:
                end -= 1
            else:
                start += 1

    def in_order_traverse(self, root):
        if root is None:
            return []

        left = self.in_order_traverse(root.left)
        right = self.in_order_traverse(root.right)

        return left + [root.val] + right



# def main():
#     s = Solution()
#
#     root = TreeNode(4)
#     root.left = TreeNode(2)
#     root.right = TreeNode(5)
#     root.left.left = TreeNode(1)
#     root.left.right = TreeNode(3)
#
#     print(s.twoSum(root, 3))
#
# if __name__ == '__main__':
#     main()
