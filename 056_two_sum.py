'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers
such that they add up to the target, where index1 must be less than index2.
Please note that your returned answers (both index1 and index2) are NOT zero-based.

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
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum_1(self, numbers, target):
        # O(n) Space, O(n) Time
        # hash set
        visited_nums = dict()
        for i in range(len(numbers)):
            num = numbers[i]
            if target - num not in visited_nums:
                visited_nums[num] = i
            else:
                return [visited_nums[target - num] + 1, i + 1]



    def twoSum_2(self, numbers, target):

        # O(n) Space, O(nlogn) Time ....Terrible Idea!!!!!
        #  Use two pointers... however, still need to use the hash map to store index before sorting.

        mapping = defaultdict(list)
        for i, num in enumerate(numbers):
            mapping[num].append(i + 1)

        numbers.sort()
        start, end = 0, len(numbers) - 1

        while start < end:
            num = numbers[start] + numbers[end]
            if num > target:
                end -= 1
            elif num < target:
                start += 1
            else:
                pair = [numbers[start], numbers[end]]
                break

        result = []
        for num in pair:
            result.append(mapping[num].pop())

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
