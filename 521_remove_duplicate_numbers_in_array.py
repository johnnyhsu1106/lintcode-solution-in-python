'''
Given an array of integers, remove the duplicate numbers in it.

You should:
1. Do it in place in the array.
2. Move the unique numbers to the front of the array.
3. Return the total number of the unique numbers.

Notice

You don't need to keep the original order of the integers.


Example
Given nums = [1,3,1,4,4,2], you should:

Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
Return the number of unique integers in nums => 4.
Actually we don't care about what you place in ?,
we only care about the part which has no duplicate integers.

Challenge
Do it in O(n) time complexity.
Do it in O(nlogn) time without extra space.
'''
class Solution:
    """
    @param: nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication_1(self, nums):
        # Time: O(n)
        # use hash set
        uniques = set()
        index = 0
        for num in nums:
            if num not in uniques:
                uniques.add(num)
                nums[index] = num
                index += 1
        return index


    def deduplication_2(self, nums):
        if not nums or len(nums) == 0:
            return 0

        nums.sort()
        index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[index] = nums[i]
                index += 1
        return index



# def main():
#     s = Solution()
#     nums = [1,3,1,4,4,2]
#     print(s.deduplication_1(nums))
#     print(s.deduplication_2(nums))
# if __name__ == '__main__':
#     main()
