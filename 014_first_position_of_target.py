'''
For a given sorted array (ascending order) and a target number,
find the first index of this number in O(log n) time complexity.

If the target number does not exist in the array, return -1.

Example
If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.

Challenge
If the count of numbers is bigger than 2^32, can your code work properly?
'''

class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):

        if len(nums) == 0:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        return -1



# def main():
#     s = Solution()
#     nums = [1, 2, 3, 3, 4, 5, 10]
#     print(s.binarySearch([], 1) == -1)
#     print(s.binarySearch(nums, 0) == -1)
#     print(s.binarySearch(nums, 1) == 0)
#     print(s.binarySearch(nums, 3) == 2)
#     print(s.binarySearch(nums, 10) == 6)
#
# if __name__ == '__main__':
#     main()
