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
        # do intialization if necessary
        self.stack1 = [] # old stack (keep older element)
        self.stack2 = [] # new stack


    def push(self, element):
        self.stack2.append(element)


    def pop(self):

        if len(self.stack1) == 0:
            while len(self.stack2) != 0:
                self.stack1.append(self.stack2.pop())

        return self.stack1.pop()


    def top(self):
        if len(self.stack1) == 0:
            while len(self.stack2) != 0:
                self.stack1.append(self.stack2.pop())

        if len(self.stack1) != 0:
            return self.stack1[-1]

        return None



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
