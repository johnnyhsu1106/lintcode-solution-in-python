'''
Given a target number, a non-negative integer k and
an integer array A sorted in ascending order,
find the k closest numbers to target in A,
sorted in ascending order by the difference between the number and target.
Otherwise, sorted in ascending order by number if the difference is same.


Example
Given A = [1, 2, 3], target = 2 and k = 3, return [2, 1, 3].

Given A = [1, 4, 6, 8], target = 3 and k = 3, return [4, 1, 6].

Challenge
O(logn + k) time complexity.
'''
class Solution:
    """
    @param: nums: an integer array
    @param: target: An integer
    @param: k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, nums, target, k):
        if not nums or len(nums) == 0:
            return []

        result = []
        # find the closest number's index
        index =  self.findClosestNumber(nums, target)

        #  two pointer
        left, right = index - 1, index
        for i in range(k):
            if left < 0:
                result.append(nums[right])
                right += 1
            elif right >= len(nums):
                result.append(nums[left])
                left -= 1
            else:
                if target - nums[left] <= nums[right] - target:
                    result.append(nums[left])
                    left -= 1
                else:
                    result.append(nums[right])
                    right += 1

        return result


    def findClosestNumber(self, nums, target):

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if (target - nums[start]) < (nums[end] - target):
            return start
        return end



#
# def main():
#     s = Solution()
#     nums = [1, 2, 3]
#     target = 2
#     k = 3
#     print(s.kClosestNumbers(nums, target, k) == [2, 1, 3])
#
#     nums = [1, 4, 6, 8]
#     target = 3
#     k = 3
#     print(s.kClosestNumbers(nums, target, k) == [4, 1, 6 ])
#
#     nums =  
#     target = 1
#     k = 4
#     print(s.kClosestNumbers(nums, target, k) == [1, 4, 6, 10])
#
#
#
# if __name__ == '__main__':
#     main()
