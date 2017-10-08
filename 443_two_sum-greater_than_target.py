'''
Two Sum - Greater than target

Given an array of integers,
find how many pairs in the array such that their sum is bigger than a specific target number.
Please return the number of pairs.

Example
Given numbers = [2, 7, 11, 15], target = 24. Return 1. (11 + 15 is the only pair)
'''
class Solution:
    """
    @param: nums: an array of integer
    @param: target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # use two pointer (please see the problem 382 triangle count as well.)
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:

            if nums[left] + nums[right] > target:
                count += right - left
                right -= 1


            elif nums[left] + nums[right] <= target:
                left += 1

        return count


# def main():
#     s = Solution()
#     nums = [2, 7, 11, 15]
#     target = 24
#     print(s.twoSum2(nums, target))
#
#     nums = [2, 7, 11, 11, 15]
#     target = 24
#     print(s.twoSum2(nums, target))
#
#     nums = [2, 7, 11, 15, 15]
#     target = 24
#     print(s.twoSum2(nums, target))
#
# if __name__ == '__main__':
#     main()
