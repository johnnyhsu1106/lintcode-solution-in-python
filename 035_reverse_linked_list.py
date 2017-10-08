'''
Reverse a linked list.

Example
For linked list 1->2->3, the reversed linked list is 3->2->1

Challenge
Reverse it in-place and in one-pass
'''
# Definition of ListNode

class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        prev_node = None
        curr_node = head
        while curr:
            next_node = curr_node.next
            curr_node.next = prev
            prev_node = curr_node
            curr_node = next_node
        return prev_node
