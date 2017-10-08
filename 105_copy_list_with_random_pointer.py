'''
A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.

Return a deep copy of the list.

Example
Challenge
Could you solve it with O(1) space?
'''
# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList_1(self, head):
        '''
        please see the problme 137 clone graph.
        use the hash map/ dict to mapping the node: new node
        Space: O(n)
        input:  1->2->3->4
        mapping = {1: 1', 2: 2', 3: 3', 4: 4'}
        output: 1'->2'->3'->4'

        '''
        if not head:
            return None
        #  mapping the node to new node
        mapping = {}
        curr = head
        while curr:
            mapping[curr] = RandomListNode(curr.label)
            curr = curr.next

        #  copy the next and ramdon pointer
        for node in mapping:
            if node.next:
                mapping[node].next = mapping[node.next]
            if node.random:
                mapping[node].random = mapping[node.random]

        return mapping[head]



    def copyRandomList_2(self, head):
        '''
        idea: space O(1)
        input: 1->2->3->4
        store: 1->1'->2->2'->3->3'->4->4'
        output: 1'->2'->3'->4'
        '''

        if not head:
            return None

        self.copy_next(head)
        self.copy_random(head)
        new_head = self.split_list(head)
        return new_head


    def copy_next(self, head):
        # Copy node:
        # input: 1->2->3->4
        # new_nodes: 1->1'->2->2'->3->3'->4->4'

        old_curr = head
        while old_curr:
            new_curr = RandomListNode(old_curr.label)
            new_curr.random = old_curr.random
            new_curr.next = old_curr.next #store the cld current next
            old_curr.next = new_curr
            old_curr = old_curr.next.next


    def copy_random(self, head):
        curr = head
        while curr:
            if curr.next.random:
                curr.next.random = curr.random.next
            curr = curr.next.next


    def split_list(self, head):
        # 1->1'->2->2'->3->3'->4->4'
        # => 1->2->3->4
        # => 1'->2'->3'->4'
        new_head = head.next
        old_curr = head
        while old_curr:
            new_curr = old_curr.next
            old_curr.next = old_curr.next.next
            if new_curr.next:
                new_curr.next = new_curr.next.next
                old_curr = old_curr.next
            else:
                break
        return new_head
