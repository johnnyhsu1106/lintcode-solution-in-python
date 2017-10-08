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



class Solution:
    """
    @param: nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet_bfs(self, nodes):
        '''
        bfs
        '''

        result = []
        visited = set()

        for node in nodes:
            if node not in visited:
                subgraph = []
                self.bfs(node, visited, subgraph)
                result.append(sorted(subgraph))
        return result


    def bfs(self, node, visited, subgraph):
        from collections import deque
        queue = deque([node])
        visited.add(node)

        while queue:
            node = queue.popleft()
            subgraph.append(node.label)
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)



    def connectedSet_union_find(self, nodes):


        class UnionFind:
            def __init__(self):
                self.father = dict()

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
        from collections import defaultdict
        union_find = UnionFind()
        for node in nodes:
            union_find.father[node.label] = node.label

        # connect node and its neighbors
        for node in nodes:
            for neighbor in node.neighbors:
                union_find.connect(node.label, neighbor.label)

        subgraph = defaultdict(set)
        for node in nodes:
            root = union_find.find(node.label)
            subgraph[root].add(node.label)

        result = []
        for root in subgraph:
            result.append(sorted(subgraph[root]))

        return result



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
