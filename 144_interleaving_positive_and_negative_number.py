'''
Given an array with positive and negative integers.
Re-range it to interleaving with positive and negative integers.

Notice

You are not necessary to keep the original order of positive integers or negative integers.

Have you met this question in a real interview? Yes
Example
Given [-1, -2, -3, 4, 5, 6], after re-range,
it will be [-1, 5, -2, 4, -3, 6] or any other reasonable answer.

'''

class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, nums):
        if not nums or len(nums) == 0:
            return

        self.partition(nums)
        self.interleave(nums)

        #check any continuous positive  number from beginning
        for i in range(0, len(nums) - 2):
            if nums[i] * nums[i + 1] > 0:
                nums[i + 1], nums[i + 2] = nums[i + 2], nums[i + 1]

        # check any continuous negitive number from beginning
        for i in range(len(nums) - 1, 1, -1):
            if nums[i] *  nums[i - 1] > 0:
                nums[i - 1], nums[i - 2] = nums[i - 2], nums[i - 1]


    def partition(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] < 0:
                left += 1
            while left < right and nums[right] > 0:
                right -= 1

            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1


    def interleave(self, nums):
        left, right = 0, len(nums) - 1
        is_swap = False

        while left < right:
            while left < right and nums[left] > 0:
                left += 1
            while left < right and nums[right] < 0:
                right -= 1

            if left < right and not is_swap:
                nums[left], nums[right] = nums[right], nums[left]

            is_swap = not is_swap
            left += 1
            right -= 1


# 
# def main():
#     s = Solution()
#
#     nums = [-1, -2, -3, 4, 5, 6, 7]
#     s.rerange(nums)
#     print(nums)
#
# if __name__ == '__main__':
#     main()
