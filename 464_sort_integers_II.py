'''
Given an integer array, sort it in ascending order.
Use quick sort, merge sort, heap sort or any O(nlogn) algorithm.

Example
Given [3, 2, 1, 4, 5], return [1, 2, 3, 4, 5].

'''
class Solution:
    """
    @param: A: an integer array
    @return:
    """
    def sortIntegers2(self, nums):
        if not nums or len(nums) == 0:
            return nums

        temp = [0 for i in range(len(nums))]

        self.merge_sort (nums, 0, len(nums) - 1, temp)


    def merge_sort(self, nums, start, end, temp):
        if start >= end:
            return

        mid = (start + end) // 2
        self.merge_sort(nums, start, mid, temp)
        self.merge_sort(nums, mid + 1 , end, temp)
        self.merge(nums, start, end, temp)


    def merge(self, nums, start, end, temp):
        left_idx = start
        mid = (start + end) // 2
        right_idx = mid + 1
        idx = left_idx

        while left_idx <= mid and right_idx <= end:
            if nums[left_idx] < nums[right_idx]:
                temp[idx] = nums[left_idx]
                left_idx += 1
            else:
                temp[idx] = nums[right_idx]
                right_idx += 1
            idx += 1

        while left_idx <= mid:
            temp[idx] = nums[left_idx]
            idx += 1
            left_idx += 1

        while right_idx <= end:
            temp[idx] = nums[right_idx]
            idx += 1
            right_idx += 1

            #  copy all temp to A
        for i in range(start, end + 1):
            nums[i] = temp[i]



# def main():
#     s = Solution()
#     nums = [3, 2, 1, 4, 5]
#
#     s.sortIntegers2(nums)
#     print(nums)
#
# if __name__ == '__main__':
#     main()
