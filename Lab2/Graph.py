class Graph:
    def __init__(self, number_of_vertices):
        # Matrix realization
        self.number_of_vertices = number_of_vertices
        self.graph = [[0]*number_of_vertices]*number_of_vertices

    def convertator(self, type_of_realization: str):
        pass

    def add_vertex(self, v):
        pass

    def add_edge(self, v1, v2):
        pass

    def remove_vertex(self, v):
        pass

    def remove_edge(self, v1, v2):
        pass


class UndirectedGraph(Graph):
    def __init__(self, number_of_vertices):
        super().__init__(number_of_vertices)

    def convertator(self, type_of_realization: str):
        raise NotImplementedError

    def add_vertex(self, v):
        raise NotImplementedError

    def add_edge(self, v1, v2):
        raise NotImplementedError

    def remove_vertex(self, v):
        raise NotImplementedError

    def remove_edge(self, v1, v2):
        raise NotImplementedError



class DirectedGraph(Graph):
    def __init__(self, number_of_vertices):
        super().__init__(number_of_vertices)

    def convertator(self, type_of_realization: str):
        raise NotImplementedError

    def add_vertex(self, v):
        raise NotImplementedError

    def add_edge(self, v1, v2):
        raise NotImplementedError

    def remove_vertex(self, v):
        raise NotImplementedError

    def remove_edge(self, v1, v2):
        raise NotImplementedError


class WeightedGraph(Graph):
    def __new__(cls, type_of_graph):
        if cls is not WeightedGraph:
            return super().__new__(cls)
        class_map = {
            'Undirected': WeightedGraphUndirected, 
            'Directed': WeightedGraphDirected
            }
        cls = class_map[type_of_graph]
        return super().__new__(cls, type_of_graph)

class WeightedGraphUndirected(WeightedGraph, UndirectedGraph):
    def __init__(self, number_of_vertices):
        super().__init__(number_of_vertices)

    def add_edge(self, v1, v2, weight):
        super().add_edge(v1, v2, weight)

    def remove_edge(self, v1, v2):
        super().remove_edge(v1, v2)

    def add_vertex(self, v):
        super().add_vertex(v)

    def remove_vertex(self, v):
        super().remove_vertex(v)


class WeightedGraphDirected(WeightedGraph, DirectedGraph):
    def __init__(self, number_of_vertices):
        super().__init__(number_of_vertices)

    def add_edge(self, v1, v2, weight):
        super().add_edge(v1, v2, weight)

    def remove_edge(self, v1, v2):
        super().remove_edge(v1, v2)

    def add_vertex(self, v):
        super().add_vertex(v)

    def remove_vertex(self, v):
        super().remove_vertex(v)


if __name__ == '__main__':
    undirected_graph = UndirectedGraph(5)
    directed_graph = DirectedGraph(5)
    weighted_graph_dn = WeightedGraph('Undirected')(5)
    weighted_graph_d = WeightedGraph('Directed')(5)
