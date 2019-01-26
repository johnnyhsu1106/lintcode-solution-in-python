'''
Given a list of numbers with duplicate number in it. Find all unique permutations.

Example
For numbers [1,2,2] the unique permutations are:

[
  [1,2,2],
  [2,1,2],
  [2,2,1]
]
'''
class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        if nums is None:
            return []

        if len(nums) == 0:
            return [[]]

        results = []
        permutation = []
        visited_index = set()
        nums.sort()

        self.dfs(nums, visited_index, permutation, results)

        return results

    def dfs(self, nums, visited_index, permutation, results):
        if len(permutation) == len(nums):
            results.append(permutation.copy())
            return

        for i in range(len(nums)):
            if  i not in visited_index:
                if i == 0 or nums[i] != nums[i - 1] or i - 1 in visited_index:
                    permutation.append(nums[i])
                    visited_index.add(i)
                    self.dfs(nums, visited_index, permutation, results)
                    permutation.pop()
                    visited_index.discard(i)



# def main():
#     s = Solution()
#     nums = [3, 3, 0, 3]
#     print(s.permuteUnique(nums))
#
# if __name__ == '__main__':
#     main()
