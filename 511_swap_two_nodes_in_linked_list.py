'''
Given a linked list and two values v1 and v2.
Swap the two nodes in the linked list with values v1 and v2.
It's guaranteed there is no duplicate values in the linked list.
If v1 or v2 does not exist in the given linked list, do nothing.

Notice
You should swap the two nodes with values v1 and v2.
Do not directly swap the values of the two nodes.

Example
Given 1->2->3->4->null and v1 = 2, v2 = 4.

Return 1->4->3->2->null.
'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)


    def print_all(self):
        result = ''
        curr = self
        while curr:
            result += curr.__repr__() + '->'
            curr = curr.next
        result += 'null'
        print(result)


class Solution:
    """
    @param: head: a ListNode
    @param: v1: An integer
    @param: v2: An integer
    @return: a new head of singly-linked list
    """
    def swapNodes(self, head, v1, v2):
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev1, prev2 = self.find_prevs(dummy, v1, v2)

        if prev1 is None or prev2 is None:
            return head

        if prev1 == prev2:
            return head

        if prev1.next == prev2:
            self.swap_adjcent(prev1)
        elif prev2.next == prev1:
            self.swap_adjcent(prev2)
        else:
            self.swap_remote(prev1, prev2)

        return dummy.next



    def find_prevs(self, dummy, v1, v2):
        prev1, prev2 = None, None
        node = dummy

        while node.next:
            if node.next.val == v1:
                prev1 = node
            if node.next.val == v2:
                prev2 = node

            node = node.next

        return prev1, prev2


    def swap_adjcent(self, prev):
        node1 = prev.next
        node2 = node1.next
        node2_next = node2.next

        prev.next = node2
        node2.next = node1
        node1.next = node2_next

    def swap_remote(self, prev1, prev2):
        node1 = prev1.next
        node1_next = node1.next
        node2 = prev2.next
        node2_next = node2.next

        prev1.next = node2
        node2.next = node1_next
        prev2.next = node1
        node1.next = node2_next



# def main():
#     s = Solution()
#     head = ListNode(1)
#     head.next = ListNode(2)
#     head.next.next = ListNode(3)
#     head.next.next.next = ListNode(4)
#
#     s.swapNodes(head, 1, 1)
#     head.print_all()
#
#
# if __name__ == '__main__':
#     main()
