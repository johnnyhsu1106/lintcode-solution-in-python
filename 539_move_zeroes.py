"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example
Given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Notice
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

@param: nums: an integer array
@return:
"""

class Solution:
    def moveZeroes_1(self, nums):
        '''
        idea: find th non zero number and put it in th front in order and assign zero for rest
        '''
        if not nums or len(nums) ==0:
            return

        # two pointers:
        # assign the non-zero number in the nums, starting from the beginning of nums
        # assign 0 to from start to end of nums
        index = 0 # the index from 0
        start = 0 # pointer, which is pointed to non-zero

        while index < len(nums) and start < len(nums):
            # find the nums is not equal to 0
            while start < len(nums) and nums[start] == 0:
                start += 1

            if start < len(nums):
                nums[index] = nums[start]
                index += 1
                start += 1

        while index < len(nums):
            nums[index] = 0
            index += 1


    def moveZeroes_2(self, nums):
        '''
        idea: find th non-zero number and swap to the front in order
        '''
        if not nums or len(nums) == 0:
            return

        index = 0 # the index
        start = 0 # the poiter, which will point to non zero number

        while start < len(nums):
            if nums[start] != 0:
                nums[start], nums[index] = nums[index], nums[start]
                index += 1

            start += 1


#
# def main():
#     s = Solution()
#     nums = [0, 0, 0]
#     s.moveZeroes_1(nums)
#     print(nums)
#
#     nums = [1, 2, 3]
#     s.moveZeroes_1(nums)
#     print(nums)
#
#     nums = [1, 0, 2, 0, 3]
#     s.moveZeroes_1(nums)
#     print(nums)
#
#     nums = [1, 2, 3, 0, 0]
#     s.moveZeroes_1(nums)
#     print(nums)
#
#     nums = [0, 0, 1, 2, 3]
#     s.moveZeroes_1(nums)
#     print(nums)
#
#
# if __name__ == '__main__':
#     main()
