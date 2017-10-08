'''
Implement a data structure, provide two interfaces:

add(number). Add a new number in the data structure.
topk(). Return the top k largest numbers in this data structure.
k is given when we create the data structure.

Example
s = new Solution(3);
>> create a new data structure.
s.add(3)
s.add(10)
s.topk()
>> return [10, 3]
s.add(1000)
s.add(-99)
s.topk()
>> return [1000, 10, 3]
s.add(4)
s.topk()
>> return [1000, 10, 4]
s.add(100)
s.topk()
>> return [1000, 100, 10]
'''

from heapq import heappop, heappush
class Solution:
    '''
    idea:
    assume n >>> k
    use min heap to store the top k nums instead of max heap
    Min Heap:
        Time:
            add: O(logk)
            topk: O(klogk)
        Space: O(k)

    Max Heap:
        Time:
            add: O(logn)
            topk: O(k)
        Space: O(n)
    '''
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.k = k
        self.min_heap = []

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        if len(self.min_heap) < self.k:
            heappush(self.min_heap, num)
        elif num > self.min_heap[0]:
            heappop(self.min_heap)
            heappush(self.min_heap, num)

    """
    @return: Top k element
    """
    def topk(self):
        return sorted(self.min_heap, reverse = True)


# def main():
#     s = Solution(3)
#     s.add(3)
#     s.add(10)
#     print(s.topk())
#     s.add(1000)
#     s.add(-99)
#     print(s.topk())
#     s.add(4)
#     print(s.topk())
#     s.add(100)
#     print(s.topk())
#
# if __name__ == '__main__':
#     main()
