'''
Follow up Zigzag Iterator:
What if you are given k 1d vectors?
How well can your code be extended to such cases?
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases.
If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic".


Example
Given k = 3 1d vectors:

[1,2,3]
[4,5,6,7]
[8,9]
Return [1,4,8,2,5,9,3,6,7].
'''
from collections import deque
class ZigzagIterator2:
    # use Queue
    def __init__(self, vecs):
        # only put non-empty list into queue
        self.queue = deque([v for v in vecs if v])


    def next(self):
        if self.hasNext():

            vec = self.queue.popleft()
            value = vec.pop(0)
            if len(vec) != 0:
                self.queue.append(vec)

            return value


    def hasNext(self):
        return len(self.queue) != 0



# def main():
#     vecs = [[1,2,3],
#             [4,5,6,7],
#             [8,9]]
#
#     zig = ZigzagIterator2(vecs)
#     result = []
#     while zig.hasNext():
#         result.append(zig.next())
#
#     print(result)
#
#
#     vecs = [[],
#             [4,5,6,7],
#             [8,9]]
#
#     zig = ZigzagIterator2(vecs)
#     result = []
#     while zig.hasNext():
#         result.append(zig.next())
#
#     print(result)
#
#
# if __name__ == '__main__':
#     main()
