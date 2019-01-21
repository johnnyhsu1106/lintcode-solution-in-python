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
        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        hashset = set(nums)
        longest_consecutive_length = 0

        for num in nums:
            down = num - 1
            while down in hashset:
                hashset.discard(down)
                down -= 1

            up = num + 1
            while up in hashset:
                hashset.discard(up)
                up += 1

            longest_consecutive_length = max(longest_consecutive_length, up - down - 1)

        return longest_consecutive_length


# def main():
#
#     s = Solution()
#     nums = [100, 4, 200, 1, 3, 2]
#     print(s.longestConsecutive_1(nums))
#
# if __name__ == '__main__':
#     main()
