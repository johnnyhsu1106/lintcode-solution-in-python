'''
Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island.
If two 1 is adjacent, we consider them in the same island.
We only consider up/down/left/right adjacent.

Find the number of islands.

Example
Given graph:

[
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1]
]
return 3.
'''
from collections import deque
class Solution:
    """
    @param: grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands_dfs(self, grid):
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m, n = len(grid), len(grid[0])
        num_of_islands = 0

        for x in range(m):
            for y in range(n):
                if grid[x][y]:
                    self._marked_by_dfs(x, y, grid)
                    num_of_islands += 1

        return num_of_islands


    def _marked_by_dfs(self, x, y, grid):
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        grid[x][y] = False

        for direction in directions:
            new_x = x + dx
            new_y = y + dy

            if self._is_bound(new_x, new_y, m, n) and grid[new_x][new_y]:
                self._marked_by_dfs(new_x, new_y, grid)


    def _is_bound(self, x, y,  m, n):
        return 0 <= x <= m - 1 and 0 <= y <= n - 1



###############################################################################

    def numIslands_bfs(self, grid):
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])
        num_of_islands = 0 # count stands for number of islands

        for x in range(m):
            for y in range(n):

                if grid[x][y]:
                    self._marked_by_bfs(x, y, grid)
                    num_of_islands += 1

        return num_of_islands


    def _marked_by_bfs(self, x, y, grid):
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque([(x, y)])

        while queue:
            (x, y) = queue.popleft()

            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                if self.is_bound(new_x, new_y, m, n) and grid[new_x][new_y]:
                    queue.append((new_x, new_y))
                    grid[x][y] = False

    def _is_bound(self, x, y, m ,n):
        return 0 <= x <= m - 1 and 0 <= y <= n - 1

###############################################################################

    def numIslands_union_find(self, grid):

        class UnionFind:
            def __init__(self, size):
                self.father = [i for i in range(size)]
                self.num_of_connected_components = 0


            def find(self, x):
                if self.father[x] == x:
                    return x

                self.father[x] = self.find(self.father[x])

                return self.father[x]


            def connect(self, a, b):
                root_a = self.find(a)
                root_b = self.find(b)

                if root_a != root_b:
                    self.father[root_a] = root_b
                    self.num_of_connected_components -= 1


            def query(self):
                return self.num_of_connected_components


            def set_num(self, num):
                self.num_of_connected_components = num


        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        # assume each island is isolated and get the number of islands first
        m, n = len(grid), len(grid[0])
        num_of_islands = 0

        for x in range(m):
            for y in range(n):
                if grid[x][y]:
                    num_of_islands += 1

        # use the unio find to solve this issue
        union_find = UnionFind(m * n)
        union_find.set_num(num_of_islands)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for x in range(m):
            for y in range(n):
                if grid[x][y]:
                    for dx, dy in directions:
                        new_x = x + dx
                        new_y = y + dy

                        if self._is_bound(new_x, new_y, m ,n) and grid[new_x][new_y]:
                            # remember to covert each point in 2D matrix to 1D array
                            # because in union find, we use 1D array to track each component and its root
                            union_find.connect(x * n + y, new_x * n + new_y)

        return union_find.query()


    def _is_bound(self, x, y, m ,n):
        return 0 <= x <= m - 1 and 0 <= y <= n - 1




# def main():
#     grid = [
#       [1, 1, 0, 0, 0],
#       [0, 1, 0, 0, 1],
#       [0, 0, 0, 1, 1],
#       [0, 0, 0, 0, 0],
#       [0, 0, 0, 0, 1]
#     ]
#     s = Solution()
#     print(s.numIslands_bfs(grid))
#
#     grid = [
#       [1, 1, 0, 0, 0],
#       [0, 1, 0, 0, 1],
#       [0, 0, 0, 1, 1],
#       [0, 0, 0, 0, 0],
#       [0, 0, 0, 0, 1]
#     ]
#
#     print(s.numIslands_dfs(grid))
#
#     grid = [
#       [1, 1, 0, 0, 0],
#       [0, 1, 0, 0, 1],
#       [0, 0, 0, 1, 1],
#       [0, 0, 0, 0, 0],
#       [0, 0, 0, 0, 1]
#     ]
#
#     print(s.numIslands_union_find(grid))
#
# if __name__ == '__main__':
#     main()
