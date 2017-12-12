from common import Input
from my_utils.graphs import dijkstra_all_paths
import re

graph = {}

for line in Input(12):
    node, *connections = re.findall(r'\d+', line)
    graph[node] = connections

moves = lambda x: graph[x]
paths = dijkstra_all_paths('0', moves).parents
print(len(paths))

remaining_nodes = set(graph) - set(paths)
groups = [paths]
while remaining_nodes:
    group = set(dijkstra_all_paths(remaining_nodes.pop(), moves).parents)
    remaining_nodes -= group
    groups.append(group)
print(len(groups))
