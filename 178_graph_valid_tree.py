'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges
(each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Notice

You can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Have you met this question in a real interview? Yes
Example
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
'''
from collections import defaultdict, deque
class Solution:
    """
    @param: n: An integer
    @param: edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree_bfs(self, n, edges):

        if n != len(edges) + 1:
            return False

        node_map = self._initialize_graph(edges)
        # travser all nodes
        queue = deque()
        visited = set()

        queue.append(0)
        visited.add(0)

        while queue:
            node = queue.popleft()
            neighbors = node_map[node]

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return n == len(visited)


    def _initialize_graph(self, edges):

        node_map = defaultdict(set)
        for node_1, node_2 in edges:
            node_map[node_1].add(node_2)
            node_map[node_2].add(node_1)

        return node_map



    def validTree_union_find(self, n, edges):

        class UnionFind:
            def __init__(self, n):
                self.father = [ i for i in range(n)]
                self.count = n

            def find(self, x):
                if self.father[x] == x:
                    return x

                self .father[x] = self.find(self.father[x])
                return self.father[x]

            def connect(self, a, b):
                root_a = self.find(a)
                root_b = self.find(b)

                if root_a != root_b:
                    self.father[root_a] = root_b
                    self.count -= 1

            def query(self):
                return self.count


        if n != len(edges) + 1:
            return False

        union_find = UnionFind(n)

        for a, b in edges:
            union_find.connect(a, b)

        return union_find.query() == 1


# def main():
#     s = Solution()
#     n = 5
#     edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
#     print(s.validTree_union_find(n, edges))
#
# if __name__ == '__main__':
#     main()
