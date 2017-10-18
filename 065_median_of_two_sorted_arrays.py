'''
There are two sorted arrays A and B of size m and n respectively.
Find the median of the two sorted arrays.

Example
Given A=[1,2,3,4,5,6] and B=[2,3,4,5], the median is 3.5.

Given A=[1,2,3] and B=[4,5], the median is 3.

Challenge
The overall run time complexity should be O(log (m+n)).
'''
class Solution:

    def findMedianSortedArrays_1(self, nums1, nums2):
        # Time: O(log(m+n))
        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return self.find_kth(nums1, nums2, n // 2 + 1)
        else:
            return (self.find_kth(nums1, nums2, n // 2) + self.find_kth(nums1, nums2, n // 2 + 1)) / 2.0


    def find_kth(self, nums1, nums2, k):
        if len(nums1) == 0:
            return nums2[k - 1]

        if len(nums2) == 0:
            return nums1[k - 1]

        if k == 1:
            return min(nums1[0], nums2[0])
        mid = k // 2
        a = nums1[mid - 1] if len(nums1) >= mid else float('inf')
        b = nums2[mid - 1] if len(nums2) >= mid else float('inf')

        if a  <  b:
            return self.find_kth(nums1[mid:], nums2, k - mid)
        else:
            return self.find_kth(nums1, nums2[mid:], k - mid)


    def findMedianSortedArrays_2(self, nums1, nums2):
        # idea: brute force
        # Time: O(m + n)
        nums = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        while i < len(nums1):
            nums.append(nums1[i])
            i += 1

        while j < len(nums2):
            nums.append(nums2[i])
            j += 1

        if len(nums) % 2 == 1:
            return float(nums[len(nums) // 2])
        else:
            return float((nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2)


# def main():
#     s = Solution()
#     nums1 = [1,2,3,4,5,6]
#     nums2 = [2,3,4,5]
#     print(s.findMedianSortedArrays_1(nums1, nums2))
#     # print(s.findMedianSortedArrays_2(nums1, nums2))
#
# if __name__ == '__main__':
#     main()
