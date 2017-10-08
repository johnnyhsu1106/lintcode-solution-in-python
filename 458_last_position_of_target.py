'''
Find the last position of a target number in a sorted array. Return -1 if target does not exist.

Have you met this question in a real interview? Yes
Example
Given [1, 2, 2, 4, 5, 5].

For target = 2, return 2.

For target = 5, return 5.

For target = 6, return -1.
'''
class Solution:
    """
    @param: nums: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        
        if len(nums) == 1:
            return -1

        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid

        if nums[end] == target:
            return end
        elif nums[start] == target:
            return start
        return -1




# def main():
#     s = Solution()
#     print(s.lastPosition([1, 2, 2, 4, 5, 5],2))
#     print(s.lastPosition([1, 2, 2, 4, 5, 5],5))
#     print(s.lastPosition([1, 2, 2, 4, 5, 5],6))
#
# if __name__ == '__main__':
#     main()
