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
        results, subset = [], []
        if nums is None:
            return results
        nums.sort()
        self.dfs(nums, 0, subset, results)
        return results


    def dfs(self, nums, start_index, subset, results):
        results.append(list(subset))

        for i in range(start_index, len(nums)):
            if i == start_index or nums[i] != nums[i-1]:
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
