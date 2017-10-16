'''
You have two numbers represented by a linked list,
where each node contains a single digit.
The digits are stored in reverse order,
such that the 1's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.

Example
Given 7->1->6 + 5->9->2. That is, 617 + 295.

Return 2->1->9. That is 912.

Given 3->1->5 and 5->9->2, return 8->0->8.
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
    @param: l1: the first list
    @param: l2: the second list
    @return: the sum list of l1 and l2
    """
    def addLists(self, l1, l2):
        if l1 is None and l2 is None:
            return None

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        dummy =  ListNode(0)
        curr = dummy
        carry = 0

        while l1 and l2:
            total = l1.val + l2.val + carry
            digit = total % 10
            carry = total // 10
            curr.next = ListNode(digit)
            l1 = l1.next
            l2 = l2.next
            curr = curr.next

        while l1:
            total = l1.val + carry
            digit = total % 10
            carry = total // 10
            curr.next = ListNode(digit)
            carry = digit // 10
            l1 = l1.next
            curr = curr.next

        while l2:
            total = l2.val + carry
            digit = total % 10
            carry = digit // 10
            curr.next = ListNode(digit)
            l2 = l2.next
            curr = curr.next

        if carry != 0:
            curr.next = ListNode(carry)

        return dummy.next



# def main():
#     s = Solution()
#     l1 = ListNode(7)
#     l1.next = ListNode(1)
#     l1.next.next = ListNode(6)
#     l2 = ListNode(5)
#     l2.next = ListNode(9)
#     l2.next.next = ListNode(2)
#
#     l = s.addLists(l1, l2)
#     l.print_all()
#
#
# if __name__ == '__main__':
#     main()
