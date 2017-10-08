'''
Given a node from a cyclic linked list which has been sorted,
write a function to insert a value into the list such that it remains a cyclic sorted list.
The given node can be any single node in the list. Return the inserted new node.

Notice

3->5->1 is a cyclic list, so 3 is next node of 1.
3->5->1 is same with 5->1->3

Example
Given a list, and insert a value 4:
3->5->1
Return 5->1->3->4
'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def print_all(self):
        visited = set()
        curr = self
        result = ''

        while curr:
            if curr not in visited:
                result += str(curr.val) + '->'
                visited.add(curr)
            else:
                break
            curr = curr.next

        print(result)

class Solution:
    """
    @param: node: a list node in the list
    @param: x: An integer
    @return: the inserted new list node
    """
    def insert(self, node, x):
        if node is None:
            node = ListNode(x)
            node.next = node
            return node

        curr = node
        prev = None
        while True:
            prev = curr
            curr = curr.next
            # inseat new node between head and tail
            if prev.val <= x <= curr.val:
                break
            # insert new node between tail and head
            if (prev.val > curr.val) and (x < curr.val or x > prev.val):
                break
            #  node is the only one node
            if curr is node:
                break

        new_node = ListNode(x)
        new_node.next = curr
        prev.next = new_node
        return new_node

#
# def main():
#     node1 = ListNode(2)
#     node2 = ListNode(2)
#     node3 = ListNode(2)
#     node1.next = node2
#     node2.next = node3
#     node3.next = node1
#
#     s = Solution()
#     new_head = s.insert(node1, 3)
#     new_head.print_all()
#
#
# if __name__ == '__main__':
#     main()
