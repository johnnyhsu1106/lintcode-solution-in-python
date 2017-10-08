'''
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

How we serialize an undirected graph:

Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.

As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

   1
  / \
 /   \
0 --- 2
     / \
     \_/
Example
return a deep copied graph.
'''
# Definition for undirected graph.
class UndirectedGraphNode:
    def __init__(self, x):
         self.label = x
         neighbors = []

from collections import deque
class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # edge case
        root = node
        if not node:
            return node

        mapping ={}
        # 1. get all nodes: a Set of all nodes and mapping node to new node
        nodes = self.get_nodes_mapping(node, mapping)

        # 2. copy all neighbors
        for node in nodes:
            new_node = node_map[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

        return mapping[root]


    def get_nodes_and_mapping(self, node, mapping):
        # travese all nodes (using BFS)
        queue = deque([node])
        visited = set([node])

        while queue:
            node = queue.popleft()
            mapping[node] = UndirectedGraphNode(node.label)
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
