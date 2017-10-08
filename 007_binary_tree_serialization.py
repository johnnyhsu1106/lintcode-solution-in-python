'''
Design an algorithm and write code to serialize and deserialize a binary tree.
Writing the tree to a file is called 'serialization' and
reading back from the file to reconstruct the exact same binary tree is 'deserialization'.

Notice

There is no limit of how you deserialize or serialize a binary tree,
LintCode will take your output of serialize as the input of deserialize,
it won't check the result of serialize.

Example
An example of testdata: Binary tree {3,9,20,#,#,15,7}, denote the following structure:

  3
 / \
9  20
  /  \
 15   7
Our data serialization use bfs traversal. This is just for when you got wrong answer and want to debug the input.

You can use other method to do serializaiton and deserialization.
'''

from collections import deque

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        if not root:
            return '{}'

        data = []
        queue  = deque()
        queue.append(root)
        flag = True

        while queue and flag:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                # node maybe None...
                if node: #if node is not None
                    data.append(str(node.val))
                    if node.left:
                        next_level.append(node.left)
                    else:
                        next_level.append(None)

                    if node.right:
                        next_level.append(node.right)
                    else:
                        next_level.append(None)
                else:
                    data.append('#')

            for node in queue:
                flag = False
                if node is not None:
                    flag = True
                    break

        return '{' + ','.join(data) + '}'


    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    """
    def deserialize(self, data):
        if data == '{}':
            return None

        values = data[1:-1].split(',')

        root = TreeNode(int(values[0]))
        index = 0
        queue = [root]
        is_left_child = True

        for val in values[1:]:
            if val != '#':
                node = TreeNode(int(val))
                if is_left_child:
                    queue[index].left = node
                else:
                    queue[index].right = node

                queue.append(node)

            if not is_left_child:
                index += 1
            is_left_child = not is_left_child

        return root
