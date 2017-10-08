'''
Reverse a linked list from position m to n.

 Notice

Given m, n satisfy the following condition: 1 ≤ m ≤ n ≤ length of list.

Have you met this question in a real interview? Yes
Example
Given 1->2->3->4->5->NULL, m = 2 and n = 4, return 1->4->3->2->5->NULL.
'''

# Definition of ListNode

class ListNode:

    def __init__(self, val, next= None):
        self.val = val
        self.next = next

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
    @param: head: ListNode head is the head of the linked list
    @param: m: An integer
    @param: n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # Given 1->2->3->4->5->NULL, m = 2 and n = 4, return 1->4->3->2->5->NULL.

        dummy = ListNode(0)
        dummy.next = head

        prev_m_node = self.find_kth(dummy, m - 1)
        m_node = prev_m_node.next
        n_node = self.find_kth(dummy, n)
        next_n_node = n_node.next #  store the all node after n_node

        n_node.next = None
        # 1->2->3->4->5->NULL
        # 1->2  4->3->2->NULL,
        # 5->NUL
        n_node = self.reverse(m_node)
        
        prev_m_node.next = n_node
        m_node.next = next_n_node

        return dummy.next


    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        new_head = prev
        return new_head


    def find_kth(self, dummy, k):
        curr = dummy
        for i in range(k):
            curr = curr.next
        kth_node = curr
        return kth_node



# def main():
#     s = Solution()
#     head = ListNode(1)
#     head.insert(2)
#     head.insert(3)
#     head.insert(4)
#     head.insert(5)
#     new_head = s.reverseBetween(head, 1, 4)
#     new_head.print_all()
# if __name__ == '__main__':
#     main()
