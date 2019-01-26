'''
As the title described, you should only use two stacks to implement a queue's actions.

The queue should support push(element), pop() and top()
where pop is pop the first(a.k.a front) element in the queue.

Both pop and top methods should return the value of first element.


Example
push(1)
pop()     // return 1
push(2)
push(3)
top()     // return 2
pop()     // return 2
Challenge
implement it by two stacks, do not use any other data structure and
push, pop and top should be O(1) by AVERAGE.
'''

class MyQueue:
    def __init__(self):
        self.pop_stack = [] # a stack for the poping element
        self.push_stack = [] # a stack for pushing element

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        self.push_stack.append(element)

    """
    @return: An integer
    """
    def pop(self):
        if len(self.pop_stack) == 0:
            while len(self.push_stack) != 0:
                self.pop_stack.append(self.push_stack.pop())

        if len(self.pop_stack) != 0:
            return self.pop_stack.pop()
        return
    """
    @return: An integer
    """
    def top(self):
        if len(self.pop_stack) == 0:
            while len(self.push_stack) != 0:
                self.pop_stack.append(self.push_stack.pop())

        if len(self.pop_stack) != 0:
            return self.pop_stack[-1]
        return


#
# def main():
#     queue = MyQueue()
#     queue.push(1)
#     print(queue.pop() == 1)
#     queue.push(2)
#     queue.push(3)
#     print(queue.top() == 2)
#     print(queue.pop() == 2)
#
#
# if __name__ == '__main__':
#     main()
