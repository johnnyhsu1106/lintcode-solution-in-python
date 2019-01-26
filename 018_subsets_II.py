'''
Given a list of numbers that may has duplicate numbers, return all possible subsets

 Notice

Each element in a subset must be in non-descending order.
The ordering between two subsets is free.
The solution set must not contain duplicate subsets.

Example
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
Challenge
Can you do it in both recursively and iteratively?

'''
class Solution:
    """
    @param: nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        if nums is None:
            return []

        if len(nums) == 0:
            return [[]]

        results = []
        nums.sort()
        start_index = 0
        subset = []

        self._dfs(nums, start_index, subset, results)

        return results


    def _dfs(self, nums, start_index, subset, results):
        results.append(subset.copy()) #deep copy

        for i in range(start_index, len(nums)):
            if i == start_index or nums[i] != nums[i - 1]:
                subset.append(nums[i])
                self.dfs(nums, i + 1, subset, results)
                subset.pop()


# def main():
#     s = Solution()
#     # print(s.subsets_1([1,2,3]))
#     print(s.subsetsWithDup([1, 2, 2]))
#
# if __name__ == '__main__':
#     main()
