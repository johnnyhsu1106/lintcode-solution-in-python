'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.
Only constant memory is allowed.

Example
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''
class Solution:
    """
    @param: head: a ListNode
    @param: k: An integer
    @return: a ListNode
    """
    def reverseKGroup(self, head, k):
        # D->[1->2->3]->[4->5->6]->7 (k = 3)
        # D->[3->2->1]->[6->5->4]->7
        dummy = ListNode(0)
        dummy.next = head # connect dummy node to head D-> head -> .....

        prev_node = dummy
        while prev_node:
            prev_node = self.reverse_next_k_nodes (prev_node, k)

        return dummy.next # D-> head'


    def reverse_next_k_nodes(self, head, k):
        # head -> n1 -> n2 -> ... ->nk -> nk+1
        # head -> nk -> nk-1 -> ... ->n1 -> nk+1
        n1 = head.next
        nk = self.find_kth_node(head, k)
        if not nk:
            return None

        nk_plus_1 = nk.next

        # Reverse k nodes
        nk.next = None # separate the nk and nk+1
        nk = self.reverse(n1) # nk->nk-1->nk-2->......n1

        # Connect head and nk -> nk-1 -> ... ->n1,  n1 and nk+1 -> nk+2 ->...
        head.next = nk
        n1.next = nk_plus_1

        return n1


    def find_kth_node(self, head, k):
        # head -> n1 -> n2 -> ... ->nk
        curr_node = head

        for i in range(k):
            if not curr_node:
                return None

            curr_node = curr_node.next

        return curr_node


    def reverse(self, head):
        prev_node = None
        curr_node = head
        
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        return prev_node
