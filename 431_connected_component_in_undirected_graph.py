'''
Find the number connected component in the undirected graph.
Each node in the graph contains a label and a list of its neighbors.
(a connected component (or just component) of an undirected graph is a subgraph
in which any two vertices are connected to each other by paths,
and which is connected to no additional vertices in the supergraph.)


Each connected component should sort by label.

Clarification
Learn more about representation of graphs

Example
Given graph:

A------B  C
 \     |  |
  \    |  |
   \   |  |
    \  |  |
      D   E
Return {A,B,D}, {C,E}. Since there are two connected component which is {A,B,D}, {C,E}
'''
class UnDirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


from collections import deque
from collections import defaultdict

class Solution:
    """
    @param: nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet_bfs(self, nodes):
        '''
        bfs
        '''

        results = []
        visited_nodes = set()

        for node in nodes:
            if node not in visited_nodes:
                subgraph = [] # initialize every time when BFS
                self.bfs(node, visited_nodes, subgraph)
                results.append(sorted(subgraph))

        return results


    def bfs(self, node, visited_nodes, subgraph):
        queue = deque([node])
        visited_nodes.add(node)

        while queue:
            node = queue.popleft()
            subgraph.append(node.label)
            neighbors = node.neighbors

            for neighbor in neighbors:
                if neighbor not in visited_nodes:
                    queue.append(neighbor)
                    visited_nodes.add(neighbor)



    def connectedSet_union_find(self, nodes):
        class UnionFind:
            def __init__(self, nodes):
                self.father = {node.label : node.label for node in nodes}

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

        # Initialize the union_find data structre
        union_find = UnionFind(nodes)

        # connect node and its neighbors
        for node in nodes:
            neighbors = node.neighbor
            for neighbor in neighbors:
                union_find.connect(node.label, neighbor.label)

        # add those nodes with the same root in dictionary
        subgraph = defaultdict(set)
        for node in nodes:
            root = union_find.find(node.label)
            subgraph[root].add(node.label)

        # sort the result as problem requested.
        results = []
        for root in subgraph:
            results.append(sorted(subgraph[root]))

        return results



# def main():
#     s = Solution()
#     A = UnDirectedGraphNode('A')
#     B = UnDirectedGraphNode('B')
#     C = UnDirectedGraphNode('C')
#     D = UnDirectedGraphNode('D')
#     E = UnDirectedGraphNode('E')
#
#     A.neighbors = [B,D]
#     B.neighbors = [A,D]
#     C.neighbors = [E]
#     E.neighbors = [C]
#     nodes = [A, B, C, D, E]
#     print(s.connectedSet_bfs(nodes))
#     print(s.connectedSet_union_find(nodes))
#
# if __name__ == '__main__':
#     main()
