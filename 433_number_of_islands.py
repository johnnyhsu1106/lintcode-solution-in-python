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
        if not grid or len(grid) == 0 or len(grid[0]) ==0:
            return 0


        m = len(grid)
        n = len(grid[0])

        count = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y]:
                    self.marked_by_dfs(x, y, grid)
                    count += 1
        return count


    def marked_by_dfs(self, x, y, grid):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1 ]
        grid[x][y] = False

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if self.is_bound(new_x, new_y, grid) and grid[new_x][new_y]:
                self.marked_by_dfs(new_x, new_y, grid)


    def is_bound(self, x, y, grid):
        m = len(grid)
        n = len(grid[0])
        return 0 <= x <= m - 1 and 0 <= y <= n - 1



###############################################################################

    def numIslands_bfs(self, grid):
        if not grid or len(grid) == 0 or len(grid[0]) ==0:
            return 0

        m = len(grid)
        n = len(grid[0])
        count = 0 # count stands for number of islands

        for x in range(m):
            for y in range(n):
                if grid[x][y]:
                    self.marked_by_bfs(x, y, grid)
                    count += 1
        return count


    def marked_by_bfs(self, x, y, grid):
        queue = deque()
        queue.append((x, y))
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        while queue:
            (x, y) = queue.popleft()
            grid[x][y] = False

            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if self.is_bound(new_x, new_y, grid) and grid[new_x][new_y]:
                    queue.append((new_x, new_y))


###############################################################################

    def numIslands_union_find(self, grid):

        class UnionFind:
            # Please also see the problem 591
            def __init__(self, n):
                self.father = [ i for i in range(n)]
                self.count =  0

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
                    self.count -= 1

            def query(self):
                # return the number of components
                return self.count

            def set_count(self, total):
                self.count = total


        m, n = len(grid), len(grid[0])
        if not grid or m == 0 or n ==0:
            return 0

        total_island = 0 # total number of islands
        for x in range(m):
            for y in range(n):
                if grid[x][y]:
                    total_island += 1

        union_find = UnionFind(m * n)
        union_find.set_count(total_island)

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for x in range(m):
            for y in range(n):
                if grid[x][y]:
                    for i in range(4):
                        new_x = x + dx[i]
                        new_y = y + dy[i]
                        if self.is_bound(new_x, new_y, grid) and grid[new_x][new_y]:
                            union_find.connect(x * n + y, new_x * n + new_y)

        return union_find.query()



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
