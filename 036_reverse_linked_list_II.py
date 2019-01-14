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
        dummy = ListNode(0)
        dummy.next = head

        # 1. Find the node m - 1
        node_m_prev = self._find_kth_node(dummy, m - 1)
        node_m = node_m_prev.next

        # 2. Find the node n and node n + 1
        node_n = self._find_kth_node(dummy, n)
        node_n_next = node_n.next

        # 3. Disconnect the node n and node_n_next
        node_n.next = None

        # 4. Reverse the link list from node m to node n
        node_n = self._reverse(node_m)

        # 5. Connect the reversed link list
        node_m_prev.next = node_n
        node_m.next = node_n_next

        return dummy.next


    def _find_kth_node(self, dummy, k):
        curr_node = dummy

        for i in range(k):
            curr_node = curr_node.next

        return curr_node
        

    def _reverse(self, head):
        prev_node = None
        curr_node = head

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node

            prev_node = curr_node
            curr_node = next_node

        return prev_node



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
