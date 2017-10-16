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
        if not head:
            return head

        tail = self.get_tail(head)
        node = head.next
        head.next = tail
        if tail:
            tail.next = node

        self.reorderList(node)



    def get_tail(self, head):
        curr = head
        while curr.next:
            curr = curr.next
        tail = curr
        return

def main():
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.print_all()

    s.reorderList(head)
    head.print_all()




if __name__ == '__main__':
    main()
