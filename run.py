import sim
import sys
import utils
from anti_highest_degree import anti_highest_degree
from nx_strategies import *

filename = sys.argv[1]
n = len(sys.argv) - 2

graph = utils.read_graph(filename)
# Choose between these strategies by commenting/uncommenting the below lines
nodes = {
    #"highest_degree": highest_degree(graph, 10),
    "anti_highest_degree": anti_highest_degree(graph, 10),
    #"average_neighbor_degree": average_neighbor_degree(graph, 10),
    "closeness_centrality": closeness_centrality(graph, 10)
}
# for i in range(n):
#     nodes["strategy" + str(i + 1)] = utils.read_nodes(sys.argv[i + 2])

print sim.run(graph, nodes)
