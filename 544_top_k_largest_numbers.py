'''
Given an integer array, find the top k largest numbers in it.


Example
Given [3,10,1000,-99,4,100] and k = 3.
Return [1000, 100, 10].
'''
from heapq import heappush, heappop
class Solution:
    """
    @param: nums: an integer array
    @param: k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        result = []
        min_heap = []
        for num in nums:
            heappush(min_heap, num)
            if len(min_heap) > k:
                heappop(min_heap)

        return sorted(min_heap, reverse= True)


# def main():
#     s = Solution()
#     nums = [3,10,1000,-99,4,100]
#     k = 3
#     print(s.topk(nums, k))
#
# if __name__ == '__main__':
#     main()
