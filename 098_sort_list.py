'''
Sort a linked list in O(n log n) time using constant space complexity.

Example
Given 1->3->2->null, sort it to 1->2->3->null.

Challenge
Solve it by merge sort & quick sort separately.

'''

# Definition of ListNode
class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    """
    @param: head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
        if not head or not head.next:
            return head

        middle = self.find_middle(head)
        right = self.sortList(middle.next)
        middle.next = None
        left = self.sortList(head)
        return self.merge(left, right)



    def find_middle(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


    def merge(self, head1, head2):
        dummy = ListNode(0)
        tail = dummy
        curr1, curr2 = head1, head2

        while curr1 and curr2:

            if curr1.val < curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next

            tail = tail.next

        if curr1:
            tail.next = curr1
        else:
            tail.next = curr2

        return dummy.next
