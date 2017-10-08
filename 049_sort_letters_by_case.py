'''
Given a string which contains only letters. Sort it by lower case first and upper case second.

Notice

It's NOT necessary to keep the original order of lower-case letters and upper case letters.

Example
For "abAcD", a reasonable answer is "acbAD"

Challenge
Do it in one-pass and in-place.
'''

class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars):
        if not chars or len(chars) == 0:
            return

        left, right = 0, len(chars) - 1
        while left < right:
            while left < right and chars[left].islower():
                left += 1
            while left < right and chars[right].isupper():
                right -= 1
            if left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        
