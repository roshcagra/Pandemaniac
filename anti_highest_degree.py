from utils import read_graph
from utils import write_nodes
import operator
import sys

filename = sys.argv[1]
n = int(sys.argv[2])

selected = set()
def chooseNode(node):
    if len(selected) < n and node not in selected:
        selected.add(node)

G = read_graph(filename)

G_degrees = dict(map(lambda (k, v): (k, len(v)), G.iteritems()))

G_sorted = sorted(G_degrees.items(), key=operator.itemgetter(1), reverse=True)

for (node, _) in G_sorted:
    if len(selected) == n:
        break
    try:
        chooseNode(G[node][0])
        chooseNode(G[node][1])
    except:
        print "Error Choosing Node"

assert(n == len(selected))

write_nodes(list(selected))
