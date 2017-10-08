'''
Given an integer array with no duplicates.
A max tree building on this array is defined as follow:

The root is the maximum number in the array
The left subtree and right subtree are the max trees of the subarray divided by the root number.
Construct the max tree by the given array.

Example
Given [2, 5, 6, 0, 3, 1], the max tree constructed by this array is:

    6
   / \
  5   3
 /   / \
2   0   1
Challenge
O(n) time and memory.

'''

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    def maxTree(self, nums):
        stack = []
        for num in nums:
            node = TreeNode(num)
            if stack and num > stack[-1].val:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)

        return stack[0]



    def maxTree_dfs(self, A):
        # notice
        # Time: worst case O(n^2). best case: O(nlogn)....
        # Can not pass the lintcode test. exceed time limit
        if not A or len(A) == 0:
            return

        return self.maxTree_dfs(A, 0 , len(A))


    def maxTree_dfs_helper(self, A, left, right):
        if left >= right:
            return

        max_value, max_idx = float('-inf'), None
        for i in range(left, right):
            if A[i] >= max_value:
                max_value = A[i]
                max_idx = i

        root = TreeNode(max_value)

        left_node = self.maxTree_dfs_helper(A, left, max_idx)
        right_node = self.maxTree_dfs_helper(A, max_idx + 1, right)

        root.left = left_node
        root.right = right_node
        return root



def main():
    s = Solution()
    A = [2, 5, 6, 0, 3, 1]
    root = s.maxTree(A)


if __name__ == '__main__':
    main()
