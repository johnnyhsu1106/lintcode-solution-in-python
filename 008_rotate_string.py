'''
Given a string and an offset, rotate string by offset. (rotate from left to right)

Example
Given "abcdefg".

offset=0 => "abcdefg"
offset=1 => "gabcdef"
offset=2 => "fgabcde"
offset=3 => "efgabcd"
Challenge
Rotate in-place with O(1) extra memory.
'''


class Solution:
    """
    @param: str: An array of char
    @param: offset: An integer
    @return: nothing
    """
    '''
    idea:
    if offest != 0, rotate the first part of list of string, and second part of list of string.
    Then, rotate whole list of string

    offset=0 => "abcdefg"  -> do nothing
    offset=1 => "gabcdef"  -> 'fedcba' + 'g' -> 'gabcdef'
    offset=2 => "fgabcde"  -> 'edcba' + 'gf'  -> 'fgabcde'
    offset=3 => "efgabcd"  -> 'dcba' + 'gfe' -> 'efgabcd'
    ....
    it will repeat after 7 times, which is len(string)
    '''
    def rotateString(self, lst, offset):

        size = len(lst)
        if size <= 1 or offset == 0:
            return

        offset = offset % size
        self.swap(lst, size - offset, size - 1)
        self.swap(lst, 0, size - 1 - offset)
        self.swap(lst, 0, size - 1)


    def swap(self, lst, i, j):
        while i < j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1



    def rotateString(self, lst, offset):
        if len(lst) <=1 or offset == 0:
            return

        offset = offset % len(lst)

        for i in range(offset):
            lst.insert(0, lst.pop())
