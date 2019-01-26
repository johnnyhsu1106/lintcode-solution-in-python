'''
Given a set of distinct integers, return all possible subsets.
Notice

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.

Example
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
class Solution:

    """
    @param: nums: A set of numbers
    @return: A list of lists
    """
    def subsets_1(self, nums):

        nums.sort()
        results = [[]]
        for i in range(len(nums)):
            size = len(results)
            for j in range(size):
                results.append(list(results[j]))
                results[-1].append(nums[i])
        return results


    def subsets_2(self, nums):
        '''
        idea:
        divide and conquer
        '''
        return self.subsetsRecu([], sorted(nums))

    def subsetsRecu(self, curr_result, nums):
        if not nums:
            return [curr_result]

        return self.subsetsRecu(curr_result, nums[1:]) + self.subsetsRecu(curr_result+ [nums[0]], nums[1:])


    def subsets_3(self, nums):
        '''
        idea: DFS
        '''
        if nums is None:
            return []

        if len(nums) == 0:
            return [[]]

        results = []
        nums.sort() # Elements in a subset must be in non-descending order.
        start_index = 0
        subset = []

        self._dfs(nums, start_index, subset, results)
        
        return results


    def _dfs(self, nums, start_index, subset, results):
        # append new object with []
        results.append(subset.copy())

        for i in range(start_index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, results)
            subset.pop()

# def main():
#     s = Solution()
#     # print(s.subsets_1([1,2,3]))
#     print(s.subsets_3([1, 2, 3]))
#
# if __name__ == '__main__':
#     main()
