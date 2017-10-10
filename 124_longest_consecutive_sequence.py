'''
Given an unsorted array of integers,
find the length of the longest consecutive elements sequence.

Clarification
Your algorithm should run in O(n) complexity.

Example
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
'''
class Solution:
    """
    @param: num: A list of integers
    @return: An integer
    """
    def longestConsecutive_1(self, nums):
        hashset = set(nums)
        longest = 0

        for num in nums:
            down = num - 1
            while down in hashset:
                # hashset.discard(down)
                down -= 1

            up = num + 1
            while up in hashset:
                # hashset.discard(up)
                up += 1

            longest = max(longest, up - down - 1)

        return longest



    def longestConsecutive_2(self, nums):
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        nums.sort()
        result = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                result += 1
            else:
                break
        return result


# def main():
#
#     s = Solution()
#     nums = [100, 4, 200, 1, 3, 2]
#     print(s.longestConsecutive_1(nums))
#
# if __name__ == '__main__':
#     main()
