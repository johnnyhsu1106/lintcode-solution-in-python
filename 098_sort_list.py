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

        middle_node = self.find_middle(head)
        right_list = self.sortList(middle_node.next)
        middle_node.next = None # disconnect the right_list and left_list
        left_list = self.sortList(head)

        return self.merge(left_list, right_list)


    def find_middle(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


    def merge(self, head1, head2):
        dummy = ListNode(0)
        curr_node = dummy
        curr_node_1, curr_node_2 = head1, head2

        while curr_node_1 and curr_node_2:

            if curr_node_1.val < curr_node_2.val:
                curr_node.next = curr_node_1
                curr_node_1 = curr_node_1.next
            else:
                curr_node.next = curr_node_2
                curr_node_2 = curr_node_2.next

            curr_node = curr_node.next

        if curr_node_1:
            curr_node.next = curr_node_1
        else:
            curr_node.next = curr_node_2

        return dummy.next
