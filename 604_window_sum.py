'''
Given an array of n integer, and a moving window(size k),
move the window at each iteration from the start of the array,
find the sum of the element inside the window at each moving.

Have you met this question in a real interview? Yes
Example
For array [1,2,7,8,5], moving window size k = 3.
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20
return [10,17,20]
'''
class Solution:
    """
    @param: nums: a list of integers.
    @param: k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum_1(self, nums, k):
        n = len(nums)
        if not nums or n == 0 or k > n or k <=0:
            return []

        result = [0] * (n - k + 1)
        for i in range(k):
            result[0] += nums[i]

        for i in range(1, n - k + 1):
            result[i] = result[i - 1] + nums[i + k - 1] - nums[i - 1]
        return result


    def winSum_2(self, nums, k):
        n = len(nums)
        if not nums or n == 0 or k > n or k <=0:
            return []

        result = [0] * (n - k + 1)
        result[0] = sum(nums[0:k])
        i = k
        while i < n:
            result[i - k + 1] = result[i - k] + nums[i] - nums[i - k]
            i += 1
        return result



# def main():
#     s = Solution()
#     nums = [1,2,7,8,5]
#     # print(s.winSum_1(nums, 3))
#     print(s.winSum_2(nums, 3))
# if __name__ == '__main__':
#     main()
