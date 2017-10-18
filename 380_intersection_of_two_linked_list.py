'''
Write a program to find the node at which the intersection of two singly linked lists begins.

Notice

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.

Example
The following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.

Challenge
Your code should preferably run in O(n) time and use only O(1) memory.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    @param: headA: the first list
    @param: headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        size_A = self.get_list_size(headA)
        size_B = self.get_list_size(headB)
        curr_A, curr_B = headA, headB

        diff = abs(size_A - size_B)
        if size_A > size_B:
            for i in range(diff):
                curr_A = curr_A.next
        elif size_B > size_A:
            for i in range(diff):
                curr_B = curr_B.next

        while curr_A and curr_B and curr_A != curr_B:
            curr_A = curr_A.next
            curr_B = curr_B.next

        if curr_A is not None and curr_B is not None:
            return curr_A
        return None


    def get_list_size(self, head):
        size = 0
        curr = head
        while curr:
            curr = curr.next
            size += 1

        return size
