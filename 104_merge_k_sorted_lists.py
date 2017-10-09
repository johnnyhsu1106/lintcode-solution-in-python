'''
Merge k sorted linked lists and return it as one sorted list.

Analyze and describe its complexity.


Example
Given lists:

[
  2->4->null,
  null,
  -1->null
],
return -1->2->4->null.
'''

class ListNode:

    def __init__(self, val = None):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)

    def print_all(self):
        result = ''
        node = self
        while node:
            result += node.__repr__() + '->'
            node = node.next
        print(result)



from heapq import heappush, heappop
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists_1(self, lists):
        if not lists or len(lists) == 0:
            return
        # min Heap
        min_heap = []
        for node in lists:
            if node:
                heappush(min_heap, (node.val, node))

        dummy = ListNode(0)
        tail = dummy

        while min_heap:
            val, node = heappop(min_heap)
            if node.next:
                heappush(min_heap, (node.next.val, node.next))
            tail.next = node
            tail = tail.next

        return dummy.next



    # def mergeKLists_2(self, lists):
    #     # Divide andn Conquer
    #     if not lists or len(lists) == 0:
    #         return
    #     return merge_helper(self, lists, 0, len(lists) -1)
    #
    #
    # def merge_helper(self, lists,  start, end):
    #     # like merge sort... divide and conquer
    #     




# def main():
#     s = Solution()
#     node1 = ListNode(2)
#     node1.next = ListNode(4)
#     node2 = None
#     node3 = ListNode(-1)
#     heap = []
#
#     lists = [node1, node2, node3]
#     node = s.mergeKLists(lists)
#     node.print_all()
#
#
# if __name__ == '__main__':
#     main()
