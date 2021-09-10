from collections import deque
from dataclasses import dataclass
from unionfind import unionfind
import heapq as heap


@dataclass
class WEdge:
    u: int
    v: int
    weight: float


class WuGraph:
    def __init__(self, size):
        self.num_vertices = size
        self.matrix = [None] * self.num_vertices
        for i in range(len(self.matrix)):
            self.matrix[i] = [None] * self.num_vertices

    def __len__(self):
        return self.num_vertices

    def set_edge(self, u, v, weight):
        self.matrix[u][v] = weight
        self.matrix[v][u] = weight

    def get_edge(self, u, v):
        return self.matrix[u][v]

    def get_adjacent(self, v):
        lst = deque()
        for i in range(len(self.matrix[v])):
            if self.matrix[v][i] is not None:
                lst.appendleft(i)
        return lst

    def get_all_edges(self):
        lst = deque()
        if len(self.matrix) == 1 and self.matrix[0][0] is not None:
            lst.appendleft(WEdge(0, 0, self.matrix[0][0]))
        else:
            inc = 0
            for i in range(len(self.matrix) - 1, 0, -1):
                for j in range(len(self.matrix[i]) - inc):
                    if self.matrix[i][j] is not None:
                        edge = WEdge(i, j, self.matrix[i][j])
                        lst.appendleft(edge)
                inc += 1
        return lst

    def get_all_edges_increasing(self):
        edges = list(self.get_all_edges())
        weights_to_edges = {}
        for edge in edges:
            weights_to_edges[edge.weight] = edge
        weight_list = list(weights_to_edges.keys())
        heap.heapify(weight_list)
        weight_list.sort()
        edge_list = []
        for weight in weight_list:
            edge_list.append(weights_to_edges[weight])
        return edge_list


def _same_graph(g1, g2):
    if len(g1) != len(g2):
        return False
    for u in range(len(g1)):
        for v in range(u, len(g1)):
            if g1.get_edge(u, v) != g2.get_edge(u, v):
                return False
    return True


def _print_graph(graph):
    for i in range(len(graph.matrix)):
        for j in range(len(graph.matrix[i])):
            if graph.matrix[i][j] is not None:
                print(str(graph.matrix[i][j]) + "   ", end=" ")
            else:
                print(graph.matrix[i][j], end=" ")
        print()
