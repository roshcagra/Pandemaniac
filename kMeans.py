from utils import read_graph
from utils import write_nodes
from utils import adjacency_list_to_incidence_matrix
import operator
import sys

from sklearn.cluster import KMeans

filename = sys.argv[1]
# n = int(sys.argv[2])

def kmeansGraph(filename):

	G = read_graph(filename)
	i_matrix = adjacency_list_to_incidence_matrix(G)

	ass = KMeans()

	clusters = ass.fit_predict(i_matrix)

	print clusters 

if __name__ == "__main__":
	kmeansGraph(filename)