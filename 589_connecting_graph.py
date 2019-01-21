'''
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

You need to support the following method:
1. connect(a, b), add an edge to connect node a and node b. 2.query(a, b)`, check if two nodes are connected

Have you met this question in a real interview? Yes
Example
5 // n = 5
query(1, 2) return false
connect(1, 2)
query(1, 3) return false
connect(2, 4)
query(1, 4) return true
'''

class ConnectingGraph:
    '''
    idea: two way to implement Union Find data structure
    1. array (if node is the integer)
    2. dict (hash map)
    The following implementation is Union Find
    '''


    """
    @param: n: An integer
    """
    def __init__(self, n):

        #  array
        # self.father = [ i for i in range(1 + n)]

        # dict
        self.father = {}
        for i in range(1, n + 1):
            self.father[i] = i

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.father[root_a] = root_b


    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """
    def query(self, a, b):
        return self.find(a) == self.find(b)


    def find(self, x):
        if self.father[x] == x:
            return x

        self.father[x] = self.find(self.father[x])

        return self.father[x]




# ############################  BFS ############################

from collections import defaultdict, deque
class ConnectingGraph_BFS:
    '''
    Implementation: use BFS...... if query k times, n nodes, it will take O(nk).. Time Limit Exceeded.
    '''
    """
    @param: n: An integer
    """
    def __init__(self, n):
        self.node_mapping = defaultdict(set)


    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        self.node_mapping[a].add(b)
        self.node_mapping[b].add(a)

    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """
    def query(self, a, b):
        queue = deque([a])
        visited_points = set([a])

        while queue:
            node = queue.popleft()

            if node == b:
                return True

            neighbors = self.node_mapping[node]
            for neighbor in neighbors:
                if neighbor not in visited_points:
                    queue.append(neighbor)
                    visited_points.add(neighbor)

        return False

# def main():
#     '''
#     5 // n = 5
#     query(1, 2) return false
#     connect(1, 2)
#     query(1, 3) return false
#     connect(2, 4)
#     query(1, 4) return true
#     '''
#     graph = ConnectingGraph(5)
#     print(graph.query(1, 2))
#     graph.connect(1, 2)
#     print(graph.query(1, 3))
#     graph.connect(2, 4)
#     print(graph.query(1, 4))
#     print(graph.father)
#
#
# if __name__ == '__main__':
#     main()
