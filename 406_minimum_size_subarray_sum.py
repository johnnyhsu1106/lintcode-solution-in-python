'''
Given an array of n positive integers and a positive integer s,
find the minimal length of a subarray of which the sum ≥ s.
If there isn't one, return -1 instead.

Given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''

class Solution:
    """
    @param: nums: an array of integers
    @param: s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        if not nums or s < 0:
            return -1

        total = 0
        j = 0
        size = len(nums)
        min_length = size + 1

        for i in range(size):
            while j < size and total < s:
                total += nums[j]
                j += 1

            if total >= s:
                min_length = min(min_length, j - i)

            total -= nums[i]

        if min_length == size + 1:
            return -1

        return min_length



# def main():
#     s = Solution()
#     nums = [2,3,1,2,4,3]
#     target = 7
#     print(s.minimumSize(nums, target))
#
# if __name__ == '__main__':
#     main()
