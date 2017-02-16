from utils import read_graph
from utils import write_nodes
from utils import adjacency_list_to_incidence_matrix
import operator
import sys

from sklearn.cluster import spectral_clustering

filename = sys.argv[1]
n = int(sys.argv[2])

G = read_graph(filename)
i_matrix = adjacency_list_to_incidence_matrix(G)

clusters = spectral_clustering(i_matrix)
