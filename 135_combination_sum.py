'''
Given a set of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Notice

All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.

Example
Given candidate set [2,3,6,7] and target 7, a solution set is:

[7]
[2, 2, 3]
'''
class Solution:
    """
    @param: candidates: A list of integers
    @param: target: An integer
    @return: A list of lists of integers
    """
    def combinationSum_1(self, candidates, target):
        '''
        Please see the problem 017 and 153
        '''
        '''
        idea: the candicate in candicates set might be duplicate so need to remove the duplicate
        '''
        if not candidates:
            return []

        candidates.sort()

        combination = []
        start_index = 0
        results = []

        self._dfs(candidates, start_index, combination, target, results)

        return results


    def _dfs(self, candidates, start_index, combination, remains, results):
        #  base case (stoppig condition)
        if remains == 0:
            results .append(combination.copy())
            return

        for i in range(start_index, len(candidates)):
            if candidates[i] > remains:
                break

            if i == 0 or candidates[i] != candidates[i - 1] or i == start_index: #avoid add the other duplicate number into combination
                combination.append(candidates[i])
                self._dfs(candidates, i, combination, remains - candidates[i], results)
                combination.pop()


    def combinationSum_2(self, candidates, target):
        '''
        Please see the problem 017 and 153
        '''
        if not candidates:
            return []

        results = []
        candicates = sorted(list(set(candidates)))
        combination = []
        start_index = 0

        self._dfs(candidates, 0, combination, target, results)

        return results


    def _dfs(self, candidates, start_index, combination, remains, results):
        #  base case (stoppig condition)
        if remains == 0:
            results .append(combination.copy())
            return

        for i in range(start_index, len(candidates)):
            if candidates[i] > remains:
                break

            combination.append(candidates[i])
            self._dfs(candidates, i, combination, remains - candidates[i], results)
            combination.pop()

# def main():
#     s = Solution()
#     candidates = [2, 2, 3, 6, 7]
#     target = 7
#     print(s.combinationSum(candidates, target))
#
#
# if __name__ == '__main__':
#     main()
