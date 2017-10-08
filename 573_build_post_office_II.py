# '''
# Given a 2D grid, each cell is either a wall 2, an house 1 or empty 0
# (the number zero, one, two),
# find a place to build a post office so that the sum of the distance
# from the post office to all the houses is smallest.
#
# Return the smallest sum of distance. Return -1 if it is not possible.
#
# Notice
#
# You cannot pass through wall and house, but can pass through empty.
# You only build post office on an empty.
#
# Example
# Given a grid:
#
# 0 1 0 0 0
# 1 0 0 2 1
# 0 1 0 0 0
# return 8, You can build at (1,1). (Placing a post office at (1,1),
# the distance that post office to all the house sum is smallest.)
#
# Challenge
# Solve this problem within O(n^3) time.
#
# '''
#
# HOUSE = 1
# WALL = 2
# EMPTY = 0
# MAXMIUM = sys.maxsize
# from collections import deque
# class Solution:
#     """
#     @param: grid: a 2D grid
#     @return: An integer
#     """
#     def shortestDistance(self, grid):
#         m = len(grid)
#         n = len(grid[0])
#         min_distance = m * n
#
#
#
#     def bfs(self, x, y, distance_sum_matrix, visited_times_matrix):
#         m = len(distance_sum_matrix)
#         n = len(distance_sum_matrix[0])
#         visited = [[False for j in range(n) for i in range(m)]]
#
#         dx = [1, -1, 0, 0]
#         dy = [0, 0 , 1, -1]
#
#         queue = deque()
#         queue.append((x, y))
#         visited[x][y] = True
#
#         step = 0
#         while queue:
#             step += 1
#             size = len(queue)
#             for i in range(size):
#                 x, y = queue.popleft()
#                 for i in range(4):
#                     new_x = x + dx[i]
#                     new_y = y + dy[i]
#                     if self.is_bound(x, y, grid) and grid[new_x][new_y] != WALL :
#                         queue.append((new_x, new_y))
#                         visi    ted[new_x][new_y] = True
#
#
#
#     def is_unvisited_and_bound(self, x, y, visited):
#         m = len(visited)
#         n = len(visited[0])
#         if 0 <= x <= m - 1 and 0 <= y <= n - 1:
#             return not visited[x][y]
#         return False
#
# def main():
#
#     grid = [[0, 1, 0, 0, 0],
#             [1, 0, 0, 2, 1],
#             [0, 1, 0, 0, 0]]
#     s = Solution()
#     print(s.shortestDistance(grid))
#
#
# if __name__ == '__main__':
#     main()
