from UnionFindTable import UnionFindTable as UF
from Graph import WeightedGraphUndirected as Graph

# algorithm Kruskal(G) is
#     F:= ∅
#     for each v in G.V do
#         MAKE-SET(v)
#     for each {u, v} in G.E ordered by weight({u, v}), increasing do
#         if FIND-SET(u) ≠ FIND-SET(v) then
#             F := F ∪ { {u, v} }
#             UNION(FIND-SET(u), FIND-SET(v))
#     return F


class KruskalsAlgorithm:
    def __init__(self, size=5):
        graph = Graph(size)
        graph.random_graph_Erdos_Renyi(1, weight=[i for i in range(1, 2*size+1)])

        self.size = size
        self.dict_of_edges = graph.convertator('list')

        self.uf = UF([[i] for i in range(1, size+1)])

        self.msf = []

        keys_to_delete = []
        for key, value in self.dict_of_edges.items():
            if value == []:
                keys_to_delete.append(key)
        for key in keys_to_delete:
            self.dict_of_edges.pop(key)

    def start(self, need_print=False):
        for weight, edges in self.dict_of_edges.items():
            for edge in edges:
                u = int(edge[0])
                v = int(edge[1])
                if self.uf.find(u) != self.uf.find(v):
                    self.msf.append((u, v, weight))
                    self.uf.union(u, v)
        if need_print:
            print(self.uf.make_sets())
            print(self.dict_of_edges)
            print(self.msf)

        return self.msf


if __name__ == '__main__':
    kruskal = KruskalsAlgorithm(5)
    print(kruskal.start())
