'''
Given an integer array, heapify it into a min-heap array.

For a heap array A, A[0] is the root of heap, and for each A[i],
A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right child of A[i].

Clarification
What is heap?

Heap is a data structure, which usually have three methods:
push, pop and top.
where "push" add a new element the heap,
"pop" delete the minimum/maximum element in the heap,
"top" return the minimum/maximum element.

What is heapify?
Convert an unordered integer array into a heap array.
If it is min-heap, for each element A[i],
we will get A[i * 2 + 1] >= A[i] and A[i * 2 + 2] >= A[i].

What if there is a lot of solutions?
Return any of them.
Example
Given [3,2,1,4,5], return [1,2,3,4,5] or any legal heap array.

Challenge
O(n) time complexity
'''

class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify_1(self, nums):
        for i in range(len(nums)//2, -1, -1):
            self.heapify_down(i, nums)



    def heapify_down(self, i, nums):
        # i = 0
        while self.has_left(i, nums):
            child_index = self.left_index(i)
            if self.has_right(i, nums) and self.right(i, nums) < self.left(i, nums):
                child_index = self.right_index(i)

            if nums[i] < nums[child_index]:
                break
            else:
                self.swap(i, child_index, nums)
            i = child_index


    def swap(self, i, j, nums):
        nums[i], nums[j] = nums[j], nums[i]

    def left_index(self, i):
        return 2 * i + 1

    def right_index(self, i):
        return 2 * i + 2

    def has_left(self, i, nums):
        return self.left_index(i) < len(nums)

    def has_right(self, i, nums):
        return self.right_index(i) < len(nums)

    def left(self, i, nums):
        if self.has_left(i, nums):
            return nums[self.left_index(i)]

    def right(self, i, nums):
        if self.has_right(i, nums):
            return nums[self.right_index(i)]


##############################################################################

    def heapify_2(self, nums):
        for i in range(len(nums) // 2, -1, -1):
            self.percolate_down(i ,nums)


    def percolate_down(self, i, nums):
        while 2 * i + 1 < len(nums):
            child_index = 2 * i  + 1
            if 2 * i + 2 < len(nums) and nums[2 * i + 2] < nums[2 * i + 1]:
                child_index = 2 * i + 2

            if nums[i] < nums[child_index]:
                break
            else:
                nums[i], nums[child_index] = nums[child_index], nums[i]
            i = child_index


# def main():
#     s = Solution()
#     nums = [45, 39, 32, 11]
#     s.heapify_2(nums)
#     print(nums)
#
# if __name__ == '__main__':
#     main()
