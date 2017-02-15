from utils import read_graph
from utils import write_nodes
import operator
import sys

filename = sys.argv[1]
n = int(sys.argv[2])

G = read_graph(filename)

G_degrees = dict(map(lambda (k, v): (k, len(v)), G.iteritems()))

G_sorted = sorted(G_degrees.items(), key=operator.itemgetter(1), reverse=True)

top_n = [node for (node, _) in G_sorted[0:n]]

write_nodes(top_n)
