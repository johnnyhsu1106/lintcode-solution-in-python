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
        visited = [[False]* n for i in range(m)]
        min_heap = []

        # put all outer elements, (height, x, y), into min_heap
        for i in range(m):
            heappush(min_heap, (heights[i][0], i, 0))
            heappush(min_heap, (heights[i][n - 1], i, n - 1))
            visited[i][0] = True
            visited[i][n - 1] = True

        for j in range(n):
            heappush(min_heap, (heights[0][j], 0, j))
            heappush(min_heap, (heights[m - 1][j], m - 1, j))
            visited[0][j] = True
            visited[m - 1][j] = True

        # BFS ... using min_heap as queue (priority queue), 2D visited as set
        result = 0
        while min_heap:
            h, x, y = heappop(min_heap)
            visited[x][y] = True

            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]

            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if self.is_bound(new_x, new_y, heights) and not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    new_h = heights[new_x][new_y]
                    heappush(min_heap, (max(h, new_h), new_x, new_y))
                    # if new_h < h:
                        # result += h - new_h
                    result += max(0, h - new_h) # above two lines is equal to this line

        return result


    def is_bound(self, x, y, heights):
        m, n = len(heights), len(heights[0])
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
