'''
Six degrees of separation is the theory that everyone and everything is six or fewer steps away, by way of introduction, from any other person in the world, so that a chain of "a friend of a friend" statements can be made to connect any two people in a maximum of six steps.

Given a friendship relations, find the degrees of two people, return -1 if they can not been connected by friends of friends.

Example
Gien a graph:

1------2-----4
 \          /
  \        /
   \--3--/
{1,2,3#2,1,4#3,1,4#4,2,3} and s = 1, t = 4 return 2

Gien a graph:

1      2-----4
             /
           /
          3
{1#2,4#3,4#4,2,3} and s = 1, t = 4 return -1
'''


# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self. neighbors = []


from collections import deque
class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """
    def sixDegrees(self, graph, s, t):

        queue = deque()
        queue.append(s)
        visited = set()
        visited.add(s)

        degree = 0

        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.popleft()
                if node is t:
                    return degree

                for neighbor_node in node.neighbors:
                    if neighbor_node not in visited:
                        queue.append(neighbor_node)
                        visited.add(neighbor_node)
            degree += 1

        return -1
