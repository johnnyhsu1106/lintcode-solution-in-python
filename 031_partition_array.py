'''
Given an array nums of integers and an int k,
partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

 Notice

You should do really partition in array nums
instead of just counting the numbers of integers smaller than k.

If all elements in nums are smaller than k, then return nums.length

Example
If nums = [3,2,2,1] and k=2, a valid answer is 1.

Challenge
Can you partition the array in-place and in O(n)?
'''
class Solution:
    """
    @param: nums: The integer array you should partition
    @param: k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        if not nums or len(nums) == 0:
            return 0

        left, right = 0, len(nums) - 1
        
        while left < right:
            while left < right and nums[left] < k:
                left += 1
            while left < right and nums[right] >= k:
                right -= 1

            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if nums[left] < k:
            return left + 1
        return left



# def main():
#     s = Solution()
#     nums = [3, 2, 2, 1]
#     k = 2
#     print(s.partitionArray(nums, k))
#     print(nums)
#
#     nums = [7,7,9,8,6,6,8,7,9,8,6,6]
#     k = 10
#     print(s.partitionArray(nums, k))
#     print(nums)
#
# if __name__ == '__main__':
#     main()
