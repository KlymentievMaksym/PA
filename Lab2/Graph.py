import numpy as np
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, number_of_vertices: int):
        # Matrix realization
        self.number_of_vertices = number_of_vertices
        self.graph = [[0 for _ in range(number_of_vertices)] for _ in range(number_of_vertices)]

    def convertator(self, type_of_realization: str, *args, **kwargs):
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

        if type_of_realization == 'matrix':
            length = len(args[0].items())
            matrix_to_return = [[0 for _ in range(length)] for _ in range(length)]

            for vertex, vertices_connected in args[0].items():
                for vertex_second in vertices_connected:
                    if not isinstance(vertex_second, int):
                        matrix_to_return[vertex][vertex_second[0]] = vertex_second[1]
                    else:
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
                        if np.any(np.array(matrix) > 1):
                            dict_of_lists_to_return[vertex].append((vertex_second, self.graph[vertex][vertex_second]))
                        else:
                            dict_of_lists_to_return[vertex].append(vertex_second)
            return dict_of_lists_to_return

    def add_vertex(self, v: int):
        if not isinstance(v, int):
            raise TypeError(f"Vertex {v} is not an integer")
        if v < 0:
            raise ValueError(f"Vertex {v} can't be negative")

        temp_dict = self.convertator('list')
        temp_dict[v] = temp_dict.get(v, [])
        self.graph = self.convertator('matrix', temp_dict)
        self.number_of_vertices += 1

    def add_edge(self, v1: int, v2: int, weight: int, cls: 'Graph'):
        if not isinstance(v1, int) or not isinstance(v2, int):
            raise TypeError(f"Either vertex {v1} or {v2} is not an integer")
        if v1 < 0 or v2 < 0:
            raise ValueError(f"Neither {v1}, nor {v2} can be negative")
        if (cls.__class__.__name__ == 'UndirectedGraph' or cls.__class__.__name__ == 'DirectedGraph') and weight != 1:
            raise ValueError(f"Weight can be only 1 in {cls.__class__.__name__}")

    def remove_vertex(self, v: int):
        if not isinstance(v, int):
            raise TypeError(f"Vertex {v} is not an integer")
        if v < 0:
            raise ValueError(f"Vertex {v} can't be negative")
        if v >= self.number_of_vertices:
            raise ValueError(f"Vertex {v} doesn't exist")

        temp_dict = self.convertator('list')
        items = temp_dict.pop(v)
        for item in items:
            if isinstance(item, int):
                if v in temp_dict[item]:
                    temp_dict[item].remove(v)
            else:
                if (v, item[1]) in temp_dict[item[0]]:
                    temp_dict[item[0]].remove((v, item[1]))
        self.graph = self.convertator('matrix', temp_dict)
        self.number_of_vertices -= 1

    def remove_edge(self, v1: int, v2: int):
        if not isinstance(v1, int) or not isinstance(v2, int):
            raise TypeError(f"Either vertex {v1} or {v2} is not an integer")
        if v1 < 0 or v2 < 0:
            raise ValueError(f"Neither {v1}, nor {v2} can be negative")
        if v1 >= self.number_of_vertices or v2 >= self.number_of_vertices:
            raise ValueError(f"Either vertex {v1} or {v2} doesn't exist")

    def random_graph_Erdos_Renyi(self, probability: float, **kwargs):
        weight_range = kwargs.get('weight', 1)

        is_int = isinstance(weight_range, int)

        if probability < 0 or probability > 1:
            raise ValueError("Probability can't be less than 0 or more than 1")

        for i in range(self.number_of_vertices):
            for j in range(i+1, self.number_of_vertices):
                success = np.random.choice([True, False], p=[probability, 1 - probability])
                if success:
                    if is_int:
                        weight = weight_range
                    else:
                        weight = np.random.choice(weight_range)
                    self.add_edge(i, j, weight)
                else:
                    self.remove_edge(i, j)

        return self.graph

    def add_arrow(self, line, size=10, color='b'):
        xdata = line.get_xdata()
        ydata = line.get_ydata()

        line.axes.annotate('',
            xytext=(xdata[0], ydata[0]),
            xy=(xdata[1], ydata[1]),
            arrowprops=dict(arrowstyle="->", color=color),
            size=size
        )

    def draw(self):
        radius = self.number_of_vertices
        figure, ax = plt.subplots()
        temp_dict = self.convertator('list')
        print(temp_dict)
        angles = np.linspace(0, 2 * np.pi, radius, endpoint=False)

        x = np.cos(angles)
        y = np.sin(angles)

        list_of_points = []
        offset1 = 0.1
        offset2 = 0.15

        for i in range(radius):
            list_of_points.append([i, (x[i], y[i])])

        for vertex, vertices_connected in temp_dict.items():
            for vertex_second in vertices_connected:
                if isinstance(vertex_second, int):
                    self.add_arrow(ax.plot([list_of_points[vertex][1][0], list_of_points[vertex_second][1][0]], [list_of_points[vertex][1][1], list_of_points[vertex_second][1][1]], linestyle='-', color='b')[0])
                else:
                    self.add_arrow(ax.plot([list_of_points[vertex][1][0], list_of_points[vertex_second[0]][1][0]], [list_of_points[vertex][1][1], list_of_points[vertex_second[0]][1][1]], linestyle='-', color='b')[0])
                    ax.annotate(str(self.graph[vertex][vertex_second[0]]), [(list_of_points[vertex][1][1]+list_of_points[vertex][1][0])/2, (list_of_points[vertex_second[0]][1][1]+list_of_points[vertex_second[0]][1][0])/2])
        for vertex, choice in list_of_points:
            ax.scatter(*choice, color='r')
            coords = [
                [[choice[0]-offset2, choice[1]-offset2], [choice[0]+offset1, choice[1]+offset1]][choice[0] >= 0 and choice[1] >= 0],
                [[choice[0]+offset1, choice[1]-offset2], [choice[0]-offset2, choice[1]+offset1]][choice[0] < 0 and choice[1] >= 0]
            ][abs(choice[0]*choice[1]) != choice[0]*choice[1]]
            ax.annotate(str(vertex), coords)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.axis([-1-offset2, 1+offset1, -1-offset2, 1+offset1])
        plt.show()


