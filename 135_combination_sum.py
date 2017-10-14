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
    def combinationSum(self, candidates, target):
        '''
        Please see the problem 017 and 153
        '''
        if candidates is None:
            return []

        result = []
        candidates.sort()
        combination = []

        self.dfs(candidates, 0, combination, target, result)
        return result


    def dfs(self, candidates, start_index, combination, remain_target, result):
        #  base case (stoppig condition)
        if remain_target == 0:
            result.append(list(combination))
            return

        for i in range(start_index, len(candidates)):
            if candidates[i] > remain_target:
                break
            if i == 0 or candidates[i] != candidates[i - 1]:
                combination.append(candidates[i])
                self.dfs(candidates, i, combination, remain_target - candidates[i], result)
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
