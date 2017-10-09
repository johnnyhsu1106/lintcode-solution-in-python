'''
Implement a stack by two queues. The queue is first in first out (FIFO).
That means you can not directly pop the last element in a queue.
push(1)
pop()
push(2)
isEmpty() // return false
top() // return 2
pop()
isEmpty() // return true
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)


class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def push(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            node = Node(val)
            self.tail.next = node
            self.tail = node

        self.size += 1

    def pop(self):
        if not self.isEmpty():
            node = self.head
            self.head = self.head.next
            self.size -= 1
            return node.val

    def top(self):
        return self.head.val

    def isEmpty(self):
        return self.size == 0



# class Stack:
#     def __init__(self):
#         self.queue1 = Queue()
#         self.queue2 = Queue()
#         self.size = 0
#
#
#     def push(self, x):
#
#         self.queue1.push(x)
#         self.size += 1
#
#
#     def pop(self):
#         while self.queue1.size != 1:
#             self.queue2.push(self.queue1.pop())
#
#         self.queue1.pop()
#         self.queue1, self.queue2 = self.queue2, self.queue1
#
#
#     def top(self):
#
#
#
#     def isEmpty(self):
#         return self.size == 0
#
#
# def main():
#     stack = Stack()
#
#     stack.push(1)
#     stack.push(2)
#     stack.push(3)
#     print(stack.top() == 3)
#     print(stack.pop() == 3)
#     print(stack.top() == 2)
#     print(stack.pop() == 2)
#
#
#
#
#
# if __name__ == '__main__':
#     main()
