class Graph:
    def __init__(self, number_of_vertices: int):
        # Matrix realization
        self.number_of_vertices = number_of_vertices
        self.graph = [[0 for _ in range(number_of_vertices)] for _ in range(number_of_vertices)]

    def convertator(self, type_of_realization: str, *args):
        if not isinstance(type_of_realization, str) and type_of_realization != 'matrix' and type_of_realization != 'list':
            raise NameError(f"Not expected type of realization, expected 'matrix' or 'list', got {type_of_realization}")

        if len(args) > 1:
            raise OverflowError(f"Not expected number of arguments, expected 1, got {len(args)}")

        elif len(args) == 1:
            if type_of_realization == 'matrix' and not isinstance(args[0], dict):
                raise TypeError(f"Not expected type of argument, expected 'dict', got {type(args[0])}")
            if type_of_realization == 'list' and not isinstance(args[0], list):
                raise TypeError(f"Not expected type of argument, expected 'list', got {type(args[0])}")

        else:
            if type_of_realization != 'list':
                raise IndexError("No arguments can only be used with 'list' realization")

    def add_vertex(self, v: int):
        if not isinstance(v, int):
            raise TypeError(f"Vertex {v} is not an integer")
        if v < 0:
            raise ValueError(f"Vertex {v} can't be negative")

    def add_edge(self, v1: int, v2: int):
        if not isinstance(v1, int) or not isinstance(v2, int):
            raise TypeError(f"Either vertex {v1} or {v2} is not an integer")
        if v1 < 0 or v2 < 0:
            raise ValueError(f"Neither {v1}, nor {v2} can be negative")

    def remove_vertex(self, v: int):
        if not isinstance(v, int):
            raise TypeError(f"Vertex {v} is not an integer")
        if v < 0:
            raise ValueError(f"Vertex {v} can't be negative")
        if v >= self.number_of_vertices:
            raise ValueError(f"Vertex {v} doesn't exist")

    def remove_edge(self, v1: int, v2: int):
        if not isinstance(v1, int) or not isinstance(v2, int):
            raise TypeError(f"Either vertex {v1} or {v2} is not an integer")
        if v1 < 0 or v2 < 0:
            raise ValueError(f"Neither {v1}, nor {v2} can be negative")
        if v1 >= self.number_of_vertices or v2 >= self.number_of_vertices:
            raise ValueError(f"Either vertex {v1} or {v2} doesn't exist")


class UndirectedGraph(Graph):
    def convertator(self, type_of_realization: str, *args):
        super().convertator(type_of_realization, *args)
        if type_of_realization == 'matrix':
            length = len(args[0].items())
            matrix_to_return = [[0 for _ in range(length)] for _ in range(length)]
            for vertex, vertices_connected in args[0].items():
                for vertex_second in vertices_connected:
                    matrix_to_return[vertex][vertex_second] = 1
            return matrix_to_return

        elif type_of_realization == 'list':
            if len(args) == 0:
                matrix = self.graph
            else:
                matrix = args[0]
            dict_of_lists_to_return = {}
            for vertex in range(self.number_of_vertices):
                dict_of_lists_to_return[vertex] = []
                for vertex_second in range(self.number_of_vertices):
                    if matrix[vertex][vertex_second] != 0:
                        dict_of_lists_to_return[vertex].append(vertex_second)
            return dict_of_lists_to_return

    def add_vertex(self, v: int):
        super().add_vertex(v)
        temp_dict = self.convertator('list')
        temp_dict[v] = temp_dict.get(v, [])
        self.graph = self.convertator('matrix', temp_dict)
        self.number_of_vertices += 1

    def add_edge(self, v1: int, v2: int):
        super().add_edge(v1, v2)
        self.graph[v1][v2] = 1
        self.graph[v2][v1] = 1

    def remove_vertex(self, v: int):
        super().remove_vertex(v)
        temp_dict = self.convertator('list')
        items = temp_dict.pop(v)
        for item in items:
            temp_dict[item].remove(v)
        self.graph = self.convertator('matrix', temp_dict)
        self.number_of_vertices -= 1

    def remove_edge(self, v1: int, v2: int):
        super().remove_edge(v1, v2)
        self.graph[v1][v2] = 0
        self.graph[v2][v1] = 0


class DirectedGraph(Graph):
    def convertator(self, type_of_realization: str, *args):
        super().convertator(type_of_realization, *args)
        if type_of_realization == 'matrix':
            length = len(args[0].items())
            matrix_to_return = [[0 for _ in range(length)] for _ in range(length)]
            for vertex, vertices_connected in args[0].items():
                for vertex_second in vertices_connected:
                    matrix_to_return[vertex][vertex_second] = 1
            return matrix_to_return

        elif type_of_realization == 'list':
            if len(args) == 0:
                matrix = self.graph
            else:
                matrix = args[0]
            dict_of_lists_to_return = {}
            for vertex in range(self.number_of_vertices):
                dict_of_lists_to_return[vertex] = []
                for vertex_second in range(self.number_of_vertices):
                    if matrix[vertex][vertex_second] != 0:
                        dict_of_lists_to_return[vertex].append(vertex_second)
            return dict_of_lists_to_return

    def add_vertex(self, v: int):
        super().add_vertex(v)
        temp_dict = self.convertator('list')
        temp_dict[v] = temp_dict.get(v, [])
        self.graph = self.convertator('matrix', temp_dict)
        self.number_of_vertices += 1

    def add_edge(self, v1: int, v2: int):
        super().add_edge(v1, v2)
        self.graph[v1][v2] = 1

    def remove_vertex(self, v: int):
        super().remove_vertex(v)
        temp_dict = self.convertator('list')
        items = temp_dict.pop(v)
        # for item in items:
        #     temp_dict[item].remove(v)
        self.graph = self.convertator('matrix', temp_dict)
        self.number_of_vertices -= 1

    def remove_edge(self, v1: int, v2: int):
        super().remove_edge(v1, v2)
        self.graph[v1][v2] = 0


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
    def add_edge(self, v1, v2, weight):
        super().add_edge(v1, v2, weight)

    def remove_edge(self, v1, v2):
        super().remove_edge(v1, v2)

    def add_vertex(self, v):
        super().add_vertex(v)

    def remove_vertex(self, v):
        super().remove_vertex(v)


class WeightedGraphDirected(WeightedGraph, DirectedGraph):
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
