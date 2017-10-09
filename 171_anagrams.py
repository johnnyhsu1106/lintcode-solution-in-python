'''
Given an array of strings, return all groups of strings that are anagrams.

 Notice

All inputs will be in lower-case

Have you met this question in a real interview? Yes
Example
Given ["lint", "intl", "inlt", "code"], return ["lint", "inlt", "intl"].

Given ["ab", "ba", "cd", "dc", "e"], return ["ab", "ba", "cd", "dc"].

Challenge
What is Anagram?
- Two strings are anagram if they can be the same after change the order of characters.
'''
from collections import defaultdict
class Solution:
    """
    @param: strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        hashmap = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            hashmap[sorted_word].append(word)

        result = []
        for sorted_word in hashmap:
            if len(hashmap[sorted_word]) >= 2:
                result.extend(hashmap[sorted_word])

        return result

# def main():
#     s = Solution()
#     strs = ["lint", "intl", "inlt", "code"]
#     print(s.anagrams(strs))
#     strs = ["ab", "ba", "cd", "dc", "e"]
#     print(s.anagrams(strs))
#
#
# if __name__ == '__main__':
#     main()
