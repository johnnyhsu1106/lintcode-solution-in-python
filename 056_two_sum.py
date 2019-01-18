'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers
such that they add up to the target, where index1 must be less than index2.
Notice

You may assume that each input would have exactly one solution

Example
numbers=[2, 7, 11, 15], target=9

return [1, 2]

Challenge
Either of the following solutions are acceptable:

O(n) Space, O(nlogn) Time
O(n) Space, O(n) Time
'''

from collections import defaultdict

class Solution:
    """
    @param: numbers: An array of Integer
    @param: target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum_1(self, numbers, target):
        # O(n) Space, O(n) Time
        # hash set
        visited_nums = {}
        for i in range(len(numbers)):
            num = numbers[i]
            if target - num not in visited_nums:
                visited_nums[num] = i
            else:
                return [visited_nums[target - num], i]



    def twoSum_2(self, numbers, target):

        # O(n) Space, O(nlogn) Time ....Terrible Idea!!!!!
        #  Use two pointers... however, still need to use the hash map to store index before sorting.

        if not nums or len(nums) <= 1:
            return []

        size = len(nums)

        mapping = defaultdict(list)
        for i in range(size):
            mapping[nums[i]].append(i)

        nums.sort()

        left, right = 0, size - 1
        result = []

        while left < right:
            total = nums[left] + nums[right]

            if total > target:
                right -= 1

            elif total < target:
                left += 1

            else:
                value1 = nums[left]
                value2 = nums[right]
                if value1 == value2:
                    result = mapping[value1]
                else:
                    result = mapping[value1] + mapping[value2]
                break


        return sorted(result)
# def main():
#     s = Solution()
#     nums = [2, 7, 11,  15]
#     target = 9
#     print(s.twoSum_2(nums, target))
#
#     nums = [0, 4, 3, 0]
#     target = 0
#     print(s.twoSum_2(nums, target))
#
#
# if __name__ == '__main__':
#     main()
