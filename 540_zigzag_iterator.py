'''
Given two 1d vectors, implement an iterator to return their elements alternately.


Example
Given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].
'''
from collections import deque
class ZigzagIterator1:
    # use Queue
    def __init__(self, v1, v2):
        # only put non-empty list into queue
        self.queue = deque([v for v in (v1, v2) if v])


    def next(self):
        v = self.queue.popleft()
        value = v.pop(0)
        if len(v) != 0:
            self.queue.append(v)

        return value


    def hasNext(self):
        return len(self.queue) != 0


class ZigzagIterator2:

    def __init__(self, v1, v2):
        # Use Two Pointer
        self.v1 = v1
        self.v2 = v2
        self.idx1 = 0
        self.idx2 = 0


    def next(self):
        if (self.hasNext()):
            if self.idx1 < len(self.v1) and self.idx2 < len(self.v2):
                if self.idx1 == self.idx2:
                    num = self.v1[self.idx1]
                    self.idx1 += 1
                else:
                    num = self.v2[self.idx2]
                    self.idx2 += 1

            else:
                if self.idx1 < len(self.v1):
                    num = self.v1[self.idx1]
                    self.idx1 += 1

                if self.idx2 < len(self.v2):
                    num = self.v2[self.idx2]
                    self.idx2 += 1

            return num


    def hasNext(self):
        return self.idx1 < len(self.v1) or self.idx2 < len(self.v2)



# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result


# def main():
#
#     v1 = [1, 2]
#     v2 = [3, 4, 5, 6]
#     zig = ZigzagIterator1(v1, v2)
#     result = []
#     while zig.hasNext():
#         result.append(zig.next())
#     print(result)
#
#     v1 = [1, 2]
#     v2 = [3, 4, 5, 6]
#     zig = ZigzagIterator2(v1, v2)
#     result = []
#     while zig.hasNext():
#         result.append(zig.next())
#     print(result)
#
# if __name__ == '__main__':
#     main()
