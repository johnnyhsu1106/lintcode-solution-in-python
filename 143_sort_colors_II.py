'''
Given an array of n objects with k different colors (numbered from 1 to k),
sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

Notice

You are not suppose to use the library's sort function for this problem.

k <= n

Example
Given colors=[3, 2, 2, 1, 4], k=4, your code should sort colors in-place to [1, 2, 2, 3, 4].

Challenge
A rather straight forward solution is a two-pass algorithm using counting sort.
That will cost O(k) extra memory. Can you do it without using extra memory?
'''


class Solution:
    """
    @param: colors: A list of integer
    @param: k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        '''
        k = 1, O(1)
        k = 2, O(n) ... see problem 031 partition array
        k = 3, O(n) ... see problem 148 sort colors
        k = n, O(nlogn) .. quick sort or merge sort

        conclude: nlogk..
        樹形分析法 每層O(n)...共logk層
        '''
        if not colors or len(colors) == 0:
            return

        self.rainbow_sort(colors, 0, len(colors) - 1, 1, k)


    def rainbow_sort(self, colors, start, end, color_from, color_to):
        # quick sort
        if color_from == color_to:
            return

        if start >= end:
            return

        # pivot
        color_mid = (color_to + color_from) // 2
        left, right = start, end

        while left <= right:
            while left <= right and colors[left] <= color_mid:
                left += 1
                
            while left <= right and colors[right] > color_mid:
                right -= 1

            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1

        self.rainbow_sort(colors, start, right, color_from, color_mid)
        self.rainbow_sort(colors, left, end, color_mid + 1, color_to)


# def main():
#     s = Solution()
#     colors = [3,2,3,3,4,3,3,2,4,4,1,2,1,1,1,3,4,3,4,2]
#     k = 4
#     s.sortColors2(colors, k)
#     print(colors)
#
# if __name__ == '__main__':
#     main()
