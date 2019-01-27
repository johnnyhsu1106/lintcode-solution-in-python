'''
Given n books and the ith book has A[i] pages.
You are given k people to copy the n books.

n books list in a row and each person can claim a continous range of the n books.
For example one copier can copy the books from ith to jth continously,
but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).

They start copying books at the same time and they all cost 1 minute
to copy 1 page of a book. What's the best strategy to assign books
so that the slowest copier can finish at earliest time?


Example
Given array A = [3,2,4], k = 2.

Return 5( First person spends 5 minutes to copy book 1 and book 2
and second person spends 4 minutes to copy book 3. )
'''
class Solution:
    """
    @param: pages: an array of integers
    @param: k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        if not pages or k <= 0:
            return 0
        # time from max(pages), if k is len(pages), to sum(pags), if k = 1
        start, end = max(pages), sum(pages)

        while start + 1 < end:
             mid = start + (end - start) // 2

             if self._count_copier(pages, mid) <= k:
                 end = mid
             elif self._count_copier(pages, mid) > k:
                 start = mid

        if self._count_copier(pages, start) <= k:
            return start

        return end


    def _count_copier(self, pages, time):
        copiers = 1
        total = pages[0]

        for i in range(1, len(pages)):
            if total + pages[i] > time:
                copiers += 1
                total = 0
            total += pages[i]

        return copiers


# def main():
#     s = Solution()
#     pages = [13,999,1,2,3,9,11]
#     k = 2
#     print(s.copyBooks(pages, k))
# if __name__ == '__main__':
#     main()
