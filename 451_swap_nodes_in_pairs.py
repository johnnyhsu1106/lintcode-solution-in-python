'''
Given a linked list, swap every two adjacent nodes and return its head.

Example
Given 1->2->3->4, you should return the list as 2->1->4->3.

Challenge
Your algorithm should use only constant space.
You may not modify the values in the list, only nodes itself can be changed.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

    def print_all(self):
        result = ''
        curr = self
        while curr:
            result += str(curr.val) + '->'
            curr = curr.next
        result += 'null'
        print(result)


class Solution:
    """
    @param: head: a ListNode
    @return: a ListNode
    """
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next and curr.next.next:
            # D -> [n1 -> n2] -> n3 -> n4 -> .....
            # D -> [n2 -> n1] -> n3 -> n4 -> .....
            n1 = curr.next
            n2 = n1.next
            n3 = n2.next

            curr.next = n2
            n2.next = n1
            n1.next = n3

            curr = n1

        return dummy.next


# def main():
#     s = Solution()
#     head = ListNode(1)
#     head.next = ListNode(2)
#     head.next.next = ListNode(3)
#     head.next.next.next = ListNode(4)
#     head.print_all()
#     s.swapPairs(head).print_all()
#
# if __name__ == '__main__':
#     main()
