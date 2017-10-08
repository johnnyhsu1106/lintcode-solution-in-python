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

        prev = dummy
        while prev:
            prev = self.reverse_next_k_node(prev, k)

        return dummy.next # D-> head'

    def reverse_next_k_node(self, head, k):
        # head -> n1 -> n2 -> ... ->nk -> nk+1
        # head -> nk -> nk-1 -> ... ->n1 -> nk+1

        curr = head
        n1 = head.next
        # Find the nk
        for i  in range(k):
            curr = curr.next
            if curr is None:
                return None

        nk = curr
        nk_plus = curr.next

        # check the problem 035 (reverse_linked_list)
        # Reverse k nodes
        prev = head
        curr = n1
        while curr != nk_plus:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # head->n1 , nk->nk-1->nk-2->......n1 -> head
        head.next = nk # head -> nk
        n1.next = nk_plus # n1 -> nk+1
        # return n1
        return n1
