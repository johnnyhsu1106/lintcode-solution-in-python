'''
Given a sorted (increasing order) array,
Convert it to create a binary tree with minimal height.

 Notice

There may exist multiple valid solutions, return any of them.

Have you met this question in a real interview? Yes
Example
Given [1,2,3,4,5,6,7], return

     4
   /   \
  2     6
 / \    / \
1   3  5   7
'''
class Solution:
    """
    @param: A: an integer array
    @return: A tree node
    """
    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        root = self.helper(nums, 0, len(nums) -1)
        return root


    def helper(self, nums, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(nums[start])

        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums, start, mid - 1)
        root.right = self.helper(nums, mid + 1, end)

        return root
            
