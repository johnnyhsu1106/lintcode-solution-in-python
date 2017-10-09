class Solution:
    """
    @param: A: an integer array
    @return:
    """
    def mergeSort(self, nums):
        if not nums or len(nums) == 0:
            return nums

        temp = [0 for i in range(len(nums))]

        self.helper(nums, 0, len(nums) - 1, temp)


    def helper(self, nums, start, end, temp):
        if start >= end:
            return

        mid = (start + end) // 2
        self.helper(nums, start, mid, temp)
        self.helper(nums, mid + 1 , end, temp)
        self.merge(nums, start, mid, end, temp)


    def merge(self, nums, start, mid, end, temp):
        left = start
        right = mid + 1
        index = start

        while left <= mid and right <= end:
            if nums[left] < nums[right]:
                temp[index] = nums[left]
                left += 1
            else:
                temp[index] = nums[right]
                right += 1
            index += 1

        while left <= mid:
            temp[index] = nums[left]
            index += 1
            left += 1

        while right <= end:
            temp[index] = nums[right]
            index += 1
            right += 1

            #  copy all temp to A
        for i in range(start, end + 1):
            nums[i] = temp[i]



# def merge_sort(nums):
#     if len(nums) <= 1:
#         return nums
#
#     left = merge_sort(nums[0: len(nums) // 2])
#     right = merge_sort(nums[len(nums) // 2 :])
#     return merge(left, right)
#
# def merge(lst1, lst2):
#     i , j = 0, 0
#     result = []
#     while i < len(lst1) and j < len(lst2):
#         if lst1[i] < lst2[j]:
#             result.append(lst1[i])
#             i += 1
#         else:
#             result.append(lst2[j])
#             j += 1
#
#     if i == len(lst1):
#         result.extend(lst2[j:])
#     else:
#         result.extend(lst1[i:])
#
#     return result

def main():
    s = Solution()
    nums = [5, 4, 3, 2]
    s.mergeSort(nums)
    print(nums)

if __name__ == '__main__':
    main()
