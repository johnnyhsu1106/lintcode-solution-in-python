'''
Given an integer array, find a subarray where the sum of numbers is zero.
Your code should return the index of the first number and the index of the last number.

Notice
There is at least one subarray that it's sum equals to zero.

Example
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].
'''
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum_1(self, nums):
        '''
        idea:
        Time: O(n^2).. not good
        Speace: O(1)
        '''
        result = []
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total == 0:
                    return [i, j]
        return result


    def subarraySum_2(self, nums):
        # p stands for prefix sum
        # p[0] = 0
        # p[j] = nums[0] + ... + nums[j-1]
        # nums[i: j+1] = p[j+1] - p[i]


        # idea: subarray sum, nums[i:j+1] = 0
        # p[j+1] = p[i]
        # pre_sum_table = {key:value = pre[i]: i }

        pre_sum_table = {0: -1}
        total = 0
        for i in range(len(nums)):
            total += nums[i]

            if total in pre_sum_table:
                return [pre_sum_table[total] + 1, i]
            pre_sum_table[total] = i
            print(pre_sum_table)

# def main():
#     s = Solution()
#     nums = [1, -3, 1, 2, -3, 4]
#     print(s.subarraySum_1(nums))
#     print(s.subarraySum_2(nums))
#
# if __name__ == '__main__':
#     main()
