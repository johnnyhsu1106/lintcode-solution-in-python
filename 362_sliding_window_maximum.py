'''
Given an array of n integer with duplicate number,and a moving window(size k),
move the window at each iteration from the start of the array,
find the maximum number inside the window at each moving.

Example
For array [1, 2, 7, 7, 8], moving window size k = 3. return [7, 7, 8]

At first the window is at the start of the array like this

[|1, 2, 7| ,7, 8] , return the maximum 7;

then the window move one step forward.

[1, |2, 7 ,7|, 8], return the maximum 7;

then the window move one step forward again.

[1, 2, |7, 7, 8|], return the maximum 8;

Challenge
o(n) time and O(k) memory
'''
from collections import deque
class Solution:
    """
    @param: nums: A list of integers
    @param: k: An integer
    @return: The maximum number inside the window at each moving
    """
    def maxSlidingWindow_1(self, nums, k):
        if not nums or len(nums)== 0 or len(nums) < k or k == 0:
            return []

        result = []
        deq = deque()
        for i in range(k - 1):
            self.in_deque(deq, nums[i])

        for i in range(k - 1, len(nums)):
            self.in_deque(deq, nums[i])
            result.append(deq[0])
            self.out_deque(deq, nums[i - k + 1])

        return result


    def in_deque(self, deq, num):
        while deq and num > deq[-1]:
            deq.pop()
        deq.append(num)

    def out_deque(self, deq, num):
        if deq and deq[0] == num:
            deq.popleft()



    def maxSlidingWindow_2(self, nums, k):
        deq = deque()
        result = []
        if not nums or len(nums) == 0 or len(nums) < k or k == 0:
            return []

        n = len(nums)
        for i in range(n):
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i)

            if i >= k - 1:

                while deq and deq[0] <= i - k:
                    deq.popleft()
                result.append(nums[deq[0]])

        return result;



# def main():
#     s = Solution()
#     nums = [1, 2, 7, 7, 8]
#     k = 3
#     print(s.maxSlidingWindow_1(nums, k))
#     # print(s.maxSlidingWindow_2(nums, k))
#
# if __name__ == '__main__':
#     main()
