'''
You have two numbers represented by a linked list,
where each node contains a single digit.
The digits are stored in forward order,
such that the 1's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.

Have you met this question in a real interview? Yes
Example
Given 6->1->7 + 2->9->5. That is, 617 + 295.

Return 9->1->2. That is, 912.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

    def print_all(self):
        output = ''
        curr = self

        while curr:
            output += str(curr) + '->'
            curr = curr.next

        output += 'null'
        print(output)


class Solution:
    """
    @param: l1: The first list.
    @param: l2: The second list.
    @return: the sum list of l1 and l2.
    """
    def addLists2(self, l1, l2):
        l1 = self.reverse_list(l1)
        l2 = self.reverse_list(l2)
        l = self.reverse_list(self.add_two_lists(l1, l2))

        return l


    def reverse_list(self, head):
        if head is None:
            return head

        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev


    def add_two_lists(self, head1, head2):
        if head1 is None and head2 is None:
            return None

        carry = 0
        dummy = ListNode(0)
        curr, curr1, curr2 = dummy, head1, head2

        while curr1 or curr2:
            if curr1:
                carry += curr1.val
                curr1 = curr1.next
            if curr2:
                carry += curr2.val
                curr2 = curr2.next

            curr.next = ListNode(carry % 10)
            carry = carry // 10
            curr = curr.next

        if carry > 0:
            curr.next = ListNode(carry)

        return dummy.next


# def main():
#     s = Solution()
#     l1 = ListNode(6)
#     l1.next = ListNode(1)
#     l1.next.next = ListNode(7)
#     l2 = ListNode(2)
#     l2.next = ListNode(9)
#     l2.next.next = ListNode(5)
#
#     l = s.addLists2(l1, l2)
#     l.print_all()
#
# if __name__ == '__main__':
#     main()
