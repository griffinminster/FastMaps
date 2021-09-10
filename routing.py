# from collections import deque
# import wugraph as graph
#
#
# def find_route(mst, start, end):
#     pred = graph._dijkstra(mst, start)
#     wanted_id = end
#     if pred is None:
#         return None
#     lst = deque()
#     all_good = False
#
#     while wanted_id is not None:
#         if wanted_id == start:
#             all_good = True
#         lst.appendleft(wanted_id)
#         searched_id = pred[wanted_id]
#         wanted_id = searched_id
#
#     if all_good:
#         return list(lst)
#     else:
#         return None


import networkx as nx
import matplotlib.pyplot as plt


# g = nx.Graph()
# g.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# g.add_edges_from([(0, 1), (0, 4), (0, 9),
#                   (1, 5), (1, 7),
#                   (2, 6), (2, 3),
#                   (3, 3),
#                   (4, 5), (5, 4), (4, 2), (4, 8)])
# print(g.number_of_nodes())
# print(list(g.nodes))
# print(g.number_of_edges())
# print(list(g.edges))
#
# nx.draw(g, with_labels=True, font_weight='bold')
# plt.show()

g = nx.DiGraph()
# g.add_nodes_from([0, 1, 2, 3, 'DUMMY'])
# g.add_weighted_edges_from([(0, 1, 5), (0, 2, 4), (0, 3, 6),
#                            (1, 2, 7), (1, 3, 10),
#                            (2, 3, 12),
#                            (0, 'DUMMY', 0), (3, 'DUMMY', 0)])

# g.add_nodes_from([0, 1, 2, 3, 4, 5, 'DUMMY'])
# g.add_weighted_edges_from([(0, 1, 1), (0, 2, 6), (0, 3, 10), (0, 4, 13), (0, 5, 15),
#                            (1, 2, 2), (1, 3, 7), (1, 4, 11), (1, 5, 14),
#                            (2, 3, 3), (2, 4, 8), (2, 5, 12),
#                            (3, 4, 4), (3, 5, 9),
#                            (4, 5, 5),
#                            (0, 'DUMMY', 0), (5, 'DUMMY', 0)])

# g.add_nodes_from(['S', 'A', 'B', 'C', 'D', 'E', 'DUMMY'])
# g.add_weighted_edges_from([('S', 'A', 6), ('S', 'B', 5), ('S', 'C', 4), ('S', 'D', 3), ('S', 'E', 27),
#                            ('A', 'B', 10), ('A', 'C', 8), ('A', 'D', 8), ('A', 'E', 27),
#                            ('B', 'C', 6), ('B', 'D', 5), ('B', 'E', 26),
#                            ('C', 'D', 2), ('C', 'E', 36),
#                            ('D', 'E', 28),
#                            ('S', 'DUMMY', 0), ('DUMMY', 'E', 0)])

g.add_nodes_from(['S', 'A', 'B', 'C', 'DUMMY'])
g.add_weighted_edges_from([('S', 'A', 3), ('S', 'B', 5), ('S', 'C', 4),
                           ('A', 'S', 3), ('A', 'B', 5), ('A', 'C', 2),
                           ('B', 'S', 5), ('B', 'A', 3), ('B', 'C', 6),
                           ('C', 'S', 4), ('C', 'A', 2), ('C', 'B', 6),
                           ('S', 'DUMMY', 0), ('DUMMY', 'S', 0),
                           ('C', 'DUMMY', 0), ('DUMMY', 'C', 0)])
# Only right non-directed??

nx.draw(g, with_labels=True)
plt.show()

tsp = nx.approximation.traveling_salesman_problem(g, cycle=True)
print(tsp)
