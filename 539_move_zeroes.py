class Solution:
    """
    @param: nums: an integer array
    @return:
    """
    def moveZeroes_1(self, nums):
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
        #
        index = 0
        right = 0

        while right < len(nums):
            if nums[right] != 0:
                nums[right], nums[index] = nums[index], nums[right]
                index += 1

            right += 1

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
