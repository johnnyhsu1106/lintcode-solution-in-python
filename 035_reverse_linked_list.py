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

        while curr_node:
            next_node = curr_node.next # store the curr_node.next to a vairable called next_node
            curr_node.next = prev_node
            prev_node = curr_node # move the pointer `prev_node` to next node
            curr_node = next_node # move the pointer 'curr_node' to next node

        return prev_node
