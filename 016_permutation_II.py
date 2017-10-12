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

        result = []
        permutation = []
        # visited = [False for i in range(len(nums))]
        visited = set()
        nums.sort()

        self.dfs(nums, visited, permutation, result)

        return result

    def dfs(self, nums, visited, permutation, result):
        # base case
        if len(permutation) == len(nums):
            result.append([] + permutation)
            return

        for i in range(len(nums)):
            if  i not in visited:
                if i == 0 or nums[i] != nums[i - 1] or i - 1 in visited:
                    permutation.append(nums[i])
                    visited.add(i)
                    self.dfs(nums, visited, permutation, result)
                    visited.discard(i)
                    permutation.pop()


# def main():
#     s = Solution()
#     nums = [3, 3, 0, 3]
#     print(s.permuteUnique(nums))
#
# if __name__ == '__main__':
#     main()
