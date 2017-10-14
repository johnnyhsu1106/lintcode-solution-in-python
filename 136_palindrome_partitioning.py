'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Have you met this question in a real interview? Yes
Example
Given s = "aab", return:

[
  ["aa","b"],
  ["a","a","b"]
]
'''

class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        result = []
        if len(s) == 0:
            return reuslt

        self.dfs_partition(s, 0, [], result)

        return result


    def dfs_partition(self, s, start_index, partitions, result):

        if start_index == len(s) :
            result.append(partitions.copy())
            return

        for i in range(start_index, len(s)):
            substring = s[start_index: i + 1]

            if self.is_palindrome(substring):
                partitions.append(substring)
                self.dfs_partition(s, i + 1, partitions, result)
                partitions.pop()


    def is_palindrome(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True


# def main():
#     s = Solution()
#     string = 'aab'
#     print(s.partition(string))
#
#
# if __name__ == '__main__':
#     main()
