'''
Convert a binary search tree to doubly linked list with in-order traversal.

Have you met this question in a real interview? Yes
Example
Given a binary search tree:

    4
   / \
  2   5
 / \
1   3
return 1<->2<->3<->4<->5
'''

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
# Definition of Doubly-ListNode
class DoublyListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = next

    def __repr__(self):
        return str(self.val)

    def print_all(self):
        result = ''
        node = self
        while node.next:
            result += node.__repr__() + '->'
            node = node.next
        result += node.__repr__()
        print(result)


class Solution:
    """
    @param: root: The root of tree
    @return: the head of doubly list node
    """
    def bstToDoublyList_1(self, root):
        '''
        idea:
        DFS for in order traversal and store all vaues in the values(List)

        Create doubly linked list from all values.
        '''
        values = []
        self.dfs(root, values)
        if len(values) == 0:
            return None

        head = None
        prev = None
        for value in values:
            curr = DoublyListNode(value)
            if not head:
                head = curr
            else:
                prev.next = curr
            curr.prev = prev
            prev = curr # move the pointer
        return head


    def dfs(self, root, values):
        if not root:
            return
        self.dfs(root.left, values)
        values.append(root.val)
        self.dfs(root.right, values)


    def bstToDoublyList_2(self, root):
        '''
        idea:
        divide and conquer
        '''
        if not root:
            return None

        head, tail = self.helper(root)
        return head

    def helper(self, root):
        if not root:
            return None, None

        left_head, left_tail = self.helper(root.left)
        right_head, right_tail = self.helper(root.right)

        node = DoublyListNode(root.val)

        if not left_head and not left_tail:
            head = node
        else:
            head = left_head
            left_tail.next = node
            node.prev = left_tail

        if not right_head and not right_tail:
            tail = node
        else:
            tail = right_tail
            right_head.prev = node
            node.next = right_head

        return head, tail

# def main():
#     '''
#     Given a binary search tree:
#
#         4
#        / \
#       2   5
#      / \
#     1   3
#     return 1<->2<->3<->4<->5
#     '''
#     root = TreeNode(4)
#     root.left = TreeNode(2)
#     root.right = TreeNode(5)
#     root.left.left = TreeNode(1)
#     root.left.right = TreeNode(3)
#
#     s = Solution()
#     linked_lst_1 = s.bstToDoublyList_1(root)
#     linked_lst_1.print_all()
#
#     linked_lst_2 = s.bstToDoublyList_2(root)
#     linked_lst_2.print_all()
#
# if __name__ == '__main__':
#     main()
