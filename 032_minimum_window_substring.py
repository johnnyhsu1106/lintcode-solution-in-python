'''
Given a string S and a string T,
find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows,
you are guaranteed that there will always be only one unique minimum window in S.
'''
from collections import defaultdict
class Solution:
    """
    @param: source : A string
    @param: target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source, target):
        # create a hashmap/dictionary for target, {key: value = char: count}
        s_char_count = defaultdict(int)
        t_char_count = defaultdict(int)

        for char in target:
            t_char_count[char] += 1

        j = 0
        min_substr = ''
        min_length = len(source) + 1

        for i in range(len(source)):
            while j < len(source) and not self._is_contain(s_char_count, t_char_count):
                s_char_count[source[j]] += 1
                j += 1

            if self._is_contain(s_char_count, t_char_count):
                if min_length > j - i:
                    min_length = j - i
                    min_substr = source[i:j]

            s_char_count[source[i]] -= 1

        return min_substr



    def _is_contain(self, s_char_count, t_char_count):
        # the condition in if statate can be like above because use the defaultdict, the default value of each key is 0 (defaultdict(int))
        #char not in s_char_count or s_char_count[char] < t_char_count[char]:
        for char in t_char_count:
            if s_char_count[char] < t_char_count[char]: 
                return False

        return True
