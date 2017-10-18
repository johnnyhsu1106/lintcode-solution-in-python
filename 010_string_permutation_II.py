'''
Given a string, find all permutations of it without duplicates.

Have you met this question in a real interview? Yes
Example
Given "abb", return ["abb", "bab", "bba"].

Given "aabb", return ["aabb", "abab", "baba", "bbaa", "abba", "baab"].
'''
class Solution:
    """
    @param: str: A string
    @return: all permutations
    """
    def stringPermutation2(self, string):
        if string is None:
            return []

        if len(string) == 0:
            return ['']

        result = []
        permutation = []
        visited = [False for i in range(len(string))]
        string = ''.join(sorted(string))
        self.dfs(string, visited, permutation, result)

        return result


    def dfs(self, string, visited, permutation, result):
        if len(permutation) == len(string):
            result.append(''.join(permutation))

        for i in range(len(string)):
            if not visited[i]:
                if i == 0 or string[i] != string[i - 1] or visited[i - 1]:
                    permutation.append(string[i])
                    visited[i] = True
                    self.dfs(string, visited, permutation, result)
                    visited[i] = False
                    permutation.pop()


# def main():
#     s = Solution()
#     string = 'aba'
#     print(s.stringPermutation2(string))
#
# if __name__ == '__main__':
#     main()
