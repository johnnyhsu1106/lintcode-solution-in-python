'''
Given a linked list, return the node where the cycle begins.

If there is no cycle, return null.

Example
Given -21->10->4->5, tail connects to node index 1，return 10
'''


# Definition of ListNode
class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    """
    @param: head: The first node of linked list.
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        if not head:
            return None

        slow = head
        fast = head.next

        while fast and fast.next:
            if slow is fast:
                break
            slow = slow.next
            fast = fast.next.next

        if slow is fast:
            slow = head
            while show is not fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None
