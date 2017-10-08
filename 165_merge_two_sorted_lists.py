'''
Merge two sorted (ascending) linked lists and
return it as a new sorted list.
The new sorted list should be made by splicing together
the nodes of the two lists and sorted in ascending order.

Example
Given 1->3->8->11->15->null, 2->null , return 1->2->3->8->11->15->null.
'''

# Definition of ListNode
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def print_all(self):
        result = ''
        curr = self
        while curr:
            result += str(curr.val) + '->'
            curr = curr.next
        print(result)

    def insert(self, val):
        prev = None
        curr = self
        while curr:
            prev = curr
            curr = curr.next
        prev.next = ListNode(val)


class Solution:
    """
    @param: l1: ListNode l1 is the head of the linked list
    @param: l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):

        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1:
            curr.next = l1
        else:
            curr.next = l2

        return dummy.next


# def main():
#     s = Solution()
#     l1 = ListNode(1)
#     l1.insert(4)
#
#
#     l2 = ListNode(2)
#     l2.insert(3)
#
#     head = s.mergeTwoLists(l1, l2)
#     head.print_all()
#
# if __name__ == '__main__':
#     main()
