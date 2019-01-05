'''
Given a mountain sequence of n integers which increase firstly and then decrease,
find the mountain top.

Example
Given nums = [1, 2, 4, 8, 6, 3] return 8
Given nums = [10, 9, 8, 7], return 10
'''
class Solution:
    """
    @param: nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < nums[mid + 1]: # judge the slope
                start = mid
            else:
                end = mid

        return max(nums[start], nums[end])

# def main():
#     s = Solution()
#     print(s.mountainSequence([1, 2, 4, 8, 6, 3]))
#     print(s.mountainSequence([10, 9, 8, 7]))
# if __name__ == '__main__':
#     main()
