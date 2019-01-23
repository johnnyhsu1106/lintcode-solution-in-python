'''
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

You need to support the following method:
1. connect(a, b), an edge to connect node a and node b
2. query(), Returns the number of connected component in the graph

Have you met this question in a real interview? Yes
Example
5 // n = 5
query() return 5
connect(1, 2)
query() return 4
connect(2, 4)
query() return 3
connect(1, 4)
query() return 3
'''
class ConnectingGraph3:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        self.num_of_connected_component = n # a instance variable, storing number of components
        self.father = {i: i for i in range(1, n + 1)}
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
            self.num_of_connected_component -= 1


    """
    @return: An integer
    """
    def query(self):
        return self.num_of_connected_component


    def find(self, x):
        if self.father[x] == x:
            return x

        self.father[x] = self.find(self.father[x])
        
        return self.father[x]


# def main():
#
#     graph = ConnectingGraph3(5)
#     print(graph.query())
#     graph.connect(1, 2)
#     print(graph.query())
#     graph.connect(2, 4)
#     print(graph.query())
#     graph.connect(1, 4)
#     print(graph.query())
#
# if __name__ == '__main__':
#     main()
