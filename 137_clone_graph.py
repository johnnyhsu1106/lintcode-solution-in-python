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
        if not node:
            return node

        # 1. get all nodes: use the bfs to get all nodes
        nodes = self._get_nodes(node)

        # mapping the node: copy nodes and sotre the ole-> new mapping information in hash map(dictionary)
        mapping ={}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.lable)

        # 3. copy all neighbors (edges)
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                # use the mapping to find the corresponding node
                new_neighbor = mapping[neighbor]
                # append the corresponding neighbor to new node
                new_node.neighbors.append(new_neighbor)

        return mapping[node] # new_node


    def _get_nodes(self, node):
        # travese all nodes (using BFS)
        queue = deque([node])
        visited = set([node])

        while queue:
            node = queue.popleft()

            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return visited
