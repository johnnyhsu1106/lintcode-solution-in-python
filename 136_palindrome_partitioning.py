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
        if not s:
            return []

        start_index = 0
        partition = []
        results = []

        self._dfs_partition(s, start_index, partition, results)

        return results


    def _dfs_partition(self, s, start_index, partitions, results):
        if start_index == len(s) :
            results.append(partitions.copy())
            return

        for i in range(start_index, len(s)):
            substring = s[start_index : i + 1]

            if self._is_palindrome(substring):
                partitions.append(substring)
                self._dfs_partition(s, i + 1, partitions, results)
                partitions.pop()


    def _is_palindrome(self, string):
        if not string:
            return True

        i, j = 0, len(string) - 1

        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1

        return True

# def main():
#     s = Solution()
#     string = 'aab'
#     print(s.partition(string))
#
#
# if __name__ == '__main__':
#     main()
