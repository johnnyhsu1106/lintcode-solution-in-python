'''
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Notice

You don't need to implement the remove method.

Example
Given the list [[1,1],2,[1,1]], By calling next repeatedly
until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Given the list [1,[4,[6]]], By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,4,6].
'''

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""

class NestedIterator:

    def __init__(self, nestedList):
        #  nestedList, len
        self.stack = []
        self._push_list_to_stack(nestedList)


    def _push_list_to_stack(self, nestedList):
        temp_stack = []
        for ele in nestedList:
            temp_stack.append(ele)

        while temp_stack:
            self.stack.append(temp_stack.pop())


    def next(self):
        if self.hasNext():
            return self.stack.pop().getInteger()


    def hasNext(self):
        while self.stack and not self.stack[-1].isInteger():
            self._push_list_to_stack(self.stack.pop().getList)

        return len(self.stack) != 0
