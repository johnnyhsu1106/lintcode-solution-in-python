'''
Given a string s and a set of n substrings.
You are supposed to remove every instance of those n substrings from s
so that s is of the minimum length and output this minimum length.

Example
Given s = ccdaabcdbb, substrs = ["ab", "cd"]
Return 2

Explanation:
ccdaabcdbb -> ccdacdbb -> cabb -> cb (length = 2)
'''

from collections import deque
class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, string, dictionary):
        if len(string) == 0 or len(dictionary) == 0:
            return -1

        queue = deque([string])
        visited = set([string])
        min_length = len(string)
        while queue:
            string = queue.popleft()

            for sub in dictionary:
                found_idx = string.find(sub)

                while found_idx != -1:
                    new_string = string[:found_idx] + string[found_idx + len(sub):]
                    if new_string not in visited:
                        queue.append(new_string)
                        visited.add(new_string)
                        min_length = min(len(new_string), min_length)

                    found_idx = string.find(sub, found_idx + 1)

        return min_length



# def main():
#     s = Solution()
#     string = 'ccdaabcdbb'
#     dictionary = ["ab", "cd"]
#     print(s.minLength(string, dictionary))
#
#
# if __name__ == '__main__':
#     main()
