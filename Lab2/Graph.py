class Graph:
    def __init__(self, number_of_vertices):
        self.number_of_vertices = number_of_vertices
        self.graph = [[0]*number_of_vertices]*number_of_vertices

    def add_vertex(self, v):
        raise NotImplementedError

    def add_edge(self, v1, v2):
        self.graph[v1][v2] = 1
        self.graph[v2][v1] = 1

    def delete_vertex(self, v):
        raise NotImplementedError

    def remove_edge(self, v1, v2):
        self.graph[v1][v2] = 0
        self.graph[v2][v1] = 0
