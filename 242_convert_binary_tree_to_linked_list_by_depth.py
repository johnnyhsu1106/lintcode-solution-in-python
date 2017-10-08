'''
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

Have you met this question in a real interview? Yes
Example
Given binary tree:

    1
   / \
  2   3
 /
4
return

[
  1->null,
  2->3->null,
  4->null
]
'''

# Definition of TreeNode:

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

        
from collections import deque
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        if not root:
            return []

        result = []
        queue = deque()
        queue.append(root)
        last_node = None

        while queue:
            size = len(queue)
            dummy = ListNode(0)
            head = dummy
            for i in range(size):
                node = queue.popleft()
                head.next = ListNode(node.val)
                head = head.next

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(dummy.next)

        return result
