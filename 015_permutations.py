'''
Given a list of numbers, return all possible permutations.

You can assume that there is no duplicate numbers in the list.

Example
For nums = [1,2,3], the permutations are:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        if nums is None:
            return []

        if len(nums) == 0:
            return [[]]

        results = []
        visited_index = set()
        permutation = []

        self.dfs(nums, visited_index, permutation, results)

        return results


    def dfs(self, nums, visited_index, permutation, results):
        if len(permutation) == len(nums):
            results.append(permutation.copy())
            return

        for i in range(len(nums)):
            if i not in visited_index:
                permutation.append(nums[i])
                visited_index.add(i)
                self.dfs(nums, visited_index, permutation, results)
                permutation.pop()
                visited_index.discard(i)

#
# def main():
#     s = Solution()
#     nums = [1, 2, 3]
#     print(s.permute(nums))
#
# if __name__ == '__main__':
#     main()
