'''
Given a linked list, determine if it has a cycle in it.

Example
Given -21->10->4->5, tail connects to node index 1, return true

Challenge
Follow up:
Can you solve it without using extra space?
'''

# Definition of ListNode
class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    """
    @param: head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        if not head or not head.next:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True

        return False


    def hasCycle_set(self, head):
        if not head:
            return False

        visited = set()
        curr_node = head
        while curr_node:
            if curr_node not in visited:
                visited.add(curr_node)
            else:
                return True
            curr_node = curr_node.next
            
        return False
