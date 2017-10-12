'''
Given a knight in a chessboard n * m (a binary matrix with 0 as empty and 1 as barrier).
the knight initialze position is (0, 0) and he wants to reach position (n - 1, m - 1),
Knight can only be from left to right. Find the shortest path to the destination position,
return the length of the route. Return -1 if knight can not reached.

Have you met this question in a real interview? Yes
Clarification
If the knight is at (x, y), he can get to the following positions in one step:

(x + 1, y + 2)
(x - 1, y + 2)
(x + 2, y + 1)
(x - 2, y + 1)
Example
[[0,0,0,0],
 [0,0,0,0],
 [0,0,0,0]]

Return 3

[[0,0,0,0],
 [0,0,0,0],
 [0,1,0,0]]

Return -1
'''
class Solution:
    """
    @param: grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2_bfs(self, grid):
        '''
        Time Limit Exceeded... in LintCode
        '''
        from collections import deque
        #  BFS
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return -1
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0

        m,n = len(grid), len(grid[0])
        dx = [1, -1, 2, -2]
        dy = [2, 2, 1, 1]

        start = (0, 0)
        end = (m - 1 , n - 1)

        step = 0
        queue = deque([start])
        while queue:
            size = len(queue)
            for i in range(size):
                point = queue.popleft()
                if point == end:
                    return step

                for i in range(4):
                    new_x = point[0] + dx[i]
                    new_y = point[1] + dy[i]
                    if self.is_bound(new_x, new_y, grid) and grid[new_x][new_y] == 0:
                        grid[new_x][new_x] = 1
                        queue.append((new_x, new_y))
            step += 1

        return -1

    def is_bound(self, x, y, grid):
        m,n = len(grid), len(grid[0])
        return 0 <= x < m and 0 <= y < n



    # def shortestPath2_dp(self, grid):
    #     if not grid or len(grid) == 0 or len(grid[0]) == 0:
    #         return -1
    #     if len(grid) == 1 and len(grid[0]) == 1:
    #         return 0
    #



# def main():
#     s = Solution()
#     grid = [[0,0,0,0],
#             [0,0,0,0],
#             [0,0,0,0]]
#     print(s.shortestPath2_bfs(grid) == 3)
#
#     grid = [[0,0,0,0],
#             [0,0,0,0],
#             [0,1,0,0]]
#     print(s.shortestPath2_bfs(grid) == -1)
#
# if __name__ == '__main__':
#     main()
