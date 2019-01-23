'''
Given a n,m which means the row and column of the 2D matrix
and an array of pair A( size k).
Originally, the 2D matrix is all 0 which means there is only sea in the matrix.
The list pair has k operator and each operator has two integer A[i].x, A[i].y
means that you can change the is_island_grid matrix[A[i].x][A[i].y] from sea to island.
Return how many island are there in the matrix after each operator.

 Notice

0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Have you met this question in a real interview? Yes
Example
Given n = 3, m = 3, array of pair A = [(0,0),(0,1),(2,2),(2,1)].

return [1,1,2,2].
'''

 # Definition for a point.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class UnionFind:
    def __init__(self, size):
        self.num_of_connected_component = 0
        self.father = [i for i in range(size)]


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
            self.num_of_connected_component -= 1


    def query(self):
        return self.num_of_connected_component


    def set_num(self, num):
        self.num_of_connected_component = num


class Solution:
    """
    @param: n: An integer
    @param: m: An integer
    @param: operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        if n == 0 or m == 0 or not operators:
            return []

        results = []
        num_of_islands = 0
        is_island_grid = [[False] * m for i in range(n)]
        union_find = UnionFind(n * m)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for point in operators:
            x, y = point.x, point.y

            if not is_island_grid[x][y]:
                num_of_islands += 1
                union_find.set_num(num_of_islands)
                is_island_grid[x][y] = True

                for dx, dy in directions:
                    new_x = x + dx
                    new_y = y + dy

                    if self._is_bound(new_x, new_y, n, m) and is_island_grid[new_x][new_y]:
                        union_find.connect(x * m + y, new_x * m + new_y)

            num_of_islands = union_find.query()
            results.append(num_of_islands)

        return results



    def _is_bound(self, x, y, n, m):
        return 0 <= x <= n - 1 and 0 <= y <= m - 1
# def main():
#     s = Solution()
#     n = 3
#     m = 3
#     operators = [Point(0, 0), Point(0, 1), Point(2, 2), Point(2, 1)]
#     print(s.numIslands2(n, m, operators))
#
# if __name__ == '__main__':
#     main()
