'''
Implement an algorithm to delete a node in the middle of a singly linked list,
given only access to that node.

Have you met this question in a real interview? Yes
Example
Linked list is 1->2->3->4, and given node 3, delete the node in place 1->2->4
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
    """
    @param: node: the node in the list should be deleted
    @return: nothing
    """
    def deleteNode(self, node):
        if node is None or node.next is None:
            return

        node.val = node.next.val
        node.next = node.next.next




# def main():
#     s = Solution()
#     head = ListNode(1)
#     head.next = ListNode(2)
#     head.next.next = ListNode(3)
#     head.next.next.next = ListNode(4)
#     head.next.next.next.next = ListNode(5)
#
#     head.print_all()
#     node = head.next.next
#     s.deleteNode(node)
#     head.print_all()
#
# if __name__ == '__main__':
#     main()
