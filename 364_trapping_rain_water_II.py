'''
Given n x m non-negative integers representing an elevation map 2d
where the area of each cell is 1 x 1,
compute how much water it is able to trap after raining.


Example
Given 5*4 matrix

[12,13,0,12]
[13,4,13,12]
[13,8,10,12]
[12,13,12,12]
[13,13,13,13]
return 14.
'''


from heapq import heappush, heappop
class Solution:
    """
    @param: heights: a matrix of integers
    @return: an integer
    """
    def trapRainWater(self, heights):
        # edge case
        if not heights or len(heights) == 0 or len(heights[0]) == 0:
            return 0

        m, n = len(heights), len(heights[0])
        visited_matrix = [[False]* n for i in range(m)]
        min_heap = []
        # put all outer elements, (height, x, y), into min_heap
        for x in range(m):
            heappush(min_heap, (heights[x][0], x, 0))
            heappush(min_heap, (heights[x][n - 1], x, n - 1))
            visited_matrix[x][0] = True
            visited_matrix[x][n - 1] = True

        for y in range(n):
            heappush(min_heap, (heights[0][y], 0, y))
            heappush(min_heap, (heights[m - 1][y], m - 1, y))
            visited_matrix[0][y] = True
            visited_matrix[m - 1][y] = True

        # BFS ... using min_heap as queue (priority queue), 2D visited_matrix as set
        result = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while min_heap:
            h, x, y = heappop(min_heap)

            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                 if self._is_bound(new_x, new_y, m, n) and not visited_matrix[new_x][new_y]:
                    new_h = heights[new_x][new_y]
                    heappush(min_heap, (max(h, new_h), new_x, new_y))
                    visited_matrix[new_x][new_y] = True
                    # if new_h < h:
                        # result += h - new_h
                    result += max(0, h - new_h) # above two lines is equal to this line

        return result


    def _is_bound(self, x, y, m, n):
        return 0 <= x <= m - 1 and 0 <= y <= n - 1



# def main():
#     s = Solution()
#     heights = [ [12,13,0,12],
#                 [13,4,13,12],
#                 [13,8,10,12],
#                 [12,13,12,12],
#                 [13,13,13,13]]
#
#     print(s.trapRainWater(heights))
#
# if __name__ == '__main__':
#     main()
