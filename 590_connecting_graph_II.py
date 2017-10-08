'''
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

You need to support the following method:
1. connect(a, b), an edge to connect node a and node b
2. query(a), Returns the number of connected component nodes which include node a.

Example
5 // n = 5
query(1) return 1
connect(1, 2)
query(1) return 2
connect(2, 4)
query(1) return 3
connect(1, 4)
query(1) return 3
'''
class ConnectingGraph2:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # every node is connected to itself
        self.father = [ i for i in range(n + 1)]
        # every node is 1 (only connected to itself)
        self.size = [1 for i in range(n + 1)]


    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b) # root_b is the representative of set
        if root_a != root_b:
            self.father[root_a] = root_b
            self.size[root_b] += self.size[root_a]

    """
    @param: a: An integer
    @return: An integer
    """
    def query(self, a):
        root_a = self.find(a)
        return self.size[root_a]


    def find(self, a):

        if self.father[a] == a:
            return a

        self.father[a] = self.find(self.father[a])

        return self.father[a]

#
# def main():

#     graph = ConnectingGraph2(5)
#     print(graph.query(1))
#     graph.connect(1, 2)
#     print(graph.query(1))
#     graph.connect(2, 4)
#     print(graph.query(1))
#     graph.connect(1, 4)
#     print(graph.query(1))
#
#
# if __name__ == '__main__':
#     main()
