'''
Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2.
Please note that your returned answers (both index1 and index2) are not zero-based.

 Notice

You may assume that each input would have exactly one solution.

Have you met this question in a real interview? Yes
Example
Given nums = [2, 7, 11, 15], target = 9
return [1, 2]
'''
class Solution:
    """
    @param: nums: an array of Integer
    @param: target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        start, end = 0, len(nums) - 1

        while start < end:
            if nums[start] + nums[end] < target:
                start += 1
            elif nums[start] + nums[end] > target:
                end -= 1
            else:
                return [start + 1, end + 1]
