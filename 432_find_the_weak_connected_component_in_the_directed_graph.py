'''
Find the number Weak Connected Component in the directed graph.
Each node in the graph contains a label and a list of its neighbors.
(a connected set of a directed graph is a subgraph in which
any two vertices are connected by direct edge path.)

Notice

Sort the element in the set in increasing order

Example
Given graph:

A----->B  C
 \     |  |
  \    |  |
   \   |  |
    \  v  v
     ->D  E <- F
Return {A,B,D}, {C,E,F}. Since there are two connected component which are {A,B,D} and {C,E,F}
'''

class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = [] # a list of DirectedGraphNode


from collections import defaultdict
class Solution:
    """
    @param: nodes: a array of Directed graph node
    @return: a connected set of a directed graph
    """
    def connectedSet2(self, nodes):
        # BFS is not working. BFS is only used for undirected graph
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

        # initila all graph node in UnionFind data structure
        # all the node will be pointed to itself
        union_find = UnionFind()
        for node in nodes:
            union_find.father[node.label] = node.label

        # connect the node with its neighbors
        for node in nodes:
            for neighbor in node.neighbors:
                union_find.connect(node.label, neighbor.label)

        result = []
        subgraphs = defaultdict(set)
        # use union_find.find() to find the root
        # add root and its neighbors (including itself) to hash map = {node: set([node, neighbor1...])}
        for node in nodes:
            root = union_find.find(node.label)
            subgraphs[root].add(node.label)

        # get the each subgraph from hash map
        for root in subgraphs:
            result.append(sorted(subgraphs[root]))
        return result



# def main():
#     s = Solution()
#     A = DirectedGraphNode('A')
#     B = DirectedGraphNode('B')
#     C = DirectedGraphNode('C')
#     D = DirectedGraphNode('D')
#     E = DirectedGraphNode('E')
#     F = DirectedGraphNode('F')
#
#     A.neighbors = [B,D]
#     B.neighbors = [D]
#     C.neighbors = [E]
#     E.neighbors = [F]
#     nodes = [A, B, C, D, E, F]
#     print(s.connectedSet2(nodes))
#
#
# if __name__ == '__main__':
#     main()
