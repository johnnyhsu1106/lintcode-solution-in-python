'''
Given a list of integers, which denote a permutation.

Find the next permutation in ascending order.

 Notice

The list may contains duplicate integers.


Example
For [1,3,2,3], the next permutation is [1,3,3,2]

For [4,3,2,1], the next permutation is [1,2,3,4]
'''
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        if not nums:
            return []

        if len(nums) == 1:
            return nums

        i = len(nums) - 1
        
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        self.swap_list(nums, i, len(nums) - 1)

        if i != 0:
            j = i
            while nums[j] <= nums[i - 1]:
                j += 1
            self.swap(nums, j, i-1)

        return nums


    def swap_list(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


# def main():
#     s = Solution();
#     nums = [1, 2, 3, 4]
#     print(s.nextPermutation(nums))
#
# if __name__ == '__main__':
#     main()
