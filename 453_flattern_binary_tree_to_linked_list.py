'''
Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the right pointer in TreeNode as the next pointer in ListNode.

 Notice

Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.

Have you met this question in a real interview? Yes
Example
              1
               \
     1          2
    / \          \
   2   5    =>    3
  / \   \          \
 3   4   6          4
                     \
                      5
                       \
                        6
Challenge
Do it in-place without any extra memory.
'''

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self):
        return str(self.val)

    def print_all_right(self):
        node = self
        result = ''
        while node.right:
            result += node.__repr__() + '->'
            node = node.right
        result += node.__repr__()
        print(result)



class Solution:
    """
    @param: root: a TreeNode, the root of the binary tree
    @return:
    """
    def flatten_1(self, root):
        '''
        idea:
        Use DFS to post-order travese the node and get list... cost extra space O(n)
        Then use while loop to traverse all values in the list, reset the left child and right child
        Time: O(n) + O(n) = O(2n) = O(n)

        '''
        if not root:
            return None

        values = []
        self.dfs(root, values)
        i = 1
        while i < len(values):
            root.left = None
            root.right = TreeNode(values[i])
            root = root.right
            i += 1

    def dfs(self, root, values):
        if not root:
            return
        values.append(root.val)
        self.dfs(root.left, values)
        self.dfs(root.right, values)



    def flatten_2(self, root):
        '''
        idea:
        Divide and Conquer
        '''

        if not root:
            return None

        self.divide_and_conquer(root)

    def divide_and_conquer(self, root):
        '''
        idea:
        divide and conquer
        Time: O(n)
        Space: O(1)
        '''
        if not root:
            return None

        left_tail = self.divide_and_conquer(root.left)
        right_tail = self.divide_and_conquer(root.right)

        if left_tail:
            left_tail.right = root.right
            root.right = root.left
            root.left = None

        if right_tail:
            return right_tail

        if left_tail:
            return left_tail

        return root



# def main():
#     '''
#     Example
#                   1
#                    \
#          1          2
#         / \          \
#        2   5    =>    3
#       / \   \          \
#      3   4   6          4
#                          \
#                           5
#                            \
#                             6
#     '''
#     s = Solution()
#
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(5)
#     root.left.left = TreeNode(3)
#     root.left.right = TreeNode(4)
#     root.right.right = TreeNode(6)
#
#     s.flatten_1(root)
#     root.print_all_right()
#
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(5)
#     root.left.left = TreeNode(3)
#     root.left.right = TreeNode(4)
#     root.right.right = TreeNode(6)
#
#     s.flatten_2(root)
#     root.print_all_right()
#
#
# if __name__ == '__main__':
#     main()
