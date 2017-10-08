'''
Given n non-negative integers representing an elevation map
where the width of each bar is 1, compute how much water it is able to trap after raining.

Trapping Rain Water

Have you met this question in a real interview? Yes
Example
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

Challenge
O(n) time and O(1) memory

O(n) time and O(n) memory is also acceptable.
'''
class Solution:
    """
    @param: heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # the max height of water is determined by the
        # min(left_height, right_height) - height[left/right]
        # use two pointets.... start from the side of lower height one
        # Time: O(n)
        # edge case
        if not heights or len(heights) < 2:
            return 0

        left, right = 0, len(heights) - 1
        left_height = heights[left]
        right_height = heights[right]

        result = 0

        while left < right:
            if left_height < right_height:
                left += 1
                if heights[left] <= left_height:
                    result += left_height - heights[left]
                else:
                    left_height = heights[left]

            else:
                right -= 1
                if heights[right] <= right_height:
                    result += right_height - heights[right]
                else:
                    right_height = heights[right]

        return result


# def main():
#     s = Solution()
#     heights = [0,1,0,2,1,0,1,3,2,1,2,1]
#     print(s.trapRainWater(heights))
#
# if __name__ == '__main__':
#     main()
