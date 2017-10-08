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

        visited = set()
        result = []
        permutation = []
        self.dfs(nums, visited, permutation, result)

        return result


    def dfs(self, nums, visited, permutation, result):

        if len(permutation) == len(nums):
            result.append([] + permutation)
            return

        for num in nums:
            if num not in visited:
                permutation.append(num)
                visited.add(num)
                self.dfs(nums, visited, permutation, result)
                permutation.pop()
                visited.discard(num)


# def main():
#     s = Solution()
#     nums = [1, 2, 3]
#     print(s.permute(nums))
#
# if __name__ == '__main__':
#     main()
