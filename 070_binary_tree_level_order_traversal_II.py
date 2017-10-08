'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

Have you met this question in a real interview? Yes
Example
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7


return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]
'''
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from collections import deque
class Solution:
    """
    @param: root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        '''
        idea:
        Please see the problem 69
        The whole concept is the same as the problem 069.
        Then only difference is to reverse the list in the end.
        '''
        result = []
        if not root:
            return result
        #  Initialize, Use Queue
        queue = deque()
        queue.append(root)
        while queue:
            curr_level =[]
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(curr_level)
        # reverse the result
        result.reverse()
        return result
