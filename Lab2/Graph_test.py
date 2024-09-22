import unittest
from Graph import *


class TestGraph(unittest.TestCase):
    def test_init_undirected_graph(self):
        graph = UndirectedGraph(5)
        items = (
            {'case': 'Adding a vertex', 'method': graph.add_vertex,'v': [5], 'expected': 1},
            {'case': 'Adding an edge', 'method': graph.add_edge,'v': [1, 2], 'expected': 1},
            {'case': 'Removing a vertex', 'method': graph.remove_vertex,'v': [1], 'expected': 0},
            {'case': 'Removing an edge', 'method': graph.remove_edge,'v': [1, 2], 'expected': 0},
        )
        for item in items:
            with self.subTest(item['case']):
                result = item['method'](*item['v'])
                self.assertEqual(result, item['expected'])

    def test_init_directed_graph(self):
        raise NotImplementedError

    def test_init_weighted_graph_undirected(self):
        raise NotImplementedError

    def test_init_weighted_graph_directed(self):
        raise NotImplementedError

if __name__ == '__main__':
    unittest.main()
