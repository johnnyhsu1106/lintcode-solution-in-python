'''
Given two arrays, write a function to compute their intersection.

 Notice

Each element in the result must be unique.
The result can be in any order.
Have you met this question in a real interview? Yes
Example
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
'''


class Solution:

    """
    @param: nums1: an integer array
    @param: nums2: an integer array
    @return: an integer array
    """
    def intersection_1(self, nums1, nums2):
        # idea: hash set
        seen = set(nums1)
        result = set()
        for num in nums2:
            if nums in seen:
                result.add(num)
        return list(result)


    def intersection_2(self, nums1, nums2):
        return list(set(nums1) & set(nums2))


    def intersection_3(self, nums1, nums2):
        # idea: binary search + hash set
        result = set()
        if len(nums1) > len(nums2):
            s_nums = nums2
            b_nums = nums1
        else:
            s_nums = nums1
            b_nums = nums2

        s_nums.sort()
        for num in b_nums:
            if self.binary_seach(s_nums, num):
                result.add(num)
        return list(result)


    def binary_seach(self, nums, target):
        if not nums or len(nums) == 0:
            return False

        start, end = 0, len(nums) -1
        while start + 1 < end:
            middle = start + (end - start) // 2

            if nums[middle] <= target:
                start = middle
            elif nums[middle] > target:
                end = middle

        if nums[end] == target or nums[start] == target:
            return True
        return False


    def intersection_4(self, nums1, nums2):
        # idea: two pointers
        nums1.sort()
        nums2.sort()
        result = set()

        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

        return list(result)

# def main():
#     s = Solution()
#     nums1 = [1, 2, 3, 1]
#     nums2 = [1, 3]
#
#     print(s.intersection_4(nums1, nums2))
# if __name__ == '__main__':
#     main()
