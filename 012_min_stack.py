'''
Implement a stack with min() function, which will return the smallest number in the stack.

It should support push, pop and min operation all in O(1) cost.

 Notice

min operation will never be called if there is no number in the stack.

Have you met this question in a real interview? Yes
Example
push(1)
pop()   // return 1
push(2)
push(3)
min()   // return 2
push(1)
min()   // return 1

'''
class MinStack:
    """
    @param: a: An integer
    """
    '''
    idea:
    In order to store all status of min value, no matter push() or pop() method is called.
    If use only one variable to store the min value,
    once pop() is called and the min value is popped out.
    We can not know the previous min value.
    That's why we choose to use stack to store all min values.
    '''
    def __init__(self):
        # use the list(treat list as stack) to implement stack.
        # stack.pop() is equal to list.pop()
        # stack.push() is equal to list.append()
        self.items = []
        self.min_stack = [] # use the stack to store all min values.


    def push(self, number):
        self.items.append(number)

        if len(self.min_stack) == 0:
            self.min_stack.append(number)
        else:
            self.min_stack.append(min(self.min_stack[-1], number))


    def pop(self):
        if len(self.items) == 0:
            return None

        self.min_stack.pop()
        return self.items.pop()


    def min(self):
        return self.min_stack[-1]


# def main():
#     min_stack = MinStack()
#     min_stack.push(1)
#     print(min_stack.pop() == 1)
#     min_stack.push(2)
#     min_stack.push(3)
#     print(min_stack.min() == 2)
#     min_stack.push(1)
#     print(min_stack.pop() == 1)
#     print(min_stack.min() == 2)
#
#
# if __name__ == '__main__':
#     main()
