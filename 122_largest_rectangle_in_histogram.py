'''
Given n non-negative integers representing the histogram's bar height
where the width of each bar is 1, find the area of largest rectangle in the histogram.

The link of graph: http://www.lintcode.com/en/problem/largest-rectangle-in-histogram/

histogram
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

histogram
The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example
Given height = [2,1,5,6,2,3],
return 10.
'''
class Solution:
    """
    @param: height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        if not height or len(height) == 0:
            return 0

        stack = []
        area = 0
        i = 0
        while i < len(height):

            if not stack or height[i] > height[stack[-1]]:
                stack.append(i)
            else:
                curr = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                area = max(area, width * height[curr])
                i -= 1
            i += 1


        while stack:
            curr = stack.pop()
            width = len(height) if not stack else len(height) - stack[-1] - 1
            area = max(area, width * height[curr])

        return area



# def main():
#     s = Solution()
#     height = [2,1,5,6,2,3]
#     print(s.largestRectangleArea(height))
#
# if __name__ == '__main__':
#     main()
