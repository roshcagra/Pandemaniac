from utils import read_graph
from utils import write_nodes
from utils import adjacency_list_to_incidence_matrix
import operator
import sys
import numpy as np

from sklearn.cluster import spectral_clustering

filename = sys.argv[1]
n = int(sys.argv[2])

G = read_graph(filename)

G_degrees = dict(map(lambda (k, v): (k, len(v)), G.iteritems()))

i_matrix = adjacency_list_to_incidence_matrix(G)

clusters = spectral_clustering(i_matrix)

for i in range(8):
    curr_cluster = np.where(clusters==i)[0]
    best_node = -1
    best_degree = -1
    for node in curr_cluster:
        node_degree = G_degrees[node]
        if node_degree > best_degree:
            best_node = node
            best_degree = node_degree
    print "Cluster", i, best_node, len(curr_cluster)
