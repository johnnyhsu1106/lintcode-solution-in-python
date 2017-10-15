'''
Given an array nums containing n + 1 integers
where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist.
Assume that there is only one duplicate number, find the duplicate one.

Notice

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n^2).
There is only one duplicate number in the array, but it could be repeated more than once.
Example
Given nums = [5,5,4,3,2,1] return 5
Given nums = [5,4,4,3,2,1] return 4
'''
class Solution:
    """
    @param: nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate_1(self, nums):
        if nums is None or len(nums) == 1:
            return -1

        start, end = 1, max(nums)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.count_nums_less_than_target(nums, mid) <= mid:
                start = mid
            else:
                end = mid

        if self.count_nums_less_than_target(nums, start) <= start:
            return end
        return start

    def count_nums_less_than_target(self, nums, target):
        total = 0
        for num in nums:
            if num <= target:
                total += 1
        return total


    def findDuplicate_2(self, nums):
        if nums is None or len(nums) == 1:
            return -1
        # sort the nums, Time: O(nlogn)
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]


# def main():
#     s = Solution()
#     nums = [5,4,4,3,2,1]
#     print(s.findDuplicate_1(nums))
#     nums = [1,5,4,3,2,1]
#     print(s.findDuplicate_1(nums))
#
#
# if __name__ == '__main__':
#     main()
