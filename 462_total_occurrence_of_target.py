class Solution:
    """
    @param: A: A an integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        if not A or len(A) == 0:
            return 0

        start1, end1 = 0, len(A) - 1
        while start1 + 1 < end1:
            mid1 = start1 + (end1 - start1) // 2
            if A[mid1] < target:
                start1 = mid
            elif A[mid1] > target:
                end1 = mid1
            else:
                end1 = mid1

        start2, end2 = 0, len(A) - 1
        while start2 + 1 < end2:
            mid2 = start2 + (end2 - start2) // 2
            if A[mid2] < target:
                start2 = mid2
            elif A[mid2] > target:
                end2 = mid2
            else:
                start2 = mid2


        first_position = None
        if A[start1] == target:
            first_position = start1
        elif A[end1] == target:
            first_position = end1

        last_position = None
        if A[end2] == target:
            last_position = end2
        elif A[start2] == target:
            last_position = start2


        if first_position is not None and last_position is not None:
            return last_position - first_position + 1
        return 0



# def main():
#     s = Solution()
#     nums = [1,1,1,1,1,1,1,1,1,1,1]
#     target = 1
#     print(s.totalOccurrence(nums, target))
# if __name__ == '__main__':
#     main()
