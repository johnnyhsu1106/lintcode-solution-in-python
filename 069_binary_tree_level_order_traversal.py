'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

Have you met this question in a real interview? Yes
Example
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7


return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
Challenge
Challenge 1: Using only 1 queue to implement it.
Challenge 2: Use DFS algorithm to do it.
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
    @param: root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        '''
        idea: BFS(Breadth First Search)
        '''
        results = []

        # edge case
        if not root:
            return []

        queue = deque() # use deque to implement queue. Method: popleft(), pop(), appendleft(), append()
        queue.append(root) # initial the queue

        while queue:
            current_level = []
            size = len(queue) # store a current size of queue

            for i in range(size):
                node = queue.popleft()
                current_level.append(node.val)
                # append the next level of nodes into queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            results.append(current_level)

        return results
