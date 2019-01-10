'''
Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.

Notice

You can assume that there is at least one topological order in the graph.

Clarification
Learn more about representation of graphs

Example
For graph as follow:

picture

The topological order can be:

[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...
Challenge
Can you do it in both BFS and DFS?
'''
# Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


from collections import defaultdict, deque
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):

        # edge case
        if not graph: #len(graph) == 0
            return []

        # 1. Count each's node indegree (number of edge into node)
        indegree = self._get_indegree(graph)

        # 2. Topological Sorting: Get those nodes with indegree 0 (which meand those nodes in graph but not in indegree)
        start_nodes = self._get_start_nodes(graph)

        # 3. Use BFS to get the topological order (from indegree 1, 2, 3, 4)
        result = self._get_topological_order(start_nodes, indegree)

        return result


    def _get_indegree(graph):
        indegree = defaultdict(int)

        for node in graph:
            for neighbor in node.neighbor:
                indegree[neighbor] += 1

        return indegree


    def _get_start_nodes(graph):
        start_nodes = set()

        for node in graph:
            if node not in indegree:
                start_nodes.add(node)

        return start_nodes


    def _get_topological_order(start_nodes, indegree):
        result = []

        queue = deque(start_nodes)
        # no need the visited, this set to keep track of nodes we visited because this is directed graph
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor in node.neighbors:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return result
