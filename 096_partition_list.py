'''
Given a linked list and a value x,
partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example
Given 1->4->3->2->5->2->null and x = 3,
return 1->2->2->4->3->5->null.
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
    @param: head: The first node of linked list
    @param: x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        # 1->4->3->2->5->2-> None
        # D1->1->2->2
        # D2->4->3->5
        if not head:
            return head

        left_dummy = ListNode(0)
        right_dummy = ListNode(0)
        left, right = left_dummy, right_dummy

        curr = head
        while curr:
            if curr.val < x:
                left.next = curr
                left = left.next
            else:
                right.next = curr
                right = right.next
            curr = curr.next

        # D1->1->2->2
        # D2->4->3->5
        right.next = None
        left.next = right_dummy.next
        return left_dummy.next


# def main():
#     '''
#     Given 1->4->3->2->5->2->null and x = 3,
#     return 1->2->2->4->3->5->null.
#     '''
#     head = ListNode(1)
#     head.insert(4)
#     head.insert(3)
#     head.insert(2)
#     head.insert(5)
#     head.insert(2)
#     head.print_all()
#     s = Solution()
#     x = 3
#     new_head = s.partition(head, x)
#     new_head.print_all()
#
#
# if __name__ == '__main__':
#     main()