class UndirectedGraph(Graph):
    def add_edge(self, v1: int, v2: int, weight: int = 1):
        super().add_edge(v1, v2, weight, self)
        self.graph[v1][v2] = weight
        self.graph[v2][v1] = weight

    def remove_edge(self, v1: int, v2: int):
        super().remove_edge(v1, v2)
        self.graph[v1][v2] = 0
        self.graph[v2][v1] = 0


class DirectedGraph(Graph):
    def add_edge(self, v1: int, v2: int, weight: int = 1):
        super().add_edge(v1, v2, weight, self)
        self.graph[v1][v2] = weight

    def remove_edge(self, v1: int, v2: int):
        super().remove_edge(v1, v2)
        self.graph[v1][v2] = 0


class WeightedGraphUndirected(UndirectedGraph):
    pass


class WeightedGraphDirected(DirectedGraph):
    pass


if __name__ == '__main__':
    undirected_graph = UndirectedGraph(4)
    undirected_graph.random_graph_Erdos_Renyi(0.4)
    undirected_graph.draw()
    directed_graph = DirectedGraph(4)
    directed_graph.random_graph_Erdos_Renyi(0.4)
    directed_graph.draw()
    weighted_graph_dn = WeightedGraphUndirected(4)
    weighted_graph_dn.random_graph_Erdos_Renyi(0.4, weight=[5, 2, 3, 4])
    weighted_graph_dn.draw()
    weighted_graph_d = WeightedGraphDirected(4)
    weighted_graph_d.random_graph_Erdos_Renyi(0.4, weight=[5, 2, 3, 4])
    weighted_graph_d.draw()
