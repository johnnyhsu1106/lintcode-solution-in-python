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
    def heapify(self, nums):
        for i in range(len(nums) - 1, -1, -1):
            if self.has_parent(i) and nums[i] < self.parent(i, nums):
                # if nums[i]  < self.silbing(i, nums):
                self.swap(i , self.parent_index(i), nums)
                # else:
                    # self.swap(self.silbing_index(i), self.parent_index(i), nums)

    def swap(self, i, j, nums):
        nums[i], nums[j] = nums[j], nums[i]

    # def silbing_index(self, i):
    #     if i % 2 == 1:
    #         return i + 1
    #     return i - 1
    #
    # def has_silbing(self, i, nums):
    #     if i % 2 == 1:
    #         return i + 1 < len(nums)
    #     return True
    #
    # def silbing(self, i , nums):
    #     if i % 2 == 1:
    #         if self.has_silbing(i, nums):
    #             return nums[i + 1]
    #         return float('inf')
    #     else:
    #         return nums[i - 1]

    def parent_index(self, i):
        if i % 2 == 0:
            return (i - 2) // 2
        return (i - 1) // 2

    def has_parent(self, i):
        return self.parent_index(i) >= 0

    def parent(self, i , nums):
        if self.has_parent(i):
            return nums[self.parent_index(i)]


    # def left_index(self, i):
    #     return 2 * i + 1
    #
    # def right_index(self, i):
    #     return 2 * i + 2
    #
    # def has_left(self, i, nums):
    #     return self.left_index(i) < len(nums)
    #
    # def has_right(self, i, nums):
    #     return self.right_index(i) < len(nums)
    #
    # def left(self, i, nums):
    #     if self.has_left(i, nums):
    #         return nums[self.left_index(i)]
    #     return float('inf')
    #
    # def right(self, i, nums):
    #     if self.has_right(i, nums):
    #         return nums[self.right_index(i)]
    #     return float('inf')



def main():
    s = Solution()
    nums = [45, 39, 32, 11]
    s.heapify(nums)
    print(nums)

if __name__ == '__main__':
    main()
