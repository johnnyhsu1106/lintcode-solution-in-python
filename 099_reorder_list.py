'''
Given a singly linked list L: L0 → L1 → … → Ln-1 → Ln

reorder it to: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

Have you met this question in a real interview? Yes
Example
Given 1->2->3->4->null, reorder it to 1->4->2->3->null.

Challenge
Can you do this in-place without altering the nodes' values?
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
    @param: head: The head of linked list.
    @return: nothing
    """
    def reorderList(self, head):
        if head is None or head.next is None:
            return head

        middle = self.find_middle(head)
        tail = self.reverse_list(middle.next)
        middle.next = None

        self.merge_two_lists(head, tail)



    def find_middle(self, head):
        #  use slow and fast pointer
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


    def reverse_list(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev


    def merge_two_lists(self, head1, head2):
        dummy = ListNode(0)
        head = dummy
        index = 0
        while head1 and head2:
            if index % 2 == 0:
                head.next = head1
                head1 = head1.next
            else:
                head.next = head2
                head2 = head2.next

            head = head.next
            index += 1

        if head1:
            head.next = head1
        if head2:
            head.next = head2

# def main():
#     s = Solution()
#     head = ListNode(1)
#     head.next = ListNode(2)
#     head.next.next = ListNode(3)
#     head.next.next.next = ListNode(4)
#     head.print_all()
#
#     s.reorderList(head)
#     head.print_all()
#
# if __name__ == '__main__':
#     main()
