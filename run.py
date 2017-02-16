import sim
import sys
import utils
from highest_degree import highest_degree
from anti_highest_degree import anti_highest_degree

filename = sys.argv[1]
n = len(sys.argv) - 2

graph = utils.read_graph(filename)
nodes = {
    "highest_degree": highest_degree(graph, 10),
    "anti_highest_degree": anti_highest_degree(graph, 10)
}
# for i in range(n):
#     nodes["strategy" + str(i + 1)] = utils.read_nodes(sys.argv[i + 2])

print sim.run(graph, nodes)
