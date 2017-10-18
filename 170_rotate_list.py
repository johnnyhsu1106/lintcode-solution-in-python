'''
Given a list, rotate the list to the right by k places, where k is non-negative.

Example
Given 1->2->3->4->5 and k = 2, return 4->5->1->2->3.
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
            result += str(curr) + '->'
            curr = curr.next

        result += 'null'
        print(result)

class Solution:
    def rotateRight(self, head, k):
        if head is None or k < 0:
            return head

        size = self.list_size(head)
        k = k % size
        if k == 0:
            return head

        node_k_prev = self.get_kth_node(head, size - k)
        node_k = node_k_prev.next
        tail = self.get_kth_node(head, size)
        # connect the lists
        tail.next = head
        node_k_prev.next = None

        return node_k


    def get_kth_node(self, head, k):
        curr = head
        for i in  range(1, k):
            curr = curr.next
        return curr


    def list_size(self, head):
        size= 0
        curr = head
        while curr:
            size+= 1
            curr = curr.next

        return size



# def main():
#     s = Solution()
#     head = ListNode(1)
#     head.next = ListNode(2)
#     head.next.next = ListNode(3)
#     head.next.next.next = ListNode(4)
#     head.next.next.next.next = ListNode(5)
#     new_head = s.rotateRight(head, 5)
#     new_head.print_all()
#
#
# if __name__ == '__main__':
#     main()
