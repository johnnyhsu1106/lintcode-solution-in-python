'''
Partition an unsorted integer array into three parts:

The front part < low
The middle part >= low & <= high
The tail part > high
Return any of the possible solutions.

Notice

low <= high in all testcases.

Example
Given [4,3,4,1,2,3,1,2], and low = 2 and high = 3.

Change to [1,1,2,3,2,3,4,4].

([1,1,2,2,3,3,4,4] is also a correct answer, but [1,2,1,2,3,3,4,4] is not)

Challenge
Do it in place.
Do it in one pass (one loop).
'''
class Solution:
    """
    @param: nums: an integer array
    @param: low: An integer
    @param: high: An integer
    @return:
    """
    def partition2(self, nums, low, high):
        '''
        please see problem 148 sort color
        '''
        if nums is None or len(nums) == 0:
            return

        i, left, right = 0, 0, len(nums) - 1

        while i < right:
            if nums[i] < low:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] > high:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1

# def main():
#     s = Solution()
#     nums = [4,3,4,1,2,3,1,2]
#     low , high = 2, 3
#     s.partition2(nums,low, high)
#     print(nums)
#
#
# if __name__ == '__main__':
#     main()
