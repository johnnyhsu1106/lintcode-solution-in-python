"""
Given an array of integers, find how many pairs in the array
such that their sum is less than or equal to a specific target number.
Please return the number of pairs.

Example
Given nums = [2, 7, 11, 15], target = 24.
Return 5.
2 + 7 < 24
2 + 11 < 24
2 + 15 < 24
7 + 11 < 24
7 + 15 < 25
"""
class Solution:
    """
    @param: nums: an array of integer
    @param: target: an integer
    @return: an integer
    """
    def twoSum5_1(self, nums, target):
        '''
        Time: O(n^2)
        Space: O(1)
        '''
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] <= target:
                    count += 1
        return count


    def twoSum5_2(self, nums, target):
        '''
        idea: two pointer, left and right .
        First sort the nums
        '''
        if not nums or len(nums) < 2:
            return 0

        count = 0
        left , right = 0, len(nums) - 1
        nums.sort()

        while left < right:
            if nums[right] + nums[left] > target:
                right -= 1
            else:
                count += right - left
                left += 1
        return count


# def main():
#     s = Solution()
#     print(s.twoSum5_1([2, 7, 11, 15], 24))
#     print(s.twoSum5_2([2, 7, 11, 15], 24))
#
# if __name__ == '__main__':
#     main()
